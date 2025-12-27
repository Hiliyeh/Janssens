#!/usr/bin/env python3
"""Generate missing city index pages for cities that have service subpages but no main page."""

import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '_data')

# Load cities data
with open(os.path.join(DATA_DIR, 'cities.yml'), 'r', encoding='utf-8') as f:
    cities_data = yaml.safe_load(f)

# Build city lookup from all regions
ALL_CITIES = {}
CITY_REGIONS = {}

REGIONS = {
    'brussels': {'fr': 'Bruxelles', 'en': 'Brussels', 'nl': 'Brussel'},
    'walloon_brabant': {'fr': 'Brabant wallon', 'en': 'Walloon Brabant', 'nl': 'Waals-Brabant'},
    'flemish_brabant': {'fr': 'Brabant flamand', 'en': 'Flemish Brabant', 'nl': 'Vlaams-Brabant'}
}

for region_key in ['brussels', 'walloon_brabant', 'flemish_brabant']:
    if region_key in cities_data:
        for city in cities_data[region_key]:
            slug = city['slug']
            ALL_CITIES[slug] = city
            CITY_REGIONS[slug] = region_key

# Language config
LANG_CONFIG = {
    'fr': {
        'folder': 'fr/communes',
        'service': 'Serrurier',
        'suffix': 'Serrurier 24h/24 | 0489 24 73 64',
        'desc_template': "Serrurier à {city}: intervention d'urgence en 30 min. Porte claquée, serrure cassée ? Service 24h/24 sans dégât. Devis gratuit.",
        'breadcrumb_zones': "Zones d'intervention"
    },
    'en': {
        'folder': 'en/cities',
        'service': 'Locksmith',
        'suffix': 'Locksmith 24/7 | 0489 24 73 64',
        'desc_template': 'Locksmith in {city}: emergency service in 30 min. Locked out, broken lock? 24/7 service without damage. Free quote.',
        'breadcrumb_zones': 'Service Areas'
    },
    'nl': {
        'folder': 'nl/gemeenten',
        'service': 'Slotenmaker',
        'suffix': 'Slotenmaker 24/7 | 0489 24 73 64',
        'desc_template': 'Slotenmaker in {city}: noodinterventie in 30 min. Deur dicht, slot kapot? 24/7 service zonder schade. Gratis offerte.',
        'breadcrumb_zones': 'Werkgebieden'
    }
}

def get_city_name(city_data, lang):
    """Get city name for language."""
    if lang == 'en' and city_data.get('name_en'):
        return city_data['name_en']
    elif lang == 'nl' and city_data.get('name_nl'):
        return city_data['name_nl']
    return city_data['name']

def get_city_slug(city_data, lang):
    """Get city slug for language."""
    if lang == 'en' and city_data.get('slug_en'):
        return city_data['slug_en']
    elif lang == 'nl' and city_data.get('slug_nl'):
        return city_data['slug_nl']
    return city_data['slug']

def generate_city_page(city_slug, lang):
    """Generate a city index page."""
    city_data = ALL_CITIES.get(city_slug)
    if not city_data:
        print(f"  Warning: City {city_slug} not found in cities.yml")
        return None

    config = LANG_CONFIG[lang]
    region_key = CITY_REGIONS.get(city_slug, 'brussels')
    region_names = REGIONS.get(region_key, REGIONS['brussels'])

    city_name = get_city_name(city_data, lang)
    city_slug_lang = get_city_slug(city_data, lang)
    postal = city_data.get('postal', '')

    # Build alternates
    alternates = {}
    for alt_lang, alt_config in LANG_CONFIG.items():
        alt_slug = get_city_slug(city_data, alt_lang)
        alternates[alt_lang] = f"/{alt_lang}/{alt_config['folder'].split('/')[1]}/{alt_slug}/"

    # Build page content
    title = f"{config['service']} {city_name} | {config['suffix']}"
    description = config['desc_template'].format(city=city_name)

    content = f"""---
layout: city
lang: {lang}
title: {title}
description: '{description}'
city_name: {city_name}
slug: {city_slug_lang}
postal: '{postal}'
region_name: {region_names[lang]}
canonical: /{lang}/{config['folder'].split('/')[1]}/{city_slug_lang}/
breadcrumb:
- name: {config['breadcrumb_zones']}
  url: /{lang}/#zones
- name: {city_name}
alternate:
  fr: {alternates['fr']}
  en: {alternates['en']}
  nl: {alternates['nl']}
---
"""

    # Write file
    output_dir = os.path.join(BASE_DIR, config['folder'], city_slug_lang)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'index.html')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path

def main():
    """Find and generate missing city pages."""
    total_created = 0

    for lang, config in LANG_CONFIG.items():
        folder = os.path.join(BASE_DIR, config['folder'])
        created = 0

        print(f"\nProcessing {config['folder']}...")

        # Find directories without index.html
        if os.path.exists(folder):
            for city_dir in os.listdir(folder):
                city_path = os.path.join(folder, city_dir)
                index_path = os.path.join(city_path, 'index.html')

                if os.path.isdir(city_path) and not os.path.exists(index_path):
                    # Check if this city has subpages (service pages)
                    has_subpages = any(f.endswith('.html') for f in os.listdir(city_path))

                    if has_subpages:
                        # Find the original slug (might be different for NL)
                        original_slug = city_dir

                        # Try to find in ALL_CITIES
                        if city_dir not in ALL_CITIES:
                            # Try reverse lookup by checking slug_nl/slug_en
                            for slug, data in ALL_CITIES.items():
                                if data.get('slug_nl') == city_dir or data.get('slug_en') == city_dir:
                                    original_slug = slug
                                    break

                        result = generate_city_page(original_slug, lang)
                        if result:
                            created += 1
                            print(f"  Created: {result}")

        print(f"  {lang.upper()}: {created} pages created")
        total_created += created

    print(f"\nTotal: {total_created} city pages created")

if __name__ == "__main__":
    main()
