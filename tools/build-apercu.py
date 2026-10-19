#!/usr/bin/env python3
"""
Soteros — prépare le dossier d'aperçu publiable.

La page d'accueil publiée est enveloppée automatiquement dans un squelette
HTML. Elle doit donc arriver sans le sien, alors que les autres pages, qui
sont servies telles quelles, gardent le leur. Ce script fabrique cette
variante sans toucher au site réel.

Usage : python3 tools/build-apercu.py
"""
import re
import shutil
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
APERCU = RACINE / "apercu"

AUTRES = ["expertise.html", "projets.html", "agence.html",
          "engagement.html", "contact.html", "mentions-legales.html"]


def main() -> None:
    if APERCU.exists():
        shutil.rmtree(APERCU)
    APERCU.mkdir()

    for nom in ["style.css", "script.js"] + AUTRES:
        shutil.copy(RACINE / nom, APERCU / nom)

    shutil.copytree(RACINE / "img", APERCU / "img")

    brut = (RACINE / "index.html").read_text(encoding="utf-8")

    # On récupère le lien des polices tel qu'il est écrit dans la page.
    polices = re.search(r'<link href="https://fonts\.googleapis[^>]+>', brut).group(0)

    # Le corps seul, sans doctype, html, head ni body.
    corps = brut.split("<body>", 1)[1].rsplit("</body>", 1)[0]

    (APERCU / "index.html").write_text(
        "<title>Soteros</title>\n"
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        f"{polices}\n"
        '<link rel="stylesheet" href="style.css">\n'
        f"{corps}",
        encoding="utf-8",
    )

    poids = sum(f.stat().st_size for f in APERCU.iterdir())
    print(f"aperçu prêt — {len(list(APERCU.iterdir()))} fichiers, {poids/1024:.0f} Ko")


if __name__ == "__main__":
    main()
