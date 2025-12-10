#!/usr/bin/env python3
"""
Generate Province Hub pages for Janssens Serrurier
Creates 24 pages (8 provinces x 3 languages)
"""

import os
import yaml

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '_data')

# Load provinces data
with open(os.path.join(DATA_DIR, 'provinces.yml'), 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    provinces = data['provinces']

# Language configurations
languages = {
    'fr': {
        'folder': 'fr',
        'provinces_folder': 'provinces',
        'title_template': 'Serrurier {province} | Intervention 24h/24 | Janssens',
        'description_template': 'Serrurier {province} : intervention rapide dans les {count} communes. Disponible 24h/24, 7j/7. Devis gratuit.'
    },
    'en': {
        'folder': 'en',
        'provinces_folder': 'provinces',
        'title_template': 'Locksmith {province} | 24/7 Service | Janssens',
        'description_template': 'Locksmith {province}: fast intervention in all {count} municipalities. Available 24/7. Free quote.'
    },
    'nl': {
        'folder': 'nl',
        'provinces_folder': 'provincies',
        'title_template': 'Slotenmaker {province} | 24/7 Dienst | Janssens',
        'description_template': 'Slotenmaker {province}: snelle interventie in alle {count} gemeenten. 24/7 beschikbaar. Gratis offerte.'
    }
}

def get_province_name(province, lang):
    """Get province name in the given language"""
    if lang == 'fr':
        return province['name_fr']
    elif lang == 'nl':
        return province['name_nl']
    else:
        return province['name_en']

def get_province_slug(province, lang):
    """Get province slug in the given language"""
    if lang == 'fr':
        return province['slug_fr']
    elif lang == 'nl':
        return province['slug_nl']
    else:
        return province['slug_en']

def create_province_page(province, lang, lang_config):
    """Create a province page"""
    province_name = get_province_name(province, lang)
    province_slug = get_province_slug(province, lang)

    # Build the path
    dir_path = os.path.join(BASE_DIR, lang_config['folder'], lang_config['provinces_folder'], province_slug)
    os.makedirs(dir_path, exist_ok=True)

    # Generate frontmatter
    title = lang_config['title_template'].format(province=province_name)
    description = lang_config['description_template'].format(
        province=province_name,
        count=province['communes_count']
    )

    # Generate alternate URLs for hreflang
    alt_fr = f"/fr/provinces/{province['slug_fr']}/"
    alt_en = f"/en/provinces/{province['slug_en']}/"
    alt_nl = f"/nl/provincies/{province['slug_nl']}/"

    content = f"""---
layout: province
lang: {lang}
title: "{title}"
description: "{description}"
province_slug: "{province_slug}"
province_name: "{province_name}"
alternate:
  fr: "{alt_fr}"
  en: "{alt_en}"
  nl: "{alt_nl}"
---
"""

    # Write file
    file_path = os.path.join(dir_path, 'index.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return file_path

def main():
    pages_created = 0

    for province in provinces:
        for lang, config in languages.items():
            file_path = create_province_page(province, lang, config)
            print(f"Created: {file_path}")
            pages_created += 1

    print(f"\n✓ Created {pages_created} province pages")

if __name__ == '__main__':
    main()
