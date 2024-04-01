class TournamentScheduler:
    def __init__(self, pairings):
        self.pairings = pairings

    def distribute_info_rounds(self):
        round_data = []
        pairings = self.pairings.copy()
        while pairings:
            round_matches = []
            players_in_rounds = set()

        for pairing in pairings:
            if pairing[0] not in players_in_round and pairing[1] not in players_in_round:
                round_matches.append({"players": list(pairing), "completed": False, "winner": None})
                players_in_round.update(pairing)

