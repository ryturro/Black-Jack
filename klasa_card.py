class Card:
    def __init__(self, suit, value):
        self.suit = suit  # Kolor (np. "Hearts", "Diamonds")
        self.value = value  # Wartość (np. "A", "2", ..., "K")

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def get_numeric_value(self):
        if self.value in ["J", "Q", "K"]:
            return 10
        elif self.value == "A":
            return 11  # Tymczasowo 11, później dostosowane w logice gry
        else:
            return int(self.value)