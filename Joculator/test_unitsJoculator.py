import pytest
from cards import pokerCard, pokerDeck
from util import validatedInput

def test_utility_functions():
    menuOptions = {
        'test1': 'test2',
        'test3': 'test4',
        'test5': 'test6',
    }
    assert validatedInput('InvalidInput', menuOptions) == None
    assert validatedInput('test1', menuOptions) == 'test1'

def test_poker_card_identity():
    card1 = pokerCard('Hearts', 'A')
    assert (card1.suit, card1.rank, card1.chips, card1.isFace) == ('Hearts', 'A', 11, False)

    card2 = pokerCard('Spades', 10)
    assert (card2.suit, card2.rank, card2.chips, card2.isFace) == ('Spades', 10, 10, False)

    card3 = pokerCard('Diamonds', 'J')
    assert (card3.suit, card3.rank, card3.chips, card3.isFace) == ('Diamonds', 'J', 10, True)

    card4 = pokerCard('Clubs', 7)
    assert (card4.suit, card4.rank, card4.chips, card4.isFace) == ('Clubs', 7, 7, False)

def test_poker_card_setters():
    card1 = pokerCard('Hearts', 'A')
    card1.setSuit('Diamonds')
    assert card1.suit == 'Diamonds'

    card2 = pokerCard('Spades', 10)
    card2.setRank('A')
    assert card2.rank == 'A'

    card3 = pokerCard('Diamonds', 'J')
    card3.setChips(200)
    assert card3.chips == 200

    card3.setRank('J')
    assert card3.chips == 200

    card4 = pokerCard('Clubs', 7)
    card4.setFace(True)
    assert card4.isFace == True
    card4.setRank(10)
    assert card4.isFace == True

def test_poker_card_deck():
    defaultDeck = pokerDeck()
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Formats suit and ranks i.e ('Hearts', '2'), for every suit in suits and rank in ranks, giving every combination.
    deck = [(suit, rank) for suit in suits for rank in ranks]
    for card in defaultDeck.cardDeck:
        assert (card.suit, card.rank) in deck
        deck.remove((card.suit, card.rank))
    assert len(deck) == 52

test_utility_functions()
test_poker_card_identity()
test_poker_card_setters()
test_poker_card_deck()