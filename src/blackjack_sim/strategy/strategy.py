from abc import ABC, abstractmethod
from enum import Enum

from blackjack_sim.core.cards import Card
from blackjack_sim.core.hand import Hand


class Action(Enum):
    """Possible hand actions in blackjack"""

    HIT = "HIT"
    STAND = "STAND"
    DOUBLE = "DOUBLE"
    # TODO: Implement split and surrender in future
    # SPLIT = "SPLIT"
    # SURRENDER = "SURRENDER"


class Strategy(ABC):
    """Base class for blackjack strategies"""

    @abstractmethod
    def decide(
        self, player_hand: Hand, dealer_upcard: Card, can_double: bool
    ) -> Action:
        """Decides action"""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Strategy name"""
        pass
