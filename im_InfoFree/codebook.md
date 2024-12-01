# Codebook - Attributs des classes `Subsession`, `Group` et `Player`

## Subsession

| Nom de l'attribut | Label          | Codage | Type      | Choices |
|-------------------|----------------|--------|-----------|---------|
| `current_part`    | Partie actuelle | -      | IntegerField | -       |

- **current_part** : Indique la partie actuelle du jeu, initialisée en fonction de la séquence des jeux.

## Group

*Pas d’attribut défini pour cette classe.*

## Player

| Nom de l'attribut | Label                                                                                   | Codage         | Type         | Choices                 |
|-------------------|-----------------------------------------------------------------------------------------|----------------|--------------|--------------------------|
| `fumigate`        | Souhaitez-vous souscrire une assurance pour ce tour ?                                   | `True`/`False` | BooleanField | [(True, "Oui"), (False, "Non")] |
| `pest`            | Présence d'infestation                                                                  | `True`/`False` | BooleanField | -                        |
| `round_p`         | Probabilité d'infestation pour le tour                                                  | [0,1]          | FloatField   | -                        |
| `observed_p`      | Probabilité estimée de l'infestation                                                    | [0,1]          | FloatField   | -                        |
| `percentage_p`    | Probabilité estimée en pourcentage                                                      | [0,100]        | IntegerField | -                        |
| `displayed_p`     | Description qualitative de la probabilité estimée                                       | -              | StringField  | ["très faible", "faible", "moyen", "élevé", "très élevé"] |
| `round_payoff`    | Gain pour le tour                                                                       | -              | IntegerField | -                        |

- **fumigate** : Demande au participant s’il souhaite souscrire une assurance pour éviter les pertes liées à une infestation. Choix possible entre *Oui* (True) et *Non* (False), affiché sous forme de boutons radio horizontalement.
- **pest** : Indicateur de la survenue d'une infestation pour le tour en cours, déterminé en fonction de `round_p`.
- **round_p** : Probabilité qu'une infestation se produise pour le tour, calculée aléatoirement entre 0 et 1.
- **observed_p** : Probabilité estimée de l'infestation après application d'une erreur aléatoire, pour simuler l'incertitude de l'estimation.
- **percentage_p** : Probabilité estimée exprimée en pourcentage (0 à 100).
- **displayed_p** : Description qualitative de `observed_p`, utilisée pour fournir une évaluation verbale de la probabilité, avec les niveaux possibles *très faible*, *faible*, *moyen*, *élevé*, et *très élevé*.
- **round_payoff** : Gain associé au tour, calculé en fonction de la décision de souscrire une assurance et de la survenue d'une infestation.

