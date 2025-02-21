"""
The player module. Contains the player class, which regulates information related to the player. 
"""
import random
import math
from cards import PokerDeck
from util import read_file, menu_display, validate_input, clear_screen, shuffle, hand_evaluator
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
        hands_str, discard_str, hand_size_str, name, ante_str, round_str, money_str, deck_str, seed_str = data
        # Initializes save data from the save file.
        self.hands = int(hands_str)
        self.discards = int(discard_str)
        self.hand_size = int(hand_size_str)
        self.name = str(name)
        self.ante =  int(ante_str)
        self.round = int(round_str)
        self.money = int(money_str)
        self.deck = PokerDeck()
        self.deck.set_deck(deck_str)
        self.seed = tuple(seed_str)
        random.seed(self.seed)

        self.score = 0
        self.hand = []

class Blind():
    """
    Blind class, regulates score requirements and special effects. 
    One of these is called for each round. 

    Parameters:
        type(str): What kind of blind is this? Pass one of the
        methods below.
        difficulty (int): What ante is this blind on? 
    """
    def __init__(self, difficulty):
        self.score_requirement = 200 * math.exp2(int(difficulty))
        self.blind_type = 'Default'
        self.reward = 1

    def small_blind(self):
        """
        Small blind, has a 1X multiplier with reward of 3. 
        """
        self.score_requirement = self.score_requirement
        self.blind_type = 'Small Blind'
        self.reward = 3
    def big_blind(self):
        """
        Big blind, has a 1.5X multiplier with a reward of 5.
        """
        self.score_requirement = self.score_requirement * 1.5
        self.blind_type = 'Big Blind'
        self.reward = 5
    def wall(self):
        """
        The Wall: Has a 4X multiplier rather than the usual
        2X multiplier for boss binds.
        """
        score = self.score_requirement * 4
        self.blind_type = 'The Wall'
        self.reward = 7
        return score
    def challenge_query(self):
        """
        Challenge query calls a method which gives the
        player information about the next challenge. The player
        can accept or skip the challenge. 

        Raises: 
            ValueError: If the value of the input is not allowed.

        Returns: 
            blind_decision(bool) - Has the player accepted the challenge?
        """
        clear_screen()
        display = {
            'Current Blind': self.blind_type,
            'Reward': str(self.reward),
            'Options': '',
        }
        menu_display(display)
        options = {
            '1':'Select Blind',
            '2':'Skip'
        }
        menu_display(options)
        user_input = input('Choose an option: ')
        game_input = validate_input(user_input, display)
        match game_input:
            case '1':
                blind_decision = True
            case '2':
                blind_decision = False
        return blind_decision

    def challenge(self, player):
        """
        The challenge method is a method which calls a procedural
        game loop challenging the player to beat the score requirement
        with the number of hands given to them.

        Parameters:
            player (obj): The player object, representing player data.
        Returns:
            win_state (bool): Boolean representing if the game was won or not. 
        """
        shuffle(player.deck.card_deck)
        while player.score < self.score_requirement and player.hands > 0:
            clear_screen()
            selected_cards = []
            for _ in range(player.hand_size - len(player.hand)):
                player.deck.deal()
            print(f'{self.blind_type}: Score at least {self.score_requirement}')
            # Display selected cards on top of the player's hand. Update every turn.
            for card in selected_cards:
                print(f'{card.suit} {card.rank}\n', end=' ')
            for card in player.hand:
                print(f'{card.suit} {card.rank}\n', end=' ')
            display = {
                'a': 'Play',
                'b': 'Discard'
            }
            valid_choices = []
            for i in len(player.hand):
                valid_choices.append(str(i))
            for i in list(display.keys):
                valid_choices.append(str(i))
            menu_display(display)
            print('Input index to select a card\n')
            user_input = input('Choose the index of a card or the options above: ')
            game_input = validate_input(user_input, valid_choices)
            index = int(game_input)
            if game_input.isdigit():
                if index < len(player.hand):
                    card = player.hand.pop(index)
                    selected_cards.append(card)
            match game_input:
                case 'a':
                    score_list = hand_evaluator(selected_cards)
                    player.score += score_list[0] * score_list[1]
                case 'b':
                    continue
        if player.hands == 0:
            win_state = False
        elif player.score >= self.score_requirement:
            win_state = True
        else:
            win_state = None
        return win_state
