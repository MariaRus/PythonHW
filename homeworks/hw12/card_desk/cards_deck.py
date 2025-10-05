import random


class Card:
    def __init__(self):
        self.cards = []
        self.number_list = list(range(1, 14))
        self.mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        for mast in self.mast_list:
            for number in self.number_list:
                self.cards.append((mast, number))

        self.cards.append(('Joker', '1'))
        self.cards.append(('Joker', '2'))


class CardsDeck:
    def __init__(self):
        self.card = Card()
        self.deck = self.card.cards[:]

    def shuffle(self):
        random.shuffle(self.deck)

    def get_card(self, index):
        if self._card_validator(index):
            drawn_card = self.deck.pop(index - 1)
            return drawn_card
        raise ValueError("Selected card number is invalid.")

    def get_remaining_cards(self):
        return self.deck[:]

    @staticmethod
    def _card_validator(number):
        if not isinstance(number, int) or number < 1 or number > 54:
            raise ValueError("Error: enter a card number from 1 to 54")
        return number


if __name__ == "__main__":
    deck = CardsDeck()
    deck.shuffle()

    while True:
        try:
            user_input = input('Выберите карту из колоды в 54 карты: ')
            card_number = int(user_input)
            card = deck.get_card(card_number)
            print(f'Ваша карта: {card[0]} {card[1]}')
        except ValueError as e:
            print(e)
