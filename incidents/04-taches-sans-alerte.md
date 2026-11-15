## Problème

Un audit interne a découvert que l'ensemble des tâches planifiées de la
flotte tournait sans la moindre alerte d'échec configurée.

## Symptômes

Aucun : c'est précisément le problème. Une tâche planifiée pouvait échouer
silencieusement pendant des jours sans que personne ne le remarque, faute
de signal.

## Conséquences

Risque identifié comme le plus grave trouvé par cet audit : une panne
invisible est plus coûteuse qu'une panne bruyante, parce qu'elle ne
déclenche aucune réaction tant qu'elle n'est pas cherchée activement.

## Solution

Une alerte se déclenche désormais automatiquement sur tout échec de
tâche planifiée, sans exception.

## Règle qui en découle

Une tâche qui réussit aujourd'hui doit aussi prévoir le jour où elle
échouera. Une alerte sur échec n'est pas optionnelle, elle fait partie
de la tâche elle-même, pas un ajout de confort.
