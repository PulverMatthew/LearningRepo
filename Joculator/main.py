import os

def clearScreen():
    # Clear the terminal screen in a cross-platform way.
    os.system('cls' if os.name == 'nt' else 'clear')
    
def displayMenu(options):
    # Displays custom menu options
    for key, value in options.items():
        print(f"{key}: {value}")

# Game loop, shows the main game logic. 
#def playGame():
    

# Settings menu, allows user to define variables for gameplay.
#def settings():

# Main loop, mostly for menu purposes.
def main():
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
        displayMenu(menuOptions)
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