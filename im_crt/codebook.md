# Codebook - Attributs des classes `Subsession`, `Group` et `Player`

## Subsession

*Pas d’attribut défini pour cette classe.*

## Group

*Pas d’attribut défini pour cette classe.*

## Player

| Nom de l'attribut | Label                                                                                   | Codage  | Type         | Choices |
|-------------------|-----------------------------------------------------------------------------------------|---------|--------------|---------|
| `crt_1`           | Si 3 lutins de Noël peuvent emballer 3 jouets en 1 heure, combien de lutins faut-il pour emballer 6 jouets en 2 heures ? | [0, 100] | IntegerField | -       |
| `crt_2`           | Jerry a reçu à la fois la 15ème note la plus élevée et la 15ème note la plus basse de la classe. Combien d’élèves y a-t-il dans la classe ? | [0, 100] | IntegerField | -       |
| `crt_3`           | Dans une équipe d’athlétisme, les membres de grande taille ont 3 fois plus de chances de gagner une médaille que les membres de petite taille. L'équipe a gagné 60 médailles. Combien ont été gagnées par des athlètes de petite taille ? | [0, 100] | IntegerField | -       |
| `score`           | Nombre de réponses correctes                                                          | [0, 3]   | IntegerField | -       |

- **crt_1** : Réponse au premier problème du CRT (Cognitive Reflection Test) sur les lutins de Noël.
- **crt_2** : Réponse au second problème du CRT sur le classement des notes en classe.
- **crt_3** : Réponse au troisième problème du CRT concernant les médailles remportées par les athlètes de petite taille.
- **score** : Nombre de réponses correctes aux questions CRT, calculé automatiquement en fonction des réponses fournies.

