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

if __name__ == '__main__':
    while True:
        try:
            L = int(input('左邊青蛙數：'))
            R = int(input('右邊青蛙數：'))
            break
        except:
            print('抱歉！請重新輸入整數...')
    while True:
        moves = input('哪邊先走(L或R)：')
        if moves == 'L':
            moves = -1
            break
        elif moves == 'R':
            moves = 1
            break
        else:
            print('抱歉！請重新輸入L或R...')

    string = ''
    for _ in range(L):
        string += 'L'
    string += '_'
    for _ in range(R):
        string += 'R'
    underscore = L
    lines =  ['','解題邏輯：','左或右先走一隻，','每次換邊走跳隻數加一，','加一超過隻數就全數走跳。']
    lines += ['','解題過程：\t'+string]

    while True:
        L = L_left_to_underscore()
        R = R_right_to_underscore()
        if L == 0 and R == 0:
            break
        if moves < 0:
            moves *= -1
            moves = min(moves, L)
            move(moves, 'L')
            lines += ['左邊'+str(moves)+'隻向右走跳\t'+string]
            moves += 1
        else:
            moves = min(moves, R)
            move(moves, 'R')
            lines += ['右邊'+str(moves)+'隻向左走跳\t'+string]
            moves += 1
            moves *= -1
    
    for line in lines:
        print(line)