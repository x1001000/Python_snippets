from time import time  # from time module import time function
MAX = int(input('請輸入一個整數，例如 1001000 👉'))
print('\n計算中，請稍候。。。\n')
start = time()
is_prime = [False,False]+[True]*(MAX-1)
primes = ['佔住位置0讓位置N為第N個質數']
now = 2
while True:
    primes.append(now)
    for i in range(now*2, MAX+1, now):
        is_prime[i] = False
    now += 1
    try:
        while is_prime[now] == False:
            now += 1
    except:
        break
print('篩法只用了',round(time()-start,3),'秒篩出',len(primes)-1,'個',MAX,'以下的質數！')
print('想知道第 500 個優質的質數同學是幾號嗎？')
print('試試在 Python Shell 這邊輸入 primes[500]')
