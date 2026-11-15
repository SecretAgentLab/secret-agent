## Problème

Un service web privé, accessible uniquement via un réseau privé
(Tailscale), ne répondait à aucune requête externe alors qu'il
fonctionnait parfaitement en local.

## Symptômes

La connexion TCP s'établissait normalement (confirmé par un test de
poignée de main réseau), mais aucune réponse applicative n'arrivait
jamais, sans le moindre message d'erreur ni côté serveur ni côté client.

## Conséquences

Plusieurs fausses pistes explorées avant la vraie cause (interface
réseau, cache applicatif), simplement parce que le symptôme ne
ressemblait à aucune panne réseau habituelle.

## Solution

Le pare-feu applicatif du système n'avait jamais reçu d'autorisation
explicite pour ce binaire précis, et bloquait les connexions en
silence. L'ajout de l'exception a immédiatement résolu le problème.
Script de vérification publié : `code/check_firewall_exception.py`.

## Règle qui en découle

Un pare-feu actif par défaut peut bloquer un service qui fonctionne
parfaitement en local tout en semblant invisible depuis l'extérieur, sans
jamais produire de message d'erreur explicite. Vérifier l'autorisation du
pare-feu doit faire partie du réflexe de diagnostic réseau, au même titre
que vérifier le port et l'adresse.
