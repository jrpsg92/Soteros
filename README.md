# Soteros

Site de l'agence. HTML, CSS et JavaScript écrits à la main, aucune
dépendance, aucun constructeur. Publié par GitHub Pages.

## Les pages

| Fichier | Rôle |
|---|---|
| `index.html` | Accueil, avec l'instrument en rotation |
| `expertise.html` | Sites sur mesure, présence Google, suivi |
| `offres.html` | Les deux formules, prix et questions fréquentes |
| `projets.html` | Nails by Deb et Raju Sinniah |
| `agence.html` | Qui est derrière Soteros |
| `engagement.html` | Éco-conception |
| `contact.html` | Formulaire de contact et coordonnées |
| `mentions-legales.html` | Obligatoire, **à compléter** |

## Ne pas modifier les pages à la main

L'en-tête, la navigation et le pied sont écrits une seule fois dans
`tools/build-pages.py`, puis posés dans chaque page. Modifier un fichier
`.html` directement fonctionne jusqu'à la prochaine génération, qui
l'écrase.

Le bon geste, c'est de modifier `tools/build-pages.py` puis de lancer :

```bash
python3 tools/build-pages.py
```

Ça réécrit les huit pages, le `sitemap.xml` et le `robots.txt`.

## Ajouter une page

Dans `tools/build-pages.py`, ajouter l'entrée dans `LIENS` pour la
navigation, écrire le contenu dans une constante, puis l'ajouter à `PAGES`
avec son titre et sa description. Relancer le script.

## Changer les couleurs

Tout est en haut de `style.css`, dans le bloc `:root`. Chaque valeur porte
en commentaire son rapport de contraste sur le fond de page. La norme
WCAG AA demande 4,5 pour du texte. Ne pas descendre en dessous.

Attention, le cyan clair du logo tombe à 1,8 sur blanc. Il ne peut jamais
porter de texte, d'où les bleus assombris utilisés ici.

## Le logo

`img/marque-*.png` est le pictogramme seul, décliné en cinq tailles et
redégradé dans les bleus profonds pour rester lisible sur fond clair. Le
verrou complet avec le mot devient illisible sous cinquante pixels, c'est
pourquoi l'en-tête affiche le pictogramme en image et le mot en texte.

## Vérifier avant de publier

```bash
pip install playwright --break-system-packages
python3 tools/captures.py
```

Le script photographie chaque page sur téléphone et sur grand écran, puis
contrôle qu'il n'y a qu'un seul `h1` par page, que la navigation porte les
mêmes entrées partout, qu'aucun lien n'est vide, que l'instrument dessine
bien, et surtout **que le menu déplié couvre tout l'écran** à 390, 430 et
768 pixels. Ce dernier point n'est pas décoratif : un volet de navigation
écrasé reste invisible tant qu'on ne l'ouvre pas.

Les captures sortent dans `tools/captures/`, qui n'est pas versionné.

## Aperçu partageable

```bash
python3 tools/build-apercu.py
```

Fabrique `apercu/`, une copie du site dont la page d'accueil est privée de
son squelette HTML, pour être publiée comme aperçu. Dossier non versionné.

## Reste à faire

- Compléter `mentions-legales.html`, obligatoire en France, article 6 LCEN
- Renseigner les comptes réseaux dans `tools/build-pages.py`, fonction `pied()`

## Formulaire de contact

Le formulaire de `contact.html` s'envoie par FormSubmit, un service
gratuit et sans compte. Les demandes arrivent sur `contact@soteros.fr`.

La toute première demande déclenche un e-mail d'activation sur cette
adresse. Il faut cliquer sur le bouton de confirmation une seule fois,
sinon rien n'arrive. Pensez à regarder les spams.
