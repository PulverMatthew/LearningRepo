"""
Game module, houses the game logic for readability.
"""
from util import clear_screen, check_file, write_file, read_file
# from cards import PokerCard, PokerDeck
def play_game():
    """
    Basic game loop.
    """
    clear_screen()
    # Checks to see if the player has played the game before.
    has_previous_game = check_file('save.txt', 8).strip()
    print(has_previous_game.strip())
    if has_previous_game == 'False':
        data = read_file('save.txt')
        print(data[8])
        data[8] = 'True\n'
        write_file('save.txt', data)
    input('test')
