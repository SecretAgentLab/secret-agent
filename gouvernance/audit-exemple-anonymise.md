> EN summary: Anonymized excerpt from a real internal security audit of the
> agent fleet, showing the scoring method and how an accepted risk is handled.

# Extrait anonymisé d'un audit de sécurité réel

Format réel utilisé pour auditer la flotte, chiffres et constats
représentatifs d'un audit effectivement mené, identifiants et chemins
retirés.

## Synthèse

| Constat | Gravité | Correctif |
|---|---|---|
| Permissions de fichiers de secrets trop ouvertes sur un profil | Moyenne | Restreindre à lecture propriétaire seul |
| Un service d'écoute réseau visible sur toutes les interfaces au lieu de la boucle locale | Moyenne | Restreindre à l'hôte local |
| Absence d'alerte sur l'échec d'une tâche planifiée | Haute | Activer une notification d'échec |
| Jeton d'authentification partagé entre plusieurs agents | Haute | Un jeton propre par agent, ou rotation planifiée |

## Note sur 100

| Catégorie | Max | Obtenu | Pourquoi |
|---|---|---|---|
| Secrets : permissions, isolation, sauvegarde | 20 | 16 | Permissions correctes sur la majorité des profils, un écart corrigé |
| Contrôle d'accès | 20 | 17 | Listes d'accès à jour, un compte à vérifier |
| Confidentialité des données | 20 | 18 | Pas de fuite détectée vers un dépôt public |
| Surface d'exposition | 15 | 12 | Un service exposé plus largement que nécessaire, corrigé |
| Résilience et récupération | 15 | 10 | Sauvegardes présentes mais pas testées en restauration |
| Hygiène et tenue | 10 | 8 | Journaux présents, une configuration obsolète restante |

## Décision documentée : un risque accepté

Un audit n'a pas vocation à imposer un choix, mais à l'éclairer. Exemple réel
d'arbitrage tranché par le propriétaire du système plutôt que corrigé par
défaut : le chiffrement intégral du disque a été désactivé volontairement,
parce que la machine reste en lieu sûr et que le chiffrement imposerait une
saisie manuelle à chaque redémarrage, ce qui romprait la disponibilité de la
flotte après une coupure de courant. Ce choix est documenté comme un risque
accepté, avec son raisonnement, et n'est plus reproposé comme une faille aux
audits suivants.

## Ce que cet extrait montre

Un audit qui note tout pareil, sans distinguer un risque choisi d'une vraie
vulnérabilité, perd sa crédibilité à la première relecture. La valeur n'est
pas dans le chiffre final, elle est dans la trace de chaque décision.
