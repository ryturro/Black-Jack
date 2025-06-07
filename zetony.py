def end_round(self, message):
        self.message_label.config(text=message)

        msg = message.lower()
        if "you win" in msg:
            # Sprawdzamy blackjack (21 na 2 kartach) i wypłacamy 1.5x
            if len(self.player_hand) == 2 and self.calculate_score(self.player_hand) == 21 and "dealer" not in msg:
                winnings = int(self.current_bet * 2.5)  # stawka + 1.5x wygranej
            else:
                winnings = self.current_bet * 2  # stawka + wygrana
            self.player_chips += winnings

        elif "tie" in msg or "it's a tie" in msg:
            # remis - zwracamy stawkę
            self.player_chips += self.current_bet

        else:
            # przegrana - żetony przepadają (nic nie dodajemy)
            pass

        self.current_bet = 0
        self.chips_label.config(text=str(self.player_chips))

        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.double_button.config(state=tk.DISABLED)

        self.new_round_button.config(state=tk.NORMAL)
        self.bet_entry.config(state=tk.NORMAL)
        self.bet_var.set("")
        self.place_bet_button.config(state=tk.NORMAL)