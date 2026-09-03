# Bible — *La Graine Étoilée*

> Document de référence du roman. Tout ce qui est écrit ici fait foi pour la rédaction des
> chapitres, la relecture, l'illustration et les données du jeu. En cas de conflit avec un
> document plus ancien de `inspirations/worldbuilding/`, **la bible l'emporte** ; les raccords
> sont notés dans `structure/arc_1_eveil_de_la_graine.md`.

## Le roman en trois lignes
Luna Thornwick, sept ans, se réveille dans un champ de blé qui brille, dans un monde où personne ne
mange : depuis cinq cents ans, la Guilde des Mages nourrit Aethermoor de potions et interdit la
cuisine. Avec une elfe exilée et un garçon qui cherche sa mère, elle ouvre un étal, puis une
auberge, puis va chercher les cinq Parts d'une Recette gardée par cinq royaumes. À la fin, elle
sert une bouillie de blé à l'homme qui a tout interdit — et il a faim.

## Plan du dossier

```
bible/
├── README.md                          ← ce fichier
├── structure/                         ← LE SQUELETTE : 6 arcs, 60 chapitres
│   ├── arcs.md                        ← vue d'ensemble, table des 60 chapitres, courbes longues
│   ├── arc_1_eveil_de_la_graine.md    ← ch. 1-10  (fin d'été → équinoxe d'automne)
│   ├── arc_2_les_racines.md           ← ch. 11-20 (automne)
│   ├── arc_3_l_eveil.md               ← ch. 21-30 (hiver → équinoxe de printemps)
│   ├── arc_4_les_cinq_royaumes.md     ← ch. 31-40 (printemps → été)
│   ├── arc_5_la_revelation.md         ← ch. 41-50 (été)
│   └── arc_6_l_avenir.md              ← ch. 51-60 (fin d'été → un an après)
├── monde/                             ← LA BIBLE DU MONDE
│   ├── regions.md                     ← les 5 royaumes + le royaume disparu + espaces sans royaume
│   ├── lieux.md                       ← ~40 lieux, par royaume, avec chapitres
│   ├── organisations.md               ← Guilde, Lignées, cuistots, conseils, cour, la Table
│   ├── societe.md                     ← lois (Code de la Magie), rituels, économie, langue
│   ├── histoire.md                    ← chronologie : Semeurs, Famine, Interdiction, l'année du roman
│   └── magie.md                       ← le système culinaire consolidé (fait foi)
├── personnages/                       ← LES FICHES
│   ├── index.md                       ← cast complet + secondaires en une ligne
│   ├── luna_thornwick.md … (9 fiches complètes)
│   └── gorm_braise_vive.md … (8 fiches moyennes)
└── taxonomies/                        ← LES CATALOGUES (IDs stables pour le jeu)
    ├── ingredients.md                 ← ING-xxx : ~55 ingrédients, 5 Éléments, auras, rareté
    ├── recettes.md                    ← REC-xxx : ~60 recettes, 4 tiers, familles d'effet
    └── items.md                       ← ARM/VET/POT/UST/ART/DOC/DIV-xxx : ~90 objets
```

## Comment s'en servir

| Je veux… | J'ouvre… |
|---|---|
| écrire un chapitre | `structure/arc_N_*.md` à la bonne entrée, puis les fiches des personnages présents et `monde/lieux.md` |
| vérifier une règle de magie | `monde/magie.md` (fait foi) |
| savoir qui sait quoi et quand | `structure/arcs.md` §6 (courbes longues) et `monde/histoire.md` §6 |
| inventer un ingrédient / une recette / un objet | la section « Règles d'écriture » en fin de chaque taxonomie |
| préparer des données de jeu | les IDs des taxonomies (ING-, REC-, ARM-…) ; chaque entrée donne son chapitre d'apparition |
| préparer un prompt d'illustration | `monde/lieux.md` (lieux ★), `personnages/*.md` §Apparence, notes visuelles des squelettes existants |

## Conventions
- **Langue** : français. Noms propres invariants.
- **Numérotation** : chapitres 1-60 ; les fichiers existants `inspirations/worldbuilding/chapter_1..5*` restent la source pour les ch. 1-5, avec les raccords notés dans l'arc I. Le ch. 5 est **adapté** (voir `structure/arcs.md` §7).
- **Dates** : années de la Guilde (AG) ; le roman se déroule de 500 à 501 AG.
- **Statuts** dans les tables : ✅ rédigé · 📐 squelette existant · 🔁 squelette adapté · 🆕 nouveau.
- **Chaque chapitre** a : lieu, saison, personnages, ingrédient/recette, objet, résumé, 3-5 scènes clés, évolution, hook.

## Ce qui a été décidé en construisant la bible (et qu'on ne rediscute pas sans raison)
1. Le **Royaume d'Argent** du ch. 5 n'est pas un sixième royaume vivant : c'est le royaume **disparu** des cuisiniers-du-froid. Il fournit le liant (Larmes de Crépuscule) et la Carte, pas une Part.
2. La **Recette Ultime** devient la **Recette des Cinq Saveurs** : cinq Parts, une par royaume, une par Lignée, une par Élément Saveur. Feu = Cendre, Air = Or, Terre = Ambre, Eau = Émeraude, Bois = Azur.
3. La mère de Kael, **Maëlle**, est la **Sentinelle Septième** présente dès le ch. 1 (masque « 7 »). Le village lui a dit qu'elle était « malade » ; elle a été arrêtée.
4. Le fondateur de la Guilde est **Ezren Thornwick**, ancêtre de Luna. Il a raison sur la Famine. Il a tort sur la suite. Sa défaite est une cuillère.
5. Luna ne rentre pas sur Terre. Marinette a ouvert le portail elle-même. La graine est plantée au ch. 60.
6. Pas de bataille au climax : un **service** de sept cents couverts.
