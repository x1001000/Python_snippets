def isSubset(strA, strB):
    strA_dict = dict()
    for letter in strA:
        strA_dict[letter] = True
    try:
        for letter in strB:
            if(strA_dict[letter]):
                continue
        return True
    except:
        return False
    return False

def main():
    print isSubset('ABCDE', 'ACD')
    print isSubset('ABCEE', 'ACD')

if __name__ == "__main__":
    main()
