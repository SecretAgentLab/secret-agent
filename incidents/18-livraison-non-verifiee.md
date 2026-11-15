## Problème

Des fichiers réellement créés (plusieurs scripts et une synthèse)
n'étaient confirmés qu'en texte, sans jamais être réellement joints à la
conversation.

## Symptômes

Le message annonçait les fichiers comme livrés, mais rien n'apparaissait
réellement à télécharger tant que l'utilisateur ne demandait pas
explicitement leur envoi.

## Conséquences

Un écart entre ce qui est annoncé fait et ce qui est réellement
disponible : le genre d'écart qui mine la confiance accordée aux
annonces d'un agent, même quand le travail de fond est réellement fait.

## Solution

La livraison d'un fichier annoncé comme créé est désormais vérifiée
avant de confirmer sa livraison, pas supposée à partir du seul fait
qu'il a été généré.

## Règle qui en découle

Annoncer qu'une action est faite n'est pas la même chose que l'avoir
vérifiée. Un agent ne doit jamais confirmer un résultat qu'il n'a pas
réellement constaté.
