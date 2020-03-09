'''
Quang Ho
Alphabetic Telephone Number Translator
3/9/2020
Write a program that asks the user to enter a 10-character telephone number
Format of XXX-XXX-XXXX
Should display the telephone number with any alphabetic characters in the original translated to their numeric equivalent
A B C = 2
D E F = 3
G H I = 4
J K L = 5
M N O = 6
P Q R S = 7
T U V = 8
W X Y Z = 9
'''
def transNum(stringNum):
    number = 1
    #Search for any letters in the phone number
    #Translate the letters into numbers
    #Use .upper method (555-GET-FOOD)
    for ch in stringNum:
        if ch.upper() in "ABC":
            numberTranslated = 2
        elif ch.upper() in "DEF":
            numberTranslated = 3
        elif ch.upper() in "GHI":
            numberTranslated = 4
        elif ch.upper() in "JKL":
            numberTranslated = 5
        elif ch.upper() in "MNO":
            numberTranslated = 6
        elif ch.upper() in "PQRS":
            numberTranslated = 7
        elif ch.upper() in "TUV":
            numberTranslated = 8
        elif ch.upper() in "WXYZ":
            numberTranslated = 9
    return numberTranslated


def TRANSLATE_PHONE_NUM(phoneNumber):
    #If phone number has a letter in it
    #Translate it to a number
    newNumber = ""
    for ch in phoneNumber:
        if ch in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
            newNumber = newNumber + str(transNum(ch))
        else:
            newNumber = newNumber + ch
    return newNumber

def main():
    #Print out the translated phone number
    phoneNumber = input("Enter a phone number: ")
    noLetters = TRANSLATE_PHONE_NUM(phoneNumber)
    print("Translated to: ", noLetters)

main()