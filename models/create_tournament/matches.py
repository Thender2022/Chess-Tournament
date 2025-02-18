class MatchGenerator:
    def __init__(self, players=None):
        self.players = players

    def generate_pairings(self, players=None):
        if players is None:
            players = self.players
        from itertools import combinations
        import random
        pairings = list(combinations(players, 2))
        random.shuffle(pairings)
        return pairings

