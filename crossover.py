#coding:utf-8
#python2
while True:
    try:
        L = int(raw_input('左邊人數(數字)：'))
        break
    except:
        continue
while True:
    try:
        R = int(raw_input('右邊人數(數字)：'))
        break
    except:
        continue
while True:
    moves = raw_input('哪邊先走(L或R)：')
    if moves == 'L':
        moves = -1
        break
    if moves == 'R':
        moves = 1
        break

print '\n解題方法：\n左或右先走一步，\n每次換邊走跳時人數加一，\n但是以可以走跳的人數為上限。\n'

string = ''
for _ in range(L):
    string += 'L'
string += '_'
for _ in range(R):
    string += 'R'
underscore = L
print '左邊' + str(L) + '人右邊' + str(R) + '人\t' + string

def move(moves, who_to_move):
    global string, underscore
    index = underscore
    while(moves):
        if who_to_move == 'L':
            index -= 1
            moves -= 1 if string[index] == 'L' else 0
        else:
            index += 1
            moves -= 1 if string[index] == 'R' else 0
    string = string.replace('_', 'L' if who_to_move == 'L' else 'R')
    string = string[:index] + '_' + string[index+1:]
    underscore = index

def L_left_to_underscore():
    number = 0
    for char in string[:underscore]:
        if char == 'L':
            number += 1
    return number
def R_right_to_underscore():
    number = 0
    for char in string[underscore:]:
        if char == 'R':
            number += 1
    return number

while True:
    L = L_left_to_underscore()
    R = R_right_to_underscore()
    if L == 0 and R == 0:
        break
    if moves < 0:
        moves *= -1
        moves = min(moves, L)
        move(moves, 'L')
        print '左邊' + str(moves) + '人向右走跳\t' + string
        moves += 1
    else:
        moves = min(moves, R)
        move(moves, 'R')
        print '右邊' + str(moves) + '人向左走跳\t' + string
        moves += 1
        moves *= -1
