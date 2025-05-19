class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)
        self.calculate_score()

    def calculate_score(self):
        self.score = sum(card.get_numeric_value() for card in self.hand)
        # Dostosowanie dla Asa (11 lub 1)
        aces = sum(1 for card in self.hand if card.value == "A")
        while self.score > 21 and aces:
            self.score -= 10
            aces -= 1

    def show_hand(self):
        return ", ".join(str(card) for card in self.hand)