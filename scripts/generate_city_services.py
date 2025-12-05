#!/usr/bin/env python3
"""Generate city-service pages for all 44 cities with subpages × 6 services × 3 languages."""

import os
import yaml

# Base path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cities with subpages (from cities.yml)
CITIES_WITH_SUBPAGES = [
    "anderlecht", "auderghem", "beersel", "berchem-sainte-agathe", "braine-lalleud",
    "bruxelles-ville", "dilbeek", "etterbeek", "evere", "forest", "ganshoren",
    "grimbergen", "halle", "ixelles", "jette", "koekelberg", "kraainem", "la-hulpe",
    "lasne", "leuven", "machelen", "molenbeek-saint-jean", "nivelles",
    "ottignies-louvain-la-neuve", "overijse", "rixensart", "saint-gilles",
    "saint-josse-ten-noode", "schaerbeek", "sint-genesius-rode", "sint-pieters-leeuw",
    "tervuren", "tubize", "uccle", "vilvoorde", "waterloo", "watermael-boitsfort",
    "wavre", "wemmel", "wezembeek-oppem", "woluwe-saint-lambert", "woluwe-saint-pierre",
    "zaventem"
]

# City display names (for page titles)
CITY_NAMES = {
    "anderlecht": "Anderlecht",
    "auderghem": "Auderghem",
    "beersel": "Beersel",
    "berchem-sainte-agathe": "Berchem-Sainte-Agathe",
    "braine-lalleud": "Braine-l'Alleud",
    "bruxelles-ville": "Bruxelles-Ville",
    "dilbeek": "Dilbeek",
    "etterbeek": "Etterbeek",
    "evere": "Evere",
    "forest": "Forest",
    "ganshoren": "Ganshoren",
    "grimbergen": "Grimbergen",
    "halle": "Halle",
    "ixelles": "Ixelles",
    "jette": "Jette",
    "koekelberg": "Koekelberg",
    "kraainem": "Kraainem",
    "la-hulpe": "La Hulpe",
    "lasne": "Lasne",
    "leuven": "Leuven",
    "machelen": "Machelen",
    "molenbeek-saint-jean": "Molenbeek-Saint-Jean",
    "nivelles": "Nivelles",
    "ottignies-louvain-la-neuve": "Ottignies-Louvain-la-Neuve",
    "overijse": "Overijse",
    "rixensart": "Rixensart",
    "saint-gilles": "Saint-Gilles",
    "saint-josse-ten-noode": "Saint-Josse-ten-Noode",
    "schaerbeek": "Schaerbeek",
    "sint-genesius-rode": "Sint-Genesius-Rode",
    "sint-pieters-leeuw": "Sint-Pieters-Leeuw",
    "tervuren": "Tervuren",
    "tubize": "Tubize",
    "uccle": "Uccle",
    "vilvoorde": "Vilvoorde",
    "waterloo": "Waterloo",
    "watermael-boitsfort": "Watermael-Boitsfort",
    "wavre": "Wavre",
    "wemmel": "Wemmel",
    "wezembeek-oppem": "Wezembeek-Oppem",
    "woluwe-saint-lambert": "Woluwe-Saint-Lambert",
    "woluwe-saint-pierre": "Woluwe-Saint-Pierre",
    "zaventem": "Zaventem"
}

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

def generate_page(lang, city_slug, service_id, service_data, city_name):
    """Generate a city-service page."""

    service_slug = service_data["slug"]
    service_name = service_data["name"]
    cities_folder = LANG_CONFIG[lang]["cities_folder"]

    # Generate alternate links
    alternates = {}
    for alt_lang in ["fr", "en", "nl"]:
        alt_service = SERVICES[service_id][alt_lang]
        alt_folder = LANG_CONFIG[alt_lang]["cities_folder"]
        alternates[alt_lang] = f"/{alt_lang}/{alt_folder}/{city_slug}/{alt_service['slug']}/"

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

        for city_slug in CITIES_WITH_SUBPAGES:
            city_name = CITY_NAMES.get(city_slug, city_slug.replace("-", " ").title())

            for service_id, service_langs in SERVICES.items():
                service_data = service_langs[lang]

                path = generate_page(lang, city_slug, service_id, service_data, city_name)
                lang_count += 1
                total_created += 1

        print(f"{lang.upper()}: {lang_count} pages created")

    print(f"\nTotal: {total_created} city-service pages created")

if __name__ == "__main__":
    main()
