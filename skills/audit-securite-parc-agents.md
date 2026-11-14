> EN summary: Applies a phased, read-only-first security audit discipline to
> the agent fleet itself: reconnaissance, then fixes, never both at once.

**Pourquoi ce skill existe** : auditer sa propre flotte d'agents avec la même
rigueur qu'on attendrait d'un audit externe, en séparant strictement le
constat de la correction, pour qu'aucun correctif ne soit appliqué sans un
accord explicite et informé.

# Audit de sécurité du parc d'agents

## Ce que fait ce skill

- **Phase 1, lecture seule** : inventaire des identifiants, des permissions de
  fichiers, des services réseau en écoute, des sauvegardes. Aucune écriture,
  aucune modification, à aucun moment de cette phase.
- **Phase 2, vérification** : ce qui consomme réellement chaque valeur de
  configuration, ce que font effectivement les tâches planifiées, qui écoute
  vraiment sur un port ouvert.
- **Phase 3, correctifs** : classés par gravité, annoncés un par un, jamais
  appliqués sans accord explicite.
- Une note finale sur 100, rendue en tableau catégorie par catégorie avec sa
  justification, jamais en chiffre nu.

## Garde-fous

- Un choix assumé par son propriétaire (un risque accepté en connaissance de
  cause) ne retire aucun point à la note et ne se repropose jamais à l'audit
  suivant.
- Un constat qui ressemble à une faille est d'abord vérifié dans le code
  réel : une valeur de configuration qui n'est lue par rien n'est pas une
  vulnérabilité, c'est un piège d'audit. Le dire comme tel évite de
  décrédibiliser le reste du rapport.
- Aucun chiffre n'est repris d'un rapport antérieur : tout est recompté à
  chaque passe.

## Ce qu'il ne fait pas

- N'applique jamais un correctif pendant la reconnaissance, même trivial.
- Ne présente jamais une protection partielle (une permission de fichier, un
  mot de passe) comme une garantie absolue : les limites de chaque mesure
  sont dites explicitement dans le rapport.
