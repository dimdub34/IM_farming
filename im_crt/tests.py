from . import *

class PlayerBot(Bot):
    def play_round(self):
        yield Transition
        yield Submission(Questions, timeout_happened=True)