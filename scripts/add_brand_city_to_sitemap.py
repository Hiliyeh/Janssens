#!/usr/bin/env python3
"""
Add Brand + City pages to sitemap.xml
Adds 645 URLs with proper hreflang alternates
"""

import os
import yaml
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '_data')
SITEMAP_PATH = os.path.join(BASE_DIR, 'sitemap.xml')
SITE_URL = "https://janssensserrurier.be"

# Load data
with open(os.path.join(DATA_DIR, 'brands.yml'), 'r', encoding='utf-8') as f:
    brands = yaml.safe_load(f)

with open(os.path.join(DATA_DIR, 'cities.yml'), 'r', encoding='utf-8') as f:
    cities_data = yaml.safe_load(f)

# Get cities with subpages
cities_with_subpages = cities_data.get('cities_with_subpages', [])

# Build city list
all_cities = []
for region in ['brussels', 'walloon_brabant', 'flemish_brabant']:
    if region in cities_data:
        for city in cities_data[region]:
            if city.get('slug') in cities_with_subpages or city.get('has_subpages'):
                all_cities.append(city)

# Language configs
lang_configs = {
    'fr': {'brands_folder': 'marques'},
    'en': {'brands_folder': 'brands'},
    'nl': {'brands_folder': 'merken'}
}

def get_city_slug(city, lang):
    if lang == 'nl' and city.get('slug_nl'):
        return city['slug_nl']
    elif lang == 'en' and city.get('slug_en'):
        return city['slug_en']
    return city['slug']

def generate_sitemap_entries():
    """Generate sitemap XML entries for brand-city pages"""
    entries = []
    today = date.today().isoformat()

    for brand in brands:
        for city in all_cities:
            # Build URLs for all 3 languages
            urls = {}
            for lang, config in lang_configs.items():
                city_slug = get_city_slug(city, lang)
                urls[lang] = f"{SITE_URL}/{lang}/{config['brands_folder']}/{brand['slug']}/{city_slug}/"

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
    <priority>0.7</priority>
  </url>"""
                entries.append(entry)

    return entries

def main():
    # Read current sitemap
    with open(SITEMAP_PATH, 'r', encoding='utf-8') as f:
        sitemap_content = f.read()

    # Remove closing tag
    sitemap_content = sitemap_content.replace('</urlset>', '').strip()

    # Generate new entries
    entries = generate_sitemap_entries()

    # Add new entries
    sitemap_content += '\n\n  <!-- Brand + City Pages (645 URLs) -->\n'
    sitemap_content += '\n'.join(entries)
    sitemap_content += '\n</urlset>\n'

    # Write updated sitemap
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"Added {len(entries)} brand-city URLs to sitemap.xml")
    print(f"  - {len(brands)} brands")
    print(f"  - {len(all_cities)} cities")
    print(f"  - 3 languages")

if __name__ == '__main__':
    main()
