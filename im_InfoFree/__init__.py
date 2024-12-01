import random

from otree.api import *

doc = "Free Information"
app_name = 'im_InfoFree'


class C(BaseConstants):
    NAME_IN_URL = 'imfree'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    R_MAX = 500
    R_MIN = 300
    C = 100
    P_OVERALL = 0.5


class Subsession(BaseSubsession):
    current_part = models.IntegerField()


def creating_session(subsession: Subsession):
    subsession.current_part = subsession.session.vars["game_sequence"].index(app_name) + 1
    for p in subsession.get_players():
        if p.round_number == 1:
            p.participant.vars[app_name] = dict()

        p.round_p = round(random.uniform(0, 1), 2)

        error = random.choices([-0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15, 0.20],
                               weights=[0.025, 0.05, 0.075, 0.1, 0.5, 0.1, 0.075, 0.05, 0.025])[0]
        estimated_p = p.round_p + error
        if estimated_p > 1:
            estimated_p = 1
        if estimated_p < 0:
            estimated_p = 0

        p.observed_p = round(estimated_p, 2)
        p.percentage_p = int(p.observed_p * 100)
        if p.observed_p <= 0.3:
            p.displayed_p = "très faible"
        elif 0.3 < p.observed_p < 0.5:
            p.displayed_p = "faible"
        elif p.observed_p == 0.5:
            p.displayed_p = "moyen"
        elif 0.5 < p.observed_p <= 0.7:
            p.displayed_p = "élevé"
        else:
            p.displayed_p = "très élevé"



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    fumigate = models.BooleanField(
        label='Souhaitez-vous souscrire une assurance pour ce tour ?',
        choices=[(True, "Oui"), (False, "Non")], widget=widgets.RadioSelectHorizontal)
    pest = models.BooleanField()
    round_p = models.FloatField(max=1, min=0)
    observed_p = models.FloatField(max=1, min=0)
    percentage_p = models.IntegerField(max=100, min=0)
    displayed_p = models.StringField()
    round_payoff = models.IntegerField()

    def set_payoff(self):
        self.pest = random.choices([True, False], weights=[self.round_p, 1 - self.round_p])[0]
        if self.fumigate:
            self.round_payoff = C.R_MAX - C.C
        else:
            self.round_payoff = C.R_MIN if self.pest else C.R_MAX
        self.payoff = cu(self.round_payoff * self.session.config.get("real_world_currency_per_point"))

        if self.round_number == C.NUM_ROUNDS:
            paid_decision = self.participant.vars["paid_decision"]
            if paid_decision <= 2 * C.NUM_ROUNDS:  # partie 1 ou 2
                corresponding_round = None
                if self.subsession.current_part == 1 and paid_decision <= C.NUM_ROUNDS:
                    corresponding_round = self.in_round(paid_decision)
                elif self.subsession.current_part == 2 and (C.NUM_ROUNDS < paid_decision <= 2 * C.NUM_ROUNDS):
                    corresponding_round = self.in_round(paid_decision - C.NUM_ROUNDS)

                if corresponding_round is not None:
                    txt_final = (
                        f"C'est le tour {corresponding_round.round_number} de la partie {self.subsession.current_part} "
                        f"qui a été aléatoirement "
                        f"sélectionné par le programme informatique pour déterminer votre gain pour l'expérience. "
                        f"A ce tour, vous avez gagné {corresponding_round.round_payoff} points, soit "
                        f"{corresponding_round.payoff}."
                    )
                    self.participant.vars["txt_final"] = txt_final
                    self.participant.vars["payoff"] = corresponding_round.payoff

            # in any case we store the rounds
            rounds_info = list()
            for p in self.in_all_rounds():
                rounds_info.append(dict(
                    round_number=p.round_number, fumigate=p.fumigate, pest=p.pest, round_payoff=p.round_payoff,
                    payoff=p.payoff
                ))
            self.participant.vars[app_name]["rounds_info"] = rounds_info
            print(self.participant.vars[app_name]["rounds_info"])


# ======================================================================================================================#
#
# PAGES --
#
# ======================================================================================================================
class MyPage(Page):
    @staticmethod
    def js_vars(player):
        parameters = C.__dict__.copy()
        parameters.update(dict(fill_auto=player.session.config.get("fill_auto", False)))
        return parameters


class Instructions(MyPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Decision(MyPage):
    form_model = 'player'
    form_fields = ['fumigate']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.fumigate = random.choice([True, False])
        player.set_payoff()


class ResultsRound(MyPage):
    pass


class End(MyPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Instructions, Decision, ResultsRound, End]
