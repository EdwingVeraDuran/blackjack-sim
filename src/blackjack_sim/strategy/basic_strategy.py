from blackjack_sim.core.cards import Card
from blackjack_sim.core.hand import Hand
from blackjack_sim.strategy.strategy import Action, Strategy


class BasicStrategy(Strategy):
    """Basic blackjack strategy"""

    def get_name(self) -> str:
        return "Basic Strategy"

    def decide(
        self, player_hand: Hand, dealer_upcard: Card, can_double: bool
    ) -> Action:
        player_value = player_hand.value
        dealer_value = dealer_upcard.value
        is_soft = player_hand.is_soft

        # Soft hands
        if is_soft:
            return self._soft_strategy(player_value, dealer_value, can_double)

        return self._soft_strategy(player_value, dealer_value, can_double)

    def _soft_strategy(
        self, player_value: int, dealer_value: int, can_double: bool
    ) -> Action:
        """Soft hands strategy"""

        # Soft 19+ always stand
        if player_value >= 19:
            return Action.STAND

        # Soft 18
        if player_value == 18:
            if dealer_value >= 9:
                return Action.HIT
            if can_double and 3 <= dealer_value <= 6:
                return Action.DOUBLE
            return Action.STAND

        # Soft 17
        if player_value == 17:
            if can_double and 3 <= dealer_value <= 6:
                return Action.DOUBLE
            return Action.HIT

        # Soft 13-16
        if 13 <= player_value <= 16:
            if can_double and 5 <= dealer_value <= 6:
                return Action.DOUBLE
            return Action.HIT

        # Soft 12 or less
        return Action.HIT

    def _hard_strategy(
        self, player_value: int, dealer_value: int, can_double: bool
    ) -> Action:
        """Hard hands strategies"""

        # 17+ Always stands
        if player_value >= 17:
            return Action.STAND

        # 13-16: Stand against 2-6, hit against 7+
        if 13 <= player_value <= 16:
            return Action.STAND if dealer_value <= 6 else Action.HIT

        # 12: Stand against 4-6, hit against any
        if player_value == 12:
            return Action.STAND if 4 <= dealer_value <= 6 else Action.HIT

        # 11: If possible always double
        if player_value == 11:
            return Action.DOUBLE if can_double else Action.HIT

        # 10: Double against 2-9
        if player_value == 10:
            if can_double and dealer_value <= 9:
                return Action.DOUBLE
            return Action.HIT

        # 9: Double against 3-6
        if player_value == 9:
            if can_double and 3 <= dealer_value <= 6:
                return Action.DOUBLE
            return Action.HIT

        # 8 or less: Always hit
        return Action.HIT
