from util import validatedInput, checkSave, readSave, writeSave, saveFileGeneration, clearScreen, menuDisplay
import os
# Settings menu, allows user to define variables for gameplay.
def settings():
    # Reads save file and copies it to variable 'data' then closes.
    saveSettings = False
    data = readSave('save.txt')
    # Opens save file in write mode. Loops until player has confirmed every setting changed.
    while not saveSettings:
        clearScreen()
        print(data)
        menuOptions = {
            '1': 'Number of Hands',
            '2': 'Number of Discards',
            '3': 'Hand Size',
            '4': 'Save Settings'
            }
        print('Game Options:\n')
        menuDisplay(menuOptions)
        gameInput = validatedInput('Choose an option: ', menuOptions.keys())
        
        match gameInput:
            case '1':
                gameInput = validatedInput('How many hands should the next game have? ')
                # Replaces null value with 1 specifically for this menu.
                if gameInput == None:
                    gameInput = 1
                data[0] = str(gameInput) + '\n'
                saveSettings = False

            case '2':
                gameInput = validatedInput('How many discards should the next game have? ')
                # Replaces null value with 1 specifically for this menu.
                if gameInput == None:
                    gameInput = 1
                data[1] = str(gameInput) + '\n'
                saveSettings = False

            case '3':
                gameInput = validatedInput('How many cards should your hand hold? ')
                # Replaces null value with 1 specifically for this menu.
                if gameInput == None:
                    gameInput = 1
                data[2] = str(gameInput) + '\n'
                saveSettings = False

            case '4':
                writeSave('save.txt', data)
                saveSettings = True
            case _:
                saveSettings = False
                
# Game loop, shows the main game logic. 
def playGame():
    clearScreen()
    # Checks to see if the player has played the game before.
    hasPreviousGame = checkSave(3)
    pass

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
        gameInput = validatedInput('Choose an option: ', menuOptions.keys())
        match gameInput:
            case '1':
                playGame()
            case '2':
                settings()
            case '3':
                clearScreen()
                print('Joculator, based on the hit game Balatro\n')
                print('Balatro by: LocalThunk')
                print('Programming by: Matthew Pulver')
                print('Planning by: Matthew Pulver')
                validatedInput('Press enter to continue...')
            case '4':
                clearScreen()
                gameLoop = False
            case _:
                continue


if __name__ == '__main__':
    main()
    