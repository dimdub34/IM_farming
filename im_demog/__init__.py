import random

from otree.api import *
from pycountry import countries

from settings import LANGUAGE_CODE

countries_names = list([c.name for c in countries])
countries_names.sort()

doc = """
QuestionnaireDemog socio-démographique 
"""

which_language = dict(fr=False, en=False)
which_language[LANGUAGE_CODE] = True
_ = lambda x: x[LANGUAGE_CODE]


def disciplines():
    categories = [
        _(dict(
            fr="Sciences humaines et sociales : psychologie, sociologie, anthropologie, histoire, géographie, "
               "sciences politiques, droit, linguistique, philosophie, communication, etc.",
            en="Human and social sciences: psychology, sociology, anthropology, history, geography, political science, "
               "law, linguistics, philosophy, communication, etc."
        )),
        _(dict(
            fr="Sciences exactes et appliquées : mathématiques, physique, chimie, informatique, génie civil, "
               "mécanique, électrique, électronique, aéronautique, etc.",
            en="Exact and applied sciences: mathematics, physics, chemistry, computer science, civil engineering, "
               "mechanical engineering, electrical engineering, electronics, aeronautics, etc."
        )),
        _(dict(
            fr="Sciences de la vie et de la santé : biologie, médecine, pharmacologie, soins infirmiers, "
               "kinésithérapie, nutrition, etc.",
            en="Life and health sciences: biology, medicine, pharmacology, nursing, physiotherapy, nutrition, etc."
        )),
        _(dict(
            fr="Arts et lettres : arts visuels, musique, théâtre, danse, littérature, langues étrangères, etc.",
            en="Arts and letters: visual arts, music, theater, dance, literature, foreign languages, etc."
        )),
        _(dict(
            fr="Commerce, gestion et économie : administration des affaires, marketing, finance, comptabilité, "
               "commerce international, économie etc.",
            en="Business, management, and economics: business administration, marketing, finance, accounting, "
               "international trade, economics, etc."
        )),
        _(dict(
            fr="Éducation : éducation, enseignement, formation, psychologie de l'éducation, etc.",
            en="Education: education, teaching, training, educational psychology, etc."
        )),
        _(dict(
            fr="Sciences agricoles et environnementales : agriculture, sciences environnementales, foresterie, pêche, etc.",
            en="Agricultural and environmental sciences: agriculture, environmental sciences, forestry, fishing, etc."
        )),
        _(dict(fr="Sport", en="Sport")),
        _(dict(fr="Pas dans la liste", en="Not in the list")),
        _(dict(fr="Non concerné(e)", en="Not concerned"))
    ]
    return [(i, e) for i, e in enumerate(categories)]


class C(BaseConstants):
    NAME_IN_URL = 'imdemog'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Questionnaire expe
    risk_general = models.FloatField(
        label='Sur une échelle de 0 à 10, dans quelle mesure êtes-vous disposé(e) à prendre des risques, '
              'en général (de 0 pas du tout disposé(e) à 10 très disposé(e)) ?', choices=range(11),
        widget=widgets.RadioSelectHorizontal)
    cost_insurance = models.StringField(
        label='Dans les parties 1 à 3, vous aviez le choix de souscrire une assurance contre le dommage. '
              'Selon vous, le coût de cette assurance était : ',
        choices=['Elevé', 'Adéquat', 'Faible'], widget=widgets.RadioSelectHorizontal
    )
    cost_info = models.StringField(
        label="Dans certaines des parties 1 à 3, vous avez eu le choix d'acheter de l'information sur "
              "le risque de dommage. Selon vous, le coût de l'information était :",
        choices=['Elevé', 'Adéquat', 'Faible'], widget=widgets.RadioSelectHorizontal
    )
    error_big = models.FloatField(
        label="Dans certaines des parties 1 à 3, vous avez reçu des informations spécifiques sur le risque de "
              "dommage lors de certains tours particuliers. "
              "Quelle est selon vous la marge d'erreur la plus grande qui s'est produite durant un tour"
              " (en pourcentage, de 0 à 100) ?",
        max=100, min=0)
    error_small = models.FloatField(
        label="Dans certaines des parties 1 à 3, vous avez reçu des informations spécifiques sur le risque de "
              "dommage lors de certains tours particuliers. "
              "Quelle est selon vous la marge d'erreur la plus petite qui s'est produire durant un tour "
              "(en pourcentage, de 0 à 100) ?",
        max=100, min=0)
    error_average = models.FloatField(
        label="Dans certaines des parties 1 à 3, vous avez reçu des informations spécifiques sur le risque de "
              "dommage lors de certains tours particuliers. "
              "Quelle est selon vous la marge d'erreur moyenne qui s'est produite tout au long l'expérience "
              "(en pourcentage, de 0 à 100) ?",
        max=100, min=0)
    error_new = models.IntegerField(
        label="Selon vous, la marge d'erreur annoncée était :",
        choices=[(0, "Trop importante et j'ai considéré que cela rendait l'information non fiable."),
                 (1, "Acceptable et j'ai considéré que cela rendait l'information partiellement fiable."),
                 (2, "insignifiante et j'ai considéré que cela n'affectait pas la fiabilité de l'information.")],
        widget=widgets.RadioSelect)

    # Questionnaire demog ----------------------------------------------------------------------------------------------
    gender = models.IntegerField(
        label=_(dict(fr="Sexe", en="Sex")),
        choices=[(0, _(dict(fr="Féminin", en="Female"))), (1, _(dict(fr="Masculin", en="Male")))],
        widget=widgets.RadioSelectHorizontal
    )
    age = models.IntegerField(
        label="Age",
        choices=range(16, 101)
    )
    nationality = models.StringField(
        label=_(dict(fr="Nationalité", en="Nationality")),
        choices=[(i, e) for i, e in enumerate(countries_names)]
    )
    marital_status = models.IntegerField(
        label=_(dict(fr="Statut marital", en="Marital status")),
        choices=list(zip(range(5),
                         [
                             _(dict(fr="Célibataire", en="Single")),
                             _(dict(fr="Pacsé(e)", en="In a civil union")),
                             _(dict(fr="Marié(e)", en="Married")),
                             _(dict(fr="Divorcé(e)", en="Divorced")),
                             _(dict(fr="Veuf(ve)", en="Widowed"))]
                         )
                     ),
        widget=widgets.RadioSelectHorizontal
    )
    socioprofessional_group = models.IntegerField(
        label=_(dict(fr="Catégorie socio-professionnelle", en="Socio-professional category")),
        choices=[
            (0, _(dict(fr="Étudiant", en="Student"))),
            (1, _(dict(fr="Agriculteurs exploitants", en="Farmers"))),
            (2,
             _(dict(fr="Artisans, commerçants et chefs d’entreprise",
                    en="Craftsmen, shopkeepers, and business owners"))),
            (3, _(dict(fr="Cadres et professions intellectuelles supérieures",
                       en="Executives and higher intellectual professions"))),
            (4, _(dict(fr="Professions Intermédiaires", en="Intermediate professions"))),
            (5, _(dict(fr="Employés", en="Employees"))),
            (6, _(dict(fr="Ouvriers", en="Workers"))),
            (7, _(dict(fr="Retraités", en="Retired"))),
            (8, _(dict(fr="Autres personnes sans activité professionnelle", en="Other non-working individuals")))
        ],
        widget=widgets.RadioSelect
    )
    diplome = models.IntegerField(
        label=_(dict(fr="Diplôme le plus élevé obtenu", en="Highest degree obtained")),
        choices=[
            (0, _(dict(fr="Pas de diplôme", en="No diploma"))),
            (1, _(dict(fr="CEP / Brevet des collèges", en="CEP / Middle school diploma"))),
            (2, _(dict(fr="BEP / CAP", en="BEP / CAP"))),
            (3, _(dict(fr="Baccalauréat", en="Baccalaureate"))),
            (4, _(dict(fr="Licence (Bac +3)", en="Bachelor's degree (Bac +3)"))),
            (5, _(dict(fr="Master (Bac +5)", en="Master's degree (Bac +5)"))),
            (6, _(dict(fr="Doctorat (Bac +8)", en="Doctorate (Bac +8)")))
        ],
        widget=widgets.RadioSelect
    )
    discipline = models.IntegerField(
        label=_(dict(fr="Discipline étudiée", en="Field of study")), choices=disciplines(), widget=widgets.RadioSelect
    )


# ======================================================================================================================
#
# -- PAGES
#
# ======================================================================================================================
class MyPage(Page):
    @staticmethod
    def js_vars(player: Player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))


class QuestionnaireExpe(MyPage):
    form_model = "player"
    form_fields = ["risk_general", "cost_insurance", "cost_info", "error_new"
                   # "error_big", "error_small", "error_average"
                   ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.risk_general = random.randint(0, 10)
            player.cost_insurance = random.choice(['Elevé', 'Adéquat', 'Faible'])
            player.cost_info = random.choice(['Elevé', 'Adéquat', 'Faible'])
            # player.error_big = random.randint(0, 100)
            # player.error_small = random.randint(0, 100)
            # player.error_average = random.randint(0, 100)
            player.error_new = random.randint(0, 2)


class QuestionnaireDemog(MyPage):
    form_model = "player"
    form_fields = ["gender", "age", "nationality", "marital_status", "socioprofessional_group",
                   "diplome", "discipline"]

    @staticmethod
    def vars_for_template(player):
        return dict(**which_language)

    @staticmethod
    def js_vars(player: Player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))

    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.gender = random.randint(0, 1)
            player.age = random.randint(16, 100)
            player.nationality = random.choice([(i, e) for i, e in enumerate(countries_names)])[1]
            player.marital_status = random.randint(0, 4)
            player.socioprofessional_group = random.randint(0, 8)
            player.diplome = random.randint(0, 6)
            player.discipline = random.choice(disciplines())[0]


page_sequence = [QuestionnaireExpe, QuestionnaireDemog]
