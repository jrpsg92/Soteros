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
          <a class="bouton" href="contact.html?objet=devis#formulaire">Demander un devis</a>
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
        <h2>Du site internet à la visibilité sur Google</h2>
        <p>Un site n'est utile que s'il est trouvé. C'est pourquoi nous
          prenons en charge sa création comme son référencement.</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Sites sur mesure</h3>
          <div class="offre__corps">
            <p>Chaque site est créé pour votre activité, sans modèle
              préfabriqué. <strong>Il se charge rapidement</strong> et s'adapte à tous les
              écrans, du smartphone à l'ordinateur.</p>
            <ul class="livre">
              <li>Design personnalisé</li>
              <li>Adapté au mobile</li>
              <li>Chargement rapide</li>
              <li>Hébergement inclus</li>
            </ul>
          </div>
        </div>

        <div class="offre">
          <h3>Présence Google</h3>
          <div class="offre__corps">
            <p>Nous créons et optimisons votre fiche d'établissement Google.
              C'est elle qui s'affiche sur Google Maps lorsqu'un client
              recherche votre activité dans votre secteur. <strong>Nous mettons
              aussi en place un lien et un QR code</strong> pour recueillir
              facilement les avis de vos clients.</p>
            <ul class="livre">
              <li>Fiche Google</li>
              <li>Avis clients</li>
              <li>Référencement local</li>
              <li>Référencement naturel</li>
            </ul>
          </div>
        </div>

        <div class="offre">
          <h3>Suivi</h3>
          <div class="offre__corps">
            <p>Votre site évolue avec votre activité. Nous assurons la mise à
              jour de vos contenus, l'ajout de nouvelles pages et la sauvegarde
              de votre site. <strong>Le tout sans engagement de
              durée.</strong></p>
            <ul class="livre">
              <li>Mises à jour</li>
              <li>Nouvelles pages</li>
              <li>Sauvegardes</li>
            </ul>
          </div>
        </div>
      </div>
      <p style="margin-top:clamp(2rem,5vw,3rem)"><a class="bouton" href="contact.html?objet=devis#formulaire">Demander un devis</a></p>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Projets</p>
        <h2>Nos dernières réalisations</h2>
        <p>Découvrez deux sites récemment mis en ligne</p>
      </div>

      <div class="projets">
        <a class="projet" href="https://jrpsg92.github.io/NailsbyDeb/" rel="noopener">
          <p class="projet__meta">Nail artist, Val-d'Oise</p>
          <h3>Nails by Deb</h3>
          <p class="projet__corps">Refonte complète du site d'une prothésiste
            ongulaire. Une galerie de réalisations, des pages plus rapides et
            une meilleure visibilité sur Google.</p>
          <p class="projet__voir">Voir le site</p>
        </a>

        <a class="projet" href="https://jrpsg92.github.io/Rajouphoto.fr/" rel="noopener">
          <p class="projet__meta">Photographe, Île-de-France</p>
          <h3>Raju Sinniah</h3>
          <p class="projet__corps">Création du portfolio d'un photographe. Une
            mise en page sobre qui laisse toute la place aux images.</p>
          <p class="projet__voir">Voir le site</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Engagement</p>
        <h2>Créer des expériences digitales responsables et désirables</h2>
        <p>Des sites légers et sobres qui limitent leur impact sur
          l'environnement</p>
        <p style="margin-top:1.6rem"><a class="lien" href="engagement.html">Découvrir notre engagement</a></p>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Méthode</p>
        <h2>Un accompagnement en cinq étapes</h2>
        <p>Vous êtes informé de l'avancement de votre projet à chaque
          étape</p>
      </div>

      <ol class="deroule">
        <li>
          <div>
            <h3>Premier échange</h3>
            <p>Nous faisons le point sur votre activité, votre clientèle et
              vos objectifs.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Maquette</h3>
            <p>Nous vous présentons une proposition graphique. Le
              développement commence une fois la maquette validée.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Création du site</h3>
            <p>Nous réalisons l'ensemble des pages avec vos textes et vos
              photos. Vous pouvez suivre l'avancement à tout moment.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Mise en ligne</h3>
            <p>Nous nous occupons du nom de domaine, de l'hébergement et de la
              sécurité du site.</p>
          </div>
        </li>
        <li>
          <div>
            <h3>Visibilité Google</h3>
            <p>Nous créons votre fiche Google et mettons en place la collecte
              d'avis pour vous rendre visible localement.</p>
          </div>
        </li>
      </ol>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Un projet de site internet&nbsp;?</h2>
        <p>Parlez-nous de votre activité. Nous vous répondons rapidement avec
          un devis personnalisé.</p>
        <a class="bouton" href="contact.html?objet=devis#formulaire">Demander un devis</a>
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
        <h1 class="leve"><span>Création de sites et visibilité Google</span></h1>
        <p>Deux services complémentaires. Le site présente votre activité.
          La visibilité sur Google vous permet d'attirer de nouveaux
          clients.</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Sites sur mesure</h3>
          <div class="offre__corps">
            <p>Chaque site est conçu et développé sur mesure, sans modèle
              préfabriqué. Le résultat est un site unique qui vous
              ressemble.</p>
            <p style="margin-top:1rem">Nos sites sont rapides, adaptés à tous
              les écrans et respectent les bonnes pratiques d'accessibilité.
              Chaque visiteur profite d'une navigation simple et
              agréable.</p>
            <ul class="livre">
              <li>Maquette validée avant le développement</li>
              <li>Adapté au mobile</li>
              <li>Images optimisées</li>
              <li>Optimisation pour Google</li>
              <li>Hébergement inclus</li>
              <li>Vous restez propriétaire de votre site</li>
            </ul>
          </div>
        </div>

        <div class="offre">
          <h3>Présence Google</h3>
          <div class="offre__corps">
            <p>Lorsqu'un client recherche un professionnel près de chez lui,
              Google affiche d'abord une carte et quelques établissements. Y
              figurer est essentiel pour une activité locale.</p>
            <p style="margin-top:1rem">Nous créons votre fiche
              d'établissement et la complétons avec soin. Horaires, zone
              d'intervention, photos et catégorie d'activité sont renseignés.
              Nous mettons également en place un lien et un QR code pour
              inviter vos clients à laisser un avis.</p>
            <ul class="livre">
              <li>Création et vérification de la fiche Google</li>
              <li>Lien et QR code pour les avis</li>
              <li>Catégories et zone d'intervention</li>
              <li>Référencement local</li>
              <li>Suivi des performances</li>
            </ul>
          </div>
        </div>

        <div class="offre">
          <h3>Suivi</h3>
          <div class="offre__corps">
            <p>Nous assurons la maintenance de votre site. Vous nous
              transmettez vos nouveaux contenus et nous effectuons les mises à
              jour. Sans engagement de durée.</p>
            <ul class="livre">
              <li>Mises à jour de contenu</li>
              <li>Ajout de pages</li>
              <li>Sauvegardes régulières</li>
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
        <p>Décrivez-le en quelques lignes. Nous vous répondons rapidement avec
          un devis personnalisé.</p>
        <a class="bouton" href="contact.html?objet=devis#formulaire">Demander un devis</a>
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
        <p>Découvrez quelques sites que nous avons conçus et mis en
          ligne</p>
      </div>

      <div class="projets">
        <a class="projet" href="https://jrpsg92.github.io/NailsbyDeb/" rel="noopener">
          <p class="projet__meta">Nail artist, Val-d'Oise</p>
          <h3>Nails by Deb</h3>
          <p class="projet__corps">Refonte complète du site d'une prothésiste
            ongulaire. Le site est désormais plus rapide, plus lisible et
            mieux référencé sur Google.</p>
          <p class="projet__corps">La galerie présente ses réalisations par
            type de prestation et se met à jour en quelques minutes.</p>
          <p class="projet__voir">Voir le site</p>
        </a>

        <a class="projet" href="https://jrpsg92.github.io/Rajouphoto.fr/" rel="noopener">
          <p class="projet__meta">Photographe, Île-de-France</p>
          <h3>Raju Sinniah</h3>
          <p class="projet__corps">Création du portfolio d'un photographe. Plus
            de cent trente photographies sont présentées en trois séries,
            dans une mise en page sobre qui met les images en valeur.</p>
          <p class="projet__corps">Les photos sont optimisées pour s'afficher
            rapidement sur tous les écrans.</p>
          <p class="projet__voir">Voir le site</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="prose">
        <h2>Notre exigence de qualité</h2>
        <p class="fort">Avant chaque mise en ligne, nous vérifions plusieurs
          points essentiels.</p>
        <p>Nous contrôlons la vitesse de chargement, en particulier sur
          mobile. Nous vérifions la lisibilité des textes et la description
          de chaque image, utile à Google comme aux personnes malvoyantes.
          Enfin, chaque site est testé sur de vrais appareils.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Et si le prochain projet était le vôtre&nbsp;?</h2>
        <p>Parlez-nous de votre activité. Nous vous répondons avec une
          proposition adaptée.</p>
        <a class="bouton" href="contact.html?objet=devis#formulaire">Demander un devis</a>
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
        <p class="fort">Soteros vient du grec sôtêr, « celui qui
          protège ».</p>
        <p>Notre mission est d'aider les indépendants et les petites
          entreprises à se faire connaître en ligne. Beaucoup n'ont pas encore
          de site, ou un site qui ne leur apporte pas de clients. Soteros les
          accompagne pour gagner en visibilité.</p>

        <h2>Un interlocuteur unique</h2>
        <p>Vous échangez avec la même personne du premier rendez-vous à la
          mise en ligne. Vous bénéficiez ainsi d'un suivi personnalisé et de
          réponses rapides.</p>

        <h2>Des sites sur mesure</h2>
        <p>Chaque site est créé spécialement pour votre activité, sans modèle
          préfabriqué. Il est plus léger, plus rapide et plus simple à faire
          évoluer.</p>
        <p>Votre site vous appartient. Si vous changez un jour de prestataire,
          vous le conservez sans frais supplémentaires.</p>

        <h2>Nos clients</h2>
        <p>Artisans, indépendants, commerces et petites entreprises. Nous
          limitons le nombre de projets en parallèle pour consacrer à chacun
          le temps nécessaire.</p>
      </div>
    </div>
  </section>

  <section class="section section--creuse">
    <div class="enveloppe">
      <div class="appel">
        <h2>Parlons de votre projet</h2>
        <p>Un premier échange permet de comprendre vos besoins. Il est
          gratuit et sans engagement.</p>
        <a class="bouton" href="contact.html?objet=devis#formulaire">Demander un devis</a>
        <p style="margin-top:1.6rem"><a class="lien" href="contact.html">Contact</a></p>
      </div>
    </div>
  </section>
"""

CONTACT = f"""
  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Contact</p>
        <h1 class="leve"><span>Contactez-nous</span></h1>
        <p>Une question ou un projet&nbsp;? Remplissez le formulaire et nous
          vous répondrons dans les meilleurs délais.</p>
      </div>

      <div class="contact" id="formulaire">
      <div>
      <!-- Envoi par FormSubmit vers contact@soteros.fr. La toute première
           demande déclenche un e-mail d'activation à valider une fois. -->
      <form class="formulaire" action="https://formsubmit.co/contact@soteros.fr" method="POST" data-formulaire>
        <input type="hidden" name="_subject" value="Nouvelle demande depuis le site Soteros">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="{BASE}contact.html?envoye=1#formulaire">
        <input type="text" name="_honey" class="formulaire__piege" tabindex="-1" autocomplete="off" aria-hidden="true">

        <div class="formulaire__rangee">
          <div class="champ">
            <label for="nom">Nom</label>
            <input id="nom" name="Nom" type="text" autocomplete="family-name" required>
          </div>
          <div class="champ">
            <label for="prenom">Prénom</label>
            <input id="prenom" name="Prénom" type="text" autocomplete="given-name" required>
          </div>
        </div>
        <div class="formulaire__rangee">
          <div class="champ">
            <label for="email">E-mail</label>
            <input id="email" name="email" type="email" autocomplete="email" required>
          </div>
          <div class="champ">
            <label for="telephone">Téléphone <span class="champ__option">facultatif</span></label>
            <input id="telephone" name="Téléphone" type="tel" autocomplete="tel">
          </div>
        </div>
        <div class="champ">
          <label for="objet">Objet</label>
          <input id="objet" name="Objet" type="text" required>
        </div>
        <div class="champ">
          <label for="message">Message</label>
          <textarea id="message" name="Message" rows="6" required aria-describedby="message-aide"></textarea>
          <p class="champ__aide" id="message-aide">Votre activité, votre ville et votre échéance nous aident à établir un devis</p>
        </div>
        <button class="bouton" type="submit">Envoyer la demande</button>
        <p class="formulaire__mention">Vos informations servent uniquement à
          répondre à votre demande. <a href="mentions-legales.html">En savoir plus</a></p>
      </form>

      <div class="formulaire__merci" data-merci role="status" hidden>
        <h2>Merci pour votre message</h2>
        <p>Votre demande a bien été envoyée. Nous vous répondrons dans les
          meilleurs délais.</p>
      </div>
      </div>

      <div class="voies">
        <div class="voie">
          <p class="voie__nom">E-mail</p>
          <div>
            <p class="voie__valeur"><a href="mailto:contact@soteros.fr">contact@soteros.fr</a></p>
            <p class="voie__note">Pour un devis ou une question</p>
          </div>
        </div>
        <div class="voie">
          <p class="voie__nom">Zone</p>
          <div>
            <p class="voie__valeur">Île-de-France</p>
            <p class="voie__note">Interventions à distance dans toute la France</p>
          </div>
        </div>
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
        <h2>Nos actions concrètes</h2>
        <p>Quatre principes guident la conception de chaque site</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Mesurer</h3>
          <div class="offre__corps">
            <p>Nous mesurons le poids de chaque page. Sur le site Nails by
              Deb, la page d'accueil est désormais <strong>cinq fois plus
              légère</strong> qu'avant la refonte.</p>
          </div>
        </div>

        <div class="offre">
          <h3>Optimiser</h3>
          <div class="offre__corps">
            <p>Les images représentent la plus grande part du poids d'un site.
              Elles sont compressées et proposées en plusieurs tailles. Chaque
              appareil charge uniquement la version adaptée à son
              écran.</p>
          </div>
        </div>

        <div class="offre">
          <h3>Alléger</h3>
          <div class="offre__corps">
            <p>Nos sites n'utilisent ni constructeur ni extension superflue.
              Seul le code nécessaire est chargé, ce qui rend chaque page plus
              rapide.</p>
          </div>
        </div>

        <div class="offre">
          <h3>Durer</h3>
          <div class="offre__corps">
            <p>Un site simple et bien construit reste fonctionnel pendant des
              années, sans refonte coûteuse. C'est la meilleure façon de
              limiter son impact.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Un site léger fait la différence</h2>
        <p>Vos visiteurs profitent d'un site plus rapide et Google en tient
          compte dans son classement.</p>
        <a class="bouton" href="contact.html?objet=devis#formulaire">Demander un devis</a>
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
        <p>Les informations envoyées par le formulaire de contact (nom,
          prénom, e-mail, téléphone et message) servent uniquement à répondre
          à votre demande. Elles sont transmises par le service FormSubmit
          puis conservées dans notre messagerie. Elles ne sont ni cédées ni
          utilisées à des fins commerciales.</p>
        <p>Vous pouvez demander l'accès à vos données, leur correction ou
          leur suppression en écrivant à
          <a href="mailto:contact@soteros.fr">contact@soteros.fr</a>.</p>
        <p>Ce site ne dépose aucun cookie de mesure d'audience. Les polices de
          caractères sont chargées depuis Google&nbsp;Fonts, ce qui transmet
          votre adresse IP à Google lors de l'affichage des pages.</p>

        <h2>Accessibilité</h2>
        <p>Ce site vise les critères WCAG&nbsp;2.1 niveau AA. Si vous
          rencontrez une difficulté d'accès à une information, signalez-la à
          l'adresse de contact.</p>
      </div>
    </div>
  </section>
"""

DEVIS = '<p style="margin-top:1.4rem"><a class="bouton" href="contact.html?objet=devis#formulaire">Demander un devis</a></p>'


OFFRES = f"""
  <section class="section">
    <div class="enveloppe">
      <div class="chapeau">
        <p class="repere">Offres</p>
        <h1 class="leve"><span>Nos offres</span></h1>
        <p>La création de votre site, puis un accompagnement pour le faire
          évoluer</p>
      </div>

      <div class="offres">
        <div class="offre">
          <h3>Création de site</h3>
          <div class="offre__corps">
            <p>Un site sur mesure, conçu selon vos besoins et mis en ligne.
              <strong>La création de votre fiche Google et votre QR code
              d'avis sont offerts.</strong> Le tarif dépend du nombre de pages
              et fait l'objet d'un devis gratuit.</p>
            <ul class="livre">
              <li>Site sur mesure adapté au mobile</li>
              <li>Hébergement inclus</li>
              <li>Fiche Google offerte</li>
              <li>QR code d'avis offert</li>
              <li>Vous restez propriétaire de votre site</li>
            </ul>
            {DEVIS}
          </div>
        </div>

        <div class="offre">
          <h3>Entretien</h3>
          <div class="offre__corps">
            <p>Un abonnement mensuel pour garder votre site à jour. Vous nous
              transmettez vos nouveaux contenus et nous nous chargeons des
              modifications. <strong>Sans engagement de durée.</strong></p>
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
          <div class="offre__corps"><p>Le délai dépend de votre projet. Comptez en moyenne trois semaines entre le premier échange et la mise en ligne.</p></div>
        </div>
        <div class="offre">
          <h3>À quoi sert le QR code&nbsp;?</h3>
          <div class="offre__corps"><p>Il peut être affiché sur votre comptoir, vos cartes de visite ou vos factures. Vos clients le scannent et accèdent directement à la page pour laisser un avis.</p></div>
        </div>
        <div class="offre">
          <h3>L'entretien est-il obligatoire&nbsp;?</h3>
          <div class="offre__corps"><p>Non. Votre site vous appartient. L'abonnement d'entretien est facultatif et sans engagement.</p></div>
        </div>
        <div class="offre">
          <h3>Comment obtenir un devis&nbsp;?</h3>
          <div class="offre__corps"><p>Contactez-nous en présentant votre activité et vos besoins. Nous vous adressons un devis gratuit et sans engagement.</p></div>
        </div>
        <div class="offre">
          <h3>Comment nous joindre&nbsp;?</h3>
          <div class="offre__corps"><p>Par e-mail à <a href="mailto:contact@soteros.fr">contact@soteros.fr</a>. Nous vous répondons dans les meilleurs délais.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="enveloppe">
      <div class="appel">
        <h2>Discutons de votre projet</h2>
        <p>Parlez-nous de votre activité. Nous vous répondons avec un devis
          personnalisé.</p>
        <a class="bouton" href="contact.html?objet=devis#formulaire">Demander un devis</a>
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
     "Création de sites sur mesure, fiche Google, avis clients et "
     "référencement local.",
     EXPERTISE),
    ("offres.html", "Offres — Soteros",
     "Création de site avec fiche Google, page d'avis et QR code offerts. "
     "Entretien mensuel sans engagement.",
     OFFRES),
    ("projets.html", "Projets — Soteros",
     "Nos réalisations pour une nail artist et un photographe en "
     "Île-de-France.",
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
     "Parlez-nous de votre projet de site internet ou de votre visibilité "
     "sur Google.",
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
