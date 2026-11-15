#!/usr/bin/env python3
"""
Outil d'appel inter-agents, réservé à un agent relais central (ici Trinity).

Usage :
    python3 appel_agent.py <profil> "<question>" "<raison>"

<profil>   : le profil agent sollicité (doit figurer dans AUTORISES)
<question> : la question précise posée, sans état partagé
<raison>   : pourquoi cet agent est sollicité (pour le journal)

Règle de gouvernance derrière ce script : un agent central peut solliciter
un autre agent pour une question précise, jamais pour lui déléguer une
tâche entière. Chaque appel est sans état (aucune mémoire ni session
partagée entre les deux agents) et systématiquement journalisé : qui a
appelé qui, pourquoi, avec quel résultat. Si l'agent sollicité estime ne
pas être le bon interlocuteur, il le dit et recommande un autre agent :
l'agent appelant ne relance jamais cet autre agent de sa propre initiative,
il revient d'abord vers l'humain qui valide le prochain interlocuteur.

Adapté pour publication : le chemin du journal et la liste des profils
autorisés sont à configurer pour votre propre installation.
"""
import subprocess
import sys
import json
from datetime import datetime
from pathlib import Path

# A adapter : chemin du journal d'appels sur votre propre installation.
JOURNAL = Path("./journal/appels-inter-agents.md")

# A adapter : liste des profils que l'agent central est autorise a solliciter.
AUTORISES = {"neo", "morpheus", "specialiste-a", "specialiste-b", "generaliste"}


def appeler(profil, question, raison, timeout=120):
    if profil not in AUTORISES:
        raise ValueError(f"Profil non autorisé pour un appel inter-agents : {profil}")

    debut = datetime.now()
    try:
        proc = subprocess.run(
            ["hermes", "-p", profil, "chat", "-q", question],
            capture_output=True, text=True, timeout=timeout,
        )
        duree = (datetime.now() - debut).total_seconds()
        reponse = proc.stdout.strip() or proc.stderr.strip()
        statut = "ok" if proc.returncode == 0 else f"erreur (code {proc.returncode})"
    except subprocess.TimeoutExpired:
        duree = timeout
        reponse = ""
        statut = f"timeout ({timeout}s)"

    journaliser(profil, question, raison, statut, reponse, duree)
    return {"profil": profil, "statut": statut, "reponse": reponse, "duree_s": duree}


def journaliser(profil, question, raison, statut, reponse, duree):
    JOURNAL.parent.mkdir(parents=True, exist_ok=True)
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    extrait = reponse[:400].replace("\n", " ")
    ligne = (
        f"\n### {horodatage}, agent central vers {profil}\n"
        f"- **Raison** : {raison}\n"
        f"- **Question** : {question}\n"
        f"- **Statut** : {statut} ({duree:.1f}s)\n"
        f"- **Réponse (extrait)** : {extrait}\n"
    )
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(ligne)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage : appel_agent.py <profil> <question> <raison>")
        sys.exit(1)
    _, profil, question, raison = sys.argv
    resultat = appeler(profil, question, raison)
    print(json.dumps(resultat, ensure_ascii=False, indent=2))
