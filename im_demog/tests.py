from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Submission(QuestionnaireExpe, timeout_happened=True)
        yield Submission(QuestionnaireDemog, timeout_happened=True)
