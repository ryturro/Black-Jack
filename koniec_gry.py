def end_round(self, message):
    self.message_label.config(text=message)

    msg = message.lower()
    if "you win" in msg:
        if len(self.player_hand) == 2 and self.calculate_score(self.player_hand) == 21 and "dealer" not in msg:
            winnings = int(self.current_bet * 2.5)  # blackjack
        else:
            winnings = self.current_bet * 2
        self.player_chips += winnings

    elif "tie" in msg:
        self.player_chips += self.current_bet

    self.current_bet = 0
    self.chips_label.config(text=str(self.player_chips))

    self.hit_button.config(state=tk.DISABLED)
    self.stand_button.config(state=tk.DISABLED)
    self.double_button.config(state=tk.DISABLED)
    self.new_round_button.config(state=tk.NORMAL)
    self.bet_entry.config(state=tk.NORMAL)
    self.place_bet_button.config(state=tk.NORMAL)
    self.bet_var.set("")