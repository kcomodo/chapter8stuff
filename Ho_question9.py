'''
Quang Ho
Sentence Capitalizer
3/9/2020
Write a program with a function that accepts a string as an argument and returns a copy of the string
First letter of each sentence capitalized
Ex: hello. my name is joe. what is your name? = Hello. My Name Is Joe. What Is Your Name?
The program should ask the user to enter a sentence and the pass it to a function
Modified string should be displayed
'''
def main():
    #Ask user to enter a sentence
    userInput = input("Enter a sentence: ")
    #Split word by finding the spaces
    wordSplit = userInput.split(' ')
    wordAppend = []
    for word in wordSplit:
        wordTitle = word[0].upper() + word[1:]
        wordAppend.append(wordTitle)
    #After capitalizing the word, join them back together
    capitalized_word = ' '.join(wordAppend)
    print(capitalized_word)
main()