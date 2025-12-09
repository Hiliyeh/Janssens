#!/usr/bin/env python3
"""
Generate emergency city pages for all languages.
43 cities x 6 emergency types x 3 languages = 774 pages
"""

import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '_data')

# Load cities from YAML
with open(os.path.join(DATA_DIR, 'cities.yml'), 'r', encoding='utf-8') as f:
    cities_data = yaml.safe_load(f)

# Get list of cities with subpages (43 cities)
CITIES_WITH_SUBPAGES = cities_data.get('cities_with_subpages', [])

# Build city info from all regions
ALL_CITIES = {}
for region in ['brussels', 'walloon_brabant', 'flemish_brabant']:
    if region in cities_data:
        for city in cities_data[region]:
            ALL_CITIES[city['slug']] = city

# Emergency types with slugs for each language
EMERGENCIES = [
    {
        "id": "locked-out",
        "fr": {"slug": "porte-claquee"},
        "en": {"slug": "locked-out"},
        "nl": {"slug": "dichtgevallen-deur"}
    },
    {
        "id": "broken-key",
        "fr": {"slug": "cle-cassee-serrure"},
        "en": {"slug": "broken-key-lock"},
        "nl": {"slug": "gebroken-sleutel-slot"}
    },
    {
        "id": "burglary",
        "fr": {"slug": "cambriolage"},
        "en": {"slug": "burglary"},
        "nl": {"slug": "inbraak"}
    },
    {
        "id": "armored-door",
        "fr": {"slug": "porte-blindee-bloquee"},
        "en": {"slug": "armored-door-locked"},
        "nl": {"slug": "gepantserde-deur-geblokkeerd"}
    },
    {
        "id": "night-locksmith",
        "fr": {"slug": "serrurier-nuit"},
        "en": {"slug": "night-locksmith"},
        "nl": {"slug": "nacht-slotenmaker"}
    },
    {
        "id": "sunday-locksmith",
        "fr": {"slug": "serrurier-dimanche"},
        "en": {"slug": "sunday-locksmith"},
        "nl": {"slug": "zondag-slotenmaker"}
    }
]

# Language config
LANGS = [
    {"code": "fr", "folder": "urgence"},
    {"code": "en", "folder": "emergency"},
    {"code": "nl", "folder": "noodgeval"}
]

def get_city_slug(city_data, lang):
    """Get the correct city slug for a language."""
    if lang == 'en' and city_data.get('slug_en'):
        return city_data['slug_en']
    elif lang == 'nl' and city_data.get('slug_nl'):
        return city_data['slug_nl']
    return city_data['slug']

def get_city_name(city_data, lang):
    """Get city name for specific language"""
    if lang == 'en' and city_data.get('name_en'):
        return city_data['name_en']
    elif lang == 'nl' and city_data.get('name_nl'):
        return city_data['name_nl']
    return city_data['name']

def generate_page(city_data, emergency, lang_config):
    """Generate a single emergency city page"""
    lang = lang_config["code"]
    folder = lang_config["folder"]
    city_slug = get_city_slug(city_data, lang)
    city_name = get_city_name(city_data, lang)
    emergency_slug = emergency[lang]["slug"]
    emergency_id = emergency["id"]

    # Build alternates with correct slugs per language
    alternates = {}
    for l in LANGS:
        l_code = l["code"]
        l_folder = l["folder"]
        l_city_slug = get_city_slug(city_data, l_code)
        l_emergency_slug = emergency[l_code]["slug"]
        alternates[l_code] = f"/{l_code}/{l_folder}/{l_city_slug}/{l_emergency_slug}/"

    # Build title
    if lang == "fr":
        title = f"{emergency_slug.replace('-', ' ').title()} {city_name} | Janssens Serrurier"
    elif lang == "en":
        title = f"{emergency_slug.replace('-', ' ').title()} {city_name} | Janssens Locksmith"
    else:
        title = f"{emergency_slug.replace('-', ' ').title()} {city_name} | Janssens Slotenmaker"

    content = f'''---
layout: emergency-city
lang: {lang}
title: "{title}"
description: "{emergency_slug.replace('-', ' ').title()} {city_name}"
emergency_id: "{emergency_id}"
city_slug: "{city_slug}"
city_name: "{city_name}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---

'''
    return content

def main():
    count = 0

    for lang_config in LANGS:
        lang = lang_config["code"]
        folder = lang_config["folder"]

        for city_slug_fr in CITIES_WITH_SUBPAGES:
            city_data = ALL_CITIES.get(city_slug_fr)
            if not city_data:
                print(f"Warning: City {city_slug_fr} not found in cities.yml")
                continue

            city_slug = get_city_slug(city_data, lang)

            for emergency in EMERGENCIES:
                emergency_slug = emergency[lang]["slug"]

                # Determine base path
                dir_path = os.path.join(BASE_DIR, lang, folder, city_slug)

                # Create directory
                os.makedirs(dir_path, exist_ok=True)

                # Generate page content
                content = generate_page(city_data, emergency, lang_config)

                # Use subfolder with index.html for clean URLs
                sub_dir = os.path.join(dir_path, emergency_slug)
                os.makedirs(sub_dir, exist_ok=True)
                file_path = os.path.join(sub_dir, "index.html")

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

                count += 1

        print(f"{lang.upper()}: {count // len(EMERGENCIES)} cities processed")

    print(f"\n=== Generated {count} emergency city pages ===")
    print(f"  - {len(CITIES_WITH_SUBPAGES)} cities")
    print(f"  - {len(EMERGENCIES)} emergency types")
    print(f"  - {len(LANGS)} languages")

if __name__ == "__main__":
    main()
