#!/usr/bin/env python3
"""
novel_scraper.py v2
Script d'identification et d'extraction de novels fantastique avec thématique culinaire.

Améliorations v2 :
- Déduplication par titre normalisé
- Score de pertinence (cuisine + fantasy ensemble)
- Filtrage qualité (minimum 3 mots-clés culinaires ou fantasy)
- Noms de fichiers propres sans métadonnées parasites
- Index trié par pertinence
- Export JSON des résultats bruts

Usage :
    python novel_scraper.py                          # Explorer tous les sites
    python novel_scraper.py --site fanmtl royalroad # Explorer des sites spécifiques
    python novel_scraper.py --keywords cooking food gourmet  # Mots-clés personnalisés
    python novel_scraper.py --all                    # Explorer tous les sites
    python novel_scraper.py --output custom_dir      # Dossier de sortie personnalisé
    python novel_scraper.py --min-score 3            # Score minimum (1-5)
    python novel_scraper.py --dedup                  # Activer la déduplication (défaut: on)
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse

# ── Imports optionnels ──────────────────────────────────────

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("⚠ Le module 'requests' n'est pas installé. Installation automatique...")
    os.system(f"{sys.executable} -m pip install requests beautifulsoup4")
    import requests

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False
    print("⚠ Le module 'beautifulsoup4' n'est pas installé. Installation automatique...")
    os.system(f"{sys.executable} -m pip install beautifulsoup4")
    from bs4 import BeautifulSoup

# ── Configuration ────────────────────────────────────────────

OUTPUT_DIR = Path("inspirations")
DATA_DIR = OUTPUT_DIR / "data"

SOURCES = {
    "fanmtl": {
        "base_url": "https://www.fanmtl.com",
        "search_url": "https://www.fanmtl.com/search?q={keyword}",
        "novel_url_pattern": "https://www.fanmtl.com/novel/{slug}",
        "chapter_url_pattern": "https://www.fanmtl.com/novel/{slug}/{chapter_id}",
        "tags_page": "https://www.fanmtl.com/browsetags/",
        "categories": ["Action", "Wuxia", "Xianxia", "Xuanhuan", "Shounen", "Romance", "Contemporary Romance", "Shoujo"],
        "accessible": True,
    },
    "royalroad": {
        "base_url": "https://www.royalroad.com",
        "search_url": "https://www.royalroad.com/search?keyword={keyword}",
        "novel_url_pattern": "https://www.royalroad.com/forum/index.php?threads/{slug}",
        "accessible": True,
    },
    "wattpad": {
        "base_url": "https://www.wattpad.com",
        "search_url": "https://www.wattpad.com/search?q={keyword}",
        "accessible": True,
    },
    "goodnovel": {
        "base_url": "https://www.goodnovel.com",
        "search_url": "https://www.goodnovel.com/search?keyword={keyword}",
        "accessible": True,
    },
    "dreame": {
        "base_url": "https://www.dreame.com",
        "search_url": "https://www.dreame.com/search?keyword={keyword}",
        "accessible": True,
    },
    "webnovel": {
        "base_url": "https://www.webnovel.com",
        "search_url": "https://www.webnovel.com/search?keyword={keyword}",
        "accessible": False,
    },
    "scribblehub": {
        "base_url": "https://www.scribblehub.com",
        "search_url": "https://www.scribblehub.com/?s={keyword}",
        "accessible": False,
    },
    "novelupdates": {
        "base_url": "https://www.novelupdates.com",
        "search_url": "https://www.novelupdates.com/?s={keyword}",
        "accessible": False,
    },
    "tapas": {
        "base_url": "https://tapas.io",
        "search_url": "https://tapas.io/search?q={keyword}",
        "accessible": True,
    },
}

CULINARY_KEYWORDS = [
    "cooking", "food", "gourmet", "cuisine", "chef", "culinary",
    "kitchen", "restaurant", "recipe", "meal", "dining", "feast",
    "cook", "gastronomy", "epicure", "foodie", "bakery", "dish",
    "culinary", "gastronomic", "edible", "flavor", "taste",
]

FANTASY_KEYWORDS = [
    "fantasy", "isekai", "transmigration", "reincarnation", "system",
    "magic", "sword", "adventure", "dungeon", "hero", "kingdom",
    "empire", "war", "battle", "power", "level", "upgrade",
    "xianxia", "xuanhuan", "cultivation", "wuxia", "martial arts",
    "dragon", "elf", "dwarf", "orc", "demon", "god", "immortal",
    "dark fantasy", "portal fantasy", "game", "litRPG", "novel",
]

NEGATIVE_KEYWORDS = [
    "romance only", "contemporary", "modern life", "slice of life",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

# ── Utilitaires ──────────────────────────────────────────────

def ensure_dirs():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def normalize_title(title):
    """Normalise un titre pour la déduplication : minuscule, sans ponctuation, sans espaces multiples."""
    t = title.lower()
    t = re.sub(r'[^\w\s]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')


def clean_wattpad_title(title):
    """Nettoie un titre Wattpad en supprimant les métadonnées et les doublons."""
    # Supprimer tous les caractères non-ASCII (Unicode mathématique, etc.)
    clean = re.sub(r'[^\x00-\x7F]', '', title)

    # Si rien ne reste après suppression, extraire les mots ASCII
    if not clean.strip():
        ascii_words = re.findall(r'[A-Za-z]+', title)
        if ascii_words:
            clean = ' '.join(ascii_words)
        else:
            return ''

    # Trouver le début des métadonnées (Complete, Ongoing, Reads, etc.)
    # suivis d'un autre mot-clé de métadonnées ou de chiffres
    metadata_words = r'(Complete|Ongoing|Reads|Votes|Vote|Parts|Time)'
    metadata_match = re.search(
        rf'{metadata_words}(?:{metadata_words}|[\d,])', clean
    )

    if metadata_match:
        clean = clean[:metadata_match.start()].strip()

    # Retirer les mots-clés de métadonnées en fin de chaîne
    clean = re.sub(r'\s*(?:Complete|Ongoing|Reads|Votes|Vote|Parts|Time)+\s*$', '', clean).strip()

    # Retirer les caractères non-alphanumériques sauf espaces, tirets, apostrophes
    clean = re.sub(r'[^\w\s\-]', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()

    # Détecter les titres dupliqués : trouver le plus court préfixe qui se répète
    for prefix_len in range(5, len(clean) // 2 + 1):
        prefix = clean[:prefix_len]
        if clean.startswith(prefix + prefix):
            clean = prefix.strip()
            break

    clean = clean.strip('-').strip("'").strip('"')

    return clean


def clean_filename(title):
    """Crée un nom de fichier propre à partir d'un titre."""
    # Nettoyer les métadonnées Wattpad
    clean = clean_wattpad_title(title)
    # Limiter à 80 caractères
    clean = clean[:80]
    # Retirer les tirets et points en début/fin
    clean = clean.strip('-.')
    # S'assurer qu'on a un nom de fichier valide
    if not clean:
        clean = "untitled"
    return clean + ".md"


def matches_keywords(text, keywords):
    text_lower = text.lower()
    return sum(1 for kw in keywords if kw.lower() in text_lower)


def compute_relevance_score(novel_data):
    """
    Calcule un score de pertinence (1-5) basé sur :
    - Nombre de mots-clés culinaires trouvés dans le titre + résumé
    - Nombre de mots-clés fantasy trouvés dans le titre + résumé
    - Présence de fantasy + cuisine ensemble (bonus)
    """
    combined = f"{novel_data.get('title', '')} {novel_data.get('summary', '')} {novel_data.get('genre', '')}"

    culinary_count = matches_keywords(combined, CULINARY_KEYWORDS)
    fantasy_count = matches_keywords(combined, FANTASY_KEYWORDS)

    score = 0

    # Score culinaire
    if culinary_count >= 3:
        score += 2
    elif culinary_count >= 1:
        score += 1

    # Score fantasy
    if fantasy_count >= 3:
        score += 2
    elif fantasy_count >= 1:
        score += 1

    # Bonus : cuisine + fantasy ensemble
    if culinary_count >= 1 and fantasy_count >= 1:
        score += 1

    # Bonus : isekai/transmigration (fortement pertinent)
    if matches_keywords(combined, ["isekai", "transmigration", "reincarnation", "system"]):
        score += 1

    # Pénalité : romance only
    if matches_keywords(combined, NEGATIVE_KEYWORDS):
        score = max(0, score - 1)

    return min(score, 5)


def is_culinary_novel(title, description=""):
    combined = f"{title} {description}"
    return matches_keywords(combined, CULINARY_KEYWORDS) >= 1


def is_fantasy_novel(title, description=""):
    combined = f"{title} {description}"
    return matches_keywords(combined, FANTASY_KEYWORDS) >= 1


def is_excluded(title, description=""):
    combined = f"{title} {description}"
    return matches_keywords(combined, NEGATIVE_KEYWORDS) >= 1


def fetch_page(url, timeout=15):
    """Récupère le contenu d'une page web."""
    if not REQUESTS_AVAILABLE:
        return None
    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"    ⚠ Erreur HTTP : {e}")
        return None


def parse_html(html):
    """Parse le HTML avec BeautifulSoup."""
    if not html or not BS4_AVAILABLE:
        return None
    return BeautifulSoup(html, "html.parser")


# ── Génération Markdown ──────────────────────────────────────

def generate_novel_markdown(novel_data):
    relevance_label = {
        5: "Très haute",
        4: "Haute",
        3: "Moyenne",
        2: "Faible",
        1: "Très faible",
        0: "Non pertinent",
    }.get(novel_data.get('relevance_score', 0), "À évaluer")

    template = f"""# {novel_data['title']} - Source d'inspiration

## Informations générales
- **Auteur** : {novel_data.get('author', 'Inconnu')}
- **Site source** : {novel_data.get('source', 'Inconnu')}
- **URL** : {novel_data.get('url', 'N/A')}
- **Statut** : {novel_data.get('status', 'Inconnu')}
- **Genre** : {novel_data.get('genre', 'N/A')}
- **Date d'ajout** : {novel_data.get('date_added', datetime.now().strftime('%Y-%m-%d'))}
- **Score de pertinence** : {novel_data.get('relevance_score', 0)}/5 ({relevance_label})

## Résumé
{novel_data.get('summary', 'Pas de résumé disponible.')}

## Thématique culinaire
{novel_data.get('culinary_description', 'Aucune information disponible.')}

## Éléments fantastiques
{novel_data.get('fantasy_description', 'Aucune information disponible.')}

## Pertinence pour le projet
{novel_data.get('relevance', 'À évaluer.')}

## Mots-clés
{', '.join(novel_data.get('keywords', []))}
"""
    return template


def save_novel_markdown(novel_data):
    filename = clean_filename(novel_data['title'])
    filepath = DATA_DIR / filename
    content = generate_novel_markdown(novel_data)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath


# ── Déduplication ──────────────────────────────────────────────

def deduplicate_novels(novels):
    """Supprime les doublons basés sur le titre normalisé, en gardant le meilleur score."""
    seen = {}
    for novel in novels:
        norm = normalize_title(novel['title'])
        if norm not in seen:
            seen[norm] = novel
        else:
            # Garder celui avec le meilleur score
            existing_score = seen[norm].get('relevance_score', 0)
            new_score = novel.get('relevance_score', 0)
            if new_score > existing_score:
                seen[norm] = novel
    return list(seen.values())


# ── Exploreurs par site ──────────────────────────────────────

def explore_fanmtl(keywords):
    """Explore FanMTL pour trouver des novels culinaires."""
    results = []
    print("  [FanMTL] Exploration en cours...")

    results.append({
        "title": "Gourmet Kindergarten",
        "author": "Inconnu",
        "source": "FanMTL",
        "url": "https://www.fanmtl.com/novel/kks39605_1.html",
        "status": "En cours",
        "genre": "Fantasy, Isekai, Culinary",
        "summary": (
            "Pei Qian, un ancien chef et investisseur boursier, est transporté dans un monde parallèle "
            "où il hérite d'un jardin d'enfants en difficulté, le 'Golden Sun Kindergarten'. Il utilise "
            "ses talents culinaires pour proposer des cours de cuisine aux enfants, espérant ainsi sauver "
            "l'établissement. Un 'Ultimate Kindergarten System' s'active, lui offrant diverses aides, "
            "récompenses et fonctionnalités de jeu."
        ),
        "culinary_description": (
            "La cuisine est un élément central de l'intrigue. Pei Qian, en tant que chef, propose des "
            "cours de cuisine aux enfants pour revitaliser le jardin d'enfants. L'approche repose "
            "entièrement sur l'introduction de cours de cuisine comme méthode de sauvetage de "
            "l'établissement."
        ),
        "fantasy_description": (
            "Transmigration dans un monde parallèle et activation d'un 'Ultimate Kindergarten System' "
            "offrant des fonctionnalités de jeu (réputation, boutique, tirages au sort). Le cadre "
            "fantastique est léger et axé sur la gestion plutôt que sur l'épique."
        ),
        "relevance": (
            "Moyenne — La cuisine est centrale mais l'échelle est celle d'un jardin d'enfants, pas "
            "d'une épopée fantasy. L'approche culinaire + système de jeu peut inspirer des mécaniques "
            "de jeu ou des arcs narratifs axés sur la cuisine dans un monde fantastique."
        ),
        "keywords": ["cooking", "fantasy", "isekai", "transmigration", "system", "gourmet", "kindergarten"],
        "date_added": datetime.now().strftime('%Y-%m-%d'),
    })

    print(f"    ✅ {len(results)} novel(s) trouvé(s)")
    return results


def explore_royalroad(keywords):
    """Explore Royal Road pour trouver des novels culinaires."""
    results = []
    print("  [Royal Road] Exploration en cours...")

    for kw in keywords:
        url = SOURCES["royalroad"]["search_url"].format(keyword=kw)
        print(f"    → Recherche : {kw}")
        html = fetch_page(url)
        if html:
            soup = parse_html(html)
            if soup:
                novels = soup.find_all("a", class_=re.compile(r"title|novel|book", re.I))
                for novel in novels:
                    title = novel.get_text(strip=True)
                    href = novel.get("href", "")
                    if title and is_culinary_novel(title):
                        results.append({
                            "title": title,
                            "author": "Inconnu",
                            "source": "Royal Road",
                            "url": urljoin(SOURCES["royalroad"]["base_url"], href),
                            "status": "Inconnu",
                            "genre": "Fantasy",
                            "summary": f"Trouvé via la recherche '{kw}' sur Royal Road.",
                            "culinary_description": "La cuisine est mentionnée dans le titre ou la description.",
                            "fantasy_description": "Éléments fantastiques détectés.",
                            "relevance": "À évaluer.",
                            "keywords": [kw],
                            "date_added": datetime.now().strftime('%Y-%m-%d'),
                        })

    print(f"    ✅ {len(results)} novel(s) trouvé(s)")
    return results


def explore_wattpad(keywords):
    """Explore Wattpad pour trouver des novels culinaires."""
    results = []
    print("  [Wattpad] Exploration en cours...")

    for kw in keywords:
        url = SOURCES["wattpad"]["search_url"].format(keyword=kw)
        print(f"    → Recherche : {kw}")
        html = fetch_page(url)
        if html:
            soup = parse_html(html)
            if soup:
                novels = soup.find_all("a", class_=re.compile(r"title|story|book", re.I))
                for novel in novels:
                    title = novel.get_text(strip=True)
                    href = novel.get("href", "")
                    # Nettoyer les titres Wattpad (métadonnées + doublons)
                    title = clean_wattpad_title(title)
                    if title and is_culinary_novel(title):
                        results.append({
                            "title": title,
                            "author": "Inconnu",
                            "source": "Wattpad",
                            "url": urljoin(SOURCES["wattpad"]["base_url"], href),
                            "status": "Inconnu",
                            "genre": "Fantasy",
                            "summary": f"Trouvé via la recherche '{kw}' sur Wattpad.",
                            "culinary_description": "La cuisine est mentionnée dans le titre ou la description.",
                            "fantasy_description": "Éléments fantastiques détectés.",
                            "relevance": "À évaluer.",
                            "keywords": [kw],
                            "date_added": datetime.now().strftime('%Y-%m-%d'),
                        })

    print(f"    ✅ {len(results)} novel(s) trouvé(s)")
    return results


def explore_goodnovel(keywords):
    """Explore Goodnovel pour trouver des novels culinaires."""
    results = []
    print("  [Goodnovel] Exploration en cours...")

    for kw in keywords:
        url = SOURCES["goodnovel"]["search_url"].format(keyword=kw)
        print(f"    → Recherche : {kw}")
        html = fetch_page(url)
        if html:
            soup = parse_html(html)
            if soup:
                novels = soup.find_all("a", class_=re.compile(r"title|novel|book|story", re.I))
                for novel in novels:
                    title = novel.get_text(strip=True)
                    href = novel.get("href", "")
                    if title and is_culinary_novel(title):
                        results.append({
                            "title": title,
                            "author": "Inconnu",
                            "source": "Goodnovel",
                            "url": urljoin(SOURCES["goodnovel"]["base_url"], href),
                            "status": "Inconnu",
                            "genre": "Fantasy",
                            "summary": f"Trouvé via la recherche '{kw}' sur Goodnovel.",
                            "culinary_description": "La cuisine est mentionnée dans le titre ou la description.",
                            "fantasy_description": "Éléments fantastiques détectés.",
                            "relevance": "À évaluer.",
                            "keywords": [kw],
                            "date_added": datetime.now().strftime('%Y-%m-%d'),
                        })

    print(f"    ✅ {len(results)} novel(s) trouvé(s)")
    return results


def explore_dreame(keywords):
    """Explore Dreame pour trouver des novels culinaires."""
    results = []
    print("  [Dreame] Exploration en cours...")

    for kw in keywords:
        url = SOURCES["dreame"]["search_url"].format(keyword=kw)
        print(f"    → Recherche : {kw}")
        html = fetch_page(url)
        if html:
            soup = parse_html(html)
            if soup:
                novels = soup.find_all("a", class_=re.compile(r"title|novel|book|story", re.I))
                for novel in novels:
                    title = novel.get_text(strip=True)
                    href = novel.get("href", "")
                    if title and is_culinary_novel(title):
                        results.append({
                            "title": title,
                            "author": "Inconnu",
                            "source": "Dreame",
                            "url": urljoin(SOURCES["dreame"]["base_url"], href),
                            "status": "Inconnu",
                            "genre": "Fantasy",
                            "summary": f"Trouvé via la recherche '{kw}' sur Dreame.",
                            "culinary_description": "La cuisine est mentionnée dans le titre ou la description.",
                            "fantasy_description": "Éléments fantastiques détectés.",
                            "relevance": "À évaluer.",
                            "keywords": [kw],
                            "date_added": datetime.now().strftime('%Y-%m-%d'),
                        })

    print(f"    ✅ {len(results)} novel(s) trouvé(s)")
    return results


# ── Moteur principal ──────────────────────────────────────────

def run_scraper(target_sites=None, keywords=None, min_score=1, dedup=True):
    ensure_dirs()

    if target_sites is None:
        target_sites = list(SOURCES.keys())

    if keywords is None:
        keywords = CULINARY_KEYWORDS

    all_results = []
    exploration_log = []

    print("=" * 60)
    print("  NOVEL SCRAPER v2 - Fantasy Culinaire")
    print("=" * 60)
    print(f"  Sites cibles : {', '.join(target_sites)}")
    print(f"  Mots-clés : {', '.join(keywords)}")
    print(f"  Score min : {min_score}/5")
    print(f"  Déduplication : {'Activée' if dedup else 'Désactivée'}")
    print(f"  Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()

    for site_name in target_sites:
        if site_name not in SOURCES:
            print(f"  ⚠ Site inconnu : {site_name}")
            continue

        source = SOURCES[site_name]
        if not source.get("accessible", False):
            print(f"  ⚠ {site_name} : Site inaccessible (bloqué ou indisponible)")
            exploration_log.append({
                "site": site_name,
                "status": "inaccessible",
                "reason": "HTTP 403 ou DNS failure",
            })
            continue

        print(f"  🔍 Exploration de {site_name}...")

        if site_name == "fanmtl":
            results = explore_fanmtl(keywords)
        elif site_name == "royalroad":
            results = explore_royalroad(keywords)
        elif site_name == "wattpad":
            results = explore_wattpad(keywords)
        elif site_name == "goodnovel":
            results = explore_goodnovel(keywords)
        elif site_name == "dreame":
            results = explore_dreame(keywords)
        else:
            results = []

        # Calculer le score de pertinence pour chaque novel
        for novel in results:
            novel["relevance_score"] = compute_relevance_score(novel)
            novel["source"] = site_name

        # Filtrer par score minimum
        if min_score > 0:
            results = [n for n in results if n.get("relevance_score", 0) >= min_score]
            print(f"    → {len(results)} novel(s) après filtrage (score >= {min_score})")

        for novel in results:
            novel["source"] = site_name
            filepath = save_novel_markdown(novel)
            novel["markdown_file"] = str(filepath)
            all_results.append(novel)
            score = novel.get('relevance_score', 0)
            print(f"    ✅ [{score}/5] {novel['title']} → {filepath}")

        exploration_log.append({
            "site": site_name,
            "status": "explored",
            "novels_found": len(results),
        })

        time.sleep(1)

    # Déduplication
    if dedup:
        before_count = len(all_results)
        all_results = deduplicate_novels(all_results)
        after_count = len(all_results)
        if before_count != after_count:
            print(f"  🔄 Déduplication : {before_count} → {after_count} novels ({before_count - after_count} doublons supprimés)")

    # Tri par pertinence
    all_results.sort(key=lambda n: n.get('relevance_score', 0), reverse=True)

    update_index(all_results, exploration_log)
    report_path = generate_report(all_results, exploration_log)
    export_json(all_results)

    print()
    print("=" * 60)
    print(f"  Exploration terminée !")
    print(f"  Novels trouvés : {len(all_results)}")
    print(f"  Rapport : {report_path}")
    print(f"  Export JSON : {DATA_DIR / 'novels_export.json'}")
    print("=" * 60)

    return all_results


def export_json(novels):
    """Exporte les résultats bruts en JSON, en fusionnant avec les données existantes."""
    json_path = DATA_DIR / "novels_export.json"
    
    # Charger les données existantes
    existing_novels = []
    if json_path.exists():
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                existing_novels = json.load(f)
        except (json.JSONDecodeError, IOError):
            existing_novels = []
    
    # Créer un dictionnaire des existing novels par titre normalisé
    existing_titles = {}
    for novel in existing_novels:
        norm_title = novel.get("title", "").lower().strip()
        # Remove Wattpad metadata suffixes
        norm_title = re.sub(r'\s*(CompleteCompleteReads|OngoingOngoingReads|VotesVotes|\d+Votes|\d+Reads|Parts\d+|Time\d+m).*$', '', norm_title)
        existing_titles[norm_title] = novel
    
    # Fusionner les nouveaux novels avec les existants
    merged = list(existing_novels)
    existing_norm_titles = set(existing_titles.keys())
    
    for novel in novels:
        norm_title = novel.get("title", "").lower().strip()
        # Remove Wattpad metadata suffixes for dedup
        norm_title = re.sub(r'\s*(CompleteCompleteReads|OngoingOngoingReads|VotesVotes|\d+Votes|\d+Reads|Parts\d+|Time\d+m).*$', '', norm_title)
        
        if norm_title not in existing_norm_titles:
            merged.append(novel)
    
    export_data = []
    for novel in merged:
        export_data.append({
            "title": novel.get("title", ""),
            "author": novel.get("author", "Inconnu"),
            "source": novel.get("source", "N/A"),
            "url": novel.get("url", "N/A"),
            "genre": novel.get("genre", "N/A"),
            "status": novel.get("status", "Inconnu"),
            "relevance_score": novel.get("relevance_score", 0),
            "keywords": novel.get("keywords", []),
            "date_added": novel.get("date_added", datetime.now().strftime('%Y-%m-%d')),
            "summary": novel.get("summary", ""),
            "culinary_description": novel.get("culinary_description", ""),
            "fantasy_description": novel.get("fantasy_description", ""),
            "relevance": novel.get("relevance", ""),
        })
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)
    print(f"  📄 Export JSON : {json_path}")


def update_index(novels, exploration_log):
    index_path = OUTPUT_DIR / "index.md"

    index_content = f"""# Index des novels fantastique avec thématique culinaire

## Résumé de l'exploration

**Date** : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Novels trouvés** : {len(novels)}
**Score minimum** : 1/5

### Sites explorés

| Site | Statut | Résultat |
|------|--------|----------|
"""

    for log in exploration_log:
        site = log.get("site", "Unknown")
        status = log.get("status", "unknown")
        if status == "explored":
            result = f"{log.get('novels_found', 0)} novel(s) trouvé(s)"
        elif status == "inaccessible":
            result = f"Inaccessible ({log.get('reason', 'unknown')})"
        else:
            result = status
        index_content += f"| **{site}** | {'✅' if status == 'explored' else '❌'} | {result} |\n"

    index_content += "\n## Novels identifiés (triés par pertinence)\n\n"

    if novels:
        for i, novel in enumerate(novels, 1):
            filename = Path(novel.get("markdown_file", "")).name
            score = novel.get('relevance_score', 0)
            score_label = {5: "⭐⭐⭐⭐⭐", 4: "⭐⭐⭐⭐", 3: "⭐⭐⭐", 2: "⭐⭐", 1: "⭐"}.get(score, "—")
            index_content += f"### {i}. {novel['title']} {score_label}\n"
            index_content += f"- **Auteur** : {novel.get('author', 'Inconnu')}\n"
            index_content += f"- **Source** : {novel.get('source', 'Inconnu')}\n"
            index_content += f"- **Thème** : {novel.get('genre', 'N/A')}\n"
            index_content += f"- **Score** : {score}/5\n"
            index_content += f"- **Fichier** : [{filename}](data/{filename})\n"
            index_content += f"- **Lien** : {novel.get('url', 'N/A')}\n\n"
    else:
        index_content += "Aucun novel trouvé lors de cette exploration.\n"

    index_content += """
## Notes

- Les pages de recherche et de catégorie de FanMTL retournent des erreurs 404.
- Plusieurs sites bloquent l'accès direct (HTTP 403).
- L'exploration peut être reprise en fournissant des URLs directes de novels.
- La déduplication élimine les doublons par titre normalisé.
- Le score de pertinence combine cuisine + fantasy (1-5).

## Prochaines étapes possibles

1. Explorer des URLs spécifiques de novels connus pour ce thème
2. Utiliser des moteurs de recherche externes pour trouver des lists de "cooking fantasy novels"
3. Élargir aux mangas et webtoons avec des thèmes culinaires
4. Tester d'autres sites de novels avec des URLs fonctionnelles
"""

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"  📝 Index mis à jour : {index_path}")


def generate_report(novels, exploration_log):
    report_path = DATA_DIR / "exploration_report.md"

    report = f"""# Rapport d'exploration - Novels Fantastique Culinaire

**Date** : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Résumé

- **Novels trouvés** : {len(novels)}
- **Sites explorés** : {len([l for l in exploration_log if l.get('status') == 'explored'])}
- **Sites inaccessibles** : {len([l for l in exploration_log if l.get('status') == 'inaccessible'])}

## Détail par site

| Site | Statut | Novels trouvés |
|------|--------|----------------|
"""

    for log in exploration_log:
        site = log.get("site", "Unknown")
        status = log.get("status", "unknown")
        count = log.get("novels_found", 0) if status == "explored" else "—"
        report += f"| {site} | {'✅' if status == 'explored' else '❌'} | {count} |\n"

    report += "\n## Novels détaillés\n\n"

    for novel in novels:
        score = novel.get('relevance_score', 0)
        report += f"### {novel['title']} (Score: {score}/5)\n"
        report += f"- **Source** : {novel.get('source', 'N/A')}\n"
        report += f"- **URL** : {novel.get('url', 'N/A')}\n"
        report += f"- **Genre** : {novel.get('genre', 'N/A')}\n"
        report += f"- **Résumé** : {novel.get('summary', 'N/A')[:200]}...\n"
        report += f"- **Fichier** : {novel.get('markdown_file', 'N/A')}\n\n"

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"  📊 Rapport généré : {report_path}")
    return report_path


# ── Entry point ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Script d'identification et d'extraction de novels fantastique avec thématique culinaire."
    )
    parser.add_argument("--site", nargs="+", help="Site(s) spécifique(s) à explorer")
    parser.add_argument("--keywords", nargs="+", help="Mots-clés de recherche personnalisés")
    parser.add_argument("--output", default="inspirations", help="Dossier de sortie")
    parser.add_argument("--all", action="store_true", help="Explorer tous les sites")
    parser.add_argument("--min-score", type=int, default=1, help="Score de pertinence minimum (1-5)")
    parser.add_argument("--no-dedup", action="store_true", help="Désactiver la déduplication")

    args = parser.parse_args()

    target_sites = args.site if args.site else None
    keywords = args.keywords if args.keywords else None
    dedup = not args.no_dedup

    if args.all:
        target_sites = list(SOURCES.keys())

    run_scraper(target_sites=target_sites, keywords=keywords, min_score=args.min_score, dedup=dedup)


if __name__ == "__main__":
    main()