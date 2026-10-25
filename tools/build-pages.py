#!/usr/bin/env python3
"""
Soteros — génère les pages du site.

L'en-tête, la navigation et le pied sont écrits une seule fois ici, puis
posés dans chaque page. C'est ce qui empêche la navigation de divrger
d'une page à l'autre quand on en ajoute une sixième.

Usage : python3 tools/build-pages.py
"""
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
BASE = "https://jrpsg92.github.io/Soteros/"

LIENS = [
    ("index.html", "Accueil"),
    ("expertise.html", "Expertise"),
    ("offres.html", "Offres"),
    ("projets.html", "Projets"),
    ("agence.html", "Agence"),
    ("engagement.html", "Engagement"),
    ("contact.html", "Contact"),
]

POLICES = (
    "https://fonts.googleapis.com/css2"
    "?family=Sora:wght@400;600;700"
    "&family=Michroma&display=swap"
)


def tete(titre: str, description: str, fichier: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{BASE}{'' if fichier == 'index.html' else fichier}">

<meta property="og:type" content="website">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{BASE}{'' if fichier == 'index.html' else fichier}">
<meta property="og:locale" content="fr_FR">
<meta name="theme-color" content="#FAFBFC">

<link rel="icon" type="image/png" sizes="32x32" href="img/icone-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="img/icone-192.png">
<link rel="apple-touch-icon" href="img/icone-192.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{POLICES}" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="saut-contenu" href="#contenu">Aller au contenu</a>
"""


def entete(courant: str) -> str:
    items = []
    for fichier, nom in LIENS:
        marque = ' aria-current="page"' if fichier == courant else ""
        items.append(f'        <li><a href="{fichier}"{marque}>{nom}</a></li>')
    liste = "\n".join(items)
    return f"""
<header class="entete" data-entete>
  <div class="enveloppe entete__rangee">
    <a class="signature" href="index.html">
      <img src="img/marque-bleu-96.png" width="96" height="96" alt="" aria-hidden="true">
      <span>Soteros</span>
    </a>
    <button class="bascule" data-bascule aria-expanded="false" aria-controls="menu">
      <span class="bascule__traits" aria-hidden="true"></span>
      <span data-libelle>Menu</span>
    </button>
    <nav class="nav" id="menu" data-nav aria-label="Navigation principale">
      <ul>
{liste}
      </ul>
    </nav>
  </div>
</header>

<main id="contenu">
"""


def pied() -> str:
    pages = "\n".join(
        f'        <li><a href="{f}">{n}</a></li>' for f, n in LIENS[1:]
    )
    return f"""
</main>

<footer class="pied">
  <div class="enveloppe">
    <div class="pied__rangee">
      <div>
        <p class="pied__nom">
          <img src="img/marque-64.png" width="64" height="64" alt="Logo Soteros">
          <span>Soteros</span>
        </p>
        <p>Création de sites et présence Google.<br>
           Île-de-France et à distance partout en France.</p>
      </div>
      <div>
        <p class="pied__intitule">Le site</p>
        <ul>
{pages}
        </ul>
      </div>
      <div>
        <p class="pied__intitule">Réseaux</p>
        <ul>
          <li><a href="#" data-reseau>Instagram</a></li>
          <li><a href="#" data-reseau>LinkedIn</a></li>
          <li><a href="#" data-reseau>TikTok</a></li>
          <li><a href="mentions-legales.html">Mentions légales</a></li>
        </ul>
      </div>
    </div>
    <p class="pied__mention">© 2026 Soteros. Tous droits réservés.</p>
  </div>
</footer>

<script src="script.js" defer></script>
</body>
</html>
"""


# =====================================================================
# Le contenu de chaque page.
# =====================================================================

ACCUEIL = """
  <section class="ouverture">
    <div class="enveloppe ouverture__grille">
      <div>
        <h1 class="bienvenue">
          <span class="leve"><span>Bienvenue</span></span>
          <span class="bienvenue__marque leve leve--2"><span>chez <span class="nom-marque">Soteros</span></span></span>
        </h1>
        <p class="ouverture__intro">
          On vous rend trouvable. Sites sur mesure et présence Google, pour
          les indépendants et les petites structures.
        </p>
        <div class="ouverture__actions">
          <a class="bouton" href="mailto:contact@soteros.fr?subject=Demande%20de%20devis">Demander un devis</a>
          <a class="lien" href="projets.html">Voir les projets</a>
        </div>
      </div>
      <div class="instrument" data-instrument aria-hidden="true"></div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Expertise</p>
        <h2>Le site, et les clients qui vont avec</h2>
        <p>Un beau site que personne ne trouve ne sert à rien. Un bon
          référencement qui mène vers un site bancal non plus. Les deux se
          travaillent ensemble.</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Sites sur mesure</h3>
          <div class="offre__corps">
            <p>Chaque page est écrite à la main. Pas de thème acheté, pas de
              constructeur qui alourdit tout. <strong>Le site s'ouvre en moins
              d'une seconde</strong> et s'affiche aussi bien sur un téléphone
              que sur un grand écran.</p>
            <ul class="livre">
              <li>Design sur mesure</li>
              <li>Code écrit à la main</li>
              <li>Téléphone d'abord</li>
              <li>Hébergement compris</li>
            </ul>
          </div>
        </div>

        <div class="offre">
          <h3>Présence Google</h3>
          <div class="offre__corps">
            <p>Je crée et je règle votre fiche Google, celle qui sort avec la
              carte et les étoiles quand quelqu'un cherche votre métier près
              de chez lui. <strong>J'installe aussi la page qui invite vos
              clients à laisser un avis</strong>, et je vous montre comment la
              partager.</p>
            <ul class="livre">
              <li>Fiche Google</li>
              <li>Page d'avis</li>
              <li>Référencement local</li>
              <li>Données structurées</li>
            </ul>
          </div>
        </div>

        <div class="offre">
          <h3>Suivi</h3>
          <div class="offre__corps">
            <p>Un site vit. Nouvelles photos, nouveaux tarifs, une page de
              plus avant la saison. <strong>Vous écrivez, je m'en occupe</strong>,
              sans engagement de durée.</p>
            <ul class="livre">
              <li>Mises à jour</li>
              <li>Nouvelles pages</li>
              <li>Sauvegardes</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Projets</p>
        <h2>Deux clientes, deux univers</h2>
        <p>Les deux sites tournent en ligne aujourd'hui. Ouvrez-les, regardez
          la vitesse de chargement.</p>
      </div>

      <div class="projets">
        <a class="projet" href="https://jrpsg92.github.io/NailsbyDeb/" rel="noopener">
          <p class="projet__meta">Nail artist, Val-d'Oise</p>
          <h3>Nails by Deb</h3>
          <p class="projet__corps">Site vitrine et galerie de réalisations.
            La page d'accueil pesait plus d'un mégaoctet, elle en fait deux
            cents kilo-octets. Photos converties, contrastes corrigés, pages
            indexées.</p>
          <p class="projet__voir">Ouvrir le site</p>
        </a>

        <a class="projet" href="https://jrpsg92.github.io/Rajouphoto.fr/" rel="noopener">
          <p class="projet__meta">Photographe, Île-de-France</p>
          <h3>Raju Sinniah</h3>
          <p class="projet__corps">Portfolio de cent trente-six photographies
            réparties en trois séries. Tout se génère depuis un seul fichier,
            donc ajouter une photo prend une minute.</p>
          <p class="projet__voir">Ouvrir le site</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Engagement</p>
        <h2>Créer des expériences digitales responsables et désirables</h2>
        <p>Réduire l'empreinte environnementale de chaque site produit, par
          la mesure plutôt que par la promesse.</p>
        <p style="margin-top:1.6rem"><a class="lien" href="engagement.html">Voir l'engagement</a></p>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Déroulé</p>
        <h2>Cinq étapes, trois semaines</h2>
        <p>Vous savez à chaque moment où en est le travail et ce qu'on attend
          de vous.</p>
      </div>

      <ol class="deroule">
        <li>
          <div>
            <h3>On parle de votre métier</h3>
            <p>Un appel d'une heure. Qui sont vos clients, ce qu'ils tapent
              dans Google, ce qui vous distingue de la rue d'à côté.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Je dessine</h3>
            <p>Une maquette de la page d'accueil. Vous validez la direction
              avant qu'une ligne de code soit écrite.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Je construis</h3>
            <p>Toutes les pages, les textes, les photos optimisées. Vous
              suivez l'avancement sur une adresse privée.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Mise en ligne</h3>
            <p>Nom de domaine, certificat, redirections. Vous ne touchez à
              rien de technique.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Google</h3>
            <p>La fiche, la page d'avis, le suivi des recherches. C'est là que
              le téléphone commence à sonner.</p>
          </div>
        </li>
      </ol>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Prêt à être trouvé&nbsp;?</h2>
        <p>Dites-moi ce que vous faites et où vous le faites. Je reviens vers
          vous avec une proposition claire et un prix ferme.</p>
        <a class="bouton" href="mailto:contact@soteros.fr?subject=Demande%20de%20devis">Demander un devis</a>
        <p style="margin-top:1.6rem"><a class="lien" href="contact.html">Contact</a></p>
      </div>
    </div>
  </section>
"""

EXPERTISE = """
  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Expertise</p>
        <h1 class="leve"><span>Sites et visibilité</span></h1>
        <p>Deux métiers qui se tiennent. Le premier vous donne une vitrine, le
          second amène les gens devant.</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Sites sur mesure</h3>
          <div class="offre__corps">
            <p>J'écris le code à la main. Aucun thème acheté, aucun
              constructeur qui charge trois cents kilo-octets de scripts pour
              afficher un titre.</p>
            <p style="margin-top:1rem">Le résultat se mesure. Les deux sites
              de la page Projets s'ouvrent en moins d'une seconde sur un
              téléphone en 4G, et ils passent les critères d'accessibilité
              WCAG niveau AA, ce qui veut dire que le texte reste lisible pour
              tout le monde.</p>
            <ul class="livre">
              <li>Maquette validée avant le code</li>
              <li>Pensé pour le téléphone d'abord</li>
              <li>Photos converties et allégées</li>
              <li>Balises et plan de site</li>
              <li>Hébergement compris</li>
              <li>Les fichiers vous appartiennent</li>
            </ul>
          </div>
        </div>

        <div class="offre">
          <h3>Présence Google</h3>
          <div class="offre__corps">
            <p>La plupart de vos clients ne vont pas chercher votre site, ils
              tapent votre métier et leur ville. Ce qui sort en premier, c'est
              la carte et les trois fiches à côté.</p>
            <p style="margin-top:1rem">Je crée votre fiche, je la remplis
              correctement, horaires, zone d'intervention, photos, catégorie
              exacte. Puis j'installe la page qui demande un avis à vos
              clients, avec le lien direct à envoyer après un rendez-vous.</p>
            <ul class="livre">
              <li>Fiche Google créée et vérifiée</li>
              <li>Page d'avis et lien à partager</li>
              <li>Catégories et zone d'intervention</li>
              <li>Données structurées sur le site</li>
              <li>Suivi des recherches</li>
            </ul>
          </div>
        </div>

        <div class="offre">
          <h3>Suivi</h3>
          <div class="offre__corps">
            <p>Vous m'envoyez les nouvelles photos ou le nouveau tarif, je
              mets à jour. Pas de forfait obligatoire, pas d'engagement sur
              deux ans.</p>
            <ul class="livre">
              <li>Mises à jour de contenu</li>
              <li>Nouvelles pages</li>
              <li>Sauvegardes</li>
              <li>Petites évolutions</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Un projet en tête&nbsp;?</h2>
        <p>Décrivez-le en trois lignes. Je vous dis franchement si je peux
          aider et combien ça coûte.</p>
        <a class="bouton" href="mailto:contact@soteros.fr?subject=Demande%20de%20devis">Demander un devis</a>
        <p style="margin-top:1.6rem"><a class="lien" href="contact.html">Contact</a></p>
      </div>
    </div>
  </section>
"""

PROJETS = """
  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Projets</p>
        <h1 class="leve"><span>Déjà en ligne</span></h1>
        <p>Deux sites livrés, deux métiers très différents. Les deux sont
          ouverts, allez les voir et comparez avec la concurrence.</p>
      </div>

      <div class="projets">
        <a class="projet" href="https://jrpsg92.github.io/NailsbyDeb/" rel="noopener">
          <p class="projet__meta">Nail artist, Val-d'Oise</p>
          <h3>Nails by Deb</h3>
          <p class="projet__corps">Refonte complète d'un site existant. La
            page d'accueil pesait plus d'un mégaoctet, elle en fait deux cents
            kilo-octets. Les images ont été converties et allégées, les
            contrastes du texte corrigés, et le site est passé d'invisible à
            indexé avec son plan de site et ses balises.</p>
          <p class="projet__corps">La galerie de réalisations se range par
            type de pose, et toute la galerie se régénère depuis un seul
            fichier.</p>
          <p class="projet__voir">Ouvrir le site</p>
        </a>

        <a class="projet" href="https://jrpsg92.github.io/Rajouphoto.fr/" rel="noopener">
          <p class="projet__meta">Photographe, Île-de-France</p>
          <h3>Raju Sinniah</h3>
          <p class="projet__corps">Portfolio construit de zéro, cent
            trente-six photographies rangées en trois séries. Chaque image
            existe en trois largeurs, donc un téléphone ne télécharge jamais
            la version d'un grand écran.</p>
          <p class="projet__corps">Les pages se génèrent depuis un fichier
            unique, ce qui veut dire qu'ajouter une série entière demande
            quelques minutes au lieu d'une journée.</p>
          <p class="projet__voir">Ouvrir le site</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="prose">
        <h2>Comment je mesure un site</h2>
        <p class="fort">Un site réussi, ça se chiffre. Voici ce que je regarde
          avant de dire qu'il est fini.</p>
        <p>Le poids de la page d'accueil, parce qu'un visiteur sur un
          téléphone en bord de réseau part au bout de trois secondes. Le
          contraste de chaque texte, parce qu'un gris clair sur blanc exclut
          une partie de vos clients. La présence d'un texte de remplacement
          sur chaque image, pour les lecteurs d'écran et pour Google. Et le
          rendu réel sur un iPhone, pas sur une simulation.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Le prochain, c'est le vôtre</h2>
        <p>Dites-moi votre métier et votre ville. Je vous réponds avec une
          proposition claire.</p>
        <a class="bouton" href="mailto:contact@soteros.fr?subject=Demande%20de%20devis">Demander un devis</a>
        <p style="margin-top:1.6rem"><a class="lien" href="contact.html">Contact</a></p>
      </div>
    </div>
  </section>
"""

AGENCE = """
  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Agence</p>
        <h1 class="leve"><span>Soteros</span></h1>
      </div>

      <div class="prose" style="margin-top:clamp(2.5rem,6vw,4rem)">
        <p class="fort">Le nom vient du grec sôtêr, celui qui protège et qui
          sort d'affaire.</p>
        <p>C'est à peu près le métier. Beaucoup d'indépendants ont un site qui
          ne leur rapporte rien, ou pas de site du tout, et laissent filer des
          clients qui les cherchaient à deux rues de là. Soteros existe pour
          régler ça.</p>

        <h2>Une seule personne, et c'est voulu</h2>
        <p>Derrière Soteros il y a un développeur. Pas un plateau de dix
          personnes, pas de commercial qui vend un projet avant de le passer à
          un stagiaire. Vous parlez directement à celui qui écrit le code,
          du premier appel à la mise en ligne.</p>
        <p>Ça veut dire des réponses dans la journée, des décisions prises en
          une minute, et personne à convaincre en interne pour changer une
          couleur.</p>

        <h2>Écrit à la main</h2>
        <p>Chaque site part d'une page blanche. Aucun thème acheté, aucun
          constructeur. C'est plus long à produire, et c'est exactement pour
          ça que les pages s'ouvrent en moins d'une seconde quand la moyenne
          du secteur dépasse les trois secondes.</p>
        <p>Les fichiers vous appartiennent. Si un jour vous changez de
          prestataire, vous partez avec votre site, sans abonnement à résilier
          et sans rien à racheter.</p>

        <h2>Les clients</h2>
        <p>Des artisans, des indépendants, des petites structures. Une nail
          artist, un photographe, et la place pour quelques projets de plus
          chaque trimestre, parce qu'au-delà la qualité tombe.</p>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="appel">
        <h2>On se parle&nbsp;?</h2>
        <p>Un appel d'une heure suffit pour savoir si le projet tient debout.
          Il est gratuit et sans suite obligatoire.</p>
        <a class="bouton" href="mailto:contact@soteros.fr?subject=Demande%20de%20devis">Demander un devis</a>
        <p style="margin-top:1.6rem"><a class="lien" href="contact.html">Contact</a></p>
      </div>
    </div>
  </section>
"""

CONTACT = """
  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Contact</p>
        <h1 class="leve"><span>Écrivez-moi</span></h1>
        <p>Je réponds moi-même, en général dans la journée.</p>
      </div>
      <div class="voies">
        <div class="voie">
          <p class="voie__nom">Courriel</p>
          <div>
            <p class="voie__valeur"><a href="mailto:contact@soteros.fr">contact@soteros.fr</a></p>
            <p class="voie__note">Pour un devis ou une question.</p>
          </div>
        </div>
        <div class="voie">
          <p class="voie__nom">Zone</p>
          <div>
            <p class="voie__valeur">Île-de-France</p>
            <p class="voie__note">Et à distance partout en France.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="chapeau">
        <h2>Ce qui m'aide à répondre vite</h2>
        <p>Quatre lignes suffisent, pas besoin d'un cahier des charges.</p>
      </div>
      <div class="offres">
        <div class="offre">
          <h3>Votre métier</h3>
          <div class="offre__corps"><p>Et ce qui vous distingue des autres, même si ça vous paraît évident.</p></div>
        </div>
        <div class="offre">
          <h3>Votre ville</h3>
          <div class="offre__corps"><p>La commune exacte, pas le département. C'est ce qui fait tout le référencement local.</p></div>
        </div>
        <div class="offre">
          <h3>Votre site actuel</h3>
          <div class="offre__corps"><p>S'il en existe un, même raté, même abandonné.</p></div>
        </div>
        <div class="offre">
          <h3>Votre échéance</h3>
          <div class="offre__corps"><p>Une ouverture, une saison, un salon. Ça change l'ordre du travail.</p></div>
        </div>
      </div>
    </div>
  </section>
"""

ENGAGEMENT = """
  <section class="section">
    <div class="enveloppe">
      <div class="chapeau" style="max-width:58ch">
        <p class="repere">Engagement</p>
        <h1 class="leve"><span>Créer des expériences digitales responsables et désirables</span></h1>
      </div>

      <div class="prose" style="margin-top:clamp(2.5rem,6vw,4rem)">
        <p class="fort">En tant qu'agence digitale, nous nous engageons pour
          réduire l'empreinte environnementale de nos productions via une
          méthodologie d'éco-conception basée sur la mesure, la modélisation
          et la diminution de l'impact des sites internet.</p>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="chapeau">
        <h2>Ce que ça donne en chiffres</h2>
        <p>Un engagement sans mesure ne vaut rien. Voici ce qui a été relevé
          sur les sites déjà livrés.</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Mesurer</h3>
          <div class="offre__corps">
            <p>Chaque page est pesée avant et après. La page d'accueil de
              Nails by Deb est passée de plus d'un mégaoctet à
              <strong>deux cents kilo-octets</strong>, soit cinq fois moins
              de données transférées à chaque visite.</p>
          </div>
        </div>

        <div class="offre">
          <h3>Modéliser</h3>
          <div class="offre__corps">
            <p>Les images sont le premier poste d'impact d'un site. Elles
              sont converties et déclinées en trois largeurs, pour qu'un
              téléphone ne télécharge jamais la version d'un grand écran.
              Sur le portfolio de Raju Sinniah, cela représente
              <strong>cent trente-six photographies allégées</strong>.</p>
          </div>
        </div>

        <div class="offre">
          <h3>Diminuer</h3>
          <div class="offre__corps">
            <p>Pas de constructeur, pas de thème acheté, aucune bibliothèque
              chargée sans raison. L'animation de la page d'accueil de ce
              site pèse <strong>deux kilo-octets</strong> au lieu des six
              cents d'une bibliothèque 3D classique.</p>
          </div>
        </div>

        <div class="offre">
          <h3>Durer</h3>
          <div class="offre__corps">
            <p>Un site en HTML simple fonctionne encore dans dix ans sans
              mise à jour de sécurité ni migration. Refaire un site tous les
              trois ans reste le plus gros gaspillage du métier.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Un site léger, ça se voit</h2>
        <p>Vos visiteurs le ressentent avant de comprendre pourquoi, et
          Google le mesure pour de bon.</p>
        <a class="bouton" href="mailto:contact@soteros.fr?subject=Demande%20de%20devis">Demander un devis</a>
        <p style="margin-top:1.6rem"><a class="lien" href="contact.html">Contact</a></p>
      </div>
    </div>
  </section>
"""

LEGALES = """
  <section class="section">
    <div class="enveloppe">
      <div class="prose">
        <p class="repere">Informations</p>
        <h1>Mentions légales</h1>

        <!-- =================================================================
             À COMPLÉTER AVANT LA MISE EN LIGNE PUBLIQUE.
             Obligatoire pour un site professionnel en France, article 6 LCEN.
             ================================================================= -->

        <h2>Éditeur du site</h2>
        <p>Nom et prénom <strong>[À COMPLÉTER]</strong><br>
           Statut juridique <strong>[À COMPLÉTER]</strong><br>
           Numéro SIRET <strong>[À COMPLÉTER]</strong><br>
           Adresse professionnelle <strong>[À COMPLÉTER]</strong><br>
           Adresse e-mail <a href="mailto:contact@soteros.fr">contact@soteros.fr</a><br>
           Directeur de la publication <strong>[À COMPLÉTER]</strong></p>

        <h2>Hébergement</h2>
        <p>Le site est hébergé par GitHub&nbsp;Inc., 88 Colin P. Kelly Jr.
          Street, San Francisco, CA 94107, États-Unis, via GitHub&nbsp;Pages.</p>

        <h2>Propriété intellectuelle</h2>
        <p>Les textes et les éléments graphiques de ce site sont la propriété
          de son éditeur. Les captures et les noms des sites présentés en page
          Projets restent la propriété de leurs titulaires respectifs et
          apparaissent ici avec leur accord.</p>

        <h2>Données personnelles</h2>
        <p>Ce site est une vitrine. Il ne comporte aucun formulaire, ne dépose
          aucun cookie de mesure d'audience et ne collecte aucune donnée
          pendant la navigation. Les polices de caractères sont chargées
          depuis Google&nbsp;Fonts, ce qui transmet votre adresse IP à Google
          lors de l'affichage des pages.</p>

        <h2>Accessibilité</h2>
        <p>Ce site vise les critères WCAG&nbsp;2.1 niveau AA. Si vous
          rencontrez une difficulté d'accès à une information, signalez-la à
          l'adresse de contact.</p>
      </div>
    </div>
  </section>
"""

DEVIS = '<p style="margin-top:1.4rem"><a class="bouton" href="mailto:contact@soteros.fr?subject=Demande%20de%20devis">Demander un devis</a></p>'


OFFRES = f"""
  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Offres</p>
        <h1 class="leve"><span>Deux formules</span></h1>
        <p>Un site complet pour commencer. Un entretien si vous voulez que je
          m'occupe de la suite.</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Création de site</h3>
          <div class="offre__corps">
            <p>Un site sur mesure, mis en ligne. <strong>Votre fiche Google, sa
              page d'avis et le QR code sont offerts.</strong> Le prix
              dépend du nombre de pages, et vous recevez un devis écrit avant
              de vous engager.</p>
            <ul class="livre">
              <li>Site sur mesure, pensé pour le téléphone</li>
              <li>Hébergement compris</li>
              <li>Fiche Google avec avis, offerte</li>
              <li>QR code vers la page d'avis, offert</li>
              <li>Les fichiers vous appartiennent</li>
            </ul>
            {DEVIS}
          </div>
        </div>

        <div class="offre">
          <h3>Entretien</h3>
          <div class="offre__corps">
            <p>Un abonnement mensuel. Vous m'envoyez vos nouvelles photos ou
              vos nouveaux tarifs, je mets à jour. <strong>Sans engagement de
              durée.</strong></p>
            <ul class="livre">
              <li>Mises à jour de contenu</li>
              <li>Petites modifications</li>
              <li>Sauvegardes</li>
            </ul>
            {DEVIS}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="chapeau">
        <h2>Questions fréquentes</h2>
      </div>
      <div class="offres">
        <div class="offre">
          <h3>Combien de temps ça prend&nbsp;?</h3>
          <div class="offre__corps"><p>Environ trois semaines, du premier appel à la mise en ligne.</p></div>
        </div>
        <div class="offre">
          <h3>À quoi sert le QR code&nbsp;?</h3>
          <div class="offre__corps"><p>Vous le posez sur votre comptoir, votre carte de visite ou vos factures. Vos clients le scannent et arrivent directement sur la page pour laisser un avis.</p></div>
        </div>
        <div class="offre">
          <h3>L'entretien est-il obligatoire&nbsp;?</h3>
          <div class="offre__corps"><p>Non. Le site vous appartient. Vous pouvez prendre l'entretien, l'arrêter ou le reprendre quand vous voulez.</p></div>
        </div>
        <div class="offre">
          <h3>Comment avoir un prix&nbsp;?</h3>
          <div class="offre__corps"><p>Écrivez-moi votre métier et ce que vous voulez sur le site. Je vous envoie un devis écrit, sans engagement.</p></div>
        </div>
        <div class="offre">
          <h3>Comment vous joindre&nbsp;?</h3>
          <div class="offre__corps"><p>Par e-mail à <a href="mailto:contact@soteros.fr">contact@soteros.fr</a>. Je réponds en général dans la journée.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>On en parle&nbsp;?</h2>
        <p>Dites-moi votre métier et votre ville. Je reviens vers vous avec un
          devis clair.</p>
        <a class="bouton" href="mailto:contact@soteros.fr?subject=Demande%20de%20devis">Demander un devis</a>
        <p style="margin-top:1.6rem"><a class="lien" href="contact.html">Contact</a></p>
      </div>
    </div>
  </section>
"""

PAGES = [
    ("index.html", "Soteros — Création de sites et présence Google",
     "Soteros construit votre site sur mesure et installe votre présence sur "
     "Google. Pour les indépendants et les petites structures en Île-de-France.",
     ACCUEIL),
    ("expertise.html", "Expertise — Soteros",
     "Création de sites écrits à la main, fiche Google, page d'avis et "
     "référencement local.",
     EXPERTISE),
    ("offres.html", "Offres — Soteros",
     "Création de site avec fiche Google, page d'avis et QR code offerts. "
     "Entretien mensuel sans engagement.",
     OFFRES),
    ("projets.html", "Projets — Soteros",
     "Deux sites livrés et en ligne, pour une nail artist et un photographe "
     "en Île-de-France.",
     PROJETS),
    ("agence.html", "L'agence — Soteros",
     "Un développeur, des sites écrits à la main, des clients indépendants. "
     "Ce que Soteros fait et comment.",
     AGENCE),
    ("engagement.html", "Engagement — Soteros",
     "Éco-conception des sites internet. Mesurer, modéliser et diminuer "
     "l'impact environnemental de nos productions.",
     ENGAGEMENT),
    ("contact.html", "Contact — Soteros",
     "Parler de votre projet de site ou de votre présence Google. Réponse "
     "dans la journée.",
     CONTACT),
    ("mentions-legales.html", "Mentions légales — Soteros",
     "Mentions légales et données personnelles.",
     LEGALES),
]


def main() -> None:
    for fichier, titre, description, corps in PAGES:
        courant = fichier if any(f == fichier for f, _ in LIENS) else ""
        html = tete(titre, description, fichier) + entete(courant) + corps + pied()
        (RACINE / fichier).write_text(html, encoding="utf-8")
        print(f"écrit  {fichier}")

    # Plan de site, pour que Google trouve les pages du premier coup.
    urls = "\n".join(
        f"  <url><loc>{BASE}{'' if f == 'index.html' else f}</loc></url>"
        for f, _ in LIENS
    )
    (RACINE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n",
        encoding="utf-8",
    )
    (RACINE / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8"
    )
    print("écrit  sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
