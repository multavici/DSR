/* These are all exercises for the SQL crash course of DSR.
This is a multiline comment
 */

-- SELECT all films with their actors
SELECT f.title, a.first_name, a.last_name
  FROM film AS f
    JOIN film_actor ON f.film_id = film_actor.film_id
    JOIN actor AS a ON film_actor.actor_id = a.actor_id
  ORDER BY 1; -- orders by the first column of your query

-- select all films which have zero inventory
SELECT f.title
  FROM film AS f
    LEFT JOIN inventory ON f.film_id = inventory.film_id
  WHERE inventory.film_id IS NULL;

-- select all films which were returned on 2005-05-27
SELECT DISTINCT ON (f.title) f.title, r.return_date
  FROM film AS f
    JOIN inventory ON f.film_id = inventory.film_id
    JOIN rental AS r ON r.inventory_id = inventory.inventory_id
  WHERE r.return_date BETWEEN '2005-05-27' AND '2005-05-28';

-- we can also do it this way
SELECT DISTINCT ON (f.title) f.title, r.return_date
  FROM film AS f
    JOIN inventory ON f.film_id = inventory.film_id
    JOIN rental AS r ON r.inventory_id = inventory.inventory_id
      AND DATE_TRUNC('day', return_date) = '2005-05-27';

-- or
SELECT DISTINCT ON (f.title) f.title, r.return_date
  FROM film AS f
    JOIN inventory ON f.film_id = inventory.film_id
    JOIN rental AS r ON r.inventory_id = inventory.inventory_id
  WHERE date(return_date) = '2005-05-27';


-- name of all customers who returned a rental on '2005-05-27'
-- with join
SELECT c.first_name, c.last_name
  FROM customer AS c
    JOIN rental AS r ON c.customer_id = r.customer_id
  WHERE r.return_date BETWEEN '2005-05-27' AND '2005-05-28';

-- with subquery
SELECT first_name, last_name
  FROM customer
  WHERE customer_id IN (
    SELECT customer_id FROM rental
      WHERE return_date BETWEEN '2005-05-27' AND '2005-05-28'
    );

-- names of customers who made a payment
-- with subquery (and IN)
SELECT first_name, last_name
  FROM customer
  WHERE customer_id IN (
    SELECT customer_id FROM payment
    )
  ORDER BY last_name;


-- with subquery (and EXISTS)
SELECT first_name, last_name
  FROM customer
  WHERE EXISTS (
    SELECT 'a' FROM payment WHERE payment.customer_id = customer.customer_id
    )
  ORDER BY last_name;

-- with join
SELECT DISTINCT c.first_name, c.last_name
  FROM customer AS c
    JOIN payment AS p ON c.customer_id = p.customer_id
  ORDER BY last_name;
-- this is usually faster, every select statement slows down the query, but too many subqueries can also cause slowdown

-- re-do name of all customers who returned a rental on '2005-05-27' with WITH
WITH transaction AS (
  SELECT customer_id FROM rental
    WHERE return_date BETWEEN '2005-05-27' AND '2005-05-28'
)
SELECT c.first_name, c.last_name
  FROM customer AS c
  JOIN transaction AS t ON c.customer_id = t.customer_id
  ORDER BY c.last_name;
-- this is faster because you first filter and store it in a table


-- Aggregate exercises
SELECT c.customer_id, c.first_name, c.last_name, SUM(p.amount)
  FROM customer AS c
   JOIN payment AS p ON c.customer_id = p.customer_id
  GROUP BY c.customer_id
  ORDER BY SUM(p.amount) DESC;

-- customers who've spent more than 200
SELECT c.customer_id, c.first_name, c.last_name, SUM(p.amount)
  FROM customer AS c
   JOIN payment AS p ON c.customer_id = p.customer_id
  GROUP BY c.customer_id
  HAVING SUM(p.amount) > 200;

-- the number of rentals for each category
WITH film_cat AS (
  SELECT f.film_id, f.title, c.name
    FROM film AS f
      JOIN film_category AS fc on f.film_id = fc.film_id
      JOIN category AS c on fc.category_id = c.category_id
)
SELECT film_cat.name, COUNT(r.rental_id)
  FROM rental AS r
    JOIN inventory AS i ON r.inventory_id = i.inventory_id
    JOIN film AS f ON i.film_id = f.film_id
    JOIN film_cat ON f.film_id = film_cat.film_id
  GROUP BY film_cat.name
  ORDER BY COUNT(r.rental_id) DESC;

-- the number of rentals for each film + category
WITH film_cat AS (
  SELECT f.film_id, f.title, c.name
    FROM film AS f
      JOIN film_category AS fc on f.film_id = fc.film_id
      JOIN category AS c on fc.category_id = c.category_id
)
SELECT film_cat.title, film_cat.name, COUNT(r.rental_id)
  FROM rental AS r
    JOIN inventory AS i ON r.inventory_id = i.inventory_id
    JOIN film_cat ON i.film_id = film_cat.film_id
  GROUP BY film_cat.title, film_cat.name
  ORDER BY COUNT(r.rental_id) DESC;

-- films which have film.rental_rate higher than average
SELECT title, rental_rate
  FROM film
  WHERE rental_rate > ( SELECT AVG(rental_rate) FROM film )
  ORDER BY rental_rate DESC;

-- the average rental rate is
SELECT AVG(rental_rate) FROM film;

-- find the last returned film title - show customer name and return date
SELECT f.title, c.first_name, c.last_name, r.return_date, DENSE_RANK() OVER ( ORDER BY r.return_date DESC)
  FROM film AS f
    JOIN inventory i on f.film_id = i.film_id
    JOIN rental r on i.inventory_id = r.inventory_id
    JOIN customer c on r.customer_id = c.customer_id
  WHERE r.return_date IS NOT NULL
  ORDER BY r.return_date DESC
  LIMIT 10;

-- find the 10% most profitable customers
SELECT c.first_name, c.last_name, NTILE(10) OVER (ORDER BY SUM(p.amount) DESC)
  FROM customer AS c
    JOIN payment AS p ON c.customer_id = p.customer_id
  GROUP BY c.first_name, c.last_name;

-- find the most rented film for each category
SELECT *
  FROM (
         SELECT cat.name,
                f.title,
                ROW_NUMBER() OVER ( PARTITION BY cat.name ORDER BY COUNT(r.rental_id) DESC) AS rank, -- or DENSE_RANK
                COUNT(r.rental_id) AS count
         FROM rental as r
                JOIN inventory AS i ON r.inventory_id = i.inventory_id
                JOIN film AS f ON i.film_id = f.film_id
                JOIN film_category AS fc on f.film_id = fc.film_id
                JOIN category AS cat on fc.category_id = cat.category_id
         GROUP BY cat.name, f.title
       ) AS ranks
  WHERE ranks.rank < 6;