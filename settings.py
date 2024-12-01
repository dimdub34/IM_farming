from os import environ

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
DEMO_PAGE_INTRO_HTML = """
<h3>Dimitri's local otree server</h3>
<figure>
<img src='http://leem.umontpellier.fr/img/LEEM.png' style='width: 200px;' />
</figure>
"""
SECRET_KEY = '0xhi&xd=^c1i(u+18j-wbvr-*c^5+5_a*fcc#vazzotcty_x^@'
INSTALLED_APPS = ['otree']

LANGUAGE_CODE = 'fr'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False
CUSTOM_POINTS_NAME = "ECU"

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=5.00,
    fill_auto=False,
)

ROOMS = []

SESSION_CONFIGS = [
    dict(name='proba_no_free_costly',
         num_demo_participants=10,
         app_sequence=['im_welcome', 'im_InfoNo', 'im_InfoFree', 'im_InfoCostly',
                       'im_bret', 'im_ambiguity', 'im_simplicity', 'im_crt', 'im_demog', "im_final"],
         real_world_currency_per_point=0.025,
         info="proba"
         ),
    dict(
        name='proba_free_no_costly',
        num_demo_participants=10,
        app_sequence=['im_welcome', 'im_InfoFree', 'im_InfoNo', 'im_InfoCostly',
                      'im_bret', 'im_ambiguity', 'im_simplicity', 'im_crt', 'im_demog', "im_final"],
        real_world_currency_per_point=0.025,
        info="proba"
    ),
    dict(
        name='level_no_free_costly',
        num_demo_participants=10,
        app_sequence=['im_welcome', 'im_InfoNo', 'im_InfoFree', 'im_InfoCostly',
                      'im_bret', 'im_ambiguity', 'im_simplicity', 'im_crt', 'im_demog', "im_final"],
        real_world_currency_per_point=0.025,
        info="level"
    ),
    dict(
        name='level_free_no_costly',
        num_demo_participants=10,
        app_sequence=['im_welcome', 'im_InfoFree', 'im_InfoNo', 'im_InfoCostly',
                      'im_bret', 'im_ambiguity', 'im_simplicity', 'im_crt', 'im_demog', "im_final"],
        real_world_currency_per_point=0.025,
        info="level"
    ),
]
