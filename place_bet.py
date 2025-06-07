def place_bet(self):
        bet_str = self.bet_var.get()
        try:
            bet = int(bet_str)
            if bet < 1:
                raise ValueError
            if bet > self.player_chips:
                messagebox.showerror("Error", "You don't have enough chips.")
                return
        except ValueError:
            messagebox.showerror("Error", "Enter a valid bet (positive integer).")
            return

        self.current_bet = bet
        self.player_chips -= bet
        self.chips_label.config(text=str(self.player_chips))
        self.bet_entry.config(state=tk.DISABLED)
        self.place_bet_button.config(state=tk.DISABLED)
