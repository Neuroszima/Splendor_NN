import re, ast, random

from Game.Card import Card
from Game.Player import Player

class Game:

    def __init__(self, player_count=4, max_turns=200):
        if not 1 < player_count < 5:
            raise ValueError("cant start game with improper number of players")
        self.player_count = player_count
        self.l1_deck = []
        self.l2_deck = []
        self.l3_deck = []
        self.nobles = []
        self.players = []
        self.chips = []
        self.open_cards = []
        self.max_turns = max_turns

    def start(self):
        all_cards = []
        nobls = []
        with open("cards.txt", "r") as card_db:
            for line in card_db:
                if not re.match(r"#", line):
                    card_entry = ast.literal_eval(line)
                    all_cards.append(Card(card_entry))

        for card in all_cards:
            if card.get_level() == 1:
                self.l1_deck.append(card)
            elif card.get_level() == 2:
                self.l2_deck.append(card)
            elif card.get_level() == 3:
                self.l3_deck.append(card)
            elif card.get_level() == 0:
                nobls.append(card)

        self.shuffle_dek(self.l1_deck)
        self.shuffle_dek(self.l3_deck)
        self.shuffle_dek(self.l2_deck)
        self.shuffle_dek(nobls)
        if self.player_count == 4:
            self.nobles = nobls[:4]
            self.chips = [7 for _ in range(5)]
        elif self.player_count == 3:
            self.nobles = nobls[:3]
            self.chips = [5 for _ in range(5)]
        else:
            self.nobles = nobls[:2]
            self.chips = [4 for _ in range(5)]

        self.players = [{"id": i,
                         "Player": Player(i),
                         "turns": 0} for i in range(self.player_count)]

        self.open_cards = self.prep_cards()
        self.starting_player = random.randint(0, self.player_count)

        self.play()

    def shuffle_dek(self, dek):
        for i in range(100):
            j = random.randint(0, len(dek))
            k = random.randint(0, len(dek))
            if i != j:
                dek[j], dek[k] = dek[k], dek[j]

    def prep_cards(self):
        l1_out = [self.l1_deck.pop() for _ in range(4)]
        l2_out = [self.l2_deck.pop() for _ in range(4)]
        l3_out = [self.l3_deck.pop() for _ in range(4)]
        self.open_cards = [l1_out, l2_out, l3_out]

    def next_turn(self, pid, decision=None):
        if decision is None:
            decision = self.players[pid].decide(self.open_cards, self.nobles)

    def play(self):
        won = False
        turns = 0
        current_player = self.starting_player
        while not won and turns < self.max_turns:
            self.next_turn(current_player)
            current_player += 1
            if current_player > self.player_count:
                current_player = 0
            turns += 1

