## Problème

Trois pièges accumulés lors de réaffectations de modèles de langage sur
plusieurs agents : changer de fournisseur sans effacer l'ancienne
référence technique, un caractère interdit dans un nom de modèle qui
casse la syntaxe de configuration, et un cron à haute fréquence resté
non épinglé qui a failli basculer par effet de bord sur un quota payant.

## Symptômes

Des appels routés vers le mauvais point technique après un changement de
fournisseur ; une configuration qui refusait de charger à cause d'un
caractère mal interprété ; une tâche planifiée à forte fréquence
silencieusement exposée à un changement de coût non voulu.

## Conséquences

Trois incidents distincts, mais une seule cause de fond : la
configuration de modèle d'un agent n'était pas traitée avec la même
rigueur que son code ou ses accès.

## Solution

Chaque réaffectation de modèle est désormais suivie d'une vérification
explicite de la syntaxe de configuration et d'un test d'appel réel, pas
seulement d'une mise à jour de documentation.

## Règle qui en découle

Vérifier un modèle par un appel réel prouve que l'agent répond, pas qu'il
répond sur le modèle documenté. Le seul verdict fiable est la lecture de
la configuration réelle, jamais la mémoire de ce qu'on croit avoir changé.
