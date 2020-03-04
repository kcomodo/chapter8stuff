'''
Quang Ho
Chapter 7
Driver license exam
2/6/2020
Write a program that grades the writer portion of the driver's license exam
Program should store correct answer in a list. Program should read the users answer from a text file
(Create your own text file)
Read file and display a message indicating if the student has failed or pass (15 out of 20)
Should display the total number of correctly answered questions and incorrect
Display a list showing the question numbers of the incorrectly answered questions

'''
#Create file for the correct answer
correctAnswer = ["A","C","A","A","D","B","C","A","C","B","A","D","C","A","D","C","B","B","D","A"]
myFile = open('correctList.txt', 'w')
for element in correctAnswer:
    myFile.write(element)
    myFile.write('\n')
myFile.close()
userAnswer = [""] * 20
i = 0
#Ask user for answer and put it in file
while(i < correctAnswer.__len__()):
    print("Question", i+1)
    userInput = input("Answer: ")
    userAnswer[i] = userInput
    i+=1
myFileTwo = open('answerList.txt','w')
for element in userAnswer:
    myFileTwo.write(element)
    myFileTwo.write('\n')
myFileTwo.close()
count = 0
#Compare the two list
if len(userAnswer) == len(correctAnswer):
    for i in range(len(userAnswer)):
        if userAnswer[i] == correctAnswer[i]:
            count+=1
#Display the score and print if the user pass or fail
print(count,"/20")
if(count >= 15):
    print("You passed")
else:
    print("You failed")