import random


suits = ("S", "H", "D", "C")

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        if self.rank == 1:
            rank_str = "A"
        elif self.rank == 11:
            rank_str = "J"
        elif self.rank == 12:
            rank_str = "Q"
        elif self.rank == 13:
            rank_str = "K"
        elif self.rank == 14:
            rank_str = "Joker"
        else:
            rank_str = str(self.rank)
        return f"{rank_str}{self.suit}"
    
    def is_number_card(self):
        if self.rank >= 1 and self.rank <= 10:
            return True
        return False

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in range(1, 14):
                card = Card(rank, suit)
                self.cards.append(card)
        for joker_suit in ("S", "H"):
            joker = Card(14, joker_suit)
            self.cards.append(joker)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop(0)

class Caravan:
    def __init__(self):
        self.stack = []
        self.direction = None
    
    def __len__(self):
        return len(self.stack)

    def print_caravan(self):
        for i, card in enumerate(self.stack):
            if isinstance(card, tuple):
                print(f"{i}: {' + '.join(str(c) for c in card)}")
            else:
                print(f"{i}: {card}")
    
    def add_card(self, card, index = None):
        if card.rank in range (1,11):
            self.stack.append(card)
        elif card.rank in range(11,14):
            self._add_face_card(card, index)
        elif card.rank == 14:
            self._joker_remove()
    
    def _add_face_card(self, card, index):
        if index == None:
            index = len(self.stack) - 1
        if index < 0 or index >+ len(self.stack):
            return
        target_card = self.stack[index]
        if card.rank == 11:
            self.stack.remove(target_card)
        elif card.rank == 12:
            if self.direction == "Up":
                self.direction = "Down"
            elif self.direction == "Down":
                self.direction = "Up"
            if isinstance(self.stack[index], tuple):
                self.stack[index] += (card,)
            else:
                self.stack[index] = (self.stack[index], card)
        elif card.rank == 13:
            if isinstance(self.stack[index], tuple):
                self.stack[index] += (card,)
            else:
                self.stack[index] = (self.stack[index], card)
    
    def joker_remove(self, card, index):
        # implementation of joker_remove will go here
        pass
    
    def caravan_value(self):
        sum = 0
        for card in self.stack:
            if isinstance(card, tuple):
                value = card[0].rank
                for part in card:
                    if part.rank == 13:
                        value *= 2
                sum += value
            else:
                sum += card.rank
        return sum