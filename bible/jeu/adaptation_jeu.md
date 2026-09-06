# Adaptation en jeu — correspondance bible ↔ *luna-mobile*

> Le roman a un jeu : **`Kenhuri69/luna-mobile`**, RPG culinaire rétro (Android, Kotlin/Compose).
> Ce document est la **table de correspondance** entre les identifiants de la bible et ceux du
> jeu. Il est la contrepartie de `luna-mobile/docs/skeleton/`, où vit le plan d'intégration.
>
> Règle : **la bible fait foi**. Un ingrédient sans `ING-xxx` n'a rien à faire dans les données du
> jeu — on l'ajoute d'abord à `taxonomies/ingredients.md`.

---

## 1. Où en est le jeu

| | Bible | Jeu (`main`, arcs I + II livrés) |
|---|---|---|
| Chapitres | 60 (6 arcs) | 10 |
| Arcs couverts | I → VI | I compressé + II complet |
| Personnages jouables | 17 fiches | 4 (Luna, Sylvie, Kael, Pim) |
| Ingrédients | ~55 | 23 |
| Recettes | ~60 | 14 |
| Cartes | ~40 lieux, 5 royaumes | 6 zones |

Les neuf lots du plan d'intégration de l'arc II sont fusionnés dans `main` (PR #14 à #21 du jeu).
Ce qui suit décrit donc du code qui tourne, pas une intention.

**Règle de conversion** : *deux chapitres de roman = un chapitre de jeu*.

| Arc | Roman | Jeu |
|---|---|---|
| I — L'Éveil de la Graine | 1-10 | 1-5 ✅ |
| II — Les Racines | 11-20 | 6-10 📐 squelette |
| III — L'Éveil | 21-30 | 11-15 |
| IV — Les Cinq Royaumes | 31-40 | 16-20 |
| V — La Révélation | 41-50 | 21-25 |
| VI — L'Avenir | 51-60 | 26-30 |

## 2. Ingrédients

### 2.1 Présents dans le jeu, arc I
| ID bible | Nom | ID jeu | Note d'adaptation |
|---|---|---|---|
| ING-001 | Blé Étoffé | `ble_etoffe` | `STELLAIRE` en jeu, Feu dans la bible — les deux sont vrais : Feu est sa **saveur**, Stellaire dit que son champ n'est dans aucun des cinq royaumes. Voir `ingredients.md` §1.1. |
| ING-010 | Tubercule de Foyer | `patate_brase` | — |
| ING-012 | Racines de Rêve | `racines_reve` | Était Bois en jeu ; **corrigé en Eau**, la bible faisait foi. |
| ING-030 | Sel de roche | `sel_roche` | — |
| ING-034 | Éclat de Soufre | `eclat_soufre` | — |
| ING-071 | Eau de Lune | `eau_lune` | Eau/Froid dans la bible ; le jeu doit choisir, il prend Eau. Sans conséquence. |
| ING-073 | Larmes de Crépuscule | `larmes_crepuscule` | Était Eau en jeu ; **corrigé en `STELLAIRE`** — c'est le liant, le seul ingrédient que la bible met explicitement dans le sixième élément. |
| ING-044 | Baies Stellaires | `baie_stellaire` | Inventé par le jeu, **entré dans la bible**. Air, Forêt des Murmures : distinct des Baies de Givre (ING-040), qui sont Eau et pardonnent. |
| ING-025 | Menthe Sauvage | `menthe_sauvage` | Inventé par le jeu, **entré dans la bible**. |
| ING-038 | Poivre-Foudre | `poivre_foudre` | Inventé par le jeu, **entré dans la bible**. Distinct de ING-035 Poivre-Soleil. |
| ING-045 | Cristal de Sucre Stellaire | `cristal_sucre` | Inventé par le jeu, **entré dans la bible**. Hors-royaume comme tout ce que la graine a touché ; distinct de ING-043 Sucre d'Or. |
| ING-063 | Poisson Argenté | `poisson_argente` | Inventé par le jeu, **entré dans la bible**. Distinct de ING-062 Poisson-Lanterne. |

### 2.2 Ajoutés par le squelette de l'arc II
| ID bible | Nom | ID jeu | Chapitre jeu |
|---|---|---|---|
| ING-005 | Mousse de Sève | `mousse_seve` | 10 |
| ING-011 | Racine-Lune | `racine_lune` | 8 |
| ING-013 | Lait de Racine | `lait_racine` | 6 |
| ING-014 | Champignon de Cendre | `champignon_cendre` | 6 |
| ING-020 | Sauge Ardente | `sauge_ardente` | 7 |
| ING-021 | Fougère Chantante | `fougere_chantante` | 10 |
| ING-022 | Herbes de rive | `herbes_rive` | 10 |
| ING-037 | Cendre Douce | `cendre_douce` | 7 |
| ING-062 | Poisson-Lanterne | `poisson_lanterne` | 10 |
| ING-080 | Tissu de Souvenir | `tissu_souvenir` | 8 |
| ING-090 | Cendre-mana | `cendre_mana` | 9 |

## 3. Personnages

| Personnage | Fiche | Rôle en jeu | Depuis |
|---|---|---|---|
| Luna Thornwick | [luna_thornwick.md](../personnages/luna_thornwick.md) | héroïne, soigneuse, **toujours** en équipe | ch. 1 |
| Sylvie Lysdorn | [sylvie_lysdorn.md](../personnages/sylvie_lysdorn.md) | dégâts, debuff | ch. 1 |
| Kael Morrow | [kael_morrow.md](../personnages/kael_morrow.md) | tank, garde | ch. 1 |
| **Pim Ferrel** | [pim_ferrel.md](../personnages/pim_ferrel.md) | **soutien rapide et fragile** | ch. 7 📐 |
| **Gorm Braise-Vive** | [gorm_braise_vive.md](../personnages/gorm_braise_vive.md) | **PNJ : forge du Bivouac** | ch. 6 📐 |
| Maire Corvus | [corvus.md](../personnages/corvus.md) | boss ch. 1 | ch. 1 |
| Commandant Virelle | [virelle.md](../personnages/virelle.md) | boss ch. 4 et ch. 9 | ch. 4 |
| Orrin | [orrin_gardien_de_glace.md](../personnages/orrin_gardien_de_glace.md) | boss ch. 5 (« Gardien de Glace ») | ch. 5 |
| Ysolde Lysdorn | [ysolde_lysdorn.md](../personnages/ysolde_lysdorn.md) | mentionnée en fin d'arc II ; jouable arc III | ch. 10 📐 |

Les secondaires nommés de la Vallée (Hesse, Old Tam, Fenna, les jumeaux Brasque, Mira, Josse)
deviennent les **clients de l'étal** : c'est ce qui leur donne une existence jouable sans écrire
un système de PNJ. Leurs souvenirs de repli sont écrits dans le code du jeu et doivent rester
cohérents avec `personnages/index.md`.

## 4. Ce que le jeu chiffre

Un jeu doit trancher là où un roman peut rester qualitatif : « la graine est gelée » doit
devenir un nombre, ou rien ne se code. Voici les chiffres que le jeu a posés, et la phrase de la
bible dont chacun descend. **Aucun ne contredit `monde/magie.md` ; si la bible chiffre un jour
ces règles autrement, c'est la bible qui gagne et le jeu qui s'aligne.**

### 4.1 L'Intention (`IntentionRules`)

| Chiffre du jeu | Valeur | D'où ça vient |
|---|---|---|
| Jauge | 0 à 100, départ à 80 | Règle 1 du Triptyque : l'état du cuisinier *est* la magie |
| Sereine / Troublée / En colère / Gelée | ≥ 70 · ≥ 40 · ≥ 1 · 0 | les quatre pulsations de la graine, `magie.md` §3 |
| Une cendre-mana | −100 : la graine gèle d'un coup | ch. 17 : le gel est complet, pas graduel |
| Bouillon Blanc | +35, seule recette autorisée gelée | ch. 18 : « la recette de rien » redémarre la graine |
| Risque de cendre-mana en colère | (35 % + 1 point par point sous 40) × la difficulté, **plafonné à 75 %** | rien dans la bible ; le plafond est un garde-fou de jeu — sans lui, en difficulté Maître, le risque atteignait 100 % et le joueur n'avait plus un pari mais une sanction |
| Toux d'équipe | 3 tours, +25 % de dégâts subis | ch. 17-18 : « ceux qui l'ont respirée toussent des jours » |
| Graine gelée | le plat nourrit, ne porte aucun effet | `magie.md` §3, précisé pour le jeu puis réécrit dans la bible |

### 4.2 L'Étal (`StallRules`)

| Chiffre du jeu | Valeur | D'où ça vient |
|---|---|---|
| Besoins des clients | six ; le plus proche de la faim s'appelle « le ventre vide » | personne à Aethermoor n'a le mot ; ils ont froid, ils ont perdu quelqu'un, ils se méfient |
| Monnaie | paillettes d'or **ou** souvenir raconté | ch. 11 : Sylvie remplace la fiole vide par un souvenir |
| Majorité des clients | sans or : ils paient en souvenir | prémisse de l'étal, pas un détail d'équilibrage |
| Une journée parfaite | rapporte moins que le meilleur butin de l'arc | servir ne doit jamais être plus rentable qu'avancer |
| File d'attente | déterministe, liée au jour et à la tuile | anti-relance : on ne retire pas un client en quittant l'écran |
| Carnet des souvenirs | persisté, relisible hors ligne | DOC-003, le carnet de Kael, est un objet consultable |

### 4.3 Les combats qui ne se gagnent pas

`magie.md` §7 est catégorique : la cuisine **ne gagne pas une bataille**. Le jeu a donc un
objectif de combat qui n'est pas « vaincre » mais « tenir N rounds », et dans ce mode
l'adversaire ne peut pas tomber — il plie le genou et se relève.

| Scène | Rounds | Ce qui suit, et qui est écrit |
|---|---|---|
| Le raid du col (roman ch. 17) | 6 | l'étal brûle, les cuistots filent dans les tunnels |
| La Porte des Racines (roman ch. 19) | 4 | Sylvie est arrêtée, les trois autres sont « invités » |

Ni l'un ni l'autre ne rend d'or ni de butin : on ne détrousse pas Virelle, et on ne détrousse pas
un garde qui vous arrête.

### 4.4 Les deux améliorations forgées par Gorm

| Amélioration | Effet en jeu | Objet de la bible |
|---|---|---|
| Marmite de Bronze | chaque plat réussi rend une portion de plus | **UST-001** — « la première marmite *utilisée* » ; une portion de plus, c'est une personne de plus à table, donc la Règle 3 |
| Grande Cuillère de Bronze | la fenêtre de rythme s'élargit de 40 % | **UST-018** — lourde, elle porte le geste d'une enfant de sept ans qui s'épuise (`magie.md` §3, « Ce que Luna n'a pas ») |

L'amélioration de rythme s'est appelée « Touillette de Bronze » jusqu'à cette relecture. C'était
une erreur : la Touillette (UST-003) est l'épée de Kael. Corrigé des deux côtés — UST-018 est
entré dans la bible, le jeu affiche le bon nom (l'identifiant stocké reste `bronze_ladle`, il est
dans les sauvegardes).

## 5. Divergences : ce qui est tranché, ce qui reste

Six points ont été ouverts ici. Cinq sont clos ; le sixième est une note de vigilance, pas une
question.

1. ~~**L'élément « Stellaire »** existe dans le jeu et pas dans la bible.~~ **Tranché.** La bible
   avait déjà un sixième élément — le *Froid*, liant, Royaume d'Argent — et le jeu l'appelle
   `STELLAIRE`. Même case, deux noms, aucun des deux ne bouge : les deux tiennent à trop de
   choses ailleurs. Ce qui manquait n'était pas un arbitrage de nom, c'était la **règle** :
   `ingredients.md` §1.1 la porte désormais — le sixième est le **hors-royaume**, et il n'est
   *jamais* une Part. C'était le vrai risque de l'arc IV, et il est fermé.
2. ~~**Cinq ingrédients inventés par le jeu** n'ont pas d'`ING-xxx`.~~ **Tranché : ils en ont
   un.** ING-025 Menthe Sauvage, ING-038 Poivre-Foudre, ING-044 Baies Stellaires, ING-045 Cristal
   de Sucre Stellaire, ING-063 Poisson Argenté. Ils sont dans des sauvegardes de joueurs : les
   fondre dans une entrée voisine aurait cassé des sacs. Leur colonne « Ch. » porte
   **« — (jeu) »** : disponibles pour le roman, pas encore employés par lui.
3. ~~**Quelques éléments divergent** (Racines de Rêve : Eau vs Bois).~~ **Tranché côté jeu**, dans
   les deux sens : les Racines de Rêve repassent en Eau, et les Larmes de Crépuscule quittent
   l'Eau pour le sixième élément. Un test (`ProgressionAndDataTest`) empêche le jeu d'y revenir.
   Reste l'Eau de Lune, Eau/Froid dans la bible : le jeu n'a qu'une case par ingrédient, il prend
   Eau, et l'élément d'un ingrédient n'a aucun effet mécanique — c'est celui de la *recette* qui
   brise les boucliers.
4. ~~**Le chapitre 5 du jeu** se présente comme une conclusion~~ — réglé : l'arc II livré en fait
   une charnière.
5. **Le jeu invente des effets d'objets** que la bible ne chiffre pas (les deux améliorations de
   Gorm, §4.4). Ils sont cohérents avec les fiches, mais ils ne viennent pas du roman : à relire
   si un chapitre fait un jour dépendre une scène de ce que fait un ustensile. *Note de
   vigilance, pas une question ouverte.*
6. ~~**Tarel se battait** au chapitre 10 du jeu~~ — corrigé côté jeu (§4.3) : la Porte se tient,
   elle ne se gagne pas. C'est le jeu qui avait tort.

### 5.1 Ce que le jeu n'empruntera pas au roman

**La *Tisane d'Écoute* (REC-035) reste au chapitre 22.** Le squelette proposait de l'avancer de
douze chapitres pour donner au joueur un plat de Bois offensif contre Tarel. Ce besoin n'existe
plus : la Porte des Racines ne se gagne pas, donc il n'y a plus de bouclier à percer là. Et la
Tisane paie une scène précise — le Vieil Arbre-Cuisinier ne parle qu'à ceux qui l'ont bue. La
dépenser dans l'arc II pour une raison mécanique qui a disparu coûterait un moment du roman
contre rien.

## 6. Où lire la suite

- Plan d'intégration complet, ordonné, avec risques : `luna-mobile/docs/skeleton/README.md`
- Revue technique du jeu : `luna-mobile/REVIEW.md`
- Squelette de l'arc II côté roman : [`../structure/arc_2_les_racines.md`](../structure/arc_2_les_racines.md)
