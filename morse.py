# a alphabet_morse dictionary
# a space between 2 alphabet words is represented by a slash between 2 morse codes
alphabet_morse ={
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    " " : "/"
    }

# a morse_alphabet dictionary
morse_alphabet = dict((v,k) for (k,v) in alphabet_morse.items())

# encode a alphabet_string into a morse_string
def encode_alphabet_morse(alphabet_string):
    morse_string = ""
    for char in alphabet_string:
        morse_string += alphabet_morse[char.upper()] + " "
    return morse_string

# decode a morse_string into a alphabet_string
def decode_morse_alphabet(morse_string):
    alphabet_string = ""
    letter= ""
    for char in morse_string:
        if char == " ":
            try:
                alphabet_string += morse_alphabet[letter]
                letter= ""
            except:
            # happens at the space after the slash
                continue
        elif char == "/":
            alphabet_string += " "
        else:
            letter += char
    alphabet_string += morse_alphabet[letter]
    return alphabet_string

def main():
    input_string = raw_input('\nInput a string to encode or decode, for example:\n\nI am 1001000\nor\n.. / .- -- / .---- ----- ----- .---- ----- ----- -----\n\nInput:\n')
    try:
        print 'Encoded:\n' + encode_alphabet_morse(input_string)
    except:
        try:
            print 'Decoded:\n' + decode_morse_alphabet(input_string)
        except:
            print 'Wrong format!'

if __name__ == "__main__":
	main()
