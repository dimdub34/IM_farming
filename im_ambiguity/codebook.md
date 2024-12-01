# Codebook - Attributs des classes `Subsession`, `Group` et `Player`

## Subsession

*Pas d’attribut défini pour cette classe.*

## Group

*Pas d’attribut défini pour cette classe.*

## Player

| Nom de l'attribut | Label                                                                                   | Codage          | Type         | Choices                 |
|-------------------|-----------------------------------------------------------------------------------------|-----------------|--------------|--------------------------|
| `comprehension_1` | Supposons que vous ayez choisi la couleur ROUGE et que, dans la décision 9, vous choisissiez l'urne B. Quel serait votre gain potentiel si l'urne B ne contenait que des boules ROUGES ? | Valeurs possibles: 800, 0 | IntegerField  | [0, 800]                 |
| `comprehension_2` | Supposons que vous ayez choisi la couleur ROUGE et que, dans la décision 9, vous choisissiez l'urne B. Quel serait votre gain potentiel si l'urne B ne contenait que des boules BLEUES ? | Valeurs possibles: 800, 0 | IntegerField  | [0, 800]                 |
| `comprehension_3` | Supposons que vous ayez choisi la couleur BLEUE. Supposons que cette partie soit sélectionnée pour le gain de l'expérience et que vous gagniez 320 points. Pouvez-vous indiquer laquelle des 10 situations a été sélectionnée ? | Valeurs: 1-10 | IntegerField  | [1, 2, ..., 10]          |
| `color_red`       | Veuillez choisir une couleur:                                                           | `True`/`False`  | BooleanField | [(True, "ROUGE"), (False, "BLEU")] |
| `urn_b`           | Couleur de l'urne B (True : ROUGE, False : BLEU)                                        | `True`/`False`  | BooleanField | -                        |
| `urn_b_payoff`    | Gain potentiel associé à l'urne B                                                       | -               | IntegerField | -                        |
| `urna_1_red`      | Couleur de l'urne A pour la décision 1                                                  | `True`/`False`  | BooleanField | -                        |
| `urna_1_payoff`   | Gain potentiel associé à l'urne A pour la décision 1                                    | -               | IntegerField | -                        |
| `choice_1`        | Choix entre l'urne A ou B pour la décision 1                                            | `True`/`False`  | BooleanField | [(True, "A"), (False, "B")] |
| `choice_1_payoff` | Gain associé au choix pour la décision 1                                                | -               | IntegerField | -                        |
| ...               | ...                                                                                     | ...             | ...          | ...                      |
| `choice_10_payoff`| Gain associé au choix pour la décision 10                                               | -               | IntegerField | -                        |

**Note**: Les attributs `urna_i_red`, `urna_i_payoff`, `choice_i`, et `choice_i_payoff` (pour `i` variant de 1 à 10) sont définis pour chaque décision individuelle. 

- **comprehension_1** : Question de compréhension pour vérifier le gain potentiel avec l'urne B contenant uniquement des boules rouges.
- **comprehension_2** : Question de compréhension pour vérifier le gain potentiel avec l'urne B contenant uniquement des boules bleues.
- **comprehension_3** : Question de compréhension pour identifier la situation gagnante dans le cas d'un gain de 320 points.
- **color_red** : Choix de la couleur pour le jeu, entre *ROUGE* (True) et *BLEU* (False).
- **urn_b** : Indique si l'urne B est remplie de boules rouges ou bleues, déterminé aléatoirement.
- **urn_b_payoff** : Gain potentiel en fonction de la couleur de l'urne B et de la couleur choisie.
- **urna_i_red** : Couleur de l'urne A pour la décision `i` (rouge ou bleue).
- **urna_i_payoff** : Gain potentiel associé à l'urne A pour la décision `i`, en fonction de la couleur de l'urne et de la couleur choisie.
- **choice_i** : Choix entre l'urne A et l'urne B pour la décision `i`.
- **choice_i_payoff** : Gain associé au choix pour la décision `i`, déterminé en fonction du contenu de l'urne sélectionnée.

