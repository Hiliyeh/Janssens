#!/usr/bin/env python3
"""
Add Province Hub pages to sitemap.xml
Adds 24 URLs with proper hreflang alternates
"""

import os
import yaml
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '_data')
SITEMAP_PATH = os.path.join(BASE_DIR, 'sitemap.xml')
SITE_URL = "https://janssensserrurier.be"

# Load provinces data
with open(os.path.join(DATA_DIR, 'provinces.yml'), 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    provinces = data['provinces']

# Language configs
lang_configs = {
    'fr': {'provinces_folder': 'provinces'},
    'en': {'provinces_folder': 'provinces'},
    'nl': {'provinces_folder': 'provincies'}
}

def get_province_slug(province, lang):
    if lang == 'fr':
        return province['slug_fr']
    elif lang == 'nl':
        return province['slug_nl']
    else:
        return province['slug_en']

def generate_sitemap_entries():
    """Generate sitemap XML entries for province pages"""
    entries = []
    today = date.today().isoformat()

    for province in provinces:
        # Build URLs for all 3 languages
        urls = {}
        for lang, config in lang_configs.items():
            slug = get_province_slug(province, lang)
            urls[lang] = f"{SITE_URL}/{lang}/{config['provinces_folder']}/{slug}/"

        # Generate entry for each language
        for lang in ['fr', 'en', 'nl']:
            entry = f"""  <url>
    <loc>{urls[lang]}</loc>
    <xhtml:link rel="alternate" hreflang="fr-BE" href="{urls['fr']}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{urls['en']}"/>
    <xhtml:link rel="alternate" hreflang="nl-BE" href="{urls['nl']}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{urls['fr']}"/>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""
            entries.append(entry)

    return entries

def main():
    # Read current sitemap
    with open(SITEMAP_PATH, 'r', encoding='utf-8') as f:
        sitemap_content = f.read()

    # Check if provinces already in sitemap
    if '/provinces/' in sitemap_content or '/provincies/' in sitemap_content:
        print("Province URLs already exist in sitemap. Skipping.")
        return

    # Remove closing tag
    sitemap_content = sitemap_content.replace('</urlset>', '').strip()

    # Generate new entries
    entries = generate_sitemap_entries()

    # Add new entries
    sitemap_content += '\n\n  <!-- Province Hub Pages (24 URLs) -->\n'
    sitemap_content += '\n'.join(entries)
    sitemap_content += '\n</urlset>\n'

    # Write updated sitemap
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"Added {len(entries)} province URLs to sitemap.xml")
    print(f"  - {len(provinces)} provinces")
    print(f"  - 3 languages")

if __name__ == '__main__':
    main()
