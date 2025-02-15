"""
The player module. Contains the player class, which regulates information related to the player. 
"""
from cards import PokerCard, PokerDeck
from util import read_file
class Player:
    """
    The player class, represents the player and all information related to the player. 
    """
    def __init__(self):
        """
        Initializes the player object. Imports data from the save file.
        hands: Integer representing number of hands which can be played.
        discards: Integer representing times cards can be mulliganned limit 5.
        handSize: The number of cards which can be in a hand.
        name: Name of the player.
        ante: Current difficulty level of the game.
        round: Current level of the game.
        """
        # Strip all lines from the file at once
        data = [line.strip() for line in read_file('save.txt')]
        # Unpack the values for clarity
        hands_str, discards_str, hand_size_str, file_name, ante_str, round_str, money_str = data
        # Initializes save data from the save file.
        self.hands = int(hands_str)
        self.discards = int(discards_str)
        self.hand_size = int(hand_size_str)
        self.name = file_name
        self.ante = int(ante_str)
        self.round = int(round_str)
        self.money = int(money_str)

    
