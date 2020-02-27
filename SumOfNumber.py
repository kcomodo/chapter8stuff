'''
Quang Ho
Chapter 6
Sum of number
1/30/20
'''

'''
Write a program that asks the user to enter a file name (number.txt)

'''
def main():
    filename = input("Please enter a file name: ")
    try:
        infile = open(filename,'r')
        num1 = int(infile.readline())
        num2 = int(infile.readline())
        num3 = int(infile.readline())
        num4 = int(infile.readline())
        num5 = int(infile.readline())
        num6 = int(infile.readline())

        total = num1 + num2 + num3 + num4 + num5 + num6
        print(total)
    except IOError:
        print("An error has occured reading your file ")
        print("which was named", filename)
    except:
        print("Unhandled exception has occured")
    finally:
        print("Always run")
    infile.close()
main()