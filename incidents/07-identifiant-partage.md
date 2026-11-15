## Problème

Plusieurs agents d'une même flotte partageaient le même identifiant
d'authentification.

## Symptômes

Aucun signal d'alerte direct : le système fonctionnait normalement. Le
risque était structurel, pas visible dans le comportement quotidien.

## Conséquences

La perte, la révocation ou l'expiration d'une seule session
d'authentification partagée aurait fait tomber tous les agents qui en
dépendaient en même temps, sans possibilité de couper l'accès d'un seul
agent sans couper les autres. Une compromission d'un seul agent aurait
aussi donné accès aux droits de tous les autres d'un coup.

## Solution

Chaque agent a reçu son propre identifiant d'authentification isolé,
vérifié par un appel réel après la bascule. L'ancien identifiant partagé
a été supprimé une fois la migration confirmée fonctionnelle.

## Règle qui en découle

Un identifiant par agent, jamais partagé. Si plusieurs agents partagent
la même session d'authentification, perdre cette session en fait tomber
plusieurs d'un coup. Isoler chaque agent coûte un peu plus de mise en
place, rien de plus.
