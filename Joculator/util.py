import os

# Validates given input against given menu options. Can work without menu options.
def validatedInput(message, validOptions = None):
    # Try to take input. If the input is blank replace input with 1. If validOptions is left blank or the input is valid return the input. 
    try:
        defInput = input(message)
        # Patchwork fix, causes issue where the play game is selected in the main menu.
        if defInput is None or defInput == '':
            defInput = '1'
        elif validOptions is None or defInput in validOptions:
            return defInput
    except EOFError:
        input('Unexpected end of input. Please try again.')
    except KeyboardInterrupt:
        input('Input interrupted. Please try again.')
    except ValueError:
        input('Invalid input. Please enter the correct type of value.')
    # Handles any other exception.
    except Exception as e:
        input(f'Unknown error {e} occurred. Please try again.')



# List of allowed filenames
filenamesAllowed = ['save.txt']

# Returns the value of the specifed line in save file. 
def checkSave(filename, index):
    # Reads the save file and saves as a variable then closes.
    if filename not in filenamesAllowed:
        raise ValueError('Invalid filename')
    with open(filename, 'r') as saveFile:
        data = saveFile.readlines()
    saveFile.close()

    selectedData = data[index]
    return str(selectedData).strip()

# Reads save file and returns its content as a list of lines.
def readSave(filename):
    if filename not in filenamesAllowed:
        raise ValueError('Invalid filename')
    with open(filename, 'r') as saveFile:
        data = saveFile.readlines()
    return data

# Writes the provided data to the save file.
def writeSave(filename, data):
    if filename not in filenamesAllowed:
        raise ValueError('Invalid filename')
    with open(filename, 'w') as saveFile:
        saveFile.writelines(data) 

# Makes a save file in the game's main script directory.
def saveFileGeneration():
    # Try to see if the save file is readable. If it isn't, likely doesn't exist.
    try:
        saveFile = readSave('save.txt')
    # Make a new save file with default values.
    except:
        clearScreen()
        print('No save file found. Making save file.')
        validatedInput('Press enter to continue...')
        data = [
        '4\n', # 1. Number of Hands
        '4\n', # 2. Number of Discards
        '7\n', # 3. Hand Size
        'False\n' # Has a game already been started?
        ]
        writeSave('save.txt', data)

# Clear the terminal screen in a cross-platform way.
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
# Displays custom menu options
def menuDisplay(options):
    for key, value in options.items():
        #Utilizes an f-string to embed the key and value variable declared in the for loop.
        print(f"{key}: {value}")
