"""
Main module of the game. Contains functions for settings
and for the main menu. 
"""
from util import validate_input, read_file, write_file, save_generation, clear_screen, menu_display
from game import playGame

def settings():
    """
    Settings function which allows the user to modify the save file containing game settings.
    Settings cannot be changed if a game is currently being played, stored by the 4th line of the save file.
    This is mainly meant to prevent cheating, but nothing stops you from modifying the save file. 
    """
    # Reads save file and copies it to variable 'data' then closes.
    save_settings = False
    data = read_file('save.txt')
    # Opens save file in write mode. Loops until player has confirmed every setting changed.
    while not save_settings:
        clear_screen()
        for entry in data:
            print(entry.strip(), end=', ')
        print()
        menu_options = {
            '1': 'Number of Hands',
            '2': 'Number of Discards',
            '3': 'Hand Size',
            '4': 'Save Settings'
        }
        print('Game Options:\n')
        menu_display(menu_options)
        user_input = input('Choose an option: ')
        game_input = validate_input(user_input, menu_options)

        match game_input:
            case '1':
                user_input = input('How many hands should the next game have? ')
                game_input = validate_input(user_input)
                # Replaces null value with 1 specifically for this menu.
                if game_input == '':
                    game_input = 1
                data[0] = str(game_input) + '\n'
                save_settings = False

            case '2':
                user_input = input('How many discards should the next game have? ')
                game_input = validate_input(user_input)
                # Replaces null value with 1 specifically for this menu.
                if game_input == '':
                    game_input = 1
                data[1] = str(game_input) + '\n'
                save_settings = False

            case '3':
                user_input = input('How many cards should your hand hold? ')
                game_input = validate_input(user_input)
                # Replaces null value with 1 specifically for this menu.
                if game_input == '':
                    game_input = 1
                data[2] = str(game_input) + '\n'
                save_settings = False

            case '4':
                write_file('save.txt', data)
                save_settings = True

            case _:
                save_settings = False

def main():
    """
    Main loop, only valid way to start the program and contains the main menu.
    Access the game, game settings, credits menu, and exit from here.
    """
    save_generation()
    game_loop = True
    while game_loop:
        menu_options = {
            '1': 'Play',
            '2': 'Settings',
            '3': 'Credits',
            '4': 'Quit'
        }
        clear_screen()
        print('Welcome to Joculator\n')
        menu_display(menu_options)
        user_input = input('Choose an option: ')
        game_input = validate_input(user_input, menu_options)

        match game_input:
            case '1':
                playGame()

            case '2':
                settings()

            case '3':
                clear_screen()
                credits_menu = {
                    'Joculator, based on the game "Balatro"': '',
                    'Balatro by': 'LocalThunk',
                    'Programming by': 'Matthew Pulver',
                    'Planning by': 'Matthew Pulver'
                }
                menu_display(credits_menu)
                user_input = input('Press enter to continue...')
                validate_input(user_input)

            case '4':
                clear_screen()
                game_loop = False

            case _:
                continue


if __name__ == '__main__':
    main()
