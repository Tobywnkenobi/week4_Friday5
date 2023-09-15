import random

class Card:
    card_suites =['Hearts', 'Diamonds', 'Clubs', 'Spades']
    card_ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Ten', 'Jack', 'Queen', 'King','Ace']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def get_value(self):
        if self.rank in ["Jack","Queen","King"]:
            return 10
        elif self.rank == "Ace":
            return 11
        else:
            return Card.card_ranks.index(self.rank) + 2
        
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.card_suites for rank in Card.card_ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_cards(self, card):
        self.cards.append(card)

    def get_value(self):
        card_value = sum(card.get_value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == "Ace")
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

class Player:
    def __init__(self, bankroll=100):
        self.bankroll = bankroll
        self.hand = Hand()

    def bet(self, amount):
        if amount <= self.bankroll:
            self.bankroll -= amount
            return True
        return False
    
    def win(self, amount):
        self.bankroll += amount

    def __str__(self):
        return f"Bankroll: ${self.bankroll}"

class Game:
    def __init__(self):
        pass
    def play(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.play()