from jack_GUI import Game
import tkinter as tk
from tkinter import messagebox

class BJ_GUI:
    def __init__(self, main):
        self.main = main
        self.main.title("BlackJack")

        self.game = Game()
        
        #bet amounts
        self.bet_label = tk.Label(self.main, text="Bet Amount:", font=("Arial", 16))
        self.bet_label.pack(pady=10)
        
        self.bet_entry = tk.Entry(self.main, font=("Arial", 16))
        self.bet_entry.pack(pady=10)

        #method to handle bets
        self.new_game_button = tk.Button(self.main, text="Place Bet and Start New Game", command=self.place_bet_start_new)
        self.new_game_button.pack(pady=20)

        self.bankroll_label = tk.Label(self.main, text=str(self.game.player), font =("Arial", 16))
        self.bankroll_label.pack(pady=20)

               #setting the frames
        self.dealer_frame = tk.Frame(self.main)
        self.dealer_frame.pack(pady=20)

        self.player_frame = tk.Frame(self.main)
        self.player_frame.pack(pady=20)

        #Labeling Dealer
        self.dealer_label = tk.Label(self.player_frame, text="Dealer's Hand:", font=("Arial", 16))
        self.dealer_label.pack()

        #Label player
        self.player_label = tk.Label(self.player_frame, text="Your Hand", font=("Arial", 16))
        self.player_label.pack()

        self.update_display()
        
        #Buttons
        self.hit_button = tk.Button(self.main, text="Hit", command=self.hit)
        self.hit_button.pack(side=tk.LEFT, padx=20)

        self.stand_button = tk.Button(self.main, text="Stand", command=self.stand)
        self.stand_button.pack(side=tk.LEFT)

        self.new_game_button = tk.Button(self.main, text="New Game? ", command=self.new_game)
        self.new_game_button.pack(pady=20)

        self.update_display()

        
    def update_display(self):
        dealer_text = "Dealer's Hand: " + ", ".join(str(card) for card in self.game.dealer.cards)
        player_text = "Your Hand: " + ", ".join(str(card) for card in self.game.player.hand.cards)
        self.dealer_label.config(text=dealer_text)
        self.player_label.config(text=player_text)

    def hit(self):
        self.game.player.hand.add_cards(self.game.deck.deal())
        self.update_display()
        if self.game.player.hand.get_value() > 21:
            messagebox.showinfo("BlackJack", "Busted! House Wins Again!!")
            self.new_game()

    def stand(self):
        while self.game.dealer.get_value() < 17:
            self.game.dealer.add_cards(self.game.deck.deal())
            self.update_display()
        self.check_winner()

    def check_winner(self):
        player_val = self.game.player.hand.get_value()
        dealer_val = self.game.dealer.get_value()
        bet_amount = int(self.bet_entry.get())

        if player_val > 21:
            winner = "House"
        elif dealer_val > 21:
            winner = "You, yes YOU!  You Win!!"
            self.game.player.win(2 * bet_amount)
        elif player_val > dealer_val:
            winner = "Taking that Money, fair and square!!"
            self.game.player.win(2 * bet_amount)
        elif dealer_val > player_val:
            winner = "House Wins, better luck next time!!"
        else:
            winner = "It's a Tie!"
            self.game.player.win(bet_amount)

        self.bankroll_label.config(text=str(self.game.player))
        messagebox.showinfo("BlackJack", f"{winner} Win!")
        self.new_game()

    def place_bet_start_new(self):
        bet_amount = int(self.bet_entry.get())
        if self.game.player.bankroll <= 0:
            messagebox.showinfo("BlackJack", "You're out of money! Game Over - loan department is down the hall, and to the right")
            self.main.quit()
        elif not self.game.player.bet(bet_amount):
            messagebox.showinfo("BlackJack", "Insufficient Funds!")
        else:
            self.new_game()
            
        # bet_amount = int(self.bet_entry.get())
        # if not self.game.player.bet(bet_amount):
        #     messagebox.showinfo("Blackjack", "Insufficient Funds!")
        # else:
        #     self.new_game()

    def new_game(self):
        self.game.start_new_game()
        self.update_display()
        self.bankroll_label.config(text=str(self.game.player))

        # self.game = Game()
        # for _ in range(2):
        #     self.game.player.hand.add_cards(self.game.deck.deal())
        #     self.game.dealer.add_cards(self.game.deck.deal())
        # self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    gui = BJ_GUI(root)
    root.mainloop()