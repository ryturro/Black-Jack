 def start_round(self):
        self.player_hand = [self.deck.deal_card(), self.deck.deal_card()]
        self.dealer_hand = [self.deck.deal_card(), self.deck.deal_card()]
        self.double_down_used = False
        self.message_label.config(text="")

        self.show_hands(hide_dealer_first_card=True)

        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
        self.double_button.config(state=tk.NORMAL)
        self.new_round_button.config(state=tk.DISABLED)
