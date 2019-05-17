from sqlalchemy import create_engine

import pandas

eng = create_engine('postgres://newdsrsql:sql2018@192.168.2.177/dvdrental')

q = '''
SELECT f.title, a.first_name, a.last_name
  FROM film AS f
    JOIN film_actor ON f.film_id = film_actor.film_id
    JOIN actor AS a ON film_actor.actor_id = a.actor_id
  ORDER BY 1;
'''
data = pandas.read_sql(q, con=eng)
print(data)


q = '''
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
'''

data = pandas.read_sql(q, con=eng)
print(data)