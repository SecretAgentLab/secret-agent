[read in English further below]

# Règles à copier, pour sécuriser votre propre flotte d'agents

Dix règles réelles, chacune née d'un incident vécu, pas d'une bonne
pratique générique recopiée d'un article. Certaines sont formulées en
prompt prêt à coller dans la configuration ou le system prompt de votre
propre agent.

## Accès et identifiants

1. **Un identifiant par agent, jamais partagé.** Si neuf agents partagent
   la même session d'authentification, la perte d'une seule session en
   fait tomber neuf d'un coup. Isoler chaque agent coûte un peu plus de
   mise en place, rien de plus.

   > Prompt : *« Avant toute action qui utilise une authentification,
   > vérifie que cette session d'authentification est propre à ton
   > profil, pas partagée avec un autre agent. Si tu ne peux pas le
   > vérifier, signale-le au lieu de continuer. »*

2. **Jamais de lecture d'un identifiant sensible, même redemandé plus
   tard.** Un agent qui refuse une fois doit refuser systématiquement, pas
   seulement à la première demande.

## Actions irréversibles

3. **Jamais d'envoi de masse**, même si un fichier contient une liste
   d'adresses qui s'y prêterait.
4. **Jamais de suppression sans confirmation explicite**, quelle que soit
   la certitude apparente de l'agent sur le bon fichier à supprimer.

## Comportement et initiative

5. **Un agent ne décide jamais seul d'un nouveau protocole non demandé.**
   Il propose, l'humain valide, avant toute application.

   > Prompt : *« Si tu identifies un besoin non explicitement demandé
   > (un nouveau protocole, une automatisation, une règle), propose-le et
   > attends validation avant de l'appliquer. Ne l'exécute jamais en
   > anticipant un accord. »*

6. **Toute tâche de plus de quelques secondes part en tâche de fond**,
   avec un accusé de réception immédiat. Un agent qui reste silencieux en
   plein travail est indiscernable d'un agent bloqué.

## Surveillance et alerte

7. **Une tâche planifiée qui réussit doit aussi prévoir le jour où elle
   échouera.** Une alerte sur échec n'est pas optionnelle, elle fait
   partie de la tâche elle-même.
8. **Vérifier l'autorisation réseau (pare-feu) avant de chercher plus
   loin**, en cas de service injoignable qui fonctionne pourtant en local.
   Une connexion qui s'établit sans jamais transporter de données est un
   symptôme classique de pare-feu, pas de code cassé.

## Dépendances et effets de bord

9. **Avant d'installer une dépendance, même pour un test ponctuel, mesurer
   ce qu'elle change pour le reste du système.** Une bibliothèque installée
   pour un essai isolé peut changer, en silence, le comportement de toute
   une flotte si elle devient une préférence par défaut détectée
   automatiquement.

## Délégation entre agents

10. **Toute capacité d'un agent à en solliciter un autre doit être
    journalisée ET annoncée à l'humain au moment où elle a lieu**, jamais
    seulement a posteriori dans un fichier de log.

    > Prompt : *« Si tu sollicites un autre agent pour une question
    > précise, mentionne-le explicitement dans ta réponse à l'humain : qui,
    > pourquoi, ce qu'il a répondu. Le journal ne suffit pas, l'humain doit
    > le voir passer. »*

---

# Rules to copy, for securing your own agent fleet

Ten real rules, each born from a lived incident, not a generic best
practice copied from an article. Some are written as ready-to-paste
prompts for your own agent's configuration or system prompt.

## Access and credentials

1. **One credential per agent, never shared.** If nine agents share the
   same authentication session, losing that one session takes down all
   nine at once. Isolating each agent costs a bit more setup, nothing more.
2. **Never read a sensitive credential, even if asked again later.** An
   agent that refuses once should refuse every time, not just on the
   first request.

## Irreversible actions

3. **Never a mass send**, even if a file happens to contain a list of
   addresses that would make it easy.
4. **Never a deletion without explicit confirmation**, regardless of how
   certain the agent seems about the right file to delete.

## Behavior and initiative

5. **An agent never decides on its own to add a new, unrequested
   protocol.** It proposes, the human validates, before anything runs.
6. **Any task longer than a few seconds goes to the background**, with an
   immediate acknowledgement. An agent that goes silent mid-task is
   indistinguishable from a stuck one.

## Monitoring and alerting

7. **A scheduled task that succeeds today must also plan for the day it
   fails.** A failure alert is not optional, it is part of the task
   itself.
8. **Check the network firewall authorization before digging further**
   when a service is unreachable yet works fine locally. A connection
   that establishes but never carries data is a classic firewall
   symptom, not broken code.

## Dependencies and side effects

9. **Before installing a dependency, even for a one-off test, measure
   what it changes for the rest of the system.** A library installed for
   an isolated trial can silently change the behavior of an entire fleet
   if it becomes an auto-detected default.

## Inter-agent delegation

10. **Any capability for one agent to ask another must be logged AND
    announced to the human at the moment it happens**, never only after
    the fact in a log file.
