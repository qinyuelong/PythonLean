import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ransks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in set.suits for rank in self.ransks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
