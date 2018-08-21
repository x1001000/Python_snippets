A = list(range(5,0,-1))
B = []
C = []

def printABC():
    global A,B,C
    print(A)
    print(B)
    print(C)
    print('')

def hanoi(number, from_tower, to_tower, thru_tower):
    if number == 1:
        to_tower.append(from_tower.pop())
        printABC()
        return
    hanoi(number-1, from_tower, thru_tower, to_tower)
    to_tower.append(from_tower.pop())
    printABC()
    hanoi(number-1, thru_tower, to_tower, from_tower)

printABC()
hanoi(len(A),A,C,B)
