def deco(f):
    return lambda x: f(x) + 1

@deco
def y(x):
    return x * 10
