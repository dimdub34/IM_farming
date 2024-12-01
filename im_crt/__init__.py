import random

from otree.api import *

doc = 'CRT'


class C(BaseConstants):
    NAME_IN_URL = 'imcrt'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    crt_1 = models.IntegerField(
        label='Si 3 lutins de Noël peuvent emballer 3 jouets en 1 heure, combien de lutins faut-il pour emballer '
              '6 jouets en 2 heures ?', min=0, max=100)
    crt_2 = models.IntegerField(
        label='Jerry a reçu à la fois la 15ème note la plus élevée et la 15ème note la plus basse de la classe. '
              'Combien d’élèves y a-t-il dans la classe ?', min=0, max=100)
    crt_3 = models.IntegerField(
        label="Dans une équipe d’athlétisme, les membres de grande taille ont 3 fois plus de chances de gagner "
              "une médaille que les membres de petite taille. L'équipe a gagné 60 médailles. "
              "Combien ont été gagnées par des athlètes de petite taille ? ", min=0, max=100)
    score = models.IntegerField()

    def set_score(self):
        self.score = 0
        self.score += int(self.crt_1 == 3)
        self.score += int(self.crt_2 == 29)
        self.score += int(self.crt_3 == 15)

        withs = 's' if self.score > 1 else ''
        txt_final = f"Vous avez trouvé {self.score} bonne{withs} réponse{withs}."
        print(txt_final)

        self.participant.vars["CRT"] = dict(txt_final=txt_final)


# ======================================================================================================================
#
# -- PAGES
#
# ======================================================================================================================
class MyPage(Page):
    @staticmethod
    def js_vars(player: Player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))


class Transition(MyPage):
    pass


class Questions(MyPage):
    form_model = 'player'
    form_fields = ['crt_1', 'crt_2', 'crt_3']

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.crt_1 = random.choice([3, 6])
            player.crt_2 = random.choice([29, 30])
            player.crt_3 = random.choice([15, 20])
        player.set_score()


page_sequence = [Transition, Questions]
