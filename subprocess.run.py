from time import ctime, sleep
from subprocess import run
while True:
    print('____________________________________________________________')
    print(ctime())
    run('ping 172.21.2.88')
    sleep(57)
