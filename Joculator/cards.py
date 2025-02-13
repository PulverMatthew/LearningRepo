class pokerCard:
    # Valid poker suits
    suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    # Valid poker ranks 
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']

    def __init__(self, suit, rank):
        # Defines suits and ranks.
        if suit not in pokerCard.suits:
            raise ValueError(f'Invalid suit: {suit}')
        if rank not in pokerCard.ranks:
            raise ValueError(f'Invalid rank: {rank}')
        self.suit = suit
        self.rank = rank
        # Checks to see if the card has been modified in game.
        self.isModified = False

        # Chip value can be intuited based on rank value. If a face card, set to 10. If ace, set to 11. 
        self.chips = rank
        if str(self.chips) in ('J', 'Q', 'K'):
            self.chips = 10
        elif str(self.chips) in ('A'):
            self.chips = 11
        
        # Set isFace boolean to false by default. If the rank is J, Q, or K, then set isFace to true.
        self.isFace = False
        if str(self.rank) in ('J', 'Q', 'K'):
            self.isFace = True

    # Setter method for suit. 
    def setSuit(self, suit):
        if suit not in pokerCard.suits:
            raise ValueError(f'Invalid suit: {suit}')
        self.suit = suit
        self.isModified = True

    # Setter method for rank. 
    def setRank(self, rank):
        if rank not in pokerCard.ranks:
            raise ValueError(f'Invalid rank: {rank}')
        self.rank = rank
        # If set rank is J, Q, or K, then set chips to 10 and designates as a face card.
        if str(self.rank) in ('J', 'Q', 'K') and self.isModified == False:
            self.chips = 10
            self.isFace = True

        # If ace, set chips to 11.
        elif str(self.chips) in ('A') and self.isModified == False:
            self.chips = 11
        self.isModified = True

    # Setter method for chips.
    def setChips(self, chips):
        self.chips = chips
        self.isModified = True
    
    # Setter method for face card boolean. 
    def setFace(self, faceCard):
        self.isFace = faceCard
        self.isModified = True

class pokerDeck:
    # Poker deck class will instantiate with a defaultDeck which can be changed to a selected deck.
    def __init__(self):
        self.cardDeck = []
        self.cardCount = len(self.cardDeck)

    # Generates a standard deck of poker cards.
    def defaultDeck(self):
        deck = []
        # Generates a pokerCard for every pokerCard.suits and pokerCard.ranks
        for suit in pokerCard.suits:
            for rank in pokerCard.ranks:
                deck.append(pokerCard(suit, rank))
        return deck
    
    # Sets the card deck for the poker deck class.
    def setDeck(self, deck):
        self.cardDeck = deck
        self.cardCount = len(deck)