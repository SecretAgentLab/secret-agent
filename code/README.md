[also read in English further below]

# Code réel

Trois scripts réels, nettoyés de toute donnée personnelle ou employeur,
mais la logique est inchangée. Chacun existe parce qu'un incident précis
l'a rendu nécessaire.

## `audit_accents.py`

**Pourquoi il existe :** une discipline de qualité appliquée systématiquement
avant toute publication, pas une vérification ponctuelle. Vérifie l'absence
de fautes d'accent dans un texte ou un fichier, en ignorant le code inline,
les chemins et les identifiants techniques pour éviter les faux positifs.

```
python3 audit_accents.py "le cout du modele"
# 2 mot(s) sans accent :
#   « cout » -> « coût »  x1
#   « modele » -> « modèle »  x1
```

## `appel_agent.py`

**Pourquoi il existe :** une capacité d'appel inter-agents, réservée à un
agent relais central, avec des garde-fous explicites. Un agent central peut
solliciter un autre agent pour une question précise, jamais pour lui
déléguer une tâche entière. Chaque appel est sans état et systématiquement
journalisé. Si l'agent sollicité n'est pas le bon interlocuteur, il le dit
et recommande un autre agent, sans jamais enchaîner de lui-même.

## `check_firewall_exception.py`

**L'incident qui l'a produit :** un service web privé, accessible
uniquement par un réseau privé (Tailscale), ne répondait à aucune requête
externe. La connexion TCP s'établissait, confirmée par `nc`, mais aucune
réponse HTTP n'arrivait jamais. Cause réelle, trouvée après plusieurs
fausses pistes (interface réseau, cache applicatif) : le pare-feu macOS
n'avait jamais reçu d'autorisation explicite pour ce binaire précis, et
bloquait en silence, sans aucun message d'erreur ni côté serveur ni côté
client. Ce script vérifie ce point précis avant qu'il ne redevienne un
incident.

---

# Real code

Three real scripts, cleaned of any personal or employer data, logic
unchanged. Each one exists because a specific incident made it necessary.

## `audit_accents.py`

A quality discipline applied systematically before any publication, not a
one-off check. Checks for missing accents in French text or files, while
ignoring inline code, paths, and technical identifiers to avoid false
positives.

## `appel_agent.py`

An inter-agent call capability, reserved for one central relay agent, with
explicit guardrails. A central agent can ask another agent a precise
question, never hand it a full task. Every call is stateless and always
logged. If the agent asked is the wrong fit, it says so and recommends
another agent, never chaining on its own.

## `check_firewall_exception.py`

**The incident that produced it:** a private web service, reachable only
over a private network (Tailscale), answered no external request at all.
The TCP connection established fine, confirmed with `nc`, but no HTTP
response ever came back. Real cause, found after several false leads
(network interface, application cache): the macOS firewall had never been
given explicit permission for that exact binary, and silently blocked it,
with no error message on either side. This script checks that exact point
before it becomes an incident again.
