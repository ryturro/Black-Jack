def place_bet(self):
        self.current_bet = bet
        self.player_chips -= bet
        self.chips_label.config(text=str(self.player_chips))
        self.bet_entry.config(state=tk.DISABLED)
        self.place_bet_button.config(state=tk.DISABLED)