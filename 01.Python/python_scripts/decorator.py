def pos_args(f):
    def nf(x):
        if x <= 0:
            return "Argument must be positive"
        else:
            return f(x)
    return nf

@pos_args
def plusone(x):
    return x + 1

print(plusone(2))