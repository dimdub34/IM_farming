# Codebook du questionnaire socio-démographique

## **Attributs des joueurs**

### **Questions liées à l'expérience**

| **Attribut**         | **Type**       | **Codage**                                                                                          | **Description**                                                                                                                                                        |
|----------------------|----------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `risk_general`       | `FloatField`   | Valeurs de 0 à 10                                                                                 | Disposition générale à prendre des risques (0 : pas du tout disposé, 10 : très disposé).                                                                             |
| `cost_insurance`     | `StringField`  | `Elevé`, `Adéquat`, `Faible`                                                                      | Évaluation du coût de l'assurance dans les parties 1 à 3.                                                                                                            |
| `cost_info`          | `StringField`  | `Elevé`, `Adéquat`, `Faible`                                                                      | Évaluation du coût de l'information dans les parties 1 à 3.                                                                                                          |
| `error_big`          | `FloatField`   | Valeur entre 0 et 100                                                                             | Marge d'erreur maximale perçue lors de l'expérience (en pourcentage).                                                                                                |
| `error_small`        | `FloatField`   | Valeur entre 0 et 100                                                                             | Marge d'erreur minimale perçue lors de l'expérience (en pourcentage).                                                                                                |
| `error_average`      | `FloatField`   | Valeur entre 0 et 100                                                                             | Marge d'erreur moyenne perçue lors de l'expérience (en pourcentage).                                                                                                 |
| `error_new`          | `IntegerField` | `0` : Trop importante et information non fiable<br>`1` : Acceptable et information partiellement fiable<br>`2` : Insignifiante et information fiable | Évaluation de la fiabilité des marges d'erreur annoncées.                                                                                                            |

---

### **Données sociodémographiques**

| **Attribut**              | **Type**       | **Codage**                                                                                          | **Description**                                                                                                                                                        |
|---------------------------|----------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `gender`                 | `IntegerField` | `0` : Féminin, `1` : Masculin                                                                     | Sexe du participant.                                                                                                                                                 |
| `age`                    | `IntegerField` | Valeurs entre 16 et 100                                                                           | Âge du participant.                                                                                                                                                  |
| `nationality`            | `StringField`  | Liste des pays (selon le code ISO 3166)                                                           | Nationalité du participant.                                                                                                                                          |
| `marital_status`         | `IntegerField` | `0` : Célibataire<br>`1` : Pacsé(e)<br>`2` : Marié(e)<br>`3` : Divorcé(e)<br>`4` : Veuf(ve)       | Statut marital du participant.                                                                                                                                       |
| `socioprofessional_group`| `IntegerField` | `0` : Étudiant<br>`1` : Agriculteurs exploitants<br>`2` : Artisans, commerçants et chefs d’entreprise<br>`3` : Cadres et professions intellectuelles supérieures<br>`4` : Professions intermédiaires<br>`5` : Employés<br>`6` : Ouvriers<br>`7` : Retraités<br>`8` : Autres sans activité | Catégorie socio-professionnelle du participant.                                                                                                                     |
| `diplome`               | `IntegerField` | `0` : Pas de diplôme<br>`1` : CEP / Brevet<br>`2` : BEP / CAP<br>`3` : Baccalauréat<br>`4` : Licence<br>`5` : Master<br>`6` : Doctorat | Diplôme le plus élevé obtenu par le participant.                                                                                                                     |
| `discipline`            | `IntegerField` | Codes des disciplines selon la liste définie (voir ci-dessous)                                     | Discipline principale étudiée ou pratiquée par le participant.                                                                                                       |

---

### **Codes pour les disciplines**

| **Code** | **Discipline**                                                                                                                                                                       |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `0`      | Sciences humaines et sociales : psychologie, sociologie, anthropologie, histoire, géographie, sciences politiques, droit, linguistique, philosophie, communication, etc.           |
| `1`      | Sciences exactes et appliquées : mathématiques, physique, chimie, informatique, génie civil, mécanique, électrique, électronique, aéronautique, etc.                                |
| `2`      | Sciences de la vie et de la santé : biologie, médecine, pharmacologie, soins infirmiers, kinésithérapie, nutrition, etc.                                                            |
| `3`      | Arts et lettres : arts visuels, musique, théâtre, danse, littérature, langues étrangères, etc.                                                                                      |
| `4`      | Commerce, gestion et économie : administration des affaires, marketing, finance, comptabilité, commerce international, économie, etc.                                               |
| `5`      | Éducation : éducation, enseignement, formation, psychologie de l'éducation, etc.                                                                                                   |
| `6`      | Sciences agricoles et environnementales : agriculture, sciences environnementales, foresterie, pêche, etc.                                                                          |
| `7`      | Sport                                                                                                                                                                               |
| `8`      | Pas dans la liste                                                                                                                                                                   |
| `9`      | Non concerné(e)                                                                                                                                                                     |

---

## **Pages**

### **Page : QuestionnaireExpe**

- Collecte les réponses liées aux risques perçus, au coût de l'assurance et de l'information, ainsi qu'à l'évaluation des marges d'erreur.

### **Page : QuestionnaireDemog**

- Collecte les données sociodémographiques du participant : âge, genre, nationalité, statut marital, catégorie socio-professionnelle, diplôme, et discipline.
