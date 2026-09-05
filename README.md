# My Novel — Original Story Project

Original fiction project built as a visual novel / interactive story.
Inspired by the narrative depth and world-building approach of works like
*Beginning After The End*, but with an entirely original story, characters,
and setting.

## Stack technique

| Couche | Technologie |
|---|---|
| Moteur | Godot 4.x (cible à définir) |
| Langage | GDScript (scènes, logique narrative) + C# (outils, tests) |
| Dialogues | Format `.dtl` (timelines) + `.yaml` (nœuds de dialogue) |
| Persistance | FileAccess + JSON (natif Godot 4) |
| Localisation | JSON tables (FR/EN) |
| Tests | xUnit 2.x (pure .NET, sans runtime Godot) |
| CI/CD | GitHub Actions |

## Structure du projet

```
src/
  core/           ← événements, gestionnaire de jeu, audio, sauvegarde
  domain/         ← personnages, magie, combat, chapitres, monde
  systems/        ← combat, quêtes, progression
  infrastructure/ ← DTO de persistance
  ui/             ← HUD, écrans de combat
  utils/          ← extensions, utilitaires
scenes/           ← scènes Godot (.tscn)
dialogues/        ← timelines (.dtl) et nœuds (.yaml)
resources/        ← données JSON (personnages, mondes, chapitres)
localization/     ← tables FR/EN
tools/            ← scripts utilitaires, checks, forge d'assets
tests/            ← xUnit (pure .NET)
```

## Démarrage rapide

1. Installe **Godot 4.x** avec support C#
2. Clone le repo : `git clone <url>`
3. Ouvre le dossier dans Godot Hub
4. Lance depuis la scène principale

## Production en cours

### Bible du roman — `bible/`
La référence complète est dans [`bible/README.md`](bible/README.md) :
- 📚 **Structure** : [6 arcs, 60 chapitres](bible/structure/arcs.md) — squelette détaillé de chaque chapitre (lieu, saison, personnages, recette, scènes clés, évolution, hook) dans `bible/structure/arc_1..6_*.md`
- 🗺️ **Monde** : [régions](bible/monde/regions.md) · [lieux](bible/monde/lieux.md) · [organisations](bible/monde/organisations.md) · [société et lois](bible/monde/societe.md) · [histoire et chronologie](bible/monde/histoire.md) · [système de magie culinaire](bible/monde/magie.md) · [les Archives](bible/monde/archives.md)
- 🏛️ **Archives et escalade** : [`bible/monde/archives.md`](bible/monde/archives.md) — le Dépôt et ses sept niveaux, le coût de lecture, les cinq archives du monde ; l'échelle des enjeux est dans [`bible/structure/arcs.md`](bible/structure/arcs.md) §5 bis
- 🧑‍🍳 **Personnages** : [index du cast](bible/personnages/index.md) — 17 fiches (Luna, Sylvie, Kael, Marinette, Virelle, Corvus, Maëlle, Ezren, Orrin, Gorm, Pim, Idris, Brune, Ysolde, Théo, Nérine, Ouma)
- 🎮 **Adaptation en jeu** : [`bible/jeu/adaptation_jeu.md`](bible/jeu/adaptation_jeu.md) — correspondance bible ↔ *luna-mobile* (chapitres, ingrédients `ING-xxx`, cast, divergences à arbitrer)
- 🥕 **Taxonomies** : [ingrédients](bible/taxonomies/ingredients.md) (ING-xxx) · [recettes](bible/taxonomies/recettes.md) (REC-xxx) · [items : armes, armures, potions, ustensiles, artefacts](bible/taxonomies/items.md) · [structures et lieux](bible/taxonomies/structures.md) (STR-xxx)

### Écriture narrative
- ✍️ **Chapitres 1 à 10 : rédigés en prose** (environ 37 000 mots) — arc I *L'Éveil de la Graine*, complet
- 📐 **Chapitres 11 à 60** : squelettes détaillés dans [`bible/structure/`](bible/structure/)
- 🎭 **Fiches personnages** : 17 fiches dans `bible/personnages/`
- 🧠 **Système de magie culinaire** : consolidé dans [`bible/monde/magie.md`](bible/monde/magie.md) (Triptyque, Synesthésie, Résonance, buffs émotionnels, limites, Graines d'Origine)
- 😄 **Tensions et rappels comiques** : [`bible/structure/tensions_et_rappels.md`](bible/structure/tensions_et_rappels.md) — tension locale par chapitre, gestes qui renforcent les liens, carnet des rappels (l'échelle des câlins, la comptine, « hop », les plans d'évasion de Sylvie…)
- 👁️‍🗨️ **Prompt Gemini** : prêt pour relecture critique et enrichissement

### Le roman — Arc I : L'Éveil de la Graine
| # | Titre | Lieu | Texte |
|---|---|---|---|
| 1 | Éclosion dans le Champ de Blé | Champ de Blé Étoffé, Brièves-Îles | [chapter_1.md](inspirations/worldbuilding/chapter_1.md) |
| 2 | Les Cendres de la Mémoire | Vallée de Cendre, Four Ancestral | [chapter_2.md](inspirations/worldbuilding/chapter_2.md) |
| 3 | Batailles de Braises et de Souvenirs | Forêt des Murmures | [chapter_3.md](inspirations/worldbuilding/chapter_3.md) |
| 4 | Réveil des Cendres | Cendre-Basse, ruines de Halifax-sur-Aethermoor | [chapter_4.md](inspirations/worldbuilding/chapter_4.md) |
| 5 | La Chambre des Saveurs Perdues | Royaume d'Argent | [chapter_5.md](inspirations/worldbuilding/chapter_5.md) |
| 6 | Le Chemin des Caravanes | piste d'Ambre | [chapter_6.md](inspirations/worldbuilding/chapter_6.md) |
| 7 | Le Village qui Rêvait | Brièves-Îles | [chapter_7.md](inspirations/worldbuilding/chapter_7.md) |
| 8 | Le Procès de la Cuillère | Mairie de Brièves-Îles | [chapter_8.md](inspirations/worldbuilding/chapter_8.md) |
| 9 | La Nuit des Potions Éteintes | port de Brièves-Îles, mer d'Ambre | [chapter_9.md](inspirations/worldbuilding/chapter_9.md) |
| 10 | La Graine Étoilée | Bivouac des Braises | [chapter_10.md](inspirations/worldbuilding/chapter_10.md) |

### Documentation liée (historique)
- 📖 [`inspirations/worldbuilding/culinary_fantasy_framework.md`](inspirations/worldbuilding/culinary_fantasy_framework.md) — Cadre narratif initial
- 📋 [`inspirations/worldbuilding/chapter_1_outline.md`](inspirations/worldbuilding/chapter_1_outline.md) — Plan détaillé par scènes
- 🧑‍🍳 [`inspirations/worldbuilding/chapter_1_development.md`](inspirations/worldbuilding/chapter_1_development.md) — Premières fiches personnages et structures sociales
- 💬 [`inspirations/worldbuilding/gemini_prompt.md`](inspirations/worldbuilding/gemini_prompt.md) — Prompt pour Gemini (revue critique + enrichissement)
- 🖼️ [`inspirations/worldbuilding/chapter_1_image_prompt.md`](inspirations/worldbuilding/chapter_1_image_prompt.md) — Prompt d'illustration pour le Chapitre 1
- 🔍 [`inspirations/worldbuilding/character_sheets_all_chapters.md`](inspirations/worldbuilding/character_sheets_all_chapters.md) — Fiches personnages (Chapitres 1-5)
- 📁 [`inspirations/worldbuilding/asset/`](inspirations/worldbuilding/asset/) — Assets visuels (personnages, couvertures)

## Licence

Propriétaire — Tous droits réservés. Histoire originale.
