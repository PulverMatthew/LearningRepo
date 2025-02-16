"""
The player module. Contains the player class, which regulates information related to the player. 
"""
import math
from cards import PokerDeck
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
        money: Current amount of money owned by the player.
        score: Current score of the player in the current round.
        deck: Selected deck of the player.
        hand: List representing player's currently selected hand.

        """
        # Strip all lines from the file at once
        data = [line.strip() for line in read_file('save.txt')]
        # Unpack the values for clarity
        hands_str, discards_str, hand_size_str, file_name, ante_str, round_str, money_str = data
        # Initializes save data from the save file.
        self.hands = int(hands_str)
        self.discards = int(discards_str)
        self.hand_size = int(hand_size_str)
        self.name = str(file_name)
        self.ante_base = 200 * math.exp2(int(ante_str))
        self.round = int(round_str)
        self.money = int(money_str)
        self.score = int(0)
        self.deck = PokerDeck()
        self.hand = []

class Blind():
    """
    Blind class, regulates score requirements and special effects. 
    One of these is called for each round. 
    """
    def __init__(self, blind_type):
        self.score_requirement = blind_type
    def small_blind(self, difficulty):
        """
        Small blind, has a 1X multiplier with reward of 3. 
        """
        score = difficulty
        return score
    def big_blind(self, difficulty):
        """
        Big blind, has a 1.5X multiplier with a reward of 5.
        """
        score = difficulty * 1.5
        return score
    def wall(self, difficulty):
        """
        The Wall: Has a 4X multiplier rather than the usual
        2X multiplier for boss binds.
        """
        score = difficulty * 4
        return score
