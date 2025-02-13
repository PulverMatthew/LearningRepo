from util import validatedInput, readSave, writeSave, saveFileGeneration, clearScreen, menuDisplay
from cards import pokerCard, pokerDeck
from game import playGame
import os
# Settings menu, allows user to define variables for gameplay.
def settings():
    # Reads save file and copies it to variable 'data' then closes.
    saveSettings = False
    data = readSave('save.txt')
    # Opens save file in write mode. Loops until player has confirmed every setting changed.
    while not saveSettings:
        clearScreen()
        for i, entry in enumerate(data):
            print(entry.strip(), end = ', ')
        print()
        menuOptions = {
            '1': 'Number of Hands',
            '2': 'Number of Discards',
            '3': 'Hand Size',
            '4': 'Save Settings'
            }
        print('Game Options:\n')
        menuDisplay(menuOptions)
        userInput = input('Choose an option: ')
        gameInput = validatedInput(userInput, menuOptions)
        
        match gameInput:
            case '1':
                userInput = input('How many hands should the next game have? ')
                gameInput = validatedInput(userInput)
                # Replaces null value with 1 specifically for this menu.
                if gameInput == '':
                    gameInput = 1
                data[0] = str(gameInput) + '\n'
                saveSettings = False

            case '2':
                userInput = input('How many discards should the next game have? ')
                gameInput = validatedInput(userInput)
                # Replaces null value with 1 specifically for this menu.
                if gameInput == '':
                    gameInput = 1
                data[1] = str(gameInput) + '\n'
                saveSettings = False

            case '3':
                userInput = input('How many cards should your hand hold? ')
                gameInput = validatedInput(userInput)
                # Replaces null value with 1 specifically for this menu.
                if gameInput == '':
                    gameInput = 1
                data[2] = str(gameInput) + '\n'
                saveSettings = False

            case '4':
                writeSave('save.txt', data)
                saveSettings = True
            case _:
                saveSettings = False
                
# Main loop, mostly for menu purposes.
def main():
    saveFileGeneration()
    gameLoop = True
    while gameLoop:
        menuOptions = {
            '1': 'Play',
            '2': 'Settings',
            '3': 'Credits',
            '4': 'Quit'
        }
        clearScreen()
        print('Welcome to Joculator\n')
        menuDisplay(menuOptions)
        userInput = input('Choose an option: ')
        gameInput = validatedInput(userInput, menuOptions)

        match gameInput:
            case '1':
                playGame()

            case '2':
                settings()

            case '3':
                clearScreen()
                creditsMenu = {
                    'Joculator, based on the game "Balatro"': '',
                    'Balatro by': 'LocalThunk',
                    'Programming by': 'Matthew Pulver',
                    'Planning by': 'Matthew Pulver'
                }
                menuDisplay(creditsMenu)
                userInput = input('Press enter to continue...')
                validatedInput(userInput)

                
            case '4':
                clearScreen()
                gameLoop = False

            case _:
                continue


if __name__ == '__main__':
    main()
    