def countString(myString):
    '''
    Declaring counter variable to keep a running total
    of all different character types we encounter
    '''
    totalChars = 0
    digitCount = 0
    spaceCount = 0
    alphaCount = 0
    upperCase = 0
    lowerCase = 0
    noneOfTheAbove = 0

    for ch in myString:
        totalChars += 1
        if ch.isDigit():
            digitCount += 1
        elif ch.isspace():
            spaceCount += 1
        elif ch.isalpha():
            alphaCount +=1
            if ch.isUpper():
                upperCase += 1
            else:
                lowerCase += 1
        else:
            noneOfTheAbove+=1

    print("Total characters: ", totalChars)
    print("Total digit count:" + str(digitCount))
    print("Space count: ", spaceCount)
    print("Alpha count: ", alphaCount)
    print("Upper count: ", upperCase)
    print("Lower count: ", lowerCase)
    print("Other count: ", noneOfTheAbove)
def main():
        countString("Now is the winter of our discontent, #45^")
main()