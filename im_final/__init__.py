from otree.api import *

doc = """
Final screen
"""


class C(BaseConstants):
    NAME_IN_URL = 'imfinal'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    pass


def vars_for_admin_report(subsession: Subsession):
    players_infos = list()
    for p in subsession.get_players():
        paid_decision = p.participant.vars["paid_decision"]
        if paid_decision <= 10:
            part = 1
            paid_decision_number = paid_decision
        elif 10 < paid_decision <= 20:
            part = 2
            paid_decision_number = paid_decision - 10
        elif 20 < paid_decision <= 30:
            part = 3
            paid_decision_number = paid_decision - 20
        elif paid_decision == 31:
            part = 4
            paid_decision_number = 1
        elif 31 < paid_decision <= 41:
            part = 5
            paid_decision_number = paid_decision - 31
        else:
            part = 6
            paid_decision_number = paid_decision - 41

        players_infos.append(dict(
            code=p.participant.code,
            label=p.participant.label,
            paid_decision=paid_decision,
            part=part,
            paid_decision_number=paid_decision_number,
            payoff=p.participant.payoff
        ))
    return dict(players_infos=players_infos)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    comments = models.LongStringField(blank=True)


# ======================================================================================================================
#
# -- PAGES
#
# ======================================================================================================================
class BeforeFinal(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.payoff = player.participant.vars["payoff"]


class Final(Page):
    form_model = 'player'
    form_fields = ["comments"]

    @staticmethod
    def js_vars(player: Player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.comments = "Commentaires automatiques"


class FinalAfterComments(Page):
    pass


page_sequence = [BeforeFinal, Final, FinalAfterComments]
