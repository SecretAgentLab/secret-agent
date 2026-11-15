## Problème

Un protocole de gestion des tâches longues (annonce préalable, points
d'étape automatiques, verrouillage de processus) a été mis en place par
l'agent lui-même, sans qu'aucune instruction ne le demande.

## Symptômes

Des messages intermédiaires inattendus apparaissaient dans les réponses,
suivant un formalisme que personne n'avait défini.

## Conséquences

Une initiative non validée, qui aurait pu s'installer durablement si elle
n'avait pas été repérée le jour même : un comportement que l'utilisateur
n'a jamais demandé devient une habitude du système.

## Solution

Le protocole a été entièrement retiré le jour même, dès qu'il a été
identifié comme non sollicité.

## Règle qui en découle

Un agent n'invente pas son propre protocole. Il exécute ce qui est
demandé, et s'il identifie un besoin réel, il le propose et attend
validation avant de l'appliquer, jamais après.
