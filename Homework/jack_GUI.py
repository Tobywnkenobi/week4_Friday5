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
        if not self.cards:
            print("deck is empty, shuffling new deck")
            # return self.cards.pop()
            self.__init__()
            self.shuffle()

        # print(f"Dealing card: {self.cards[-1]}")
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_cards(self, card):
        self.cards.append(card)

    def get_value(self):
        card_value = sum(card.get_value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == "Ace")
        while card_value > 21 and aces:
            card_value -= 10
            aces -= 1
        return card_value
    
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
        self.deck = Deck()
        self.player = Player()
        self.dealer = Hand()

        self.start_new_game()

    def start_new_game(self):
        self.deck.shuffle()
        self.player.hand = Hand()
        self.dealer = Hand()

        for _ in range(2):
            self.player.hand.add_cards(self.deck.deal())
            self.dealer.add_cards(self.deck.deal())

    def play(self):
        # while self.player.bankroll > 0:
        #     self.deck.shuffle()
        #     self.player.hand = Hand()
        #     self.dealer = Hand()

        #     bet_amount = int(input(f"You have {self.player.bankroll}. Enter your bet: "))
        #     if not self.player.bet(bet_amount):
        #         print("Insufficient funds!")
        #         continue

        #     for _ in range (2):
        #         self.player.hand.add_cards(self.deck.deal())
        #         self.dealer.add_cards(self.deck.deal())

        #     print(f"Your hand: {self.player.hand}")
        #     print(f"Dealer's first card: {self.dealer.cards[0]}")

            #Player turn
            while self.player.hand.get_value() < 21:
                # action = input("Hit or Stand? ").lower()
                # if action == "hit":
                    self.player.hand.add_cards(self.deck.deal())
                #     print(f"Your hand: {self.player.hand}")
                # elif action == "stand":
                #     break

            #Dealer

            while self.dealer.get_value() < 17:
                self.dealer.add_cards(self.deck.deal())

            # print(f"Dealer's hand: {self.dealer}")

            # if self.player.hand.get_value() > 21:
            #     print("Busted! House Wins!")
            # elif self.dealer.get_value() > 21:
            #     print("Dealer busts! You win!!")
            #     self.player.win(2 *bet_amount)
            # elif self.player.hand.get_value() > self.dealer.get_value():
            #     print("You win!")
            #     self.player.win(2 * bet_amount)
            # elif self.player.hand.get_value() == self.dealer.get_value():
            #     print("It's a tie!")
            #     self.player.win(bet_amount)
            # else:
            #     print("Dealer Wins!")
            
                # play_again = input("Do you want to play again? (yes or no) ").lower()
                # if play_again != "yes":
                #     break
                               

        # print("Thanks for playing, come again!!")

if __name__ == "__main__":
    game = Game()
    # game.play()