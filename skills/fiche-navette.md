> EN summary: Validates device serial numbers and IMEI by checksum (Luhn),
> never from model memory, before any fleet management import.

**Pourquoi ce skill existe** : un numéro de série ou un IMEI mal lu, une fois
collé dans un document d'import, devient indétectable et l'erreur touche un
vrai appareil physique. Ce skill protège cette donnée par du calcul
vérifiable, pas par la mémoire d'un modèle de langage.

# Fiche navette, gestion de parc mobile

Support informatique : suivi du renouvellement d'appareils mobiles pour un
parc de plusieurs centaines de terminaux, répartis sur plusieurs opérateurs.

## Ce que fait ce skill

- Lit un fichier de suivi (tableur) et détecte ses colonnes par leur nom,
  jamais par leur position : une colonne renommée ou déplacée ne doit pas
  faire échouer silencieusement la lecture.
- Génère les documents d'attribution à partir des valeurs réelles du fichier,
  sans jamais recopier un numéro de mémoire.
- Valide chaque IMEI lu sur un document scanné par sa **clé de Luhn**, un
  calcul de contrôle standard : une lecture fautive la rate dans l'immense
  majorité des cas.
- Détecte les collisions : un même numéro de série attribué à deux personnes
  différentes dans le fichier.

## Garde-fous

- Aucun numéro de série ou IMEI n'est jamais inventé ou complété de mémoire :
  s'il n'est pas lisible, la ligne est signalée, pas générée.
- Un fichier correctif reçoit toujours un nouveau fichier daté, jamais une
  réécriture silencieuse de l'ancien : un double import avec deux versions
  différentes d'un même appareil est le risque le plus grave de ce processus.
- Toute anomalie de données (ligne incohérente, doublon, commentaire qui cite
  une autre personne que celle de la ligne) est signalée, jamais corrigée de
  sa propre initiative : le fichier source fait foi.

## Ce qu'il ne fait pas

- Ne décide jamais qui reçoit quel appareil : ce sont des décisions humaines,
  le skill ne fait qu'exécuter ce que le fichier dit.
- Ne contacte jamais un tiers automatiquement : toute communication externe
  passe par une validation humaine avant envoi.
