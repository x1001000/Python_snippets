# itertools.permutations(iterable[, r])
def permutations_list(string):
    result_list = []
    if len(string) == 2:
        return [string[0]+string[1],string[1]+string[0]]
    for i in range(len(string)):
        sub_string_list = permutations_list(string[:i]+string[i+1:])
        for sub_string in sub_string_list:
            result_list.append(string[i]+sub_string)
    return result_list

string = input('Input a string: ')
n = 0
for i in permutations_list(string):
    n+=1
    print(i,n)

# 解某直式
for p in permutations_list('123456789'):
    d=[]
    for c in p:
        d.append(int(c))
    if (d[0]*10+d[1])*d[2] == d[3]*10+d[4]:
        if d[3]*10+d[4] + d[5]*10+d[6] == d[7]*10+d[8]:
            print(d)
