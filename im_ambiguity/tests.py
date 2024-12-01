from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Instructions
        yield Submission(ControlQuestions, timeout_happened=True, check_html=False)
        yield Submission(Color, timeout_happened=True)
        yield Submission(Decision, timeout_happened=True)
