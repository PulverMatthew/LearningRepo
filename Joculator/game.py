"""
Game module, houses the game logic for readability.
"""
from util import clear_screen, check_file, write_file, read_file, validate_input, save_generation
from settings import settings
from player import Player
# from cards import PokerCard, PokerDeck
def play_game():
    """
    Basic game loop.
    """
    clear_screen()
    # Checks to see if the player has played the game before.
    has_previous_game = check_file('save.txt', 8).strip()
    # Update to reflect new game having been started
    if has_previous_game == 'False':
        data = read_file('save.txt')
        data[8] = 'True\n'
        write_file('save.txt', data)
    # Check to see if the player wants to restart the game or continue.
    elif has_previous_game == 'True':
        valid_options = ['y','n']
        user_input = input("You have a previous game, continue? (Y/N) ").lower()
        game_input = validate_input(user_input, valid_options)
        match game_input:
            # Resume the last game
            case 'y':
                input("Resuming your last game...")
                clear_screen()
            # Generate new save, allow player to modify settings, set game bool to true.
            case 'n':
                input("You can modify your settings here before you start the new game.")
                save_generation()
                settings()
                data = read_file('save.txt')
                data[8] = 'True\n'
                write_file('save.txt', data)
                clear_screen()
    player = Player()
