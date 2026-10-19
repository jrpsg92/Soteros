/* =====================================================================
   Soteros — comportements partagés.
   Tout est optionnel. Sans JavaScript, les pages restent entièrement
   lisibles et navigables, seul l'instrument du hero ne tourne pas.
   ===================================================================== */
(function () {
  "use strict";

  var sobre = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* --- Volet de navigation ---------------------------------------------- */

  var bascule = document.querySelector("[data-bascule]");
  var nav = document.querySelector("[data-nav]");
  var libelle = document.querySelector("[data-libelle]");

  if (bascule && nav) {
    nav.dataset.ouvert = "false";

    var basculer = function (ouvrir) {
      bascule.setAttribute("aria-expanded", String(ouvrir));
      nav.dataset.ouvert = String(ouvrir);
      if (libelle) libelle.textContent = ouvrir ? "Fermer" : "Menu";
      document.body.style.overflow = ouvrir ? "hidden" : "";
    };

    bascule.addEventListener("click", function () {
      basculer(bascule.getAttribute("aria-expanded") !== "true");
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && bascule.getAttribute("aria-expanded") === "true") {
        basculer(false);
        bascule.focus();
      }
    });

    // Repasser en navigation de bureau annule le verrou de défilement.
    window.matchMedia("(min-width: 62rem)").addEventListener("change", function (e) {
      if (e.matches) basculer(false);
    });
  }

  /* --- Filet de l'en-tête au défilement --------------------------------- */

  var entete = document.querySelector("[data-entete]");
  if (entete) {
    var poser = function () {
      entete.dataset.pose = String(window.scrollY > 24);
    };
    poser();
    window.addEventListener("scroll", poser, { passive: true });
  }

  /* =====================================================================
     L'instrument.

     Des anneaux imbriqués qui tournent, comme les cercles d'un astrolabe.
     Projection en perspective calculée à la main et tracé en Canvas 2D,
     sans aucune bibliothèque : le rendu pèse deux kilo-octets au lieu de
     six cents, tourne à soixante images par seconde sur un téléphone, et
     les traits fins d'un tracé 2D sont plus nets que des lignes WebGL.

     Les segments sont regroupés par tranche de profondeur, puis chaque
     tranche est tracée en une seule passe. Sept tracés par image au lieu
     de plusieurs centaines.
     ===================================================================== */

  var hote = document.querySelector("[data-instrument]");
  if (!hote) return;

  var toile = document.createElement("canvas");
  var ctx = toile.getContext && toile.getContext("2d");
  if (!ctx) return;              // navigateur sans canvas, le hero reste propre
  hote.appendChild(toile);

  var CYAN = "11, 95, 208";    // le bleu profond, lisible sur blanc
  var BLEU = "12, 114, 145";   // le teal, pour distinguer les anneaux
  var TRANCHES = 7;

  /* Le nom tourne en orbite autour de l'instrument, à plat comme la
     tranche gravée d'une médaille. Les lettres passées derrière la sphère
     s'effacent et rapetissent, ce sont elles qui donnent le relief. */

  /* Chaque anneau porte son inclinaison, son rayon et sa vitesse propre.
     Les inclinaisons sont volontairement étalées : deux anneaux présentés
     de profil au même instant ne se lisent plus comme des cercles, ils
     ressemblent à deux rayures en travers de l'image. */
  var anneaux = [
    { ax: .22,  ay:  0,   r: 1.00,  vit:  .085, ep: 1.5, col: CYAN, ticks: true },
    { ax: 1.02, ay:  .40, r: 0.985, vit: -.062, ep: 1.2, col: CYAN },
    { ax: .58,  ay: 1.15, r: 0.86,  vit:  .115, ep: 1.1, col: BLEU },
    { ax: 1.24, ay: -.55, r: 0.70,  vit: -.148, ep: 1.1, col: CYAN },
    { ax: .80,  ay:  .80, r: 0.50,  vit:  .205, ep: 1.1, col: BLEU }
  ];

  var SEGMENTS = 96;
  var FOCALE = 3.4;

  var larg = 0, haut = 0, cx = 0, cy = 0, rayon = 0;

  function mesurer() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var boite = hote.getBoundingClientRect();
    larg = Math.max(1, Math.round(boite.width));
    haut = Math.max(1, Math.round(boite.height));
    toile.width = Math.round(larg * dpr);
    toile.height = Math.round(haut * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cx = larg / 2;
    cy = haut / 2;
    // 0.38 et non 0.42 : le nom orbite plus loin que le plus grand anneau,
    // il lui faut la marge sinon les lettres sortent du cadre.
    rayon = Math.min(larg, haut) * 0.38;
  }

  /* Un point d'anneau, incliné puis tourné autour de l'axe vertical. */
  function projeter(t, an, lacet, tangage) {
    var x = Math.cos(t) * an.r;
    var y = Math.sin(t) * an.r;
    var z = 0;

    // inclinaison propre de l'anneau
    var ca = Math.cos(an.ax), sa = Math.sin(an.ax);
    var y1 = y * ca - z * sa;
    var z1 = y * sa + z * ca;

    var cb = Math.cos(an.ay + an.phase), sb = Math.sin(an.ay + an.phase);
    var x2 = x * cb + z1 * sb;
    var z2 = -x * sb + z1 * cb;

    // rotation d'ensemble, plus le léger suivi du pointeur
    var cl = Math.cos(lacet), sl = Math.sin(lacet);
    var x3 = x2 * cl + z2 * sl;
    var z3 = -x2 * sl + z2 * cl;

    var ct = Math.cos(tangage), st = Math.sin(tangage);
    var y4 = y1 * ct - z3 * st;
    var z4 = y1 * st + z3 * ct;

    var ech = FOCALE / (FOCALE - z4);
    return { x: cx + x3 * ech * rayon, y: cy + y4 * ech * rayon, z: z4 };
  }

  var depart = null;
  var lacet = 0;
  var virX = 0, virY = 0, cibleX = 0, cibleY = 0;
  var tracer;

  function dessiner(avance) {
    ctx.clearRect(0, 0, larg, haut);

    // Les tranches de profondeur, de la plus lointaine à la plus proche.
    var paniers = [];
    for (var k = 0; k < TRANCHES; k++) paniers.push({ cyan: null, bleu: null });

    for (var i = 0; i < anneaux.length; i++) {
      var an = anneaux[i];
      var ouvert = avance;                       // 0 à 1 pendant l'assemblage
      var vu = {
        r: an.r * (0.84 + 0.16 * ouvert),
        ax: an.ax * ouvert,
        ay: an.ay,
        phase: an.phase
      };

      var prec = projeter(0, vu, lacet, virY);
      for (var s = 1; s <= SEGMENTS; s++) {
        var t = (s / SEGMENTS) * Math.PI * 2;
        var pt = projeter(t, vu, lacet, virY);
        var zm = (prec.z + pt.z) / 2;
        var k2 = Math.min(TRANCHES - 1, Math.max(0, Math.floor(((zm + 1) / 2) * TRANCHES)));
        var cle = an.col === CYAN ? "cyan" : "bleu";
        var p = paniers[k2][cle];
        if (!p) { p = paniers[k2][cle] = { chemin: new Path2D(), ep: an.ep }; }
        p.chemin.moveTo(prec.x, prec.y);
        p.chemin.lineTo(pt.x, pt.y);
        prec = pt;
      }

      // Les graduations gravées sur l'anneau principal.
      if (an.ticks) {
        for (var g = 0; g < 48; g++) {
          var tg = (g / 48) * Math.PI * 2;
          var longue = g % 4 === 0;
          var a1 = projeter(tg, vu, lacet, virY);
          var dedans = { r: vu.r * (longue ? 0.935 : 0.962), ax: vu.ax, ay: vu.ay, phase: vu.phase };
          var a2 = projeter(tg, dedans, lacet, virY);
          var kt = Math.min(TRANCHES - 1, Math.max(0, Math.floor(((a1.z + 1) / 2) * TRANCHES)));
          var pt2 = paniers[kt].cyan;
          if (!pt2) { pt2 = paniers[kt].cyan = { chemin: new Path2D(), ep: 1 }; }
          pt2.chemin.moveTo(a1.x, a1.y);
          pt2.chemin.lineTo(a2.x, a2.y);
        }
      }
    }

    ctx.lineCap = "round";
    for (var k3 = 0; k3 < TRANCHES; k3++) {
      var prof = k3 / (TRANCHES - 1);          // 0 au fond, 1 devant
      var alpha = (0.26 + 0.74 * prof) * avance;   // relevé pour le fond clair
      ["cyan", "bleu"].forEach(function (cle) {
        var p = paniers[k3][cle];
        if (!p) return;
        ctx.strokeStyle = "rgba(" + (cle === "cyan" ? CYAN : BLEU) + ", " + alpha.toFixed(3) + ")";
        ctx.lineWidth = p.ep * (0.6 + 0.4 * prof);
        ctx.stroke(p.chemin);
      });
    }

    // Le noyau.
    var rn = rayon * 0.085 * avance;
    ctx.beginPath();
    ctx.arc(cx, cy, rn, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(" + CYAN + ", " + (0.9 * avance).toFixed(3) + ")";
    ctx.fill();

  }

  function boucle(temps) {
    if (depart === null) depart = temps;
    var ecoule = temps - depart;

    // Assemblage : les anneaux basculent vers leur inclinaison en 1,4 s.
    var brut = Math.min(1, ecoule / 1400);
    var avance = 1 - Math.pow(1 - brut, 3);

    lacet = ecoule / 1000 * 0.16;
    for (var i = 0; i < anneaux.length; i++) {
      anneaux[i].phase = ecoule / 1000 * anneaux[i].vit;
    }

    dessiner(avance);
    tracer = requestAnimationFrame(boucle);
  }

  function poseFixe() {
    for (var i = 0; i < anneaux.length; i++) anneaux[i].phase = i * 0.7;
    lacet = 0.4;
    dessiner(1);
  }

  mesurer();

  if (sobre) {
    poseFixe();
  } else {
    tracer = requestAnimationFrame(boucle);

    /* L'instrument tourne seul et ne réagit pas au pointeur. L'élément
       qu'on manipule, c'est le mot d'accueil, plus haut. */

    // Rien ne tourne quand l'onglet est caché ou l'instrument hors cadre.
    var actif = true;
    var relancer = function () {
      if (actif && !tracer) { depart = performance.now() - 1400; tracer = requestAnimationFrame(boucle); }
    };
    var suspendre = function () {
      if (tracer) { cancelAnimationFrame(tracer); tracer = null; }
    };
    document.addEventListener("visibilitychange", function () {
      document.hidden ? suspendre() : relancer();
    });
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (entrees) {
        actif = entrees[0].isIntersecting;
        actif ? relancer() : suspendre();
      }, { threshold: 0 }).observe(hote);
    }
  }

  var minuteur;
  window.addEventListener("resize", function () {
    clearTimeout(minuteur);
    minuteur = setTimeout(function () {
      mesurer();
      if (sobre) poseFixe();
    }, 150);
  });
})();
