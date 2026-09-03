# Taxonomie — Structures et lieux

> Typologie exhaustive de **ce qui est bâti, poussé ou creusé** dans Aethermoor. Identifiants
> **STR-xxx** stables, réutilisables dans les données de jeu (`resources/`), les prompts
> d'illustration et les fiches de lieux.
>
> Un **lieu** est une occurrence (le Four Ancestral). Une **structure** est un type dont il peut
> exister zéro, une ou trois cents occurrences (le four communautaire). Ce fichier classe les
> **types** ; `bible/monde/lieux.md` décrit les **occurrences**.

---

## 1. Axes de classification

### 1.1 Les huit familles
| Code | Famille | Question à laquelle la structure répond | Matériau dominant |
|---|---|---|---|
| **CTRL** | Contrôle | qui obéit ? | verre et cristal |
| **MEM** | Mémoire | qu'a-t-on gardé ? | pierre, bois vivant, glace |
| **NOUR** | Nourriture | qui mange, et avec qui ? | bronze, brique, lave |
| **PASS** | Passage | qui entre, qui sort ? | roche taillée, racine, eau |
| **HAB** | Habitation | comment vit ce peuple ? | selon le peuple |
| **ASSEM** | Assemblée | qui décide ? | le siège du pouvoir local |
| **PROD** | Production | d'où vient ce qu'on boit ? | verre soufflé, sel, sève |
| **EFF** | Effacement | où va ce qu'on retire ? | verre opaque, mana clair |

### 1.2 Régime d'accès (six degrés)
| Degré | Nom | Comment on entre |
|---|---|---|
| A1 | **Ouvert** | on entre. Personne ne demande rien. |
| A2 | **Coutumier** | il faut être du lieu, ou accompagné de quelqu'un du lieu |
| A3 | **Jetonné** | il faut un objet administratif : jeton, passe, sceau |
| A4 | **Lignagé** | il faut le sang ou la marque d'une Lignée |
| A5 | **Éprouvé** | il faut ressentir quelque chose de vrai (les portes de la Chambre) |
| A6 | **Interdit** | la structure elle-même refuse : empreinte de main, sceau à deux mains, refus du Levain |

### 1.3 Ce que chaque structure cache
Règle d'écriture d'Aethermoor : **toute structure cache quelque chose de la même nature qu'elle**.
Un four cache du feu. Une archive cache un oubli. Une fabrique de fioles cache une recette. Un
conseil cache un vote. Si une structure ne cache rien, elle n'est pas encore écrite.

### 1.4 Échelle de rareté
| Rang | Occurrences dans le monde |
|---|---|
| ★ | des centaines à des milliers |
| ★★ | quelques dizaines |
| ★★★ | une par royaume, ou moins de dix |
| ★★★★ | une seule au monde |

---

## 2. CTRL — Structures de contrôle

| ID | Structure | Rareté | Royaume | Matériaux | Accès | Fonction | Ce qu'elle cache | Ch. |
|---|---|---|---|---|---|---|---|---|
| STR-001 | **La Tour de Verre** | ★★★★ | Or (Aurelis) | pierre dorée gainée de verre ; pas d'escalier, un ascenseur de mana | A6 | siège du Conseil des Cinq ; demeure de l'Archimage | qu'il n'y a qu'un homme en haut, et qu'il a faim | 28, 49, 50 |
| STR-002 | **La Forteresse de Verre** | ★★★ | Or, et une par capitale de région | galeries de verre, cour d'honneur en granit, cellules transparentes | A3 | caserne des Sentinelles ; centre de relève | qu'on n'y forme pas des soldats : on y en fabrique | 40, 44-47 |
| STR-003 | **La Mairie** | ★ | partout où il y a un village sédentaire | bois et pierre du pays, un fronton, un tampon | A1 (salle) / A3 (cellier) | distribution des fioles, registre, police locale | le cellier aux fioles, et le registre des consommations nominatives | 1, 7, 8, 9 |
| STR-004 | **Le Poste de Relève** | ★ | tous les royaumes, tous les vingt milles sur les grandes routes | quatre murs, un toit, un râtelier à bâtons | A3 | relais des patrouilles de Sentinelles | un lit et une table : les Sentinelles s'y assoient, et parfois elles restent assises trop longtemps | 31, 56 |
| STR-005 | **Le Bureau de Commandement** | ★★ | un par région | bureau, encrier, coffre, une carte au mur | A3 | commandement régional | dans le tiroir de Virelle : une pancarte calcinée et une baie de givre | 28, 51 (par le pli) |
| STR-006 | **L'Avenue de Défilé** | ★★ | capitales | dalles de verre coulé, gouttières à mana clair diffusé | A1 | montrer la force ; parfumer le vide | que les riverains, à force, ne sentent plus rien du tout | 39, 40 |
| STR-007 | **Le Cercle de Purification** | ★★ | mobile : là où le Conseil l'ordonne | rien. On le trace à la chaux sur le sol du village | A6 | périmètre d'une purge : on brûle ce qui est dedans | qu'il n'a jamais été tracé dans la Vallée de Cendre, et que personne à Aurelis ne sait pourquoi | mention 17, 30 |

### Détail — STR-001, la Tour de Verre
**Élévation** : onze étages visibles, aucun escalier. L'ascenseur de mana est une plaque de verre
qui monte dans une gaine ; il ne monte que pour ceux qu'Ezren appelle, et il redescend seul.
**Étages** : 1 à 4, administration (six cents commis) ; 5 à 8, les cinq bureaux du Conseil et leurs
antichambres ; 9, la salle du Conseil, cinq sièges et un écran de verre dépoli ; 10, vide, entretenu,
jamais utilisé — personne ne sait pourquoi ; 11, la salle d'Ezren : blanche, sans odeur, une table.
**Sous-sol** : le Dépôt (voir `bible/monde/archives.md`).
**Mise en scène** : filmer toujours de bas en haut, sauf au ch. 49 où on filme de haut en bas, une
seule fois, quand Luna voit la ville à travers le corps d'un homme.

### Détail — STR-002, la Forteresse de Verre
**Plan** : un carré de deux cents pas de côté. Cour d'honneur (granit, seul sol opaque du bâtiment).
Quatre galeries de verre sur trois niveaux : on voit tout, on est vu de partout, il n'y a pas d'angle
mort et c'est le principe. Aile nord : cellules. Aile est : **Salle des Masques** (voir STR-060).
Aile ouest : forge de fioles, réfectoire sans nourriture, magasin d'uniformes. Sous-sol : **Serre
Noire** (STR-030), et un escalier de service non porté sur les plans, qui rejoint le Dépôt.
**Détail qui compte** : les cellules sont en verre et les Sentinelles y dorment **debout**. Un
prisonnier ordinaire y devient fou en trois jours ; Kael y tient quatre jours parce qu'il a passé sa
vie à être regardé sans être vu.

---

## 3. MEM — Structures de mémoire

| ID | Structure | Rareté | Royaume | Matériaux | Accès | Fonction | Ce qu'elle cache | Ch. |
|---|---|---|---|---|---|---|---|---|
| STR-010 | **Le Four Ancestral** | ★★★★ | Vallée de Cendre | pierre noire monolithe, gravures au ciseau | A2 puis A4 | foyer commun des cinq Lignées ; il allumait les fours du monde | sous la crasse, l'histoire entière, et un nom effacé au burin dont il reste un T | 2, 13, 57-59 |
| STR-011 | **Le Dépôt** (les Archives) | ★★★★ | Or | pierre, casiers de laiton, ardoise, mana clair | A1 → A6 par niveau | tout garder et que personne ne lise | sept niveaux, et au fond un cahier d'écolier | 28, 48 ; détail dans `archives.md` |
| STR-012 | **Les Racines-Mémoire** | ★★★★ | Émeraude (Sylvanthe) | arbres-mères vivants, écorce lisse à hauteur de paume | A2 | conserver ce que les elfes refusent d'oublier | ce que le Conseil a **voté** de ne pas y mettre | 24 |
| STR-013 | **La Chambre des Saveurs Perdues** | ★★★★ | Argent | glace claire, vitraux, un foyer central | A5 | enseigner à **lier** les cinq saveurs | trente-huit tabliers, trente-huit noms brodés, lisibles | 5 |
| STR-014 | **La Statue du Cuisinier Inconnu** | ★★ (il en restait des centaines ; il en reste une) | toutes ; détruites | pierre, mains ouvertes, visage lisse | A5 | recevoir une offrande qui n'a rien à voir avec la cuisine | qu'elle indique l'est et qu'elle sent l'ouest | 5 |
| STR-015 | **Le Puits-à-Pain** | ★★★★ | Ambre (Sept Puits) | cave de pierre rose, une jarre, du sable frais | A4 | nourrir le Levain-Mère sans jamais le cuire | qu'il a refusé des rois, et Ezren | 32, 33 |
| STR-016 | **Les Caves Givrées** | ★★★★ | Azur (Roc-de-Sel) | sel gelé, sept niveaux, un par siècle | A2 → A4 | affiner ; c'est-à-dire attendre | au septième niveau, une seule meule et cent quarante ans de patience | 35, 36 |
| STR-017 | **Le Jardin Scellé** | ★★★★ | Émeraude | mur de ronces vivantes, sceau à deux empreintes | A6 | protéger la Part d'Eau ; et enfermer une faute | qu'Aelis ne l'a pas subi : elle l'a fermé de l'intérieur | 22, 23 |
| STR-018 | **La Ruche de Verre** | ★★★★ | Or (Jardins Impériaux) | verre soufflé, abeilles translucides | A4 | produire un miel qu'on n'a pas récolté depuis 500 ans | qu'on s'en sert comme encre pour les décrets qui l'interdisent | 39 |
| STR-019 | **Le Cercle des Sept Socles** | ★★★★ | Vallée de Cendre | sept socles de pierre creusés par l'usage | A1 | recevoir les sept marmites des Lignées | qu'il y a sept socles et cinq Lignées | 2, 26, 57 |
| STR-020 | **Le Compte des Comptes** | ★★★★ | Ambre (Conseil des Caravanes) | sept bâtons de bois entaillés | A2 | tenir la généalogie des porteurs de croûte | cent soixante-douze entailles : sept lignées de bouche | — |
| STR-021 | **Le Placard du Fond** | ★ | partout sur la côte d'Ambre | une planche, un torchon, une consigne | A2 | garder un objet dont on ne sait plus l'usage | une cuillère, et l'ordre de ne pas la perdre | 4, 7 |

### Détail — STR-021, le Placard du Fond
La structure la plus répandue et la moins visible du monde. Ce n'est pas un meuble : c'est un
**comportement bâti**. Dans chaque village de la côte d'Ambre, une famille au moins a, quelque part,
un objet enveloppé de toile, et une phrase transmise avec : *ne le perds pas*. Ni l'objet ni la
phrase n'ont d'explication.
**Occurrences relevées** : chez Mira à Cendre-Basse (une cuillère), chez Ouma à Brièves-Îles (la
cuillère de Taïs, et le tablier de Maëlle), dans dix-neuf autres maisons que Luna ne visitera jamais.
**Usage narratif** : c'est le rappel grave du roman (voir `tensions_et_rappels.md` §R7). Ne jamais
l'expliquer par un personnage. Le lecteur comprend seul, vers le ch. 7, et c'est plus fort.

---

## 4. NOUR — Structures de nourriture

| ID | Structure | Rareté | Royaume | Matériaux | Accès | Fonction | Ce qu'elle cache | Ch. |
|---|---|---|---|---|---|---|---|---|
| STR-040 | **Le Four communautaire** | ★★ (ruines) | partout ; toutes détruites sauf deux | brique réfractaire, voûte, cheminée trapue | A1 | cuire pour vingt familles à la fois | qu'il reste chaud cinq cents ans après | 4 |
| STR-041 | **L'Étal** | ★ (un, puis des dizaines) | Vallée de Cendre, puis partout | une planche, deux pierres, une pancarte | A1 | servir à manger à qui passe | rien. C'est la seule structure du monde qui ne cache rien, et c'est sa force | 10 |
| STR-042 | **L'Auberge aux Sept Marmites** | ★★★★ | Vallée de Cendre | pierre de lave, charpente d'Émeraude, four mi-tandoor mi-four à pain | A1 | nourrir ; et donner une adresse à la cuisine | sous la grande table, le sceptre en os de dragon d'un ancien maire, devenu tisonnier | 26-30, 51-60 |
| STR-043 | **Le Lit de Sable** | ★★ | Ambre | du sable, des braises, douze heures | A2 | le meilleur four du monde, et le monde l'a oublié | qu'il ne demande aucune construction : seulement de savoir | 6, 33 |
| STR-044 | **L'École des Marmites** | ★★★★ | Vallée de Cendre | l'auberge, plus un préau | A1 | apprendre à cuisiner à des enfants de cinq royaumes | que le maître a neuf ans et onze lettres | 60 |
| STR-045 | **La Forge à Marmites** | ★★ | Vallée de Cendre (Bivouac) | soufflet, enclume, creuset, deux cents marmites suspendues | A2 | forger ce qu'on n'utilisera pas | qu'on les fait pour se souvenir qu'on en faisait | 10-18 |
| STR-046 | **Le Feu qui ne cuit rien** | ★ | Ambre, toutes les caravanes | un feu. Rien dessus | A2 | se réunir sans manger | vingt-deux chiffons, vingt-deux croûtes, et un rituel qui a sauvé un savoir | 6 |
| STR-047 | **Le Réchaud à algue** | ★ | côtes d'Ambre | un pot de fonte, de l'algue-lanterne | A1 | voir la nuit en mer. Pas cuire. | qu'on peut cuire dessus, et que personne n'avait essayé | 9 |
| STR-048 | **Le Grenier à sacs** | ★ | Vallée de Cendre, côte d'Ambre | bois, torchis, une porte qu'on ne ferme pas | A2 | garder des sacs de grain qu'on n'ouvre jamais | que les grands-parents en mettaient de côté sans savoir pourquoi | 4 |

### Détail — STR-041, l'Étal
**Composition canonique** : une planche de bois de tente ; deux pierres de lave ; une pancarte de
bois avec des fautes. Rien d'autre n'est nécessaire et rien d'autre n'est autorisé : dès qu'un étal
a un toit, ce n'est plus un étal, c'est une auberge, et il devient attaquable.
**Régime juridique** : l'étal n'existe pas dans le Code de la Magie. Il n'y a pas d'article pour lui.
C'est ce qui permet à Corvus, au ch. 30, de plaider l'article 22 : une anomalie **non classée**.
**Occurrences** : un seul au ch. 10 (La Graine Étoilée). Trois au ch. 27. Onze au ch. 51. Ne pas
compter au-delà : à partir de l'arc VI, l'étal est un fait de société, pas un décor.

---

## 5. PASS — Structures de passage

| ID | Structure | Rareté | Royaume | Matériaux | Accès | Fonction | Ce qu'elle cache | Ch. |
|---|---|---|---|---|---|---|---|---|
| STR-050 | **Le Portail-Graine** | ★★★★ (quarante mille fiches, un seul germé) | hors monde | une graine, un porteur, une intention | A6 | relier deux mondes | qu'il ne s'ouvre que dans un sens sans un Thornwick des deux côtés | 1, 47, 53, 60 |
| STR-051 | **La Porte des Racines** | ★★★ | Émeraude | deux arbres tressés, deux gardes de trois siècles | A2 | filtrer qui entre en Confédération | qu'elle n'a pas de serrure : les arbres décident | 19 |
| STR-052 | **Le Col** | ★★ | tous les royaumes | roche, neige, vent | A1 | passer, ou ne pas passer | qu'un col se tient avec quarante chaudrons de fumée douce aussi bien qu'avec trois cents hommes | 17, 30, 54-56 |
| STR-053 | **Les Marches d'Argent** | ★★★★ | Argent | deux cents marches taillées, une rampe brisée | A1 | monter vers un royaume qui n'existe pas | qu'elles existent, et que personne n'a le droit de dire qui les a faites | 5 |
| STR-054 | **Le Tunnel de Racines** | ★★★★ | Champ de Blé Étoffé | racines vivantes, lumière, chaleur | A4 | fuir en une seconde sur trente lieues | que le Champ décide de la sortie, pas le voyageur | 1, 2 |
| STR-055 | **La Jetée** | ★ | côtes | pierre sèche, anneaux de fer | A1 | embarquer | qu'elle a exactement la longueur qu'il faut pour qu'une mère et un fils se regardent trop longtemps | 9 |
| STR-056 | **La Piste bornée** | ★ | Ambre | cailloux tassés, bornes de pierre rose creusées au sommet | A1 | traverser le désert en trouvant l'eau de pluie | que les bornes sont un alphabet, et que les caravaniers le lisent | 6, 31 |
| STR-057 | **La Faille de Verre** | ★★★★ | Marches Grises | sable vitrifié sur trois lieues, arêtes coupantes | A6 | rien. C'est une cicatrice | l'endroit exact où un portail-graine a été **éteint de force** en l'an 9 | nouveau |

### Détail — STR-050, le Portail-Graine
**Conditions d'ouverture** : une graine germée ; un porteur de Lignée ; une intention nette ; et de
l'autre côté, quelque chose qui appelle. Marinette a ouvert le portail de Halifax **seule**, en
sachant qu'elle n'en reviendrait pas : sans porteur de l'autre côté, le passage se referme sur celui
qui l'ouvre.
**Durée** : quelques secondes. Le portail du ch. 60, dans le blé, s'ouvre trois secondes et se
referme sur un refus poli.
**État du parc** : quarante mille fiches en Salle des Portes. *Éteint* pour trente-six mille.
*Dormant* pour trois mille neuf cents. *Perdu* pour cent. *Germé* : un.

---

## 6. EFF — Structures d'effacement

| ID | Structure | Rareté | Royaume | Matériaux | Accès | Fonction | Ce qu'elle cache | Ch. |
|---|---|---|---|---|---|---|---|---|
| STR-060 | **La Salle des Masques** | ★★★ | une par Forteresse | verre, un fauteuil, un râtelier de fioles vides, un four à recuire les masques | A3 | vider un cuisinier et le remplir de mana clair | que le mot officiel est *soulagement*, et qu'il n'est pas ironique : ceux qui l'ont écrit y croyaient | 46 |
| STR-061 | **La Serre Noire** | ★★★★ | Or | verre opaque noir, gouttières à mana clair, rangées de terre stérile | A3 | faire pousser des graines confiscables sans qu'elles germent | quarante mille graines qui ont faim depuis cinq siècles | 47 |
| STR-062 | **Le Cellier aux Fioles** | ★ | chaque mairie | terre battue, rayonnages, quatre cents fioles par trimestre | A3 | stocker la distribution | qu'elles s'éteignent autour d'une enfant de sept ans, et que personne ne sait pourquoi | 8 |
| STR-063 | **Les Relevés de Mémoire** (niveau -2) | ★★★★ | Or | rotonde de six étages, casiers de laiton, deux millions de fioles étiquetées | A3 | conserver ce qu'on a retiré aux gens | qu'on peut le **rendre** | `archives.md` |
| STR-064 | **Le Village Numéroté** | ★★ | Marches Grises | maisons identiques, une plaque, un chiffre | A1 | loger les soulagés qui n'ont pas pu devenir Sentinelles | qu'ils sont douze mille, qu'ils sont doux, et qu'ils ne se souviennent pas d'avoir demandé à être là | nouveau |

### Détail — STR-060, la Salle des Masques
**Protocole**, tel qu'il est affiché au mur en douze points, dans une police soignée :
1. le sujet s'assied ; 2. on ôte les objets personnels et on les remet à la famille ; 3. on souffle
les souvenirs dans les fioles, par années, en commençant par la plus récente ; 4. on étiquette ;
5. on remplit de mana clair jusqu'à ce que le sujet cesse de répondre à son nom ; 6. on donne un
numéro ; 7 à 11, entretien du masque ; 12. *« On remercie le sujet. »*
Le point 12 est la chose la plus glaçante de la Guilde, et il est appliqué à la lettre : chaque
opérateur dit merci à quelqu'un qui n'est plus personne.
**Faille** : le protocole ne prévoit rien pour l'**odorat**. On n'a jamais pensé à le retirer, parce
qu'il n'y avait plus rien à sentir dans le monde. C'est par là que tout revient (ch. 46, 56, 58).

---

## 7. PROD — Structures de production

| ID | Structure | Rareté | Royaume | Matériaux | Accès | Fonction | Ce qu'elle cache | Ch. |
|---|---|---|---|---|---|---|---|---|
| STR-070 | **La Fabrique de Fioles** | ★★ | Or (Bas-Quartiers), une par grande ville | fours à verre, cuves, canne de souffleur, cheminées basses | A2 | produire les fioles et le mana qu'elles portent | la recette du mana clair, que seuls les souffleurs connaissent | 41 |
| STR-071 | **La Saline de Roc** | ★★ | Azur | galeries de sel gelé, wagonnets, cristaux d'éclairage | A2 | extraire le sel et le cristal, seule exportation naine | que le sel gris fumé est un ingrédient, pas un minerai | 34, 35 |
| STR-072 | **L'Arbre-Mère** | ★★ | Émeraude | un arbre de soixante mètres, une écorce à boire | A2 | nourrir les elfes en sève | qu'on peut lui **demander** autre chose, et qu'il répond | 21 |
| STR-073 | **Le Puits d'Ombre** | ★ | Ambre (sept par oasis majeure) | margelle de pierre rose, poulie, ombre tournante | A2 | l'eau, et le calendrier : les tentes suivent l'ombre | que le septième puits n'a pas d'eau et sert d'autre chose | 32 |
| STR-074 | **Le Champ de Blé Étoffé** | ★★★★ | se déplace | du blé, un ciel d'opale à lui | A4 | pousser, suivre, attendre | qu'il n'est pas un lieu mais un **être**, et qu'il veut être mangé | 1, 52, 53, 60 |

### Détail — STR-070, la Fabrique de Fioles
**Chaîne** : four à verre (1400°) → canne → soufflage → recuit → remplissage → scellement à la cire
→ caisse de cinquante. Un atelier moyen sort huit mille unités par jour.
**Le point de bascule** : le remplissage. Le mana synthétique arrive par conduite depuis la Tour ;
le **mana clair**, lui, est composé sur place, et sa formule est un tour de main transmis de
souffleur en souffleur, jamais écrit. Douze personnes au monde savent la faire.
**Conséquence** : les Bas-Quartiers d'Aurelis ne sont pas un faubourg pauvre. C'est le point le plus
fragile de la Guilde. Douze personnes qui croisent les bras arrêtent la mémoire-effaçante.
**Enjeu ouvert (arc V-VI)** : Dora et le vieux Selm en connaissent trois. Le Syndicat des Souffleurs
peut être convaincu par un repas, et cela vaut trois cents Sentinelles.

---

## 8. ASSEM — Structures d'assemblée

| ID | Structure | Rareté | Royaume | Forme du siège | Accès | Comment on décide | Ce qu'elle cache | Ch. |
|---|---|---|---|---|---|---|---|---|
| STR-080 | **La salle du Conseil des Cinq** | ★★★★ | Or | cinq fauteuils et un écran de verre dépoli | A3 | à la majorité, sauf si l'écran parle | que l'écran ne parle qu'une fois par siècle, et qu'alors la majorité ne compte plus | 28, 30 |
| STR-081 | **Le Conseil des Racines** | ★★★★ | Émeraude | sept sièges de racines dans un arbre creux | A2 | par vote, et le vote est enraciné — ou non | les votes non enracinés, dont la purge de 419 | 20, 22 |
| STR-082 | **Le Cercle des Selles** | ★★★★ | Ambre | sept selles en cercle qui tournent avec le soleil | A2 | à voix haute, et Zahra a voix prépondérante sur le Levain | qu'ils ont dit non à un roi, et qu'ils le rediront | 32, 33 |
| STR-083 | **Le Doyenné** | ★★★ | Azur | une table, deux bancs, pas de siège pour le Doyen | A2 | le travail parle ; celui qui a la plus grosse forge tranche | qu'une lamelle de fromage peut faire basculer un peuple | 34, 36 |
| STR-084 | **La Grande Table** | ★★★★ | Vallée de Cendre | une table. Des chaises. Une place au bout | A1 | on mange, puis on parle | qu'il n'y a pas de règlement, seulement une ligne : *personne ne mange seul* | 59, 60 |

---

## 9. HAB — Habitation, par peuple

| ID | Peuple | Structure type | Matériaux | Particularité qui compte |
|---|---|---|---|---|
| STR-090 | Humains côtiers (Ambre) | maison basse à mur mitoyen | bois, pierre, toit de roseau | **aucune cuisine**. Un âtre reconverti en rangement à cordages |
| STR-091 | Nomades (Ambre) | tente à quatre pans, déplacée deux fois par jour | toile ocre, piquets de fer | on suspend la croûte au montant nord, à hauteur de bouche d'enfant |
| STR-092 | Nains-brumiers (Azur) | logement creusé, sept par galerie | sel gelé taillé, cristaux d'éclairage | pas de fenêtre, pas de cheminée, jamais de feu à l'intérieur |
| STR-093 | Elfes-sylvains (Émeraude) | maison **poussée**, jamais taillée | arbre vivant guidé sur soixante ans | on demande à la maison avant d'ajouter une pièce ; elle peut refuser |
| STR-094 | Nobles d'Or | hôtel à cour, vitrines à fioles | pierre dorée, verre, marbre | la vitrine à fioles est le meuble de prestige : on y expose ce qu'on boit |
| STR-095 | Ouvriers d'Or (Bas-Quartiers) | logement d'atelier, une pièce, une lucarne | brique, verre de rebut | la lucarne donne sur la Forteresse. Toutes. C'est un choix d'urbanisme |
| STR-096 | Cuistots ambulants (Cendre) | abri de lave à trois niveaux, passerelles | lave taillée, cuir, tuyaux de terre cuite | des grappes de marmites suspendues partout, propres, inutilisées |
| STR-097 | Soulagés (Marches Grises) | maison identique à la voisine, une plaque, un chiffre | torchis gris, ardoise | douze mille maisons rigoureusement semblables, et personne ne se plaint |

---

## 10. Grille vierge pour créer une structure

À remplir avant d'écrire une scène dans un lieu nouveau. Si une ligne reste vide, le lieu n'est pas prêt.

```
ID            : STR-xxx
Nom           :
Famille       : CTRL / MEM / NOUR / PASS / HAB / ASSEM / PROD / EFF
Rareté        : ★ à ★★★★  (combien y en a-t-il dans le monde ?)
Royaume       :
Matériaux     : (trois maximum ; le troisième doit surprendre)
Dimensions    : (à hauteur d'enfant de sept ans : que voit Luna en entrant ?)
Accès         : A1 à A6, et QUI exactement possède le droit
Fonction      : en une phrase, au présent
Ce qu'elle cache : de même nature qu'elle (règle §1.3)
Odeur         : obligatoire. Même « rien » est une réponse, et c'est la plus grave.
Son           : que fait le lieu quand personne ne parle ?
Ce qui s'y perd : toute structure prend quelque chose à qui y entre
Occurrences   : où ailleurs dans le monde ?
Chapitres     :
Note de mise en scène : un plan, une lumière, un détail à ne pas oublier
```

---

## 11. Index croisé lieu → structure

| Lieu (occurrence) | Structures qui le composent |
|---|---|
| Brièves-Îles | STR-003 mairie, STR-062 cellier, STR-021 placard, STR-055 jetée, STR-090 maisons, STR-048 grenier |
| Aurelis | STR-001 Tour, STR-002 Forteresse, STR-011 Dépôt, STR-060 Salle des Masques, STR-061 Serre Noire, STR-070 fabriques, STR-018 Ruche, STR-006 avenue, STR-094 et STR-095 habitat |
| Vallée de Cendre | STR-010 Four Ancestral, STR-019 sept socles, STR-042 auberge, STR-041 étal, STR-045 forge, STR-044 école, STR-096 abris, STR-052 col |
| Sylvanthe | STR-012 Racines-Mémoire, STR-017 Jardin Scellé, STR-081 Conseil, STR-072 arbres-mères, STR-093 maisons, STR-051 Porte des Racines |
| Sept Puits | STR-015 Puits-à-Pain, STR-073 puits d'ombre, STR-082 cercle des selles, STR-091 tentes, STR-043 lit de sable, STR-020 Compte des Comptes |
| Roc-de-Sel | STR-016 Caves Givrées, STR-071 saline, STR-083 doyenné, STR-092 logements |
| Royaume d'Argent | STR-013 Chambre, STR-014 statue, STR-053 marches |
| Marches Grises | STR-064 villages numérotés, STR-057 Faille de Verre, STR-097 habitat, STR-004 postes de relève |
