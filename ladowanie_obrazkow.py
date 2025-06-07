    def show_hands(self, hide_dealer_first_card=True):
        for widget in self.player_frame.winfo_children():
            widget.destroy()
        for widget in self.dealer_frame.winfo_children():
            widget.destroy()