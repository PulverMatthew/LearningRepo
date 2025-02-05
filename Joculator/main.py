import os

# Returns the value of the specifed line in save file. 
def checkSave(index):
    # Reads the save file and saves as a variable then closes.
    saveFile = open('save.txt', 'r')
    data = saveFile.readlines()
    saveFile.close()

    selectedData = data[index]
    print(selectedData)
    return str(selectedData).strip()
    
# Makes a save file in the game's main script directory.
def saveFileGeneration():
    # Try to see if the save file is readable. If it isn't, likely doesn't exist.
    try:
        saveFile = open('save.txt', 'r')
        saveFile.close()
    
    # Make a new save file with default values.
    except:
        clearScreen()
        print("No save file found. Making save file.")
        input('Press enter to continue...')
        saveFile = open('save.txt', 'w')
        data = [
        '4', # 1. Number of Hands
        '4', # 2. Number of Discards
        '7', # 3. Hand Size
        'False' # Has a game already been started?
        ]
        for lines in range(4):
            saveFile.write(f"{data[lines]}\n")
        saveFile.close() 

# Clear the terminal screen in a cross-platform way.
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def menuDisplay(options):
    # Displays custom menu options
    for key, value in options.items():
        #Utilizes an f-string to embed the key and value variable declared in the for loop.
        print(f"{key}: {value}")

# Settings menu, allows user to define variables for gameplay.
def settings():
    # Reads save file and copies it to variable 'data' then closes.
    saveSettings = False
    saveFile = open('save.txt', 'r')
    data = saveFile.readlines()
    saveFile.close()

    # Opens save file in write mode. Loops until player has confirmed every setting changed.
    saveFile = open('save.txt', 'w')
    while not saveSettings:
        clearScreen()
        menuOptions = {
            '1': 'Number of Hands',
            '2': 'Number of Discards',
            '3': 'Hand Size',
            '4': 'Save Settings'
            }
        print('Game Options:\n')
        menuDisplay(menuOptions)
        gameInput = input('Choose an option: ')
        match gameInput:

            case '1':
                gameInput = input('How many hands should the next game have? ')
                data[0] = str(gameInput) + '\n'
                saveSettings = False

            case '2':
                gameInput = input('How many discards should the next game have? ')
                data[1] = str(gameInput) + '\n'
                saveSettings = False

            case '3':
                gameInput = input('How many cards should your hand hold? ')
                data[2] = str(gameInput) + '\n'
                saveSettings = False

            case '4':
                for lines in range(4):
                    saveFile.write(f"{data[lines]}")                
                saveFile.close()
                saveSettings = True
    
# Game loop, shows the main game logic. 
def playGame():
    clearScreen()

    # Placeholder logic. Checks to see if the player has played the game before.
    hasPreviousGame = checkSave(3)

    # Continues the game based on given save data.
    if hasPreviousGame == 'True':
        print('Player has played game before')
    
    # Writes to the save file to mark the game as started.
    elif hasPreviousGame == 'False':
        print("This is player's first game")
        saveFile = open('save.txt', 'r')
        data = saveFile.readlines()
        data[3] = 'True'
        saveFile.close()
        saveFile = open('save.txt', 'w')
        for lines in range(4):
            saveFile.write(f"{data[lines]}")
        saveFile.close() 

    # Displays an error and quits out of the game loop.
    else:
        print("Save game has been modified or another error has occurred.")
        gameLoop = False
    input('Press enter to continue...')

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
        gameInput = input('Choose an option: ')
        if gameInput not in menuOptions:
            clearScreen()
            print('Please choose a valid option.\n')
            input('Press enter to continue...')
            continue
        match gameInput.lower():
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
                input('Press enter to continue...')
            case '4' | 'quit':
                clearScreen()
                gameLoop = False

if __name__ == '__main__':
    main()
    