###
### CS 4811 - AI
### TEAM: Maria
### NAMES: Justin Milliman, Drake Parker, Saeed Peyman, Jack Snowden
### Last Modified: 1/18/2023
###

from random import *

# The computer should load a game when the following gets called.
# Open the 'words_alpha.txt' file and select a random word

#### CONSTANTS
WORD_SRC = 'words_alpha.txt'
WORD_LEN = 5 # 
MAX_ATTEMPTS = 6
MATCH_GREEN = '\033[92m'
CLOSE_ORANGE = '\033[93m'
ENDC = '\033[0m'

NO_MATCH = 0
CLOSE_MATCH = 1
MATCH = 2

#### Mutable variables / game state controls
mysteryWord = []
playerGuess = [] 
guessMatch  = []
gameActive  = False
playerAttempts = 0
wordPool = []

def playWordle():
    global mysteryWord
    global playerAttempts
    global gameActive
    global playerGuess
    global wordPool
    
    # Open the file
    f = open(WORD_SRC, "r")

    # Filter list for word length
    for line in f:
        newLine = line.strip()
        if len( newLine ) == WORD_LEN: wordPool.append(newLine)
     
    # Grab a rando word
    index = randint(0, len(wordPool) )
    
    # mysteryWord = [*wordPool[index]]
    mysteryWord = "wormy"
    playerAttempts = 0
    gameActive = True
    
    # Instantiate player guess to NONE
    for _ in range(WORD_LEN):
        playerGuess.append("*") 
        guessMatch.append(NO_MATCH) 
    
    print("==> GAME STARTED!")
    
    
    
# Make a guess with the given word
def makeGuess(word):
    global playerGuess
    global guessMatch
    global playerAttempts
    
    print(f"==> Guessing {word}")
    playerGuess = [*word]
    playerAttempts += 1    
    
# Give up the game by doing the thing in here
def giveUp():
    print("Should do something... :)")
    
# Draw the current state of the game
def showState():
    global guessMatch
    print("==> Showing State:")
    print("================================")
    print(f"Game In Progess? --> {gameActive}")
    print("Attempts Made / Total Attempts -->", playerAttempts, "/", MAX_ATTEMPTS)
    print("Mystery Word -->", end=" "),
    for i in range(WORD_LEN):
        if playerGuess[i] == mysteryWord[i]:
            print(f"{MATCH_GREEN}{playerGuess[i]}{ENDC}", end="")
            guessMatch[i] = [MATCH, playerGuess[i]]
        elif playerGuess[i] in mysteryWord:
            print(f"{CLOSE_ORANGE}{playerGuess[i]}{ENDC}", end="")
            guessMatch[i]
        else:
            print(playerGuess[i], end="")
    print()
    print("================================")
    
    
def playerAI():
    global wordPool
    
    playWordle()
    for _ in range(MAX_ATTEMPTS):
        makeGuess(wordPool[randint(0, len(wordPool) )])
        showState()
        

playerAI()