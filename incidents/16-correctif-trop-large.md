## Problème

Un correctif posé pour éviter des notifications non sollicitées a été
mal calibré : il a supprimé toute notification, même pendant une
conversation active où un message était légitimement attendu.

## Symptômes

Des réponses qui auraient dû arriver normalement ont cessé d'apparaître,
cette fois parce que le correctif lui-même était trop large.

## Conséquences

Le même soir, un deuxième correctif a dû être écrit pour réparer le
premier, qui avait remplacé un défaut visible par un défaut plus
discret.

## Solution

Le comportement a été recalibré pour ne couper que les notifications
réellement non sollicitées, en laissant intactes celles qui
correspondent à une conversation en cours.

## Règle qui en découle

Corriger un défaut par une règle trop large peut créer un second défaut,
parfois plus difficile à repérer que le premier. Une correction doit
viser le cas précis, pas le supprimer en bloc.
