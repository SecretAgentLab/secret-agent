## Problème

Le format utilisé pour un contenu pédagogique de langue utilisait des
tirets longs qui s'affichaient de façon illisible sur l'application
mobile de la plateforme de livraison.

## Symptômes

Le contenu restait lisible sur certains supports mais devenait confus
sur d'autres, selon l'appareil utilisé pour le consulter.

## Conséquences

Une expérience de lecture dégradée sans que rien ne signale le problème
côté production : le contenu semblait correct tant qu'on ne le
consultait pas sur le bon support.

## Solution

Le tiret long a été remplacé par une ponctuation plus robuste à travers
tous les supports de lecture visés.

## Règle qui en découle

Un format de contenu doit être vérifié sur tous les supports de
consultation réels, pas seulement sur celui utilisé pour le produire.
Ce qui s'affiche bien d'un côté peut casser ailleurs.
