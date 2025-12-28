#!/usr/bin/env python3
"""
Generate province service pages for all 8 provinces.
Creates 168 pages (8 provinces × 7 services × 3 languages)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Province data with slugs per language
PROVINCES = [
    {"fr": "anvers", "nl": "antwerpen", "en": "antwerp", "name_fr": "Anvers", "name_nl": "Antwerpen", "name_en": "Antwerp"},
    {"fr": "limbourg", "nl": "limburg", "en": "limburg", "name_fr": "Limbourg", "name_nl": "Limburg", "name_en": "Limburg"},
    {"fr": "flandre-orientale", "nl": "oost-vlaanderen", "en": "east-flanders", "name_fr": "Flandre orientale", "name_nl": "Oost-Vlaanderen", "name_en": "East Flanders"},
    {"fr": "flandre-occidentale", "nl": "west-vlaanderen", "en": "west-flanders", "name_fr": "Flandre occidentale", "name_nl": "West-Vlaanderen", "name_en": "West Flanders"},
    {"fr": "hainaut", "nl": "henegouwen", "en": "hainaut", "name_fr": "Hainaut", "name_nl": "Henegouwen", "name_en": "Hainaut"},
    {"fr": "liege", "nl": "luik", "en": "liege", "name_fr": "Liege", "name_nl": "Luik", "name_en": "Liege"},
    {"fr": "namur", "nl": "namen", "en": "namur", "name_fr": "Namur", "name_nl": "Namen", "name_en": "Namur"},
    {"fr": "luxembourg", "nl": "luxemburg", "en": "luxembourg", "name_fr": "Luxembourg", "name_nl": "Luxemburg", "name_en": "Luxembourg"},
]

# Service data with slugs and IDs per language
SERVICES = [
    {
        "id": "door-opening",
        "fr": {"slug": "ouverture-porte", "name": "Ouverture de porte"},
        "nl": {"slug": "deuropening", "name": "Deuropening"},
        "en": {"slug": "door-opening", "name": "Door Opening"},
    },
    {
        "id": "lock-replacement",
        "fr": {"slug": "remplacement-serrure", "name": "Remplacement serrure"},
        "nl": {"slug": "slotvervanging", "name": "Slotvervanging"},
        "en": {"slug": "lock-replacement", "name": "Lock Replacement"},
    },
    {
        "id": "key-duplication",
        "fr": {"slug": "double-cles", "name": "Double de cles"},
        "nl": {"slug": "sleutel-kopie", "name": "Sleutel kopie"},
        "en": {"slug": "key-duplication", "name": "Key Duplication"},
    },
    {
        "id": "door-reinforcement",
        "fr": {"slug": "blindage-porte", "name": "Blindage de porte"},
        "nl": {"slug": "deurbepantsering", "name": "Deurbepantsering"},
        "en": {"slug": "door-reinforcement", "name": "Door Reinforcement"},
    },
    {
        "id": "safe",
        "fr": {"slug": "coffre-fort", "name": "Coffre-fort"},
        "nl": {"slug": "kluis", "name": "Kluis"},
        "en": {"slug": "safe", "name": "Safe"},
    },
    {
        "id": "automotive",
        "fr": {"slug": "serrurerie-automobile", "name": "Serrurerie automobile"},
        "nl": {"slug": "auto-slotenmaker", "name": "Auto slotenmaker"},
        "en": {"slug": "automotive-locksmith", "name": "Automotive Locksmith"},
    },
    {
        "id": "license-plate",
        "fr": {"slug": "plaque-immatriculation", "name": "Plaque d'immatriculation"},
        "nl": {"slug": "kentekenplaat", "name": "Kentekenplaat"},
        "en": {"slug": "license-plate", "name": "License Plate"},
    },
]


def generate_province_service_pages():
    """Generate service pages for each province"""
    count = 0

    for province in PROVINCES:
        for service in SERVICES:
            # French page
            content_fr = f"""---
layout: province-service
lang: fr
title: "{service['fr']['name']} {province['name_fr']} | Serrurier 24h/24 | 0495 205 400"
description: "{service['fr']['name']} dans la province de {province['name_fr']}. Intervention rapide dans toutes les communes. Devis gratuit 24h/24."
province_slug: "{province['fr']}"
province_name: "{province['name_fr']}"
service_id: "{service['id']}"
alternate:
  fr: "/fr/provinces/{province['fr']}/{service['fr']['slug']}/"
  en: "/en/provinces/{province['en']}/{service['en']['slug']}/"
  nl: "/nl/provincies/{province['nl']}/{service['nl']['slug']}/"
---
"""
            path_fr = os.path.join(BASE_DIR, "fr", "provinces", province['fr'], f"{service['fr']['slug']}.html")
            os.makedirs(os.path.dirname(path_fr), exist_ok=True)
            with open(path_fr, 'w', encoding='utf-8') as f:
                f.write(content_fr)
            count += 1

            # Dutch page
            content_nl = f"""---
layout: province-service
lang: nl
title: "{service['nl']['name']} {province['name_nl']} | Slotenmaker 24/7 | 0495 205 400"
description: "{service['nl']['name']} in de provincie {province['name_nl']}. Snelle interventie in alle gemeenten. Gratis offerte 24u/24."
province_slug: "{province['nl']}"
province_name: "{province['name_nl']}"
service_id: "{service['id']}"
alternate:
  fr: "/fr/provinces/{province['fr']}/{service['fr']['slug']}/"
  en: "/en/provinces/{province['en']}/{service['en']['slug']}/"
  nl: "/nl/provincies/{province['nl']}/{service['nl']['slug']}/"
---
"""
            path_nl = os.path.join(BASE_DIR, "nl", "provincies", province['nl'], f"{service['nl']['slug']}.html")
            os.makedirs(os.path.dirname(path_nl), exist_ok=True)
            with open(path_nl, 'w', encoding='utf-8') as f:
                f.write(content_nl)
            count += 1

            # English page
            content_en = f"""---
layout: province-service
lang: en
title: "{service['en']['name']} {province['name_en']} | Locksmith 24/7 | 0495 205 400"
description: "{service['en']['name']} in {province['name_en']} province. Fast intervention in all municipalities. Free quote 24/7."
province_slug: "{province['en']}"
province_name: "{province['name_en']}"
service_id: "{service['id']}"
alternate:
  fr: "/fr/provinces/{province['fr']}/{service['fr']['slug']}/"
  en: "/en/provinces/{province['en']}/{service['en']['slug']}/"
  nl: "/nl/provincies/{province['nl']}/{service['nl']['slug']}/"
---
"""
            path_en = os.path.join(BASE_DIR, "en", "provinces", province['en'], f"{service['en']['slug']}.html")
            os.makedirs(os.path.dirname(path_en), exist_ok=True)
            with open(path_en, 'w', encoding='utf-8') as f:
                f.write(content_en)
            count += 1

    return count


def main():
    print("=== Generating Province Service Pages ===\n")

    page_count = generate_province_service_pages()
    print(f"Generated: {page_count} province service pages")

    print(f"\nTotal: 8 provinces x 7 services x 3 languages = {page_count} pages")


if __name__ == "__main__":
    main()
