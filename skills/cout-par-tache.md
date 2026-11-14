> EN summary: Recomputes the real token cost of any task or project from
> session logs and public pricing, never from memory or an estimate.

**Pourquoi ce skill existe** : piloter un système multi-agents sans connaître
son coût réel revient à piloter à l'aveugle. Ce skill calcule le coût depuis
les tokens effectivement consommés et les tarifs publics, jamais au doigt
mouillé.

# Coût par tâche et par projet

## Ce que fait ce skill

- Lit les tokens réellement consommés (entrée, sortie, cache) dans
  l'historique des sessions, par tâche ou par projet.
- Recalcule le coût depuis les tarifs publics du fournisseur du modèle
  utilisé, plutôt que de se fier à une estimation déjà affichée qui peut être
  périmée.
- Découpe une longue session en plusieurs tâches distinctes, pour ne pas
  attribuer le coût d'un projet entier à une seule demande.
- Classe chaque tâche par ordre de grandeur : échange simple, projet outillé,
  gros chantier, pour que le budget se lise d'un coup d'œil.

## Garde-fous

- Le chiffre produit est un **équivalent au tarif public**, pas
  nécessairement la facture réelle : le mode de facturation réel (abonnement
  ou usage) n'est pas toujours connu, et ça se dit.
- Un coût affiché à zéro dans les données est un tarif inconnu, jamais un
  coût nul : les deux ne doivent jamais être confondus.
- Une tâche récurrente mal placée sur le mauvais modèle peut coûter dix fois
  plus cher par exécution : ce skill le signale dès qu'il le détecte.

## Ce qu'il ne fait pas

- Ne devine jamais un tarif manquant : un prix absent reste signalé comme
  absent.
- Ne confond jamais une tâche que l'on croit avoir déléguée à un agent avec
  une tâche réellement exécutée par lui : il chiffre ce qui a eu lieu, pas ce
  qu'on pense avoir demandé.
