## Problème

Huit profils d'agents sur dix avaient hérité, copiée telle quelle, la
mémoire d'un agent de direction, au moment de leur création.

## Symptômes

Les agents concernés raisonnaient parfois dans le mauvais rôle : des
réflexes et des priorités qui appartenaient à l'agent de direction
remontaient dans des contextes où ils n'avaient pas de sens.

## Conséquences

Un biais de raisonnement diffus, difficile à repérer au cas par cas parce
qu'il ne provoquait pas d'erreur immédiate, seulement un angle d'approche
légèrement décalé par rapport au rôle réel de chaque agent.

## Solution

Chaque profil a reçu sa propre mémoire, écrite depuis son périmètre réel,
plutôt qu'héritée par copie d'un autre agent.

## Règle qui en découle

Cloner un agent pour en créer un nouveau ne doit jamais cloner sa
mémoire. L'identité et les réflexes d'un agent doivent être écrits pour
son rôle réel, jamais hérités par défaut d'un autre.
