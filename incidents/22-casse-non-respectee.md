## Problème

Une convention de casse établie pour une catégorie de fichiers
personnels n'a pas été respectée pendant trois jours consécutifs.

## Symptômes

Les fichiers créés sur cette période ne correspondaient pas au format
attendu, obligeant à les renommer après coup une fois l'écart repéré.

## Conséquences

Un correctif rétroactif sur plusieurs fichiers, évitable si la
convention avait été vérifiée au moment de la création plutôt
qu'après coup.

## Solution

La convention de casse a été ajoutée aux vérifications automatiques
avant la création de ce type de fichier, plutôt que de dépendre de la
mémoire de l'agent à chaque usage.

## Règle qui en découle

Une convention répétée dans le temps doit être vérifiée
automatiquement, pas simplement rappelée une fois et supposée retenue
indéfiniment.
