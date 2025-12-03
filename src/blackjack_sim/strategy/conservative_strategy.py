from blackjack_sim.core.cards import Card
from blackjack_sim.core.hand import Hand
from blackjack_sim.strategy.strategy import Action, Strategy


class ConservativeStrategy(Strategy):
    """Simple and basic strategy"""

    def get_name(self) -> str:
        return "Conservative Strategy"

    def decide(
        self, player_hand: Hand, dealer_upcard: Card, can_double: bool
    ) -> Action:
        player_value = player_hand.value
        dealer_value = dealer_upcard.value

        # Simple rules
        if player_value >= 17:
            return Action.STAND
        elif player_value <= 11:
            return Action.HIT
        else:  # 12-16
            return Action.STAND if dealer_value <= 6 else Action.HIT
