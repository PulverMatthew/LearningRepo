from util import clearScreen, checkSave
from cards import pokerCard, pokerDeck
# Game loop, shows the main game logic. 
def playGame():
    clearScreen()
    # Checks to see if the player has played the game before.
    hasPreviousGame = checkSave('save.txt', 3)