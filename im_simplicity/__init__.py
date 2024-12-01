import random

from otree.api import *

doc = 'Simplicity Equivalents'
app_name = "im_simplicity"


def get_field():
    return models.BooleanField(choices=[(True, 'A'), (False, 'B')], label="")


class C(BaseConstants):
    NAME_IN_URL = 'imsimp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    VALUES = {
        1: [80, 550, 300],
        2: [160, 550, 300],
        3: [280, 550, 300],
        4: [320, 550, 300],
        5: [360, 550, 300],
        6: [400, 550, 300],
        7: [440, 550, 300],
        8: [480, 550, 300],
        9: [520, 550, 300],
        10: [550, 550, 300]
    }

    PROBAS = [100, 40, 60]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice_1 = get_field()
    choice_2 = get_field()
    choice_3 = get_field()
    choice_4 = get_field()
    choice_5 = get_field()
    choice_6 = get_field()
    choice_7 = get_field()
    choice_8 = get_field()
    choice_9 = get_field()
    choice_10 = get_field()

    choice_1_payoff = models.IntegerField()
    choice_2_payoff = models.IntegerField()
    choice_3_payoff = models.IntegerField()
    choice_4_payoff = models.IntegerField()
    choice_5_payoff = models.IntegerField()
    choice_6_payoff = models.IntegerField()
    choice_7_payoff = models.IntegerField()
    choice_8_payoff = models.IntegerField()
    choice_9_payoff = models.IntegerField()
    choice_10_payoff = models.IntegerField()

    def set_payoff(self):
        choices_info = list()
        for i in range(1, 11):
            values = C.VALUES[i]
            selected_choice_option = ['B', 'A'][getattr(self, f"choice_{i}")]
            if selected_choice_option == 'A':
                setattr(self, f"choice_{i}_payoff", values[0])
            else:
                setattr(self, f"choice_{i}_payoff",
                        int(values[1] * C.PROBAS[1] / 100 + values[2] * C.PROBAS[2] / 100))
            choices_info.append(dict(
                choice_number=i, choice=selected_choice_option, choice_payoff=getattr(self, f"choice_{i}_payoff"),
                payoff=cu(
                    getattr(self, f"choice_{i}_payoff") * self.session.config.get("real_world_currency_per_point"))))

        self.participant.vars[app_name] = dict(choices_info=choices_info)
        print(self.participant.vars[app_name])

        paid_decision = self.participant.vars["paid_decision"]
        if 41 < paid_decision <= 51:
            corresponding_choice = paid_decision - 41
            choice = getattr(self, f"choice_{corresponding_choice}")
            choice_payoff = getattr(self, f"choice_{corresponding_choice}_payoff")
            self.payoff = cu(choice_payoff * self.session.config.get("real_world_currency_per_point"))

            txt_final = (
                f"C'est la décision {corresponding_choice} de la partie 6 qui a été aléatoirement sélectionnée "
                f"par le programme informatique pour déterminer votre gain pour l'expérience. "
                f"A cette décision vous avez choisi l'option {'A' if choice else 'B'}, votre gain est donc "
                f" de {choice_payoff} points, soit {self.payoff}.")

            self.participant.vars["txt_final"] = txt_final
            self.participant.vars["payoff"] = self.payoff


# ======================================================================================================================
#
# -- PAGES
#
# ======================================================================================================================

class MyPage(Page):
    @staticmethod
    def js_vars(player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))


class Decision(MyPage):
    form_model = 'player'
    form_fields = ['choice_1', 'choice_2', 'choice_3', 'choice_4', 'choice_5', 'choice_6', 'choice_7', 'choice_8',
                   'choice_9', 'choice_10']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            for i in range(1, 11):
                setattr(player, f"choice_{i}", random.choice([True, False]))
        player.set_payoff()


page_sequence = [Decision]
