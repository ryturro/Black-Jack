def new_round(self):
    if self.player_chips <= 0:
        messagebox.showinfo("Game Over", "You have no more chips to play.")
        self.new_round_button.config(state=tk.DISABLED)
        self.place_bet_button.config(state=tk.DISABLED)
        self.bet_entry.config(state=tk.DISABLED)
        return

    self.player_hand = []
    self.dealer_hand = []
    self.current_bet = 0
    self.double_down_used = False
    self.message_label.config(text="")
    self.show_hands(hide_dealer_first_card=True)

    self.hit_button.config(state=tk.DISABLED)
    self.stand_button.config(state=tk.DISABLED)
    self.double_button.config(state=tk.DISABLED)
    self.bet_entry.config(state=tk.NORMAL)
    self.place_bet_button.config(state=tk.NORMAL)