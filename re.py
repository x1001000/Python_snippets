import re
import sys
str=""
with open('testdata.txt') as f:
    for line in f:
        str += line[:-1]
#print(str)
while True:
    match1 = re.search('\-?\d+\.?\d*\*10\^\d+', str)
    match2 = re.search('\-?\d+\.?\d*', str)
    if match1 or match2:
        match = match1 if match1 else match2
        number = match.group(0)
        print(number)
        str = str[str.find(number)+len(number):]+str[:str.find(number)]
    else:
        break
