import random

from otree.api import *

doc = 'BRET'
app_name = "im_bret"


class C(BaseConstants):
    NAME_IN_URL = 'imbret'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    NB_ROWS = 10
    NB_COLS = 10

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    n_boxes = models.IntegerField(label="Combien de boîtes souhaitez-vous collecter ?", min=1, max=100)
    bomb_box = models.IntegerField(max=100, min=0)
    explode = models.BooleanField()
    payoff_points = models.IntegerField()

    def bomb(self):
        self.bomb_box = random.randint(1, 100)
        self.explode = self.n_boxes > self.bomb_box
        self.payoff_points = self.n_boxes * 8 * (1 - self.explode)
        self.payoff = cu(self.payoff_points * self.session.config.get("real_world_currency_per_point"))

        withs = 's' if self.payoff_points > 1 else ''
        txt_final = (f"Vous avez collecté {self.n_boxes} boîtes. La bombe était derrière la boîte {self.bomb_box}. "
                     f"Votre gain pour cette partie est donc de {self.payoff_points} point{withs}, soit {self.payoff}.")
        self.participant.vars[app_name] = dict(txt_final=txt_final, payoff=self.payoff)
        print(self.participant.vars[app_name])

        if self.participant.vars["paid_decision"] == 31:
            txt_final_final = (
                f"C'est la décision de la partie 4 qui a été aléatoirement sélectionnée par le programme "
                f"informatique pour déterminer votre gain de l'expérience. ")
            txt_final_final += txt_final
            self.participant.vars["txt_final"] = txt_final_final
            self.participant.vars["payoff"] = self.payoff


# ======================================================================================================================
#
# -- PAGES
#
# ======================================================================================================================
class MyPage(Page):
    @staticmethod
    def js_vars(player: Player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))


class Decision(MyPage):
    form_model = 'player'
    form_fields = ['n_boxes']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.n_boxes = random.randint(1, 100)
        player.bomb()


page_sequence = [Decision]
