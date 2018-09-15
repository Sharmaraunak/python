# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretClone = list(secretWord)
    if lettersGuessed == [] or len(secretWord) == 0:
        return False
    else:
        for i in lettersGuessed:
            if i in secretWord:
                for letter in secretWord:
                    if i in secretClone:
                        secretClone.remove(i)
                
                if secretClone !=[]:
                    ans = False
                else:
                    ans = True
                if secretClone == []:
                    break
            else:
               ans = False
        return ans

    
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    printList = list(len(secretWord)*'_')
    secretList = list(secretWord)
    myDict = {}
    for i in range(len(secretWord)):
        myDict[i] = secretList[i]
    for i in lettersGuessed:
        for value in myDict:
            if myDict[value] == i:
                printList[value] = myDict[value]
                myDict[value] = '#'
    return ' '.join(printList)

    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        availableLetters.remove(letter)
    return ''.join(availableLetters)
    
   
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    word = secretWord
    print("I am thinking of a word that is",len(word),"letters long.")
    numguesses = 8
    guessList = []
    while numguesses>0:
        print("----------------------")
        print("You have",numguesses,"guesses left")
        print("Available Letters:",getAvailableLetters(guessList))
        guess = input("Please guess a letter: ")
        if guess not in guessList:
            guessList.append(guess)
            if guess in word:
                print("Good guess:",getGuessedWord(secretWord,guessList))
            else:
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord,guessList))
                numguesses-=1
        else:
            print("Oops! You've already guessed that letter: ",end = '')
            print(getGuessedWord(secretWord,guessList))
            
       
           
           # print("you have",numguesses,"guesses left")
        end = isWordGuessed(word,guessList)
        if end == True:
            print("----------------------")
            print("Congratulations, you won!")
            break
        if numguesses == 0:
            print("----------------------")
            print("Sorry, you ran out of guesses.The word was",word)
        
        
        
    
    
     
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
