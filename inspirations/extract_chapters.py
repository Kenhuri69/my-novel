#!/usr/bin/env python3
"""
Chapter extraction script for novel inspiration files.
Extracts chapter text from FanMTL stories (Wattpad requires JavaScript rendering).
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

def fetch_page(url, timeout=15):
    if not REQUESTS_AVAILABLE:
        return None
    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"    ⚠ Error fetching {url}: {e}")
        return None

def extract_fanmtl_toc(novel_url):
    """Extract chapter list from FanMTL TOC page.
    
    FanMTL TOC page format: /novel/{slug}.html (not /novel/{slug}_{chapter}.html)
    """
    # Convert chapter URL to TOC URL
    # e.g., /novel/kks39605_1.html -> /novel/kks39605.html
    toc_url = re.sub(r'/\d+\.html$', '.html', novel_url)
    
    html = fetch_page(toc_url)
    if not html or not BS4_AVAILABLE:
        return []
    
    soup = BeautifulSoup(html, "html.parser")
    chapters = []
    
    # FanMTL chapter list is in <ul class="chapter-list">
    chapter_list = soup.find("ul", class_="chapter-list")
    if not chapter_list:
        # Try alternative selectors
        chapter_list = soup.find("ul", id=re.compile(r"chapter", re.I))
    
    if not chapter_list:
        print(f"    ⚠ No chapter list found on TOC page")
        return []
    
    for li in chapter_list.find_all("li"):
        link = li.find("a")
        if not link:
            continue
        href = link.get("href", "")
        title = link.get("title", "") or link.get_text(strip=True)
        if href:
            chapter_url = f"https://www.fanmtl.com{href}" if href.startswith("/") else href
            chapters.append({
                "title": title,
                "url": chapter_url,
            })
    
    # Remove duplicates while preserving order
    seen = set()
    unique = []
    for ch in chapters:
        key = ch["url"]
        if key not in seen:
            seen.add(key)
            unique.append(ch)
    
    return unique

def extract_fanmtl_chapter_text(chapter_url):
    """Extract the text content of a FanMTL chapter."""
    html = fetch_page(chapter_url)
    if not html or not BS4_AVAILABLE:
        return None
    
    soup = BeautifulSoup(html, "html.parser")
    
    # FanMTL chapter text selectors (try in order of specificity)
    text_selectors = [
        "div.chapter-content",
        "div.story-content",
        "div#chapter-content",
        "div.text-left",
        "div.readable",
        "div[property=articleBody]",
        "article",
    ]
    
    for selector in text_selectors:
        content = soup.select(selector)
        if content:
            text = content[0].get_text(separator="\n", strip=True)
            if text and len(text) > 100:
                return text
    
    # Fallback: get all paragraph text from main content area
    main = soup.find("main") or soup.find("div", id=re.compile(r"content|main", re.I))
    if main:
        paragraphs = main.find_all("p")
        if paragraphs:
            text = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
            if text:
                return text
    
    return None

def save_chapter_text(chapter_dir, chapter_num, title, text):
    """Save chapter text to a markdown file."""
    clean_title = re.sub(r'[^\w\s-]', '', title)[:60]
    clean_title = re.sub(r'[\s_]+', '-', clean_title).strip('-')
    filename = f"{chapter_num:04d}_{clean_title}.md"
    filepath = chapter_dir / filename
    
    content = f"""# {title}

**Chapter {chapter_num}**

{text}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return filepath

def process_fanmtl_novel(novel_data, chapters_dir):
    """Process a FanMTL novel to extract all chapters."""
    title = novel_data["title"]
    url = novel_data.get("url", "")
    
    # Create chapter directory
    clean_title = re.sub(r'[^\w\s-]', '', title)
    clean_title = re.sub(r'[\s_]+', '-', clean_title).strip('-')
    chapter_dir = chapters_dir / clean_title[:80]
    chapter_dir.mkdir(exist_ok=True)
    
    # Save novel info
    info_file = chapter_dir / "_novel_info.json"
    with open(info_file, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
    
    # Extract chapter list from TOC page
    print(f"    Fetching TOC page...")
    chapters = extract_fanmtl_toc(url)
    print(f"    Found {len(chapters)} chapters")
    
    # Save chapter list
    chapter_list_file = chapter_dir / "_chapters.md"
    list_content = f"""# Chapters: {title}

**Source**: fanmtl
**TOC URL**: {re.sub(r'/\d+\.html$', '.html', url)}
**Novel URL**: {url}
**Total Chapters**: {len(chapters)}

## Chapter List

"""
    for i, ch in enumerate(chapters, 1):
        list_content += f"{i}. [{ch.get('title', 'Chapter ' + str(i))}]({ch.get('url', '')})\n"
    
    with open(chapter_list_file, "w", encoding="utf-8") as f:
        f.write(list_content)
    
    # Fetch all chapters (not just first 5)
    fetched = 0
    for i, ch in enumerate(chapters, 1):
        ch_url = ch.get("url", "")
        if not ch_url:
            continue
        
        ch_title = ch.get("title", f"Chapter {i}")
        print(f"    [{i}/{len(chapters)}] Fetching: {ch_title[:50]}...", end=" ")
        
        text = extract_fanmtl_chapter_text(ch_url)
        if text:
            save_chapter_text(chapter_dir, i, ch_title, text)
            fetched += 1
            print(f"✅ ({len(text)} chars)")
        else:
            print("❌ No text")
        
        # Rate limiting - be respectful to the server
        time.sleep(1.0)
    
    print(f"    Fetched {fetched}/{len(chapters)} chapters")
    return len(chapters), fetched

def process_wattpad_novel(novel_data, chapters_dir):
    """Process a Wattpad novel - save metadata and explain limitation."""
    title = novel_data["title"]
    url = novel_data.get("url", "")
    
    # Create chapter directory
    clean_title = re.sub(r'[^\w\s-]', '', title)
    clean_title = re.sub(r'[\s_]+', '-', clean_title).strip('-')
    chapter_dir = chapters_dir / clean_title[:80]
    chapter_dir.mkdir(exist_ok=True)
    
    # Save novel info
    info_file = chapter_dir / "_novel_info.json"
    with open(info_file, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
    
    # Save README explaining Wattpad limitation
    readme = f"""# Wattpad Story: {title}

**Source**: wattpad
**URL**: {url}

## ⚠ Dynamic Content Limitation

Wattpad is a Single Page Application (SPA) that loads chapter content dynamically via JavaScript.
Simple HTTP requests (using `requests` library) cannot access the chapter text because:

1. The initial HTML response does not contain the chapter content
2. Chapter text is loaded asynchronously via JavaScript after page load
3. Wattpad requires authentication or API access for full content extraction

## Possible Alternatives for Extraction

1. **Wattpad API**: Wattpad has an unofficial API that may provide chapter data
2. **Headless Browser**: Tools like Playwright or Selenium can render JavaScript and extract content
3. **Wattpad API Token**: With proper authentication, the Wattpad API can return chapter text

## What Was Saved

- `_novel_info.json` - Novel metadata
- `_story_page.html` - Raw HTML snapshot of the story page (for reference)
- This README file explaining the limitation

## Chapter Extraction Status

Chapters could not be extracted automatically due to Wattpad's SPA architecture.
Manual extraction using a headless browser is required.
"""
    with open(chapter_dir / "_README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    
    # Try to save the story page HTML for reference
    html = fetch_page(url)
    if html:
        with open(chapter_dir / "_story_page.html", "w", encoding="utf-8") as f:
            f.write(html)
    
    print(f"    Wattpad story saved (SPA limitation - chapters not extractable)")
    return 0, 0

def process_novel(novel_data, chapters_dir):
    """Process a single novel based on its source."""
    source = novel_data.get("source", "unknown")
    title = novel_data["title"][:60]
    
    if source == "fanmtl":
        return process_fanmtl_novel(novel_data, chapters_dir)
    elif source == "wattpad":
        return process_wattpad_novel(novel_data, chapters_dir)
    else:
        print(f"    ⚠ Unknown source '{source}', skipping chapter extraction")
        return 0, 0

def main():
    # Load novel data
    data_file = Path("inspirations/data/novels_export.json")
    if not data_file.exists():
        print("Error: novels_export.json not found")
        return
    
    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    chapters_dir = Path("inspirations/data/chapters")
    chapters_dir.mkdir(exist_ok=True)
    
    # Deduplicate by title
    seen = set()
    unique_novels = []
    for n in data:
        title = n["title"]
        if title not in seen:
            seen.add(title)
            unique_novels.append(n)
    
    # Filter to only FanMTL novels for now (Wattpad chapters can't be extracted)
    fanmtl_novels = [n for n in unique_novels if n.get("source") == "fanmtl"]
    wattpad_novels = [n for n in unique_novels if n.get("source") == "wattpad"]
    
    print(f"Total unique novels: {len(unique_novels)}")
    print(f"FanMTL novels (extractable): {len(fanmtl_novels)}")
    print(f"Wattpad novels (SPA limitation): {len(wattpad_novels)}")
    print("=" * 60)
    
    total_chapters = 0
    total_fetched = 0
    
    # Process FanMTL novels first
    for i, novel in enumerate(fanmtl_novels, 1):
        title = novel["title"][:60]
        print(f"[{i}/{len(fanmtl_novels)}] FanMTL: {title}")
        
        try:
            ch_count, fetched = process_novel(novel, chapters_dir)
            total_chapters += ch_count
            total_fetched += fetched
        except Exception as e:
            print(f"    ⚠ Error: {e}")
            import traceback
            traceback.print_exc()
        
        time.sleep(0.5)
    
    # Process Wattpad novels (metadata only)
    if wattpad_novels:
        print(f"\nProcessing {len(wattpad_novels)} Wattpad novels (metadata only)...")
        for i, novel in enumerate(wattpad_novels, 1):
            title = novel["title"][:60]
            print(f"[{i}/{len(wattpad_novels)}] Wattpad: {title}", end=" ")
            try:
                process_novel(novel, chapters_dir)
                print("✅ (metadata saved)")
            except Exception as e:
                print(f"⚠ Error: {e}")
            time.sleep(0.3)
    
    print("=" * 60)
    print(f"Done! Total chapters found: {total_chapters}, fetched: {total_fetched}")

if __name__ == "__main__":
    main()
