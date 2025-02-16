"""
util.py: provides utility functions for the rest of Joculator:
    validate_input validates given inputs, used for menus.
    check_file, read_file, write_file do file handling tasks.
    save_generation makes a save file if one doesn't exist.
    clear_screen clears the screen and is cross-platform on Linux and Windows.
    menu_display provides a readable alternative for making menu options.
"""
import os

# Validates given input against given menu options. Can work without menu options.
def validate_input(message, valid_options=None):
    """
    Validates the provided input message against the valid_options.

    Parameters:
        message (str): The input provided by the user.
        valid_options (list, optional): A list of valid options. If None, any message is valid.

    Returns:
        str: The original message if it is valid.
    """
    try:
        if valid_options is None or message in valid_options:
            return message
    except KeyboardInterrupt:
        clear_screen()
        print("Input was cancelled by the user. Exiting.")
        exit(0)
    except ValueError as ve:
        print(f"Input error: {ve}")

# List of allowed filenames
filenamesAllowed = ['save.txt']

# Returns the value of the specified line in file.
def check_file(filename, index):
    """
    Returns the content of the specified line in the file.

    Parameters:
        filename (str): The name of the file to read.
        index (int): The index of the line to retrieve.

    Returns:
        str: The content of the specified line, stripped of extra whitespace.

    Raises:
        ValueError: If the filename is not allowed.
    """
    if filename not in filenamesAllowed:
        raise ValueError('Invalid filename')
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.readlines()
    # Explicit close is not needed due to context manager usage.
    selected_data = data[index]
    return str(selected_data).strip()

# Reads file and returns its content as a list of lines.
def read_file(filename):
    """
    Reads the provided file and returns its contents as a list of lines.

    Parameters:
        filename (str): The name of the file to read.

    Returns:
        list: A list containing each line from the file.

    Raises:
        ValueError: If the filename is not allowed.
    """
    if filename not in filenamesAllowed:
        raise ValueError('Invalid filename')
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

# Writes the provided data to the file.
def write_file(filename, data):
    """
    Writes the provided data to a file.

    Parameters:
        filename (str): The name of the file to write to.
        data (list): A list of strings to write into the file.

    Raises:
        ValueError: If the filename is not allowed.
    """
    if filename not in filenamesAllowed:
        raise ValueError('Invalid filename')
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(data)

# Makes a save file in the game's main script directory.
def save_generation():
    """
    Checks for the existence of the save file. If the save file is not found, 
    creates one with default values.
    """
    try:
        read_file('save.txt')
    except FileNotFoundError:
        clear_screen()
        print('No save file found. Making save file.')
        input('Press enter to continue...')
        data = [
            '4\n',  # 1. Number of Hands
            '3\n',  # 2. Number of Discards
            '7\n',  # 3. Hand Size
            'Jack Joculator\n', # 4. Name
            '1\n', # 5. Current ante
            '1\n', # 6. Current round
            '4\n', # 7. Current Money
            'Default\n', # 8. Chosen card deck
            'False\n'  # Has a game already been started?
        ]
        write_file('save.txt', data)

# Clear the terminal screen in a cross-platform way.
def clear_screen() -> None:
    """
    Clears the terminal screen using the appropriate command for the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Displays custom menu options.
def menu_display(options):
    """
    Displays menu options on the console.

    Parameters:
        options (dict): A dictionary of options where the key is option and value is descriptor.
    """
    for key, value in options.items():
        print(f"{key}: {value}")
