import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDesk:
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]


	
beer_card = Card('7', 'diamonds')
print(beer_card)


deck = FrenchDesk()
print('len(deck) = %s' % len(deck))


from random import choice

print(choice(deck))
print(choice(deck))
print(choice(deck))


r = deck[:3]
print(r)

r = deck[12::13]
print(r)


print("-" * 50)

for card in deck:
	print(card)

print("-" * 50)

for card in reversed(deck):
	print(card)

print("-" * 50)

# 排序

suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
	rank_value = FrenchDesk.ranks.index(card.rank)
	return rank_value * len(suit_value) + suit_value[card.suit]


for card in sorted(deck, key=spades_high):
	print(card)
	rank_value = FrenchDesk.ranks.index(card.rank)
	r = rank_value * len(suit_value) + suit_value[card.suit]
	print (r)
