# 公鑰(N,e)加密n為密文c=n**e%N
# 私鑰(N,d)解密c為明文n=c**d%N
# e*d % ((p-1)*(q-1)) == 1

from time import time
N=55029461
e=122527
c=48098163

# 分解公鑰(N,e)的N
t=time()
for i in range(2,N):
  if N%i==0:
    p = i
    q = N//i
    break
print('p =',p)
print('q =',q)
print(round(time()-t,3),'秒\n')

# 找出私鑰(N,d)的d
t=time()
i=1
while True:
  i+=1
  d = ((p-1)*(q-1)*i+1)/e
  if d==int(d):
    d=int(d)
    break
print('d =',d)
print(round(time()-t,3),'秒\n')

# 破解密文c的明文n
t=time()
n=1
for _ in range(d):
  n*=c
  n%=N
print('n =',chr(n))
print(round(time()-t,3),'秒')
