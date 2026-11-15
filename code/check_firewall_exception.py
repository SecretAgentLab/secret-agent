#!/usr/bin/env python3
"""
Vérifie si un binaire a l'autorisation du pare-feu macOS pour recevoir des
connexions entrantes. Lecture seule : ne modifie rien, ne corrige rien.

Naît d'un vrai incident : un service web privé, accessible uniquement via
un réseau privé (Tailscale), ne répondait à aucune requête externe. La
connexion TCP s'établissait (confirmée par `nc`), mais aucune réponse HTTP
n'arrivait jamais. Cause réelle, trouvée après plusieurs fausses pistes
(interface réseau, cache applicatif) : le pare-feu macOS n'avait jamais
reçu d'autorisation explicite pour ce binaire Python précis, et bloquait
les connexions en silence, sans aucun message d'erreur côté serveur ni
côté client. Un `nc` réussissait (poignée de main TCP), mais `curl`
échouait (aucune donnée applicative ne passait).

Leçon : un pare-feu actif par défaut peut bloquer un service qui fonctionne
parfaitement en local (127.0.0.1) tout en semblant invisible depuis
l'extérieur, sans jamais produire de message d'erreur explicite. Vérifier
l'autorisation du pare-feu doit faire partie du réflexe de diagnostic
réseau, au même titre que vérifier le port et l'adresse.

Usage :
    python3 check_firewall_exception.py /chemin/vers/binaire
"""
import subprocess
import sys


def etat_global():
    """Le pare-feu applicatif macOS est-il actif ?"""
    out = subprocess.run(
        ["/usr/libexec/ApplicationFirewall/socketfilterfw", "--getglobalstate"],
        capture_output=True, text=True,
    ).stdout
    return "enabled" in out.lower()


def binaire_autorise(chemin):
    """Le binaire figure-t-il dans la liste des applications autorisées ?"""
    out = subprocess.run(
        ["/usr/libexec/ApplicationFirewall/socketfilterfw", "--listapps"],
        capture_output=True, text=True,
    ).stdout
    return chemin in out


def main():
    if len(sys.argv) != 2:
        print("Usage : check_firewall_exception.py /chemin/vers/binaire")
        return 1

    chemin = sys.argv[1]
    actif = etat_global()
    autorise = binaire_autorise(chemin)

    print(f"Pare-feu macOS actif : {'oui' if actif else 'non'}")
    print(f"Binaire dans la liste des autorisations : {'oui' if autorise else 'non'}")

    if actif and not autorise:
        print(
            "\nRISQUE : le pare-feu est actif et ce binaire n'a jamais été "
            "autorisé explicitement. Une connexion TCP peut sembler "
            "s'établir (poignée de main) sans que la moindre donnée "
            "applicative ne passe jamais. Corriger via :\n"
            f'  sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add "{chemin}"\n'
            f'  sudo /usr/libexec/ApplicationFirewall/socketfilterfw --unblockapp "{chemin}"'
        )
        return 1

    print("\nAucun risque détecté sur ce point précis.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
