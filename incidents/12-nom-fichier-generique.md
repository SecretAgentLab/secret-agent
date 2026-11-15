## Problème

Les fichiers livrés par upload passaient par une copie temporaire et
affichaient ce nom générique au lieu du nom réel du fichier.

## Symptômes

Les fichiers reçus portaient un nom impossible à relier à leur contenu
une fois le canal de conversation quitté.

## Conséquences

Une perte de traçabilité silencieuse : le fichier existait bien et
fonctionnait, mais son nom ne disait plus rien de ce qu'il contenait.

## Solution

Le nom réel du fichier est désormais conservé bout en bout, de sa
création jusqu'à sa livraison, sans passer par un nom de fichier
temporaire générique au moment de l'envoi.

## Règle qui en découle

Un système qui fonctionne mais détruit la traçabilité de ce qu'il produit
a un vrai défaut, même sans erreur visible. L'observabilité fait partie
du fonctionnement, pas un supplément.
