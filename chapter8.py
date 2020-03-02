def main():
    '''
    for count in range (10):
        print("Z"*count)
    print("-"*25)
    for count in range (1,10):
        print("Z"*count)
    '''
    '''
    myString = input("Give me a string: ")
    print("Your string is: ", myString)

    if myString.isalnum():
        print("It is alphanumeric")
    if myString.isalnum():
        print("Is a digit")
    if myString.isalpha():
        print("Is alpha")
    if myString.isspace():
        print("It is a space")
    if myString.isupper():
        print("Its upper")
    if myString.islower():
        print("Its lower")
    '''
    name = "John"
    print("Name: ",name)
    name += " "
    name += "Doe"
    print("Name: ", name)
    firstname = input("First name: ")
    lastname = input("Last name: ")
    name = firstname.strip() + " " + lastname.strip()
    print("New name:", name)

main()