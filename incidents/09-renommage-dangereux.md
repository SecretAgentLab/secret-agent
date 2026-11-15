## Problème

Une commande de renommage a failli déplacer le dossier entier d'un agent,
avec ses tâches planifiées, ses sessions et ses extensions.

## Symptômes

Aucun, jusqu'au moment où la commande s'est arrêtée d'elle-même sur une
validation de caractères dans le nouveau nom, par accident de
conception plutôt que par une protection pensée pour ce cas.

## Conséquences

Un déplacement de dossier entier aurait cassé les références internes de
l'agent (chemins de tâches, de sessions), sans garantie de récupération
simple.

## Solution

La protection accidentelle a été reconnue comme un vrai garde-fou
nécessaire, et une vérification explicite a été ajoutée avant toute
opération de renommage touchant un dossier d'agent.

## Règle qui en découle

Une action destructrice évitée par accident doit être transformée en
règle écrite, pas célébrée comme un coup de chance. Le hasard n'est pas
une stratégie de sécurité.
