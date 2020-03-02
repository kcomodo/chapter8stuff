def main():
    '''
    myString = "One, Two, Three, Four"
    myWordList = myString.split(', ')
    print(myWordList)
    '''
    '''
    myIPAddresses = ''
    for i in range (255):
        myIPAddresses += mySubNet+str(i)+','

        print(myIPAddresses)
    '''
    '''
    myNumbers = "23456789"
    myEvenNumbers = myNumbers[1:len(myNumbers):2]
    print("Even: "+myEvenNumbers)
    myOddNumbers = myNumbers[0:len(myNumbers):2]
    print("Odd: "+myOddNumbers)
    '''
    '''''
    myNumbers = '1234.00 92.241111.11'
    myOddNumbers = myNumbers[0:len(myNumbers):7]
    print("Odd: "+myOddNumbers)
    '''
    fullName = "John Adam Doe"
    firstName = fullName[0:4]
    middleName = fullName[5:9]
    lastName = fullName[10:]
    print(firstName)
    print(middleName)
    print(lastName)
main()