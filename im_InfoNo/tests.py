from . import *


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield Instructions

        yield Submission(Decision, timeout_happened=True)
        yield ResultsRound

        if self.round_number == C.NUM_ROUNDS:
            yield End