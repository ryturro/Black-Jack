    def load_card_image(self, card):
        path = os.path.join(CARD_PATH, card.filename())
        if not os.path.exists(path):
            path = CARD_BACK
        img = Image.open(path).resize((80, 120))
        return ImageTk.PhotoImage(img)