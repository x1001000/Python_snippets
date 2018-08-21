# Return True if the given string contains an appearance of abc where
# the abc is not directly preceded by a period (.). So aabc counts
# but a.abc does not.
#
# abc(’qweabc’) -> True
# abc(’qwe.abc’) -> False
# abc(’abc.qwe’) -> True

def abc(s):
    for i in range(len(s) - 2): 
        if s[i:i+3] == 'abc':
            if s[i-1] != '.':
                return True
    return False
    pass

def main():
    assert abc('qweabc')
    assert not abc('qwe.abc')
    assert abc('abc.qwe')

if __name__ == "__main__":
    main()

# Not familiar with assert
## Assert is simple, it raise exception if the statement return false.
# Got it
# Am I far from the solution? :(
## okay, thanks for your time
## I will email you again to arrange another face to face interview in TW office
## see you!
# Thanks!
# See you!
