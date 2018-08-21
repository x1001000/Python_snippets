def f():
    a0,a1=0,1
    while True:
        a0,a1=a1,a0+a1
        yield a1
a=f()
A=[a.__next__() for _ in range(10)]
print(A)
