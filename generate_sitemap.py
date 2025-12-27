#!/usr/bin/env python3
"""
Generate complete sitemap.xml with all pages and hreflang support
"""

import os
from pathlib import Path
from datetime import datetime
import re

BASE_URL = "https://janssensserrurier.be"
ROOT_DIR = Path(__file__).parent

# Priority mapping
PRIORITY_MAP = {
    'index.html': 1.0,
    'cities': 0.8,
    'communes': 0.8,
    'gemeenten': 0.8,
    'urgence': 0.9,
    'emergency': 0.9,
    'noodgeval': 0.9,
    'services': 0.85,
    'diensten': 0.85,
    'marques': 0.7,
    'brands': 0.7,
    'merken': 0.7,
    'guides': 0.6,
    'gidsen': 0.6,
}

# Path mappings between languages
PATH_MAPPINGS = {
    'urgence': {'fr': 'urgence', 'en': 'emergency', 'nl': 'noodgeval'},
    'emergency': {'fr': 'urgence', 'en': 'emergency', 'nl': 'noodgeval'},
    'noodgeval': {'fr': 'urgence', 'en': 'emergency', 'nl': 'noodgeval'},
    'services': {'fr': 'services', 'en': 'services', 'nl': 'diensten'},
    'diensten': {'fr': 'services', 'en': 'services', 'nl': 'diensten'},
    'marques': {'fr': 'marques', 'en': 'brands', 'nl': 'merken'},
    'brands': {'fr': 'marques', 'en': 'brands', 'nl': 'merken'},
    'merken': {'fr': 'marques', 'en': 'brands', 'nl': 'merken'},
    'guides': {'fr': 'guides', 'en': 'guides', 'nl': 'gidsen'},
    'gidsen': {'fr': 'guides', 'en': 'guides', 'nl': 'gidsen'},
    'cities': {'fr': 'communes', 'en': 'cities', 'nl': 'gemeenten'},
    'communes': {'fr': 'communes', 'en': 'cities', 'nl': 'gemeenten'},
    'gemeenten': {'fr': 'communes', 'en': 'cities', 'nl': 'gemeenten'},
    'conditions': {'fr': 'conditions', 'en': 'terms', 'nl': 'voorwaarden'},
    'terms': {'fr': 'conditions', 'en': 'terms', 'nl': 'voorwaarden'},
    'voorwaarden': {'fr': 'conditions', 'en': 'terms', 'nl': 'voorwaarden'},
    'confidentialite': {'fr': 'confidentialite', 'en': 'privacy', 'nl': 'privacy'},
    'privacy': {'fr': 'confidentialite', 'en': 'privacy', 'nl': 'privacy'},
}

def get_priority(path):
    """Determine priority based on path"""
    # Homepage gets highest priority
    if path in ['index.html', 'fr/index.html', 'en/index.html', 'nl/index.html']:
        return 1.0
    for key, priority in PRIORITY_MAP.items():
        if key in path:
            return priority
    return 0.5

def get_changefreq(path):
    """Determine change frequency"""
    if 'index.html' in path:
        return 'weekly'
    return 'monthly'

def path_to_url(path):
    """Convert file path to URL"""
    url = '/' + path.replace('.html', '/')
    url = url.replace('/index/', '/')
    if url == '//':
        url = '/'
    return url

def find_alternates(file_path, all_files_set):
    """Find alternate language versions of a page"""
    alternates = {}

    # Root index
    if file_path == 'index.html':
        return {'fr': '/fr/', 'en': '/en/', 'nl': '/nl/'}

    # Check if it's a language-specific page
    parts = file_path.split('/')
    if len(parts) < 2:
        return {}

    lang = parts[0]
    if lang not in ['fr', 'en', 'nl']:
        return {}

    # Get the rest of the path
    rest = '/'.join(parts[1:])

    # Check for section mapping
    section = parts[1] if len(parts) > 1 else None

    if section in PATH_MAPPINGS:
        mapping = PATH_MAPPINGS[section]
        for target_lang in ['fr', 'en', 'nl']:
            target_section = mapping[target_lang]
            # Replace the section in the path
            target_path = f"{target_lang}/{target_section}/{'/'.join(parts[2:])}" if len(parts) > 2 else f"{target_lang}/{target_section}.html"

            # For index files in sections
            if rest == f"{section}/index.html" or rest == f"{section}.html":
                target_path = f"{target_lang}/{target_section}/index.html"

            # Check variations
            if target_path in all_files_set:
                alternates[target_lang] = path_to_url(target_path)
            elif target_path.replace('/index.html', '.html') in all_files_set:
                alternates[target_lang] = path_to_url(target_path.replace('/index.html', '.html'))

    # For language index pages
    if file_path in ['fr/index.html', 'en/index.html', 'nl/index.html']:
        return {'fr': '/fr/', 'en': '/en/', 'nl': '/nl/'}

    # For city pages, they share the same slug across languages
    if 'cities' in file_path:
        city_part = '/'.join(parts[2:]) if len(parts) > 2 else ''
        if city_part:
            for target_lang in ['fr', 'en', 'nl']:
                target_path = f"{target_lang}/cities/{city_part}"
                if target_path in all_files_set:
                    alternates[target_lang] = path_to_url(target_path)

    return alternates

def generate_sitemap():
    """Generate the complete sitemap"""

    # Find all HTML files
    all_files = []
    exclude_dirs = {'_site', '_includes', '_layouts', '_archive', 'node_modules', 'vendor', 'doc', '.git'}

    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]

        for file in files:
            if file.endswith('.html'):
                full_path = Path(root) / file
                rel_path = str(full_path.relative_to(ROOT_DIR))
                all_files.append(rel_path)

    all_files.sort()
    all_files_set = set(all_files)

    today = datetime.now().strftime('%Y-%m-%d')

    xml_parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
        ''
    ]

    for file_path in all_files:
        # Skip 404 page
        if '404' in file_path:
            continue

        url = path_to_url(file_path)
        full_url = BASE_URL + url
        priority = get_priority(file_path)
        changefreq = get_changefreq(file_path)

        alternates = find_alternates(file_path, all_files_set)

        xml_parts.append('  <url>')
        xml_parts.append(f'    <loc>{full_url}</loc>')

        if alternates:
            for lang in ['fr', 'en', 'nl']:
                if lang in alternates:
                    hreflang = f"{lang}-BE" if lang in ['fr', 'nl'] else lang
                    xml_parts.append(f'    <xhtml:link rel="alternate" hreflang="{hreflang}" href="{BASE_URL}{alternates[lang]}"/>')
            if 'fr' in alternates:
                xml_parts.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}{alternates["fr"]}"/>')

        xml_parts.append(f'    <lastmod>{today}</lastmod>')
        xml_parts.append(f'    <changefreq>{changefreq}</changefreq>')
        xml_parts.append(f'    <priority>{priority}</priority>')
        xml_parts.append('  </url>')

    xml_parts.append('</urlset>')

    return '\n'.join(xml_parts)

if __name__ == '__main__':
    sitemap = generate_sitemap()

    output_path = ROOT_DIR / 'sitemap.xml'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(sitemap)

    url_count = sitemap.count('<url>')
    hreflang_count = sitemap.count('hreflang=')
    print(f"Sitemap generated with {url_count} URLs")
    print(f"Hreflang links: {hreflang_count}")
    print(f"Saved to: {output_path}")
