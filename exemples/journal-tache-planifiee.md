> EN summary: Anonymized excerpt from a real scheduled-task execution log,
> showing the trace format every run leaves behind.

# Journal d'une tâche planifiée, extrait réel anonymisé

```
[2026-11-01 07:00:03] tâche=veille statut=démarrée
[2026-11-01 07:00:04] étape=collecte sources=12 trouvées=47
[2026-11-01 07:00:19] étape=filtrage retenues=8 écartées=39
[2026-11-01 07:00:22] étape=rédaction modèle=flash tokens_entrée=14200 tokens_sortie=1100
[2026-11-01 07:00:24] étape=livraison canal=veille statut=livré
[2026-11-01 07:00:24] tâche=veille statut=terminée durée=21s
```

## Ce que cet exemple montre

Chaque tâche planifiée laisse une trace lisible : ce qui est entré, les
étapes traversées, la décision prise à chaque étape, et la sortie. C'est
exactement ce qui manquait lors de l'incident du 1er juin 2026 documenté dans
le README principal : les tâches tournaient, mais aucune n'était configurée
pour prévenir en cas d'échec. Depuis, un journal comme celui-ci se relit
automatiquement, et une alerte se déclenche si le statut final n'est pas
« terminée ».
