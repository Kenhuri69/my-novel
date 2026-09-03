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
- 🗺️ **Monde** : [régions](bible/monde/regions.md) · [lieux](bible/monde/lieux.md) · [organisations](bible/monde/organisations.md) · [société et lois](bible/monde/societe.md) · [histoire et chronologie](bible/monde/histoire.md) · [système de magie culinaire](bible/monde/magie.md)
- 🧑‍🍳 **Personnages** : [index du cast](bible/personnages/index.md) — 17 fiches (Luna, Sylvie, Kael, Marinette, Virelle, Corvus, Maëlle, Ezren, Orrin, Gorm, Pim, Idris, Brune, Ysolde, Théo, Nérine, Ouma)
- 🥕 **Taxonomies** : [ingrédients](bible/taxonomies/ingredients.md) (ING-xxx) · [recettes](bible/taxonomies/recettes.md) (REC-xxx) · [items : armes, armures, potions, ustensiles, artefacts](bible/taxonomies/items.md)

### Écriture narrative
- 📝 **Chapitre 1** : rédigé — [`inspirations/worldbuilding/chapter_1.md`](inspirations/worldbuilding/chapter_1.md)
- 📐 **Chapitres 2-5** : squelettes détaillés existants (le ch. 5 est adapté par la bible, voir `bible/structure/arcs.md` §7)
- 🆕 **Chapitres 6-60** : squelettes dans `bible/structure/`
- 🎭 **Fiches personnages** : 17 fiches dans `bible/personnages/` (les anciennes fiches de `inspirations/worldbuilding/` restent en référence historique)
- 🧠 **Système de magie culinaire** : consolidé dans [`bible/monde/magie.md`](bible/monde/magie.md) (Triptyque, Synesthésie, Résonance, buffs émotionnels, limites, Graines d'Origine)
- 👁️‍🗨️ **Prompt Gemini** : prêt pour relecture critique et enrichissement

### Documentation liée (historique)
- 📖 [`inspirations/worldbuilding/culinary_fantasy_framework.md`](inspirations/worldbuilding/culinary_fantasy_framework.md) — Cadre narratif initial
- 📋 [`inspirations/worldbuilding/chapter_1_outline.md`](inspirations/worldbuilding/chapter_1_outline.md) — Plan détaillé par scènes
- 🧑‍🍳 [`inspirations/worldbuilding/chapter_1_development.md`](inspirations/worldbuilding/chapter_1_development.md) — Premières fiches personnages et structures sociales
- 💬 [`inspirations/worldbuilding/gemini_prompt.md`](inspirations/worldbuilding/gemini_prompt.md) — Prompt pour Gemini (revue critique + enrichissement)
- 🖼️ [`inspirations/worldbuilding/chapter_1_image_prompt.md`](inspirations/worldbuilding/chapter_1_image_prompt.md) — Prompt d'illustration pour le Chapitre 1
- 🔍 [`inspirations/worldbuilding/character_sheets_all_chapters.md`](inspirations/worldbuilding/character_sheets_all_chapters.md) — Fiches personnages (Chapitres 1-5)
- 📁 [`inspirations/worldbuilding/asset/`](inspirations/worldbuilding/asset/) — Assets visuels (personnages, couvertures)

### Chapitres 1-5 (fichiers existants)
- 📘 [Chapitre 1 — Éclosion dans le Champ de Blé (Terminé)](inspirations/worldbuilding/chapter_1.md)
- 📘 [Chapitre 2 — Les Cendres de la Mémoire (Squelette)](inspirations/worldbuilding/chapter_2_skeleton.md)
- 📘 [Chapitre 3 — Batailles de Braises et de Souvenirs (Squelette)](inspirations/worldbuilding/chapter_3_skeleton.md)
- 📘 [Chapitre 4 — Réveil des Cendres (Squelette)](inspirations/worldbuilding/chapter_4_skeleton.md)
- 📘 [Chapitre 5 — La Chambre des Saveurs Perdues (Squelette, adapté)](inspirations/worldbuilding/chapter_5_skeleton.md)

## Licence

Propriétaire — Tous droits réservés. Histoire originale.
