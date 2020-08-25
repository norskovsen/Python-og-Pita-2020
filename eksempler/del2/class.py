class Card:
    def __init__(self, type_string, number):
        self.type_string = type_string
        self.number = number

    def __repr__(self):
        return f'{self.get_value_string()} of {self.type_string}'

    def get_value_string(self):
        if self.number <= 10:
            return str(self.number)
        elif self.number == 11:
            return "JACK"
        elif self.number == 12:
            return "QUEEN"
        elif self.number == 13:
            return "KING"
        elif self.number == 14:
            return "ACE"

    def __gt__(self, other):
        return self.number > other.number

    def __lt__(self, other):
        return self.number < other.number
        
    def __eq__(self, other):
        return self.number == other.number

cards = [Card("DIAMOND", 12), Card("SPADES", 6), Card("HEARTS", 14)]

for card in cards:
    print(card)

print(cards[0] > cards[1])
print(cards[1] > cards[2])
