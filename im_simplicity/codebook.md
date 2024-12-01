# Codebook - Attributs des classes `Subsession`, `Group` et `Player`

## Subsession

*Pas d’attribut défini pour cette classe.*

## Group

*Pas d’attribut défini pour cette classe.*

## Player

| Nom de l'attribut     | Label                                      | Codage       | Type         | Choices           |
|-----------------------|--------------------------------------------|--------------|--------------|--------------------|
| `choice_1`            |                                            | `True`/`False` | BooleanField | [(True, "A"), (False, "B")] |
| `choice_2`            |                                            | `True`/`False` | BooleanField | [(True, "A"), (False, "B")] |
| `choice_3`            |                                            | `True`/`False` | BooleanField | [(True, "A"), (False, "B")] |
| `choice_4`            |                                            | `True`/`False` | BooleanField | [(True, "A"), (False, "B")] |
| `choice_5`            |                                            | `True`/`False` | BooleanField | [(True, "A"), (False, "B")] |
| `choice_6`            |                                            | `True`/`False` | BooleanField | [(True, "A"), (False, "B")] |
| `choice_7`            |                                            | `True`/`False` | BooleanField | [(True, "A"), (False, "B")] |
| `choice_8`            |                                            | `True`/`False` | BooleanField | [(True, "A"), (False, "B")] |
| `choice_9`            |                                            | `True`/`False` | BooleanField | [(True, "A"), (False, "B")] |
| `choice_10`           |                                            | `True`/`False` | BooleanField | [(True, "A"), (False, "B")] |
| `choice_1_payoff`     | Gain associé au choix pour la décision 1   | -            | IntegerField | -                  |
| `choice_2_payoff`     | Gain associé au choix pour la décision 2   | -            | IntegerField | -                  |
| `choice_3_payoff`     | Gain associé au choix pour la décision 3   | -            | IntegerField | -                  |
| `choice_4_payoff`     | Gain associé au choix pour la décision 4   | -            | IntegerField | -                  |
| `choice_5_payoff`     | Gain associé au choix pour la décision 5   | -            | IntegerField | -                  |
| `choice_6_payoff`     | Gain associé au choix pour la décision 6   | -            | IntegerField | -                  |
| `choice_7_payoff`     | Gain associé au choix pour la décision 7   | -            | IntegerField | -                  |
| `choice_8_payoff`     | Gain associé au choix pour la décision 8   | -            | IntegerField | -                  |
| `choice_9_payoff`     | Gain associé au choix pour la décision 9   | -            | IntegerField | -                  |
| `choice_10_payoff`    | Gain associé au choix pour la décision 10  | -            | IntegerField | -                  |

**Note** : Les attributs `choice_i` et `choice_i_payoff` (pour `i` variant de 1 à 10) sont définis pour chaque décision individuelle.

- **choice_i** : Choix entre l'option A et B pour la décision `i`, avec A étant associée à une valeur fixe et B à une combinaison de probabilités.
- **choice_i_payoff** : Gain associé au choix fait pour la décision `i`, calculé en fonction des valeurs dans `C.VALUES` et des probabilités dans `C.PROBAS`.

