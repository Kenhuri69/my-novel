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

## Licence

Propriétaire — Tous droits réservés. Histoire originale.
