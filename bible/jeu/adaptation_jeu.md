# Adaptation en jeu — correspondance bible ↔ *luna-mobile*

> Le roman a un jeu : **`Kenhuri69/luna-mobile`**, RPG culinaire rétro (Android, Kotlin/Compose).
> Ce document est la **table de correspondance** entre les identifiants de la bible et ceux du
> jeu. Il est la contrepartie de `luna-mobile/docs/skeleton/`, où vit le plan d'intégration.
>
> Règle : **la bible fait foi**. Un ingrédient sans `ING-xxx` n'a rien à faire dans les données du
> jeu — on l'ajoute d'abord à `taxonomies/ingredients.md`.

---

## 1. Où en est le jeu

| | Bible | Jeu (`main`) | Jeu (squelette arc II) |
|---|---|---|---|
| Chapitres | 60 (6 arcs) | 5 | 10 |
| Arcs couverts | I → VI | arc I compressé | arcs I + II |
| Personnages jouables | 17 fiches | 3 | 4 (+ Pim Ferrel) |
| Ingrédients | ~55 | 12 | 23 |
| Recettes | ~60 | 8 | 14 |
| Cartes | ~40 lieux, 5 royaumes | 4 zones | 6 zones |

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
| ING-001 | Blé Étoffé | `ble_etoffe` | Élément **Stellaire** en jeu, Feu (origine Terre) dans la bible. Voir §5. |
| ING-010 | Tubercule de Foyer | `patate_brase` | — |
| ING-012 | Racines de Rêve | `racines_reve` | Bois en jeu, Eau dans la bible. |
| ING-030 | Sel de roche | `sel_roche` | — |
| ING-034 | Éclat de Soufre | `eclat_soufre` | — |
| ING-071 | Eau de Lune | `eau_lune` | — |
| ING-073 | Larmes de Crépuscule | `larmes_crepuscule` | — |
| — | Baies Stellaires | `baie_stellaire` | **Inventé par le jeu.** Proche de ING-040 Baies de Givre. À arbitrer. |
| — | Menthe Sauvage | `menthe_sauvage` | **Inventé par le jeu.** Candidat à une entrée ING-0xx. |
| — | Poivre-Foudre | `poivre_foudre` | **Inventé par le jeu.** Distinct de ING-035 Poivre-Soleil. |
| — | Cristal de Sucre Stellaire | `cristal_sucre` | **Inventé par le jeu.** Proche de ING-043 Sucre d'Or. |
| — | Poisson Argenté | `poisson_argente` | **Inventé par le jeu.** Distinct de ING-062 Poisson-Lanterne. |

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

## 4. Ce que le jeu ajoute au roman

Deux mécaniques traduisent directement des scènes du roman, mais elles n'ont pas d'équivalent
« objet » dans la bible. Si le roman revient dessus, c'est ici qu'il faut vérifier la cohérence :

| Mécanique de jeu | Scène source | Ce que le jeu suppose |
|---|---|---|
| **L'Étal et la monnaie des souvenirs** | ch. 11, Sylvie invente la monnaie | Que la réputation du Bivouac se construit assiette par assiette, et que le carnet de Kael est un objet consultable. |
| **L'Intention** (jauge 0-100, cendre-mana, Bouillon Blanc) | ch. 17-18 | Que la cendre-mana **gèle** la graine, que seule « la recette de rien » la dégèle, et que l'état de la graine se lit en permanence. |

Aucune des deux ne contredit `monde/magie.md` ; elles la chiffrent. Si la bible chiffre un jour
ces règles autrement, c'est la bible qui gagne et le jeu qui s'aligne.

## 5. Divergences connues, à arbitrer

1. **L'élément « Stellaire »** existe dans le jeu et pas dans la bible. La bible a cinq Saveurs et
   le **Froid**, qui est un liant. Le jeu utilise `STELLAIRE` là où la bible dirait Froid ou
   « matière à mémoire ». À trancher au plus tard quand les cinq Parts arrivent (arc IV), parce
   que la correspondance Élément ↔ Royaume devient alors structurante.
2. **Cinq ingrédients inventés par le jeu** (§2.1) n'ont pas d'`ING-xxx`. Deux options : leur en
   donner un dans `taxonomies/ingredients.md`, ou les fusionner avec l'entrée bible la plus
   proche. Recommandation : leur donner un ID — ils sont déjà dans des sauvegardes de joueurs.
3. **Quelques éléments divergent** entre bible et jeu (Racines de Rêve : Eau vs Bois). Sans
   conséquence tant que la résonance de combat reste une règle de jeu, à corriger si le roman
   fait un jour dépendre une scène de l'élément d'un ingrédient.
4. **Le chapitre 5 du jeu** se présente comme une conclusion (« La Recette Ultime et les Cinq
   Royaumes ») alors que la bible en fait une charnière. Corrigé par le squelette de l'arc II.

## 6. Où lire la suite

- Plan d'intégration complet, ordonné, avec risques : `luna-mobile/docs/skeleton/README.md`
- Revue technique du jeu : `luna-mobile/REVIEW.md`
- Squelette de l'arc II côté roman : [`../structure/arc_2_les_racines.md`](../structure/arc_2_les_racines.md)
