#THIS IS ALL COLTS CODE
from random import shuffle
 
 
class Card:
 
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
 
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)
 
 
class Deck:
 
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
 
    def __repr__(self):
        return "Deck of {} cards".format(self.count())
 
    def count(self):
        return len(self.cards)
 
    def _deal(self, num):
        """
        Return a list of cards dealt
        """
        count = self.count()
        actual = min([num, count])  # make sure we don't try to over-deal
 
        if count == 0:
            raise ValueError("All cards have been dealt")
 
        if actual == 1:
            return [self.cards.pop()]
 
        cards = self.cards[-actual:]  # slice off the end
        self.cards = self.cards[:-actual]  # adjust cards
 
        return cards
 
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
 
        shuffle(self.cards)
        return self
 
    def deal_card(self):
        """
        Returns a single Card
        """
        return self._deal(1)[0]
 
    def deal_hand(self, hand_size):
        """
        Returns a list of Cards
        """
        return self._deal(hand_size)
