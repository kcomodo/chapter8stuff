import random
'''
Quang Ho
Chapter 7
Magic 8 ball
2/10/2020
Write a program that simulates a Magic 8 ball
Display yes or no responses to random questions
text file 8_ball_responses.txt, contains 12 responses
Response: "I don't think so", "Yes of course","I'm not sure" and so forth
The program should read the responses from the file into a list. It should prompt a user to ask a question
Display one of the response, randomly selected from the list
Should repeat till user quits

'''
myFile = open('8_ball_responses.txt','r')


#Had to google, didn't understand how to convert file back to a list
'''
results = []
with open('8_ball_responses.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(','))
        print(results)
'''
'''
Add in loop so user can continue playing.
Ask user if they want to quit
'''
gameStop = ""
while gameStop != "Quit":

    userInput = input("Enter a yes/no question: ")
    i = random.randint(0,11)
    randomAnswer = []
    with open('8_ball_responses.txt') as inputfile:
        for line in inputfile:
            randomAnswer.append(line.strip().split(','))
        #Unable to remove bracket around list
        #Used the .join method
        print(",".join(randomAnswer[i]))
    print("To continue, press any key and then press Enter")
    gameStop = input("Enter 'Quit' to end the game: ")
    if gameStop == "Quit":
        print("Thank you for playing the game")