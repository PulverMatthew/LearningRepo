from util import clear_screen, check_file
# from cards import PokerCard, PokerDeck
# Game loop, shows the main game logic.
def play_game():
    clear_screen()
    # Checks to see if the player has played the game before.
    has_previous_game = check_file('save.txt', 3)