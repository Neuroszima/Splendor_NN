
class Player:

    def __init__(self, p_id):
        """
        chips are represented as:
            [red_chips, white_chips, black_chips, green_chips, blue_chips]
        same goes for power
        """
        self.p_id = p_id
        self.cards = []
        self.power = []
        self.chips = []
        self.network = None

    def decide(self, cards_in_open, nobles_in_open):
        pass

    def points(self):
        return sum([c.get_points() for c in self.cards])
