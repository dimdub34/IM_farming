from otree.api import *
import random


doc = """
Welcome
"""
app_name = "im_welcome"


class C(BaseConstants):
    NAME_IN_URL = 'im_welcome'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    game_sequence = models.StringField()
    info = models.StringField()

def creating_session(subsession: Subsession):
    game_sequence = subsession.session.config.get("app_sequence")
    game_sequence = [g for g in game_sequence if "Info" in g]
    subsession.game_sequence = "-".join(game_sequence)
    if "game_sequence" not in subsession.session.vars:
        subsession.session.vars["game_sequence"] = game_sequence

    subsession.info = subsession.session.config.get("info")
    subsession.session.vars["info"] = subsession.info

    # selection de la décision rémunérée
    for p in subsession.get_players():
        p.paid_decision = random.randint(1, 51)
        p.participant.vars['paid_decision'] = p.paid_decision

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    paid_decision = models.IntegerField()

# ======================================================================================================================
#
# PAGES
#
# ======================================================================================================================

class MyPage(Page):
    @staticmethod
    def js_vars(player: Player):
        return dict(
            fill_auto=player.session.config.get("fill_auto", False)
        )


class Welcome(MyPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


page_sequence = [Welcome]
