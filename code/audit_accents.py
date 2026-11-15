#!/usr/bin/env python3
"""Vérifie les accents français dans un texte ou un fichier.

Usage :
    python3 audit_accents.py "texte à vérifier"
    python3 audit_accents.py --fichier chemin/vers/fichier.md
    python3 audit_accents.py --fichier a.md b.html c.py    # plusieurs fichiers
    echo "texte" | python3 audit_accents.py -

Sortie : liste des mots sans accent, avec la forme correcte.
Code de sortie 1 si au moins une faute est trouvée.

Les identifiants techniques (code inline, chemins, noms de variables) sont ignorés :
`model_snapshot` ou `reasoning_effort` ne sont pas des fautes.
"""
import re
import sys
from pathlib import Path

# forme sans accent -> forme correcte
FAUTES = {
    "cout": "coût", "couts": "coûts",
    "entree": "entrée", "entrees": "entrées",
    "modele": "modèle", "modeles": "modèles",
    "donnee": "donnée", "donnees": "données",
    "reel": "réel", "reelle": "réelle", "reels": "réels", "reelles": "réelles",
    "deja": "déjà",
    "apres": "après",
    "verifie": "vérifié", "verifier": "vérifier", "verifiee": "vérifiée",
    "securite": "sécurité",
    "francais": "français", "francaise": "française",
    "execution": "exécution", "execute": "exécuté", "executer": "exécuter",
    "necessaire": "nécessaire",
    "reponse": "réponse", "reponses": "réponses",
    "modifie": "modifié", "modifiee": "modifiée",
    "premiere": "première", "derniere": "dernière",
    "parametre": "paramètre", "parametres": "paramètres",
    "coherence": "cohérence",
    "numero": "numéro",
    "resume": "résumé", "resumes": "résumés",
    "theme": "thème", "themes": "thèmes",
    "methode": "méthode", "methodes": "méthodes",
    "systeme": "système", "systemes": "systèmes",
    "tache": "tâche", "taches": "tâches",
    "probleme": "problème", "problemes": "problèmes",
    "decision": "décision", "decisions": "décisions",
    "categorie": "catégorie", "categories": "catégories",
    "qualite": "qualité", "quantite": "quantité",
}

# ce qu'on retire avant analyse : code inline, blocs de code, chemins, URLs
CODE_INLINE = re.compile(r"`[^`]*`")
BLOCS = re.compile(r"```.*?```", re.S)
CHEMINS = re.compile(r"(?:/[\w./-]{2,}|https?://\S+|[a-z0-9_-]+\.[a-z]{2,4}\b)", re.I)
IDENTIFIANTS = re.compile(r"\b[a-z]+(?:_[a-z0-9]+)+\b", re.I)  # snake_case


def analyser(txt):
    """Retourne {mot_fautif: (correct, nb_occurrences)}."""
    propre = BLOCS.sub(" ", txt)
    propre = CODE_INLINE.sub(" ", propre)
    propre = CHEMINS.sub(" ", propre)
    propre = IDENTIFIANTS.sub(" ", propre)

    trouves = {}
    for fautif, correct in FAUTES.items():
        n = len(re.findall(rf"\b{re.escape(fautif)}\b", propre, re.I))
        if n:
            trouves[fautif] = (correct, n)
    return trouves


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 0

    if args[0] == "--fichier":
        cibles = args[1:]
        total = 0
        for c in cibles:
            p = Path(c)
            if not p.exists():
                print(f"ABSENT : {c}")
                continue
            txt = p.read_text(encoding="utf-8", errors="ignore")
            r = analyser(txt)
            n = sum(v[1] for v in r.values())
            total += n
            if n == 0:
                print(f"{p.name:<42} accents OK")
            else:
                print(f"{p.name:<42} {n} faute(s)")
                for fautif, (correct, cnt) in sorted(r.items(), key=lambda x: -x[1][1]):
                    print(f"      « {fautif} » -> « {correct} »  x{cnt}")
        print()
        print(f"TOTAL : {total} mot(s) sans accent")
        return 1 if total else 0

    txt = sys.stdin.read() if args[0] == "-" else " ".join(args)
    r = analyser(txt)
    if not r:
        print("Accents OK : aucune faute detectee.")
        return 0
    n = sum(v[1] for v in r.values())
    print(f"{n} mot(s) sans accent :")
    for fautif, (correct, cnt) in sorted(r.items(), key=lambda x: -x[1][1]):
        print(f"  « {fautif} » -> « {correct} »  x{cnt}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
