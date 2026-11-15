## Problème

L'installation d'une bibliothèque pour un simple test a changé, en
silence, le choix du modèle de transcription vocale de toute la flotte.

## Symptômes

Un modèle documenté depuis des mois comme actif s'est révélé n'avoir
jamais réellement tourné, faute d'identifiant valide : le système
préférait silencieusement une ressource locale dès qu'elle était
détectée, sans avertissement ni journal.

## Conséquences

Un écart durable entre la documentation et la réalité technique, passé
inaperçu pendant des mois parce que rien ne signalait le changement de
comportement au moment où il s'est produit.

## Solution

Le choix du modèle est désormais fixé explicitement dans la
configuration, plus question de laisser un comportement implicite
décider à la place de l'opérateur.

## Règle qui en découle

Ce qui n'est pas explicitement fixé finira par changer tout seul, et en
silence. Avant d'installer une dépendance, même pour un test ponctuel,
mesurer ce qu'elle change pour le reste du système.
