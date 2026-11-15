## Problème

Une correction antérieure avait fait disparaître l'horodatage d'une
convention de nommage de fichiers personnels, cassant une habitude
établie de longue date.

## Symptômes

Les nouveaux fichiers ne portaient plus l'information d'heure que les
précédents portaient tous, sans qu'aucune décision explicite n'ait
demandé ce changement.

## Conséquences

Une rupture de cohérence dans l'historique des fichiers, remarquée
seulement après coup, parce que la correction d'origine visait autre
chose et avait emporté cet élément sans le vouloir.

## Solution

L'horodatage a été réintégré dans la convention de nommage, et la
correction d'origine revue pour isoler précisément ce qu'elle devait
changer.

## Règle qui en découle

Corriger un défaut précis doit être vérifié pour ne pas emporter autre
chose au passage. Une convention établie ne doit jamais changer comme
effet secondaire d'une correction qui visait un point différent.
