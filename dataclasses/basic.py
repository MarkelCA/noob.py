from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str


queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))


# VS Regular class

class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

queen_of_hearts = RegularCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == RegularCard('Q', 'Hearts'))

########
# Default values
########
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 4.0

print(Position(name='str', lon='eu'))
