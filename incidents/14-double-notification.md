## Problème

Les mêmes récapitulatifs arrivaient en double, sur deux canaux
différents à la fois.

## Symptômes

Signalé deux jours de suite avant correction : le même contenu, livré
deux fois, sur deux plateformes distinctes.

## Conséquences

Une confusion sur ce qui était réellement à lire, et une perte de
confiance sur la fiabilité du routage des messages.

## Solution

Chaque type de récapitulatif a été rattaché explicitement à un seul
canal de destination, plutôt que de laisser le système choisir par
défaut.

## Règle qui en découle

Un contenu ne doit jamais avoir deux destinations possibles par défaut.
Si plusieurs canaux existent, la destination doit être explicite,
jamais déduite.
