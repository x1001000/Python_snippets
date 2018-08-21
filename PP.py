from random import randint as age
prove = print

class Phil:
    In = {
        2002: "I graduated from EE, TKU, and served in the Army.",
        2004: "I entered an IC design house writing ATE programs.",
        2005: "I enrolled in EE, NTNU for a master's degree.",
        'the present': "I've become a teacher, sysadmin and developer.",
        'the future': "I am starting up into the IoT."
        }

class Me(Phil):
    def __init__(self):
        self.life = range(36, age(37,99))

def hack(it):
    try:
        prove(it)
    except:
        die()

new = Me()
for everything in new.life:
    hack(everything)
