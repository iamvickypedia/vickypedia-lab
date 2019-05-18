# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(msg):
     cipher = ""
     for word in msg:
          for a_word in word:
               cipher += MORSE_CODE_DICT[a_word] + "█"*3
          cipher += "█"*7
     return cipher


if __name__ == '__main__':
     print("Length of a dot is 1 unit")
     print("Length of a dash is 3 units")
     print("Space between parts of same letter is one unit")
     print("Space between letters is ███(3 units)")
     print("Space between words is ███████(7 units)")
     sent = input('Enter the sentence\n')
     print(encrypt(sent.upper().split(' ')))