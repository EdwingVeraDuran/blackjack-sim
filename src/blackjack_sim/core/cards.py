import random

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♣", "♠"]
VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
        self.value = VALUES[rank]

    def __str__(self) -> str:
        return f"{self.rank} - {self.suit}"


class Shoe:
    def __init__(self, num_decks: int = 1) -> None:
        self.num_decks = num_decks
        self.shoe: list[Card] = []

    def create(self) -> None:
        self.clear()
        for _ in range(self.num_decks):
            for s in SUITS:
                for r in RANKS:
                    self.shoe.append(Card(rank=r, suit=s))

    def shuffle(self) -> None:
        if not self.shoe:
            raise ValueError("Shoe is empty")
        random.shuffle(self.shoe)

    def clear(self) -> None:
        self.shoe.clear()

    def draw_card(self) -> Card:
        if not self.shoe:
            raise ValueError("Shoe is empty")
        return self.shoe.pop()

    def __len__(self):
        return len(self.shoe)
