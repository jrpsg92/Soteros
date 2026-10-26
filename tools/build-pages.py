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
        <p>Création de sites et présence Google<br>
           Île-de-France et à distance dans toute la France</p>
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
          Un site sur mesure et une présence Google pour que vos clients
          vous trouvent en premier
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
        <h2>Un site et une visibilité pensés ensemble</h2>
        <p>Un site performant n'a de valeur que s'il est trouvé. Nous
          traitons donc le site et le référencement en même temps.</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Sites sur mesure</h3>
          <div class="offre__corps">
            <p>Chaque page est développée à la main sans thème acheté ni
              constructeur. <strong>Le site s'ouvre en moins d'une
              seconde</strong> et s'affiche parfaitement sur téléphone comme
              sur ordinateur.</p>
            <ul class="livre">
              <li>Design sur mesure</li>
              <li>Code développé à la main</li>
              <li>Conçu pour le mobile</li>
              <li>Hébergement inclus</li>
            </ul>
          </div>
        </div>

        <div class="offre">
          <h3>Présence Google</h3>
          <div class="offre__corps">
            <p>Nous créons et optimisons votre fiche Google. C'est elle qui
              apparaît avec la carte et les avis quand un client cherche votre
              métier près de chez lui. <strong>Nous installons aussi une page
              dédiée aux avis clients</strong> et vous accompagnons pour la
              diffuser.</p>
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
            <p>Un site évolue avec votre activité. Nouvelles photos, nouveaux
              tarifs ou nouvelle page avant la saison. <strong>Vous nous
              transmettez vos demandes et nous nous occupons du
              reste</strong> sans engagement de durée.</p>
            <ul class="livre">
              <li>Mises à jour</li>
              <li>Nouvelles pages</li>
              <li>Sauvegardes</li>
            </ul>
          </div>
        </div>
      </div>
      <p style="margin-top:clamp(2rem,5vw,3rem)"><a class="bouton" href="mailto:contact@soteros.fr?subject=Demande%20de%20devis">Demander un devis</a></p>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Projets</p>
        <h2>Deux métiers, deux univers</h2>
        <p>Ces deux sites sont en ligne. Découvrez-les et constatez leur
          vitesse de chargement.</p>
      </div>

      <div class="projets">
        <a class="projet" href="https://jrpsg92.github.io/NailsbyDeb/" rel="noopener">
          <p class="projet__meta">Nail artist, Val-d'Oise</p>
          <h3>Nails by Deb</h3>
          <p class="projet__corps">Site vitrine et galerie de réalisations.
            La page d'accueil est passée de plus d'un mégaoctet à deux cents
            kilo-octets. Photos optimisées, contrastes corrigés et pages
            indexées sur Google.</p>
          <p class="projet__voir">Ouvrir le site</p>
        </a>

        <a class="projet" href="https://jrpsg92.github.io/Rajouphoto.fr/" rel="noopener">
          <p class="projet__meta">Photographe, Île-de-France</p>
          <h3>Raju Sinniah</h3>
          <p class="projet__corps">Portfolio de cent trente-six photographies
            réparties en trois séries. Le site se met à jour depuis un fichier
            unique et l'ajout d'une photo prend une minute.</p>
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
        <p>Réduire l'empreinte environnementale de chaque site grâce à la
          mesure plutôt qu'à la promesse</p>
        <p style="margin-top:1.6rem"><a class="lien" href="engagement.html">Voir l'engagement</a></p>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Déroulé</p>
        <h2>Cinq étapes, trois semaines</h2>
        <p>Vous savez à chaque étape où en est le projet et ce que nous
          attendons de vous</p>
      </div>

      <ol class="deroule">
        <li>
          <div>
            <h3>Échange sur votre activité</h3>
            <p>Un appel d'une heure pour comprendre vos clients, leurs
              recherches sur Google et ce qui vous distingue de vos
              concurrents.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Maquette</h3>
            <p>Nous concevons la maquette de la page d'accueil. Vous validez
              la direction avant le début du développement.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Développement</h3>
            <p>Toutes les pages, les textes et les photos optimisées. Vous
              suivez l'avancement sur une adresse privée.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Mise en ligne</h3>
            <p>Nom de domaine, certificat de sécurité et redirections. Nous
              prenons en charge toute la partie technique.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Visibilité Google</h3>
            <p>La fiche, la page d'avis et le suivi des recherches. C'est à
              cette étape que les premières demandes arrivent.</p>
          </div>
        </li>
      </ol>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Prêt à développer votre visibilité&nbsp;?</h2>
        <p>Présentez-nous votre activité et votre secteur. Nous revenons vers
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
        <p>Deux expertises complémentaires. Le site présente votre activité
          et la visibilité Google vous amène des clients.</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Sites sur mesure</h3>
          <div class="offre__corps">
            <p>Le code est développé à la main. Aucun thème acheté ni
              constructeur qui alourdit inutilement les pages.</p>
            <p style="margin-top:1rem">Le résultat se mesure. Les deux sites
              de la page Projets s'ouvrent en moins d'une seconde sur un
              téléphone en 4G. Ils respectent les critères d'accessibilité
              WCAG niveau AA pour un texte lisible par tous.</p>
            <ul class="livre">
              <li>Maquette validée avant le développement</li>
              <li>Conçu pour le mobile en priorité</li>
              <li>Photos optimisées</li>
              <li>Balises et plan de site</li>
              <li>Hébergement inclus</li>
              <li>Les fichiers vous appartiennent</li>
            </ul>
          </div>
        </div>

        <div class="offre">
          <h3>Présence Google</h3>
          <div class="offre__corps">
            <p>La plupart de vos clients ne cherchent pas directement votre
              site. Ils recherchent votre métier suivi de leur ville. Les
              premiers résultats affichés sont la carte et trois fiches
              d'établissement.</p>
            <p style="margin-top:1rem">Nous créons votre fiche et renseignons
              chaque information utile comme les horaires, la zone
              d'intervention, les photos et la catégorie exacte. Nous
              installons ensuite la page qui invite vos clients à laisser un
              avis avec un lien direct à leur envoyer après chaque
              rendez-vous.</p>
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
            <p>Vous nous envoyez vos nouvelles photos ou vos nouveaux tarifs
              et nous mettons le site à jour. Aucun forfait imposé ni
              engagement de longue durée.</p>
            <ul class="livre">
              <li>Mises à jour de contenu</li>
              <li>Nouvelles pages</li>
              <li>Sauvegardes</li>
              <li>Évolutions ponctuelles</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Vous avez un projet&nbsp;?</h2>
        <p>Décrivez-le en quelques lignes. Nous vous indiquons rapidement ce
          que nous pouvons faire et à quel prix.</p>
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
        <h1 class="leve"><span>Réalisations</span></h1>
        <p>Deux sites livrés pour deux métiers très différents. Ils sont en
          ligne et vous pouvez les comparer à la concurrence.</p>
      </div>

      <div class="projets">
        <a class="projet" href="https://jrpsg92.github.io/NailsbyDeb/" rel="noopener">
          <p class="projet__meta">Nail artist, Val-d'Oise</p>
          <h3>Nails by Deb</h3>
          <p class="projet__corps">Refonte complète d'un site existant. La
            page d'accueil est passée de plus d'un mégaoctet à deux cents
            kilo-octets. Les images ont été optimisées et les contrastes
            corrigés. Le site est désormais indexé sur Google grâce à son plan
            de site et ses balises.</p>
          <p class="projet__corps">La galerie de réalisations est classée par
            type de pose et se met à jour depuis un fichier unique.</p>
          <p class="projet__voir">Ouvrir le site</p>
        </a>

        <a class="projet" href="https://jrpsg92.github.io/Rajouphoto.fr/" rel="noopener">
          <p class="projet__meta">Photographe, Île-de-France</p>
          <h3>Raju Sinniah</h3>
          <p class="projet__corps">Portfolio conçu de zéro avec cent
            trente-six photographies réparties en trois séries. Chaque image
            existe en trois largeurs pour qu'un téléphone ne télécharge jamais
            la version grand écran.</p>
          <p class="projet__corps">Les pages sont générées depuis un fichier
            unique. L'ajout d'une série complète prend quelques minutes au
            lieu d'une journée.</p>
          <p class="projet__voir">Ouvrir le site</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="prose">
        <h2>Comment nous évaluons un site</h2>
        <p class="fort">Un site réussi se mesure. Voici les critères vérifiés
          avant chaque livraison.</p>
        <p>Le poids de la page d'accueil, car un visiteur sur mobile quitte la
          page après trois secondes d'attente. Le contraste de chaque texte,
          car un gris clair sur fond blanc exclut une partie de vos clients.
          Un texte alternatif sur chaque image pour les lecteurs d'écran comme
          pour Google. Enfin le rendu réel sur iPhone et non sur une
          simulation.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Et si le prochain projet était le vôtre&nbsp;?</h2>
        <p>Présentez-nous votre métier et votre ville. Nous vous répondons
          avec une proposition claire.</p>
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
          tire d'affaire.</p>
        <p>Cette idée guide notre travail. Beaucoup d'indépendants ont un site
          qui ne leur apporte aucun client ou pas de site du tout. Ils passent
          à côté de clients qui les cherchaient tout près de chez eux. Soteros
          est né pour changer cela.</p>

        <h2>Un interlocuteur unique</h2>
        <p>Derrière Soteros se trouve un développeur. Pas d'équipe commerciale
          ni de sous-traitance. Vous échangez directement avec la personne qui
          conçoit votre site du premier appel à la mise en ligne.</p>
        <p>Vous obtenez des réponses dans la journée et des décisions rapides
          sans intermédiaire.</p>

        <h2>Développé à la main</h2>
        <p>Chaque site part d'une page blanche sans thème ni constructeur. Ce
          travail demande plus de temps. C'est aussi ce qui permet d'ouvrir
          les pages en moins d'une seconde quand la moyenne du secteur dépasse
          trois secondes.</p>
        <p>Les fichiers vous appartiennent. Si vous changez un jour de
          prestataire, vous conservez votre site sans abonnement à résilier ni
          frais de rachat.</p>

        <h2>Nos clients</h2>
        <p>Des artisans, des indépendants et des petites entreprises. Une nail
          artist, un photographe et quelques nouveaux projets chaque
          trimestre. Ce nombre limité garantit la qualité de chaque site.</p>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="appel">
        <h2>Parlons de votre projet</h2>
        <p>Un premier échange d'une heure suffit pour cadrer votre projet. Il
          est gratuit et sans engagement.</p>
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
        <h1 class="leve"><span>Contactez-nous</span></h1>
        <p>Nous répondons en général dans la journée</p>
      </div>
      <div class="voies">
        <div class="voie">
          <p class="voie__nom">Courriel</p>
          <div>
            <p class="voie__valeur"><a href="mailto:contact@soteros.fr">contact@soteros.fr</a></p>
            <p class="voie__note">Pour un devis ou une question</p>
          </div>
        </div>
        <div class="voie">
          <p class="voie__nom">Zone</p>
          <div>
            <p class="voie__valeur">Île-de-France</p>
            <p class="voie__note">Et à distance dans toute la France</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="chapeau">
        <h2>Pour une réponse rapide</h2>
        <p>Quatre informations suffisent. Aucun cahier des charges n'est
          nécessaire.</p>
      </div>
      <div class="offres">
        <div class="offre">
          <h3>Votre métier</h3>
          <div class="offre__corps"><p>Votre activité et ce qui vous distingue de vos concurrents</p></div>
        </div>
        <div class="offre">
          <h3>Votre ville</h3>
          <div class="offre__corps"><p>La commune exacte plutôt que le département. C'est la base du référencement local.</p></div>
        </div>
        <div class="offre">
          <h3>Votre site actuel</h3>
          <div class="offre__corps"><p>S'il en existe un, même ancien ou inactif</p></div>
        </div>
        <div class="offre">
          <h3>Votre échéance</h3>
          <div class="offre__corps"><p>Une ouverture, une saison ou un salon. Cela nous aide à planifier le travail.</p></div>
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
        <p class="fort">En tant qu'agence digitale, nous nous engageons à
          réduire l'empreinte environnementale de nos productions. Notre
          méthode d'éco-conception repose sur la mesure, la modélisation et la
          diminution de l'impact des sites internet.</p>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="chapeau">
        <h2>Ce que ça donne en chiffres</h2>
        <p>Un engagement doit se mesurer. Voici les résultats relevés sur les
          sites déjà livrés.</p>
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
        <h2>Un site léger fait la différence</h2>
        <p>Vos visiteurs le ressentent immédiatement et Google en tient compte
          dans son classement.</p>
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
        <p>Un site complet pour démarrer. Un entretien mensuel pour le faire
          évoluer.</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Création de site</h3>
          <div class="offre__corps">
            <p>Un site sur mesure livré en ligne. <strong>La fiche Google, sa
              page d'avis et le QR code sont offerts.</strong> Le prix dépend
              du nombre de pages. Vous recevez un devis écrit avant tout
              engagement.</p>
            <ul class="livre">
              <li>Site sur mesure conçu pour le mobile</li>
              <li>Hébergement inclus</li>
              <li>Fiche Google avec avis offerte</li>
              <li>QR code vers la page d'avis offert</li>
              <li>Les fichiers vous appartiennent</li>
            </ul>
            {DEVIS}
          </div>
        </div>

        <div class="offre">
          <h3>Entretien</h3>
          <div class="offre__corps">
            <p>Un abonnement mensuel. Vous nous envoyez vos nouvelles photos ou
              vos nouveaux tarifs et nous mettons le site à jour.
              <strong>Sans engagement de durée.</strong></p>
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
          <h3>Quel est le délai de réalisation&nbsp;?</h3>
          <div class="offre__corps"><p>Environ trois semaines du premier échange à la mise en ligne</p></div>
        </div>
        <div class="offre">
          <h3>À quoi sert le QR code&nbsp;?</h3>
          <div class="offre__corps"><p>Il se place sur votre comptoir, votre carte de visite ou vos factures. Vos clients le scannent et arrivent directement sur la page pour laisser un avis.</p></div>
        </div>
        <div class="offre">
          <h3>L'entretien est-il obligatoire&nbsp;?</h3>
          <div class="offre__corps"><p>Non. Le site vous appartient. Vous pouvez souscrire à l'entretien, l'arrêter ou le reprendre à tout moment.</p></div>
        </div>
        <div class="offre">
          <h3>Comment obtenir un devis&nbsp;?</h3>
          <div class="offre__corps"><p>Indiquez-nous votre métier et le contenu souhaité. Nous vous envoyons un devis écrit et sans engagement.</p></div>
        </div>
        <div class="offre">
          <h3>Comment nous joindre&nbsp;?</h3>
          <div class="offre__corps"><p>Par e-mail à <a href="mailto:contact@soteros.fr">contact@soteros.fr</a>. Nous répondons en général dans la journée.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Discutons de votre projet</h2>
        <p>Présentez-nous votre métier et votre ville. Nous revenons vers vous
          avec un devis clair.</p>
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
     "Un interlocuteur unique et des sites développés à la main pour les "
     "indépendants et les petites entreprises.",
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
