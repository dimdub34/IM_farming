import random

from otree.api import *

doc = 'Ambiguity Elicitation'
app_name = "im_ambiguity"


class C(BaseConstants):
    NAME_IN_URL = 'imamb'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    A_VALUES = {
        1: [160, 0],
        2: [320, 0],
        3: [560, 0],
        4: [640, 0],
        5: [720, 0],
        6: [800, 0],
        7: [880, 0],
        8: [960, 0],
        9: [1040, 0],
        10: [1120, 0]
    }

    B_VALUES = [800, 0]

    VALUES = {k: v + [800, 0] for k, v in A_VALUES.items()}


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    comprehension_1 = models.IntegerField(
        label="Supposons que vous ayez choisi la couleur ROUGE et que, dans la décision 9, vous choisissiez "
              "l'urne B. Quel serait votre gain potentiel si l'urne B ne contenait que des boules ROUGES ?",
        choices=set(C.VALUES[9]))
    comprehension_2 = models.IntegerField(
        label="Supposons que vous ayez choisi la couleur ROUGE et que, dans la décision 9, vous choisissiez l'urne B. "
              "Quel serait votre gain potentiel si l'urne B ne contenait que des boules BLEUES ?",
        choices=set(C.VALUES[9]))
    comprehension_3 = models.IntegerField(
        label='Supposons que vous ayez choisi la couleur BLEUE. Supposons que cette partie soit sélectionnée pour le '
              'gain de l\'expérience et que vous gagniez 320 points. Pouvez-vous indiquer laquelle des 10 situations a été '
              'sélectionnée ?',
        choices=range(1, 11))

    color_red = models.BooleanField(
        label="Veuillez choisir une couleur:", choices=[[True, 'ROUGE'], [False, 'BLEU']],
        widget=widgets.RadioSelectHorizontal)
    urn_b = models.BooleanField(doc="True : ROUGE, False : Bleu")
    urn_b_payoff = models.IntegerField()

    urna_1_red = models.BooleanField()
    urna_1_payoff = models.IntegerField()
    choice_1 = models.BooleanField(choices=[[True, 'A'], [False, 'B']], label='')
    choice_1_payoff = models.IntegerField()

    urna_2_red = models.BooleanField()
    urna_2_payoff = models.IntegerField()
    choice_2 = models.BooleanField(choices=[[True, 'A'], [False, 'B']], label='')
    choice_2_payoff = models.IntegerField()

    urna_3_red = models.BooleanField()
    urna_3_payoff = models.IntegerField()
    choice_3 = models.BooleanField(choices=[[True, 'A'], [False, 'B']], label='')
    choice_3_payoff = models.IntegerField()

    urna_4_red = models.BooleanField()
    urna_4_payoff = models.IntegerField()
    choice_4 = models.BooleanField(choices=[[True, 'A'], [False, 'B']], label='')
    choice_4_payoff = models.IntegerField()

    urna_5_red = models.BooleanField()
    urna_5_payoff = models.IntegerField()
    choice_5 = models.BooleanField(choices=[[True, 'A'], [False, 'B']], label='')
    choice_5_payoff = models.IntegerField()

    urna_6_red = models.BooleanField()
    urna_6_payoff = models.IntegerField()
    choice_6 = models.BooleanField(choices=[[True, 'A'], [False, 'B']], label='')
    choice_6_payoff = models.IntegerField()

    urna_7_red = models.BooleanField()
    urna_7_payoff = models.IntegerField()
    choice_7 = models.BooleanField(choices=[[True, 'A'], [False, 'B']], label='')
    choice_7_payoff = models.IntegerField()

    urna_8_red = models.BooleanField()
    urna_8_payoff = models.IntegerField()
    choice_8 = models.BooleanField(choices=[[True, 'A'], [False, 'B']], label='')
    choice_8_payoff = models.IntegerField()

    urna_9_red = models.BooleanField()
    urna_9_payoff = models.IntegerField()
    choice_9 = models.BooleanField(choices=[[True, 'A'], [False, 'B']], label='')
    choice_9_payoff = models.IntegerField()

    urna_10_red = models.BooleanField()
    urna_10_payoff = models.IntegerField()
    choice_10 = models.BooleanField(choices=[[True, 'A'], [False, 'B']], label='')
    choice_10_payoff = models.IntegerField()

    def set_payoff(self):
        # boules de l'urne B, soit toutes rouges soit toutes bleues
        p_urn_b = random.uniform(0, 1)
        self.urn_b = random.choices([True, False], weights=[p_urn_b, 1 - p_urn_b])[0]
        self.urn_b_payoff = C.B_VALUES[0] if self.urn_b == self.color_red else C.B_VALUES[1]
        print(
            f"Couleur choisie : {'Rouge' if self.color_red else 'Bleue'}, Urne B: {'Rouge' if self.urn_b else 'Bleue'} "
            f"-> gain si urne B : {self.urn_b_payoff}")

        # tirage dans l'urne A, pour chaque décision, afin de déterminer si la couleur de l'urne est rouge ou bleue.
        # affectation du gain associé, selon la couleur choisie et la couleur de l'urne
        # détermination du gain selon que le joueur a choisi l'urne A ou l'urne B
        for i in range(1, 11):
            setattr(self, f"urna_{i}_red", random.choice([True, False]))
            setattr(self, f"urna_{i}_payoff",
                    C.A_VALUES[i][0] if getattr(self, f'urna_{i}_red') == self.color_red else C.A_VALUES[i][1])
            setattr(self, f"choice_{i}_payoff",
                    [self.urn_b_payoff, getattr(self, f"urna_{i}_payoff")][getattr(self, f"choice_{i}")])
            print(f"Décision {i} : choix {['B', 'A'][getattr(self, f'choice_{i}')]}, "
                  f"urne A: {'Rouge' if getattr(self, f'urna_{i}_red') else 'Bleue'} ({getattr(self, f'urna_{i}_payoff')}), "
                  f"urne B: {self.urn_b_payoff} -> gain {getattr(self, f'choice_{i}_payoff')}")

        # stockage pour fin expé
        chosen_color = f"{'Rouge' if self.color_red else 'Bleue'}"
        choices_info = list()
        for i in range(1, 11):
            choices_info.append(dict(
                choice_number=i,
                choice=['B', 'A'][getattr(self, f'choice_{i}')],
                A='Rouge' if getattr(self, f'urna_{i}_red') else 'Bleue',
                B='Rouge' if self.urn_b else 'Bleue',
                choice_payoff=getattr(self, f'choice_{i}_payoff'),
                payoff=cu(
                    getattr(self, f'choice_{i}_payoff') * self.session.config.get("real_world_currency_per_point"))
            ))
        self.participant.vars[app_name] = dict(chosen_color=chosen_color, choices_info=choices_info)
        print(self.participant.vars[app_name])

        paid_decision = self.participant.vars["paid_decision"]
        if 31 < paid_decision <= 41:
            corresponding_choice = paid_decision - 31
            choice_info = choices_info[corresponding_choice - 1]
            decision_choix = choice_info['choice']
            urne_decision_couleur = choice_info[decision_choix]
            decision_payoff = choice_info['choice_payoff']
            self.payoff = choice_info["payoff"]

            txt_final = (f"C'est la décision {corresponding_choice} de la partie 5 qui a été aléatoirement sélectionnée "
                         f"par le programme informatique pour déterminer votre gain pour l'expérience. ")
            txt_final += (f"Vous avez choisi la couleur {chosen_color}, et pour cette "
                          f"décision vous avez choisi l'urne {decision_choix}. "
                          f"Après tirage au sort par le programme informatique selon les règles de l'urne, cette "
                          f"urne était {urne_decision_couleur}. Votre gain est donc de {decision_payoff} points, soit "
                          f"{self.payoff}.")
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


class Instructions(MyPage):
    pass


class ControlQuestions(MyPage):
    form_model = 'player'
    form_fields = ['comprehension_1', 'comprehension_2', 'comprehension_3']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.comprehension_1 = random.choice(list(set(C.VALUES[9])))
            player.comprehension_2 = random.choice(list(set(C.VALUES[9])))
            player.comprehension_3 = random.randint(1, 10)


class Color(MyPage):
    form_model = 'player'
    form_fields = ['color_red']

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.color_red = random.choice([True, False])


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


page_sequence = [Instructions, ControlQuestions, Color, Decision]
