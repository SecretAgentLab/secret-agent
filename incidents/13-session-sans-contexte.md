## Problème

Une nouvelle session de conversation a nié avoir parlé d'un sujet évoqué
dix minutes plus tôt dans le même canal.

## Symptômes

Une réponse incohérente avec l'historique réel de la conversation, parce
que l'agent n'avait pas vérifié ce qui s'était déjà dit avant de
répondre.

## Conséquences

Une perte de confiance ponctuelle : un agent qui semble ne pas se
souvenir de ce qui vient d'être dit, dans le même canal, est perçu comme
moins fiable qu'un agent qui ne sait simplement pas.

## Solution

La vérification de l'historique récent du canal est devenue un réflexe
systématique au démarrage d'une nouvelle session, avant toute réponse.

## Règle qui en découle

Une nouvelle session de conversation n'est pas une page blanche pour le
canal lui-même. Ce qui s'y est dit juste avant reste pertinent, même si
la session technique a changé.
