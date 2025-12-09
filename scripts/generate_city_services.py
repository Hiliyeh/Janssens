#!/usr/bin/env python3
"""Generate city-service pages for all 44 cities with subpages × 6 services × 3 languages."""

import os
import yaml

# Base path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '_data')

# Load cities from YAML
with open(os.path.join(DATA_DIR, 'cities.yml'), 'r', encoding='utf-8') as f:
    cities_data = yaml.safe_load(f)

# Get list of cities with subpages
CITIES_WITH_SUBPAGES = cities_data.get('cities_with_subpages', [])

# Build city info from all regions
ALL_CITIES = {}
for region in ['brussels', 'walloon_brabant', 'flemish_brabant']:
    if region in cities_data:
        for city in cities_data[region]:
            ALL_CITIES[city['slug']] = city

# Services by language
SERVICES = {
    "door-opening": {
        "fr": {"slug": "ouverture-porte", "name": "Ouverture de porte"},
        "en": {"slug": "door-opening", "name": "Door Opening"},
        "nl": {"slug": "deuropening", "name": "Deuropening"}
    },
    "lock-replacement": {
        "fr": {"slug": "remplacement-serrure", "name": "Remplacement serrure"},
        "en": {"slug": "lock-replacement", "name": "Lock Replacement"},
        "nl": {"slug": "slotvervanging", "name": "Slotvervanging"}
    },
    "key-duplication": {
        "fr": {"slug": "double-cles", "name": "Double de clés"},
        "en": {"slug": "key-duplication", "name": "Key Duplication"},
        "nl": {"slug": "sleutel-kopie", "name": "Sleutel kopië"}
    },
    "door-reinforcement": {
        "fr": {"slug": "blindage-porte", "name": "Blindage de porte"},
        "en": {"slug": "door-reinforcement", "name": "Door Reinforcement"},
        "nl": {"slug": "deurbepantsering", "name": "Deurbepantsering"}
    },
    "safe": {
        "fr": {"slug": "coffre-fort", "name": "Coffre-fort"},
        "en": {"slug": "safe", "name": "Safe Services"},
        "nl": {"slug": "kluis", "name": "Kluisdiensten"}
    },
    "automotive": {
        "fr": {"slug": "serrurerie-automobile", "name": "Serrurerie automobile"},
        "en": {"slug": "automotive-locksmith", "name": "Automotive Locksmith"},
        "nl": {"slug": "auto-slotenmaker", "name": "Auto slotenmaker"}
    }
}

# Language folder configuration
LANG_CONFIG = {
    "fr": {"cities_folder": "cities"},
    "en": {"cities_folder": "cities"},
    "nl": {"cities_folder": "cities"}
}

def get_city_slug(city_data, lang):
    """Get the correct city slug for a language."""
    if lang == 'en' and city_data.get('slug_en'):
        return city_data['slug_en']
    elif lang == 'nl' and city_data.get('slug_nl'):
        return city_data['slug_nl']
    return city_data['slug']

def get_city_name(city_data, lang):
    """Get the correct city name for a language."""
    if lang == 'en' and city_data.get('name_en'):
        return city_data['name_en']
    elif lang == 'nl' and city_data.get('name_nl'):
        return city_data['name_nl']
    return city_data['name']

def generate_page(lang, city_data, service_id, service_data):
    """Generate a city-service page."""

    city_slug = get_city_slug(city_data, lang)
    city_name = get_city_name(city_data, lang)
    service_slug = service_data["slug"]
    service_name = service_data["name"]
    cities_folder = LANG_CONFIG[lang]["cities_folder"]

    # Generate alternate links with correct slugs per language
    alternates = {}
    for alt_lang in ["fr", "en", "nl"]:
        alt_city_slug = get_city_slug(city_data, alt_lang)
        alt_service = SERVICES[service_id][alt_lang]
        alt_folder = LANG_CONFIG[alt_lang]["cities_folder"]
        alternates[alt_lang] = f"/{alt_lang}/{alt_folder}/{alt_city_slug}/{alt_service['slug']}/"

    # Create page content
    content = f"""---
layout: city-service
lang: {lang}
title: "{service_name} {city_name} | Janssens Serrurier"
description: "{service_name} à {city_name}. Intervention rapide 24h/24, 7j/7. Devis gratuit. Appelez le 0495 205 400."
city_name: "{city_name}"
city_slug: "{city_slug}"
service_id: "{service_id}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---
"""

    # Determine output path
    output_dir = os.path.join(BASE_DIR, lang, cities_folder, city_slug)
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{service_slug}.html")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path

def main():
    """Generate all city-service pages."""

    total_created = 0

    for lang in ["fr", "en", "nl"]:
        lang_count = 0

        for city_slug_fr in CITIES_WITH_SUBPAGES:
            city_data = ALL_CITIES.get(city_slug_fr)
            if not city_data:
                print(f"Warning: City {city_slug_fr} not found in cities.yml")
                continue

            for service_id, service_langs in SERVICES.items():
                service_data = service_langs[lang]

                path = generate_page(lang, city_data, service_id, service_data)
                lang_count += 1
                total_created += 1

        print(f"{lang.upper()}: {lang_count} pages created")

    print(f"\nTotal: {total_created} city-service pages created")

if __name__ == "__main__":
    main()
