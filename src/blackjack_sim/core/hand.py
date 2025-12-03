from blackjack_sim.core.cards import Card


class Hand:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def new_card(self, new_card: Card) -> None:
        self.cards.append(new_card)

    def clear(self) -> None:
        self.cards.clear()

    @property
    def value(self) -> int:
        """Calcula el valor óptimo de la mano"""
        total = 0
        aces = 0

        for c in self.cards:
            v = c.value
            total += v
            if c.rank == "A":
                aces += 1

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    @property
    def is_soft(self) -> bool:
        """Una mano es soft si tiene un As contado como 11"""
        if not any(c.rank == "A" for c in self.cards):
            return False

        hard_value = sum(1 if c.rank == "A" else min(c.value, 10) for c in self.cards)

        return self.value == hard_value + 10 and self.value <= 21

    @property
    def is_blackjack(self) -> bool:
        """Blackjack es 21 con exactamente 2 cartas"""
        return len(self.cards) == 2 and self.value == 21

    def to_list(self) -> list[str]:
        """Retorna lista de strings representando las cartas"""
        return [card.__str__() for card in self.cards]
