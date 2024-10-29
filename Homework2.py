# Eddie Neitenbach
# UWYO COSC 1010
# 10/29/24
# HW 02
# Lab Section: 11
# Sources, people worked with, help given to: 
# your
# comments
# here


def translate(string):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..'
    }
    
    product = ""
    for letter in string:  
        if letter.isalpha():  
            product += morse_code[letter.upper()] + " " 
        elif letter == " ":
            product += "  "



    return product.strip
word = input("Hello") 
produced = translate(word) 
print(produced)
