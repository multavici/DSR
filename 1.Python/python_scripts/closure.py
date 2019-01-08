def adder(x):
    def f(n):
        return n + x
    return f

my_adder = adder(5)
print(my_adder(100))