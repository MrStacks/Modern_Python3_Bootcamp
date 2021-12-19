
from random import shuffle

class Card:

	def __init__(self, value, suit):
		self.suit = suit #suit variable
		self.value = value #value variable

	def __repr__(self):
		# return "{} of {}".format(self.value, self.suit) # Udemy compatible version
		return f"{self.value} of {self.suit}"
		
class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		self.cards = [Card(value, suit) for suit in suits for value in values]
		# for suit in suits: # does the same thing as the list comprehension above
		# 	for value in values:
		# 		self.cards.append(Card(value, suit))
		# print(self.cards)		

	def __repr__(self):
		return f"Deck of {self.count()} cards"	#or could use len(cards_list)
		# return "Deck of {}cards".format(self.count()) #Udemy compatible version

	def count(self):
		return len(self.cards)

	def _deal(self, num):
		# I would like to know why the below code does not work
		# if count >= num:#remove num cards from the end
		# 	for x in xrange(1,num):
		# 		actual = self.cards.pop()#but only returns one suit or value in cards_list	
		# elif count > 0:#remove all cards in the list	
		# 	while count > 0:
		# 		actual = self.cards.pop()
		# else: return ValueError("All cards have been dealt")

		#He does:
		count = self.count()
		actual = min([num,count])
		if count == 0:
			raise ValueError("All cards have been dealt")
		#print(f"Going to remove {actual} cards")

		if actual == 1:
			return [self.cards.pop()]

		hand = self.cards[-actual:] #!!! This part was weird
		self.cards = self.cards[:-actual]
		return hand

	def shuffle(self):
		if len(self.cards) < 52: # he does "self.count() < 52"
			raise ValueError("Only full decks can be shuffled")#MUST raise NOT return
		shuffle(self.cards)
		return self # self is returned just for good practice "it's just a conventional thing to do"

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size) #needs to return a list			

# d = Deck()
# d.shuffle()

# card = d.deal_card()
# print(card)
# hand = d.deal_hand(50)
# print(hand)

# card2 = d.deal_card()
# print(card2)
# print(d.cards)
# card3 = d.deal_card()


# print(d._deal(52))
# print(d.count())				
# print(d._deal(3))

	