#!/usr/bin/env python3
"""
Soteros — contrôle du rendu réel.

Ce script ne se contente pas de photographier les pages. Il ouvre le menu
et mesure sa boîte, parce qu'un volet de navigation écrasé reste invisible
tant qu'on ne le déplie pas, et c'est exactement le genre de défaut qui
arrive jusque sur le téléphone du client.

Usage : python3 tools/captures.py
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "tools" / "captures"
SORTIE.mkdir(parents=True, exist_ok=True)

PAGES = ["index", "expertise", "projets", "agence", "engagement", "contact"]
POSTES = [("telephone", 390, 844), ("bureau", 1440, 900)]
LARGEURS_MENU = [390, 430, 768, 1440]

echecs = []


def verifier(condition: bool, message: str) -> None:
    print(("OK  " if condition else "NON ") + message)
    if not condition:
        echecs.append(message)


with sync_playwright() as pw:
    nav = pw.chromium.launch()

    # ---- Captures et contrôles de structure -------------------------------
    for nom, larg, haut in POSTES:
        page = nav.new_page(viewport={"width": larg, "height": haut},
                            device_scale_factor=2)
        erreurs = []
        page.on("pageerror", lambda e: erreurs.append(str(e)))
        page.on("console", lambda m: erreurs.append(m.text) if m.type == "error" else None)

        for cible in PAGES:
            page.goto((RACINE / f"{cible}.html").as_uri())
            page.wait_for_timeout(1900)          # laisse l'instrument s'assembler

            # Un seul h1 par page, sinon la hiérarchie est fausse pour Google.
            verifier(page.locator("h1").count() == 1,
                     f"{cible} — un seul h1")

            # La navigation doit porter les cinq entrées sur chaque page.
            verifier(page.locator("[data-nav] a").count() == 6,
                     f"{cible} — six entrées de navigation")

            # Aucun lien mort hors emplacements marqués.
            morts = page.eval_on_selector_all(
                "a[href='#']",
                "els => els.filter(e => !e.hasAttribute('data-coordonnee')"
                " && !e.hasAttribute('data-reseau')).length")
            verifier(morts == 0, f"{cible} — pas de lien vide non marqué")

            # Balayage complet pour déclencher ce qui doit l'être.
            page.evaluate("""() => new Promise(r => {
                let y = 0;
                const pas = () => {
                    window.scrollTo({ top: y, behavior: 'auto' });
                    y += window.innerHeight;
                    if (y < document.body.scrollHeight + window.innerHeight) {
                        requestAnimationFrame(pas);
                    } else { window.scrollTo({ top: 0, behavior: 'auto' }); setTimeout(r, 250); }
                };
                pas();
            })""")
            page.screenshot(path=str(SORTIE / f"{nom}-{cible}.png"), full_page=True)

        # L'instrument a-t-il vraiment dessiné quelque chose ?
        page.goto((RACINE / "index.html").as_uri())
        page.wait_for_timeout(1900)
        encre = page.evaluate("""() => {
            const c = document.querySelector('[data-instrument] canvas');
            if (!c) return -1;
            const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
            let n = 0;
            for (let i = 3; i < d.length; i += 40) { if (d[i] > 8) n++; }
            return n;
        }""")
        verifier(encre > 200, f"{nom} — l'instrument a tracé ({encre} points relevés)")

        verifier(not erreurs, f"{nom} — aucune erreur JavaScript {erreurs[:2]}")
        page.close()

    # ---- Le mot d'accueil reste bien de la typographie nue ----------------
    page = nav.new_page(viewport={"width": 1440, "height": 900})
    page.goto((RACINE / "index.html").as_uri())
    page.wait_for_timeout(1200)

    mot = page.locator(".bienvenue")
    verifier(mot.count() == 1, "le mot d'accueil est présent")

    # Ni relief, ni bascule, ni reste des versions précédentes.
    verifier(mot.evaluate("el => getComputedStyle(el).textShadow") == "none",
             "aucun relief en ombres empilées")
    verifier(page.locator("[data-scene], [data-relief]").count() == 0,
             "aucun reste de la scène interactive")
    verifier(page.locator(".instrument__nom").count() == 0,
             "le mot Soteros a bien quitté l'instrument")

    # Le survol ne doit strictement rien déclencher.
    boite = mot.bounding_box()
    avant = mot.evaluate("el => getComputedStyle(el).transform")
    page.mouse.move(boite["x"] + boite["width"] * .5,
                    boite["y"] + boite["height"] * .5, steps=8)
    page.wait_for_timeout(250)
    verifier(mot.evaluate("el => getComputedStyle(el).transform") == avant,
             "le survol ne déclenche rien")
    page.close()

    # ---- Le menu, déplié, à quatre largeurs -------------------------------
    for larg in LARGEURS_MENU:
        page = nav.new_page(viewport={"width": larg, "height": 844})
        page.goto((RACINE / "index.html").as_uri())
        page.wait_for_timeout(700)

        visible = page.locator("[data-bascule]").is_visible()
        if visible:
            page.locator("[data-bascule]").click()
            page.wait_for_timeout(500)
            boite = page.locator("[data-nav]").bounding_box()
            couvre = boite and boite["width"] >= larg - 1 and boite["height"] >= 800
            verifier(bool(couvre),
                     f"{larg}px — le volet couvre l'écran "
                     f"({int(boite['width'])}x{int(boite['height'])})" if boite
                     else f"{larg}px — volet introuvable")
            # Le premier lien du menu doit être réellement cliquable.
            verifier(page.locator("[data-nav] a").first.is_visible(),
                     f"{larg}px — les liens du menu sont visibles")
            page.screenshot(path=str(SORTIE / f"menu-{larg}.png"))
        else:
            # Au-delà du seuil, la navigation est en ligne dans l'en-tête.
            verifier(page.locator("[data-nav] a").first.is_visible(),
                     f"{larg}px — navigation en ligne visible")
        page.close()

    nav.close()

print()
if echecs:
    print(f"{len(echecs)} contrôle(s) en échec")
    for e in echecs:
        print("  -", e)
    sys.exit(1)
print("Tous les contrôles passent.")
