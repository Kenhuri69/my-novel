#!/usr/bin/env python3
"""
Chapter extraction script for novel inspiration files.
Extracts chapter text from Wattpad and FanMTL stories.
"""

import json
import os
import re
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

def extract_wattpad_chapters(story_url, story_id):
    """Extract chapter list from a Wattpad story page."""
    html = fetch_page(story_url)
    if not html or not BS4_AVAILABLE:
        return []
    
    soup = BeautifulSoup(html, "html.parser")
    chapters = []
    
    # Wattpad chapter list is in the story page
    # Look for chapter links in the page
    chapter_links = soup.find_all("a", href=re.compile(r"/story/\d+/chapter-\d+", re.I))
    
    if not chapter_links:
        # Try alternative selectors
        chapter_links = soup.find_all("a", class_=re.compile(r"chapter", re.I))
    
    for link in chapter_links:
        href = link.get("href", "")
        text = link.get_text(strip=True)
        if href and text:
            chapter_url = f"https://www.wattpad.com{href}" if href.startswith("/") else href
            chapters.append({
                "title": text,
                "url": chapter_url,
                "id": href.split("-")[-1].replace(".html", "") if ".html" in href else href.split("/")[-1],
            })
    
    return chapters

def extract_wattpad_chapter_text(chapter_url):
    """Extract the text content of a Wattpad chapter."""
    html = fetch_page(chapter_url)
    if not html or not BS4_AVAILABLE:
        return None
    
    soup = BeautifulSoup(html, "html.parser")
    
    # Wattpad chapter text is typically in divs with specific classes
    # Try multiple selectors
    text_selectors = [
        "div.story-body",
        "div[data-action=view-chapter]",
        "div.readable",
        "div#storyContent",
        "div.chapter-content",
        "div.text-left",
        "div[property=content:encoded]",
    ]
    
    for selector in text_selectors:
        content = soup.select(selector)
        if content:
            text = content[0].get_text(separator="\n", strip=True)
            if text and len(text) > 100:
                return text
    
    # Fallback: get all paragraph text
    paragraphs = soup.find_all("p")
    if paragraphs:
        text = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        if text:
            return text
    
    return None

def extract_fanmtl_chapters(novel_url):
    """Extract chapter list from a FanMTL novel page."""
    html = fetch_page(novel_url)
    if not html or not BS4_AVAILABLE:
        return []
    
    soup = BeautifulSoup(html, "html.parser")
    chapters = []
    
    # FanMTL chapter list
    chapter_links = soup.find_all("a", href=re.compile(r"/novel/.*chapter", re.I))
    
    for link in chapter_links:
        href = link.get("href", "")
        text = link.get_text(strip=True)
        if href and text:
            chapter_url = f"https://www.fanmtl.com{href}" if href.startswith("/") else href
            chapters.append({
                "title": text,
                "url": chapter_url,
            })
    
    return chapters

def extract_fanmtl_chapter_text(chapter_url):
    """Extract the text content of a FanMTL chapter."""
    html = fetch_page(chapter_url)
    if not html or not BS4_AVAILABLE:
        return None
    
    soup = BeautifulSoup(html, "html.parser")
    
    # FanMTL chapter text
    text_selectors = [
        "div.chapter-content",
        "div.story-content",
        "div#chapter-content",
        "div.text-left",
        "div.readable",
    ]
    
    for selector in text_selectors:
        content = soup.select(selector)
        if content:
            text = content[0].get_text(separator="\n", strip=True)
            if text and len(text) > 100:
                return text
    
    return None

def save_chapter_text(chapter_dir, chapter_num, title, text):
    """Save chapter text to a file."""
    clean_title = re.sub(r[^\w\s-], "", title)[:60]
    clean_title = re.sub(r[\s_]+, "-", clean_title).strip("-")
    filename = f"{chapter_num:04d}_{clean_title}.md"
    filepath = chapter_dir / filename
    
    content = f"""# {title}

**Chapter {chapter_num}**

{text}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return filepath

def process_novel(novel_data, chapters_dir):
    """Process a single novel to extract chapters."""
    title = novel_data["title"]
    url = novel_data.get("url", "")
    source = novel_data.get("source", "unknown")
    
    # Create chapter directory
    clean_title = re.sub(r[^\w\s-], "", title)
    clean_title = re.sub(r[\s_]+, "-", clean_title).strip("-")
    chapter_dir = chapters_dir / clean_title[:80]
    chapter_dir.mkdir(exist_ok=True)
    
    # Write novel info
    info_file = chapter_dir / "_novel_info.json"
    with open(info_file, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
    
    chapters = []
    
    if "wattpad.com/story/" in url:
        story_id = url.split("/story/")[-1].split("?")[0].split("/")[0]
        chapters = extract_wattpad_chapters(url, story_id)
    elif "fanmtl.com/novel/" in url:
        chapters = extract_fanmtl_chapters(url)
    
    # Save chapter list
    chapter_list_file = chapter_dir / "_chapter_list.md"
    list_content = f"""# Chapter List: {title}

**Source**: {source}
**URL**: {url}
**Total Chapters**: {len(chapters)}

## Chapters

"""
    for i, ch in enumerate(chapters, 1):
        list_content += f"{i}. [{ch.get('title', 'Chapter ' + str(i))}]({ch.get('url', '')})\n"
    
    with open(chapter_list_file, "w", encoding="utf-8") as f:
        f.write(list_content)
    
    # Fetch first few chapters (limit to 5 to avoid rate limiting)
    fetched = 0
    for i, ch in enumerate(chapters[:5], 1):
        ch_url = ch.get("url", "")
        if not ch_url:
            continue
        
        print(f"    Fetching chapter {i}: {ch.get('title', 'Unknown')[:50]}...")
        
        if "wattpad.com" in ch_url:
            text = extract_wattpad_chapter_text(ch_url)
        elif "fanmtl.com" in ch_url:
            text = extract_fanmtl_chapter_text(ch_url)
        else:
            text = None
        
        if text:
            save_chapter_text(chapter_dir, i, ch.get("title", f"Chapter {i}"), text)
            fetched += 1
            print(f"      ✅ Saved ({len(text)} chars)")
        
        time.sleep(1)  # Be respectful with rate limiting
    
    print(f"    Fetched {fetched}/{min(5, len(chapters))} chapters")
    return len(chapters), fetched

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
    
    print(f"Processing {len(unique_novels)} unique novels...")
    print("=" * 60)
    
    total_chapters = 0
    total_fetched = 0
    
    for i, novel in enumerate(unique_novels, 1):
        title = novel["title"][:60]
        source = novel.get("source", "unknown")
        print(f"[{i}/{len(unique_novels)}] {title} ({source})")
        
        try:
            ch_count, fetched = process_novel(novel, chapters_dir)
            total_chapters += ch_count
            total_fetched += fetched
        except Exception as e:
            print(f"    ⚠ Error: {e}")
        
        time.sleep(0.5)
    
    print("=" * 60)
    print(f"Done! Total chapters found: {total_chapters}, fetched: {total_fetched}")

if __name__ == "__main__":
    main()
