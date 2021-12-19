#THIS IS ALL COLTS CODE
from deck_of_cards import Card, Deck
import unittest

class CardTests(unittest.TestCase):
	def setUp(self): #make a new Card to test
		self.card = Card(suit="Hearts", value="A")

	def test_init(self):
		"""cards should have a suit and a value"""
		self.assertEqual(self.card.suit, "Hearts")
		self.assertEqual(self.card.value, "A")

class DeckTests(unittest.TestCase):
	def setUp(self): #make a new Deck to test (runs 1x before each test function)
		self.deck = Deck()

	def test_init(self):
		"""deck should be a list"""
		self.assertTrue(isinstance(self.deck.cards, list)) #deck of cards must be a list
		self.assertEqual(len(self.deck.cards), 52) #must initialize 52 cards

	def test_repr(self):
		"""must return "Deck of 52 cards" at initialization"""
		self.assertEqual(repr(self.deck), "Deck of 52 cards")

	def test_count(self):
		"""must return # of cards in the deck"""
		self.assertEqual(self.deck.count(), 52)
		"""test removing one card"""
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)

	def test_deal_sufficient_cards(self):
		"""test that the number of cards specified are dealt, if possible"""	
		cards = self.deck._deal(10)
		self.assertEqual(len(cards), 10)
		self.assertEqual(self.deck.count(), 42)

	def test_deal_insufficient_cards(self):
		"""_deal should deal the # of cards left in the deck"""
		cards = self.deck._deal(100) #thus, when dealing 100, it should only deal 52
		self.assertEqual(len(cards), 52) # all cards must be now dealt
		self.assertEqual(self.deck.count(), 0) #check that deck is now empty

	def test_deal_no_cards(self):
		"""_deal must throw ValueError if the deck is empty"""
		self.deck._deal(self.deck.count())#deals everything in the deck
		with self.assertRaises(ValueError):
			self.deck._deal(1)

	def test_deal_card(self):
		"""deal_card should deal a single card from the deck"""
		card = self.deck.cards[-1]#save variable equal to last card in deck
		dealt_card = self.deck.deal_card()#saves card & should be same as above
		self.assertEqual(card, dealt_card) #should be the same
		self.assertEqual(self.deck.count(), 51) #deck must have 1 removed

	def test_deal_hand(self):
		"""deal_hand must deal the # of cards passed"""	
		cards = self.deck.deal_hand(20)#deal 20
		self.assertEqual(len(cards), 20)#test if 20
		self.assertEqual(self.deck.count(), 32)

	def test_shuffle_full_deck(self):
		"""must shuffle the deck if deck is full"""
		cards = self.deck.cards[:]#single-colon slice makes a copy of everything (initial state)
		self.deck.shuffle()#shuffle the original deck
		self.assertNotEqual(cards, self.deck.cards)#ensure initial state different than current state
		self.assertEqual(self.deck.count(), 52)#ensure the length is same as before

	def test_shuffle_not_full_deck(self):
		"""shuffle should throw ValueError if deck is not full"""
		self.deck._deal(1)
		with self.assertRaises(ValueError):
			self.deck.shuffle()#assert that shuffle raises a ValueError

if __name__ == '__main__':
    unittest.main()	


























