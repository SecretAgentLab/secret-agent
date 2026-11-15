## Problème

Deux messages postés en chaîne sont arrivés dans le désordre, et l'un
en double.

## Symptômes

Un envoi en échec a été relancé en bloc, sans vérifier individuellement
lequel des deux messages était réellement passé.

## Conséquences

Un doublon visible pour le destinataire, et un ordre de lecture incohérent
sur un envoi qui se voulait séquentiel.

## Solution

Après tout envoi en chaîne, vérifier individuellement ce qui est
réellement arrivé avant de relancer quoi que ce soit, plutôt que de
relancer le groupe entier par précaution.

## Règle qui en découle

Ne jamais relancer à l'aveugle un groupe d'actions à cause de l'échec
d'une seule. Vérifier l'état réel avant de corriger.
