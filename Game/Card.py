from Game.Player import Player

class Card:

    def __init__(self, card_entry):
        self.__color = tuple(card_entry[0])
        self.__power = tuple(card_entry[1])
        self.__points = tuple(card_entry[2])
        self.__level = tuple(card_entry[3])
        self.__cost = tuple(card_entry[4:])

    def __gt__(self, other):
        if isinstance(other, Player):
            for i in range(len(self.__cost)):
                if not (self.__cost[i] > other.power[i] + other.chips[i]):
                    return False
            return True
        if isinstance(other, Card):
            if self.get_level() > other.get_level():
                return True
            return False
        raise TypeError(f"{other.__class__} object can't be used in comparison")

    def __lt__(self, other):
        return not self > other

    def can_buy(self, player, ignore_costs=False):
        if isinstance(player, Player):
            if not ignore_costs:
                if player > self:
                    return True
                return False
            return True
        raise TypeError(f"{player.__class__} object can't be used in 'buy' action")

    def get_level(self):
        return self.__level

    def get_points(self):
        return self.__points
