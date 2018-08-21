Fib = [0, 1] + [0 for i in range(10000)]
def fib(n):
    if n > 1:
        x = fib(n-1) if Fib[n-1]==0 else Fib[n-1]
        y = fib(n-2) if Fib[n-2]==0 else Fib[n-2]
        Fib[n] = x+y
    return Fib[n]

N = 100   # Try different N by yourself

from time import time
t = time()
for i in range(N+1):
    print('第', i, '項：', fib(i))
print('計算時間', round(time()-t,2), '秒')
