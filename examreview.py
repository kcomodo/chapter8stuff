import random
'''
Quang Ho
Exam review
2/12/2020
Write a program that will assign 10 random values for potential home prices
Values should be in range from 50,000 - 550,000
Should be stored in a text file
The program should read the information from the file and output the following information:
Lowest sale in list
Highest sale in list
Total of all sale in list
Average of all sales in list

'''
def main():
    i = 0
    average = 0
    total = 0
    filename = open('randomNumbers.txt', 'w')

    #10 random number value
    while(i < 10):
        randomNum = random.randint(50000,550000)
        total = total+randomNum
        filename.write(str(randomNum) + '\n')
        i+=1
    filename = open('randomNumbers.txt', 'r')
    #convert list to int and not string
    intlst = [int(x) for x in filename]
    count = 0
    highestNum = intlst[0]
    lowestNum = intlst[0]
    #find lowest and highest
    while(count < 10):
        if(intlst[count] > highestNum):
            highestNum = intlst[count]
        if(intlst[count] < lowestNum):
            lowestNum = intlst[count]
        count+=1
    average = total/10

    #print lowest, highest, total and average sale price
    print("Highest sale price: ",'{:,.2f}'.format(highestNum))
    print("Lowest sale price: ", '{:,.2f}'.format(lowestNum))
    print("Total sale price: ", '{:,.2f}'.format(total))
    print("Average sale price: ",'{:,.2f}'.format(average))

main()