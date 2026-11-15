## Problème

Une recherche de fichiers a été lancée en blocage dans la session
principale, au lieu d'être détachée en tâche de fond.

## Symptômes

L'agent restait silencieux plusieurs minutes, sans retour intermédiaire,
indiscernable d'un agent bloqué ou planté aux yeux de l'utilisateur.

## Conséquences

Perte de confiance ponctuelle : impossible de savoir si le système
travaillait encore ou avait planté, sans autre moyen de vérifier que
d'attendre ou de redémarrer.

## Solution

Toute tâche de plus de 30 secondes part désormais systématiquement en
tâche de fond, avec un accusé de réception immédiat pendant qu'elle
tourne.

## Règle qui en découle

Un agent ne doit jamais rester silencieux plus de quelques secondes,
même en plein travail. Le silence et la panne sont indiscernables pour
un humain qui attend.
