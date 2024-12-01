# Codebook - Attributs des classes `Subsession`, `Group` et `Player`

## Subsession

*Pas d’attribut défini pour cette classe.*

## Group

*Pas d’attribut défini pour cette classe.*

## Player

| Nom de l'attribut | Label                                             | Codage         | Type         | Choices                 |
|-------------------|---------------------------------------------------|----------------|--------------|--------------------------|
| `n_boxes`         | Combien de boîtes souhaitez-vous collecter ?      | [1, 100]       | IntegerField | -                        |
| `bomb_box`        | Boîte contenant la bombe                          | [1, 100]       | IntegerField | -                        |
| `explode`         | Indicateur d'explosion                            | `True`/`False` | BooleanField | -                        |
| `payoff_points`   | Points de gain si pas d'explosion                 | -              | IntegerField | -                        |

- **n_boxes** : Nombre de boîtes que le participant souhaite collecter, avec une valeur comprise entre 1 et 100.
- **bomb_box** : Boîte contenant la bombe, déterminée aléatoirement entre 1 et 100.
- **explode** : Indicateur indiquant si la bombe a explosé. True si le nombre de boîtes collectées est supérieur au numéro de la boîte contenant la bombe.
- **payoff_points** : Points de gain pour le participant s'il n'y a pas d'explosion, calculé comme `n_boxes * 8 * (1 - explode)`.

