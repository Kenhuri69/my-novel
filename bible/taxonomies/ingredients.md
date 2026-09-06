# Taxonomie — Ingrédients

> Classification et catalogue des ingrédients d'Aethermoor. Identifiants **ING-xxx** stables, à
> réutiliser dans les recettes, les scripts et les données de jeu (`resources/`).
> Champs : Élément Saveur · Aura · Rareté · Royaume · Récolte · Effet brut · Chapitre.
> Un chapitre noté **« — (jeu) »** signale un ingrédient qui existe dans `luna-mobile` et que le
> roman n'a pas encore utilisé : il est disponible, pas obsolète.

## 1. Axes de classification

### 1.1 Élément Saveur (le « quoi »)
| Élément | Saveur | Royaume | Couleur de vapeur | Ce qu'il apporte au plat |
|---|---|---|---|---|
| **Feu** | Épicé | Vallée de Cendre | rouge | chaleur, courage, cuisson |
| **Air** | Sucré | Empire d'Or | blanc | légèreté, joie, audace |
| **Terre** | Salé | Territoires d'Ambre | brun | ancrage, temps, mains nombreuses |
| **Eau** | Acide | Confédération d'Émeraude | bleu | vivacité, vérité, larmes |
| **Bois** | Gras | Royaume d'Azur | or | patience, profondeur, mémoire longue |
| *(Froid)* | — (liant) | Royaume d'Argent | argent | lie les cinq ; conserve ; attend |

Les cinq premiers sont les **Saveurs**, une par royaume, une par Part. Le sixième n'en est pas
une : c'est le **hors-royaume**, ce qui ne pousse dans aucun des cinq. Il couvre trois choses —
le liant (Larmes de Crépuscule, ING-073), les **matières à mémoire** de §2.9, qui n'ont pas
d'élément du tout, et ce qui est venu **par une graine** (le Blé Étoffé, dont le champ est de
l'autre côté d'un portail).

> **Règle dure : le hors-royaume n'est jamais une Part.** Les cinq Parts sont gardées par cinq
> Lignées dans cinq royaumes ; un ingrédient qui n'appartient à aucun ne peut donc en être une,
> quelle que soit sa rareté. Le Blé Étoffé est ★★★ et central, il n'est pas une Part.

Le jeu (`luna-mobile`) nomme ce sixième élément **`STELLAIRE`** et le peint en doré, là où le
roman dit *Froid* et le peint en argent. Les deux noms désignent la même case, et aucun des deux
ne bougera : « Froid » tient au Royaume d'Argent, à la Chambre des Saveurs Perdues et au Gardien
de Glace ; « Stellaire » tient à ce que le jeu range dedans en premier, le Blé Étoffé. La
correspondance est tenue dans [`../jeu/adaptation_jeu.md`](../jeu/adaptation_jeu.md).

### 1.2 Aura (ce que Luna voit)
| Aura | État | Usage |
|---|---|---|
| Bleu / froid | affamé, sec, vidé | à réveiller (eau, chaleur douce) ou à jeter |
| Vert / pulsé | frais, sain | réconfort immédiat, quotidien |
| Doré / étoilé | ancestral ou sauvage | mémoire ; effets profonds ; coût en fatigue |
| Blanc | cinq siècles de patience | les Parts ; « pas de couleur pour ça » |
| Gris | corrompu (cendre-mana) | danger |

### 1.3 Rareté
| Rang | Nom | Où | Exemple |
|---|---|---|---|
| ★ | **Commun** | partout, avec un peu d'attention | sel de roche, algue séchée |
| ★★ | **Sauvage** | il faut *demander* | Racine-Lune, Lait de Racine |
| ★★★ | **Ancestral** | gardé ou oublié depuis des générations | Blé Étoffé, Tubercule de Foyer, Croûte de Givre |
| ★★★★ | **Légendaire** | une Part, ou un ingrédient qui n'existe qu'une fois | Levain-Mère, Larmes de Crépuscule |

### 1.4 Mode de récolte
- **Cueillette douce** : on demande ; la réponse peut être non (Fougère Chantante).
- **Méthode douce** : s'agenouiller, chanter, écouter, laisser venir (Tubercule de Foyer).
- **Don** : l'ingrédient se donne à une personne, à des mains, à une décision (les Parts).
- **Troc / achat** : sel des nains, farine des caravanes.
- **Interdit** : la force. Elle produit cendre toxique (Tubercule), refus (Levain), flétrissement.

## 2. Catalogue

### 2.1 Céréales, farines, levains
| ID | Nom | Élément | Aura | Rareté | Royaume | Récolte | Effet brut | Ch. |
|---|---|---|---|---|---|---|---|---|
| ING-001 | **Blé Étoffé** | Feu (origine Terre) | doré | ★★★ | Champ de Blé Étoffé | moisson ; les épis se penchent | nostalgie, sécurité ; base de la Bouillie | 1, 53 |
| ING-002 | Farine de pierre | Terre | vert | ★ | Ambre | mouture des caravanes | tient, sèche, garde | 6, 26 |
| ING-003 | **Levain-Mère** — *Part de Terre* | Terre | blanc | ★★★★ | Puits-à-Pain | don à deux cents mains ; à nourrir chaque jour | vivant ; refuse ceux qui prennent ; fait lever tout ce qu'il touche | 32-33 |
| ING-004 | Pain de pierre (croûte rituelle) | Terre | bleu → vert (trempé) | ★★ | Ambre | héritage ; se suce, ne se mord pas | redevient pain dans l'eau tiède | 6, 32 |
| ING-005 | Mousse de Sève | Eau | vert | ★★ | Émeraude (écorce) | cueillette douce | mâchable ; première mastication des elfes | 21 |

### 2.2 Racines, tubercules, champignons
| ID | Nom | Élément | Aura | Rareté | Royaume | Récolte | Effet brut | Ch. |
|---|---|---|---|---|---|---|---|---|
| ING-010 | **Tubercule de Foyer** (« Patate-Brase ») | Feu | rouge-orangé | ★★★ | Vallée de Cendre | **méthode douce** (comptine) ; par la force → cendre toxique | courage de l'âtre ; résistance au froid ; révèle des souvenirs | 1, 2, 15, 17 |
| ING-011 | Racine-Lune | Terre/Eau | doré pâle | ★★ | Forêt des Murmures | cueillette douce, de nuit | patience, calme ; invisibilité brève aux Sentinelles | (cadre) |
| ING-012 | **Racines de Rêve** | Eau | translucide ; goût métallique dans l'air | ★★★ | Forêt des Murmures (lisière) | délicat ; **surdose = coma sensoriel** | infusion : souvenirs refoulés, visions | 3, 16, 19 |
| ING-013 | Lait de Racine | Bois | vert pulsé | ★★ | Vallée de Cendre (sous la cendre) | Luna « écoute », Sylvie creuse | apaisant ; nourrit les nourrissons | 12 |
| ING-014 | Champignon de Cendre | Feu | orange | ★★ | Vallée de Cendre | cueillette après pluie chaude | umami de braise ; base de la Soupe du Premier Soir | 10 |
| ING-015 | Champignon de Mine | Bois | gris-vert | ★★ | Azur (galeries) | troc avec les mineurs | terreux, profond | 35 |
| ING-016 | Racines de caniveau | Terre | bleu → vert | ★ | Aurelis, Bas-Quartiers | ce qu'il y a | survie ; Soupe des Bas-Quartiers | 41 |

### 2.3 Herbes, feuilles, fleurs
| ID | Nom | Élément | Aura | Rareté | Royaume | Récolte | Effet brut | Ch. |
|---|---|---|---|---|---|---|---|---|
| ING-020 | Sauge Ardente | Feu | rouge | ★★ | Vallée de Cendre | cueillette | réchauffe ; Ragoût de Braises | 2 |
| ING-021 | **Fougère Chantante** | Eau | doré, *chante* | ★★★ | Émeraude | cueillette douce ; **peut refuser** ; donne une fronde | écoute ; Tisane d'Écoute (parler aux Gardiens) | 19, 22 |
| ING-022 | Herbes de rive (sept sortes) | Eau | vert | ★★ | rives de l'Ylle | demandées une à une | vivacité ; Court-Bouillon, Infusion de Forêt Secrète | 20, 24, 54 |
| ING-023 | **Thé d'Aurore** | Air | doré clair | ★★★ | Jardins Impériaux | volé par Théo ; puis offert | chaleur douce, joie ; première boisson chaude d'Aurelis | 37 |
| ING-024 | Fleur de Verre | Air | blanc-rosé | ★★ | Jardins Impériaux | cueillette | parfum ; décor du Gâteau de Miel | 43 |
| ING-025 | Menthe Sauvage | Bois | vert, *froisse sous les doigts* | ★ | lisières de la Vallée de Cendre | cueillette | dénoue ; ce qu'on ajoute quand quelqu'un serre les mâchoires sans savoir pourquoi | — (jeu) |

### 2.4 Épices, sels, minéraux
| ID | Nom | Élément | Aura | Rareté | Royaume | Récolte | Effet brut | Ch. |
|---|---|---|---|---|---|---|---|---|
| ING-030 | Sel de roche | Terre | vert | ★ | partout | ramassage | assaisonne ; « la recette de rien » | 1, 18 |
| ING-031 | Sel des Dunes (rose) | Terre | rose-doré | ★★ | Ambre | troc caravanes | garde la chaleur ; Pain de Pierre | 6, 32 |
| ING-032 | Sel de Roc (gris fumé) | Bois | gris-or | ★★ | Azur | troc nains | profondeur ; fromages | 34 |
| ING-033 | Sel de fiole | Terre | bleu | ★ | Aurelis | résidu des ateliers | amer ; dernier recours | 41 |
| ING-034 | **Éclat de Soufre** (pierre à feu) | Feu | rouge orangé, « presque vivant » | ★★★ | Forêt des Murmures (fissures), Vallée | ramassage dans les fissures | + eau → brouillard réconfortant ; brûlé → **Fumée Douce** (dissipe le silence, fait hésiter les Sentinelles) | 3, 44, 56 |
| ING-035 | **Poivre-Soleil** | Air/Feu | doré vif | ★★★ | Empire d'Or | vendu comme parfum | seul « goût » toléré à Aurelis ; Soupe Dorée | 38 |
| ING-036 | Piment-Braise | Feu | rouge | ★★ | Vallée de Cendre | cueillette | pique ; réveille | 60 |
| ING-037 | Cendre Douce | Feu | gris clair (non corrompu) | ★★ | Four Ancestral + Eau de Lune | mélange de Gorm | révèle les gravures ; soigne les brûlures | 13, 14 |
| ING-038 | **Poivre-Foudre** | Air | violet, *zigzague* | ★★ | crêtes de la Vallée de Cendre | ramassage après l'orage, quand les grains crépitent encore | réveille net ; distinct du Poivre-Soleil (ING-035), qui parfume au lieu de piquer | — (jeu) |

### 2.5 Fruits, baies, douceurs
| ID | Nom | Élément | Aura | Rareté | Royaume | Récolte | Effet brut | Ch. |
|---|---|---|---|---|---|---|---|---|
| ING-040 | **Baies de Givre** | Eau | bleu-argent | ★★ | lisière du Champ, côte d'Ambre | cueillette | culpabilité résolue, pardon ; **larme de cristal** ; « goût de neige » | 7, 9, 31, 58 |
| ING-041 | Datte de Verre | Terre/Air | ambre translucide | ★★ | Ambre | palmiers des oasis | sucre du désert ; Galette de Route, Confiture de Braise | 6, 27 |
| ING-042 | **Miel des Abeilles de Verre** — *Part d'Air* | Air | blanc | ★★★★ | Ruche de Verre, Aurelis | ouverture par un Aurelian, devant témoin | jamais récolté depuis 500 ans (servait d'encre) ; audace, douceur | 39, 43 |
| ING-043 | Sucre d'Or | Air | doré | ★★ | toits d'Aurelis (rosée cristallisée) | ramassage à l'aube | douceur légère | 43 |
| ING-044 | **Baies Stellaires** | Air | cyan étincelant, *murmure* | ★★★ | Forêt des Murmures | cueillette de nuit, **en silence** : elles se taisent si on parle | la joie légère qui revient sans prévenir ; à ne pas confondre avec les Baies de Givre (ING-040), qui pardonnent | — (jeu) |
| ING-045 | Cristal de Sucre Stellaire | *(Froid)* | doré étoilé, *carillonne* | ★★★ | ruines de Halifax, là où la graine a germé | ramassage à l'aube dans les gravats | douceur constellée ; hors-royaume, comme tout ce que la graine a touché | — (jeu) |

### 2.6 Laits, fromages, gras
| ID | Nom | Élément | Aura | Rareté | Royaume | Récolte | Effet brut | Ch. |
|---|---|---|---|---|---|---|---|---|
| ING-050 | Lait de Brume | Bois | blanc-vert, *fume au froid* | ★★ | Azur (chèvres-des-brumes) | traite | frais, sans mémoire ; Fromage Blanc du Col | 34 |
| ING-051 | Croûte de Givre | Bois | doré profond | ★★★ | Caves Givrées (niveaux 1-6) | prélèvement (Brune enrage) | deux siècles fondus ; chaleur profonde | 35 |
| ING-052 | **Cœur de Meule** — *Part de Bois* | Bois | **blanc** | ★★★★ | septième niveau | décision partagée ; une lamelle chacun | cinq siècles de patience ; indescriptible | 36, 39 |

### 2.7 Poissons, produits de mer
| ID | Nom | Élément | Aura | Rareté | Royaume | Récolte | Effet brut | Ch. |
|---|---|---|---|---|---|---|---|---|
| ING-060 | Algue-Lanterne | Eau | vert lumineux | ★★ | mer d'Ambre | pêche de nuit ; brûle en réchaud | chaleur, orientation (la vapeur montre la côte) | 8, 9 |
| ING-061 | Algue séchée | Eau | bleu → vert | ★ | Brièves-Îles | greniers | sel marin ; Soupe de Bord de Mer | 8 |
| ING-062 | **Poisson-Lanterne** | Eau | doré, *lumineux* | ★★★ | rivière Ylle | pêche en demandant ; sa lumière passe dans le bouillon | mémoire des sœurs ; Court-Bouillon | 20, 54 |
| ING-063 | Poisson Argenté | Eau | argenté, reflets de lune | ★ | étangs de la Vallée de Cendre | pêche ordinaire — le seul poisson qu'on prend sans demander | nourrit, et ne raconte rien : c'est l'ordinaire dont Sylvie connaît les coins | — (jeu) |

### 2.8 Eaux et liquides
| ID | Nom | Élément | Aura | Rareté | Royaume | Récolte | Effet brut | Ch. |
|---|---|---|---|---|---|---|---|---|
| ING-070 | Eau pure | — | vert | ★ | partout | — | base | — |
| ING-071 | **Eau de Lune** | Eau/Froid | argent | ★★★ | source de la Forêt des Murmures | puisée la nuit | dilue la magie crue ; réactive la graine sans fatigue ; Cendre Douce | 3, 13 |
| ING-072 | Eau de l'Ylle (source) | Eau | doré | ★★★ | Jardin Scellé | — | le premier *goût* d'Émeraude | 23 |
| ING-073 | **Larmes de Crépuscule** | Froid (liant) | argenté clair, vaporeux | ★★★★ | Chambre des Saveurs Perdues, à l'équinoxe | libérées par un plat commun | lient les saveurs ; révèlent les souvenirs des autres ; dessinent la Carte | 5, 30, 58 |
| ING-074 | **Larme de Sève** — *Part d'Eau* | Eau | doré → sève → lumière | ★★★★ | source de l'Ylle | une larme de Lysdorn « pour la bonne raison » | vérité, pardon ; la plus dorée des auras | 23 |
| ING-075 | Sève d'arbre-mère | Eau | vert | ★ | Émeraude | bue à l'écorce | nourrit les elfes ; sans envie | 21 |

### 2.9 Matières à mémoire (non comestibles, mais entrent dans les recettes)
| ID | Nom | Élément | Aura | Rareté | Où | Effet brut | Ch. |
|---|---|---|---|---|---|---|---|
| ING-080 | **Tissu de Souvenir** (le tablier de Maëlle) | — | rose pâle, doux | ★★★ | au cou de Kael (ch. 1-5 : le carré) ; porté par lui (ch. 7+ : le tablier entier, rendu par Ouma) | au fond du panier : plat qui évoque l'enfance ; réveille une mémoire partagée. Le carré part à la statue au ch. 5 ; le tablier entier arrive au ch. 7 | 4, 5, 7, 9, 16, 45, 46 |
| ING-081 | Fibre de Graine d'Origine | — | doré éteint | ★★★★ | Serre Noire | remplace une corde de luth ; réveille un Gardien | 47 |
| ING-082 | **Graine d'Or Noire** | Feu | violet profond → **Braise Première** | ★★★★ | ruines de Halifax | brûlée : *Part de Feu* ; « une seule peut exister pleinement » | 4, 57 |

### 2.10 Poisons et corruptions
| ID | Nom | Aura | Origine | Effet | Ch. |
|---|---|---|---|---|---|
| ING-090 | **Cendre-mana** | gris | cuisiner sous la colère / la haine | fumée toxique ; fait tousser ; rend malade deux semaines ; gèle la graine | 17-18 |
| ING-091 | Cendre toxique du Tubercule | noir | creuser par la force | explosion, nuage irritant (comique quand raté par les Brasque) | 2, 15 |
| ING-092 | Mana clair | bleu vide | Guilde | vide les souvenirs ; à ne jamais mettre dans un plat | voir `items.md` |

## 3. Les cinq Parts (récapitulatif)
| Part | ID | Élément | Obtenue par | Ch. |
|---|---|---|---|---|
| Part d'Eau | ING-074 Larme de Sève | Eau | une larme donnée pour la bonne raison | 23 |
| Part de Terre | ING-003 Levain-Mère | Terre | deux cents mains | 33 |
| Part de Bois | ING-052 Cœur de Meule | Bois | une décision prise ensemble | 36 |
| Part d'Air | ING-042 Miel de Verre | Air | un acte d'audace devant témoin | 39 |
| Part de Feu | ING-082 → Braise Première | Feu | un sacrifice | 57 |
| Liant | ING-073 Larmes de Crépuscule | Froid | un plat commun de trois souvenirs | 5 |

## 4. Règles d'écriture pour inventer un ingrédient
1. Il a poussé, coulé ou vieilli quelque part : nommer le royaume.
2. Il a une aura, donc un état émotionnel : il veut quelque chose.
3. Il a une manière de se récolter, et une manière de se refuser.
4. Son effet est **émotionnel**, jamais statistique.
5. Il a un nom en deux mots maximum, concret, souvent oxymore (Lait de Brume, Datte de Verre, Sel des Dunes).
