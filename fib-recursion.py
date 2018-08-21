def fib(n):
    return fib(n-1)+fib(n-2) if n>1 else n

N = 33   # Try different N by yourself

from time import time
t = time()
for i in range(N+1):
    print('第', i, '項：', fib(i))
print('計算時間', round(time()-t,2), '秒')
