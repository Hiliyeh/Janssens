#!/usr/bin/env python3
"""
Generate service and brand pages for FR, EN, NL with localized URLs
"""
import os

BASE_PATH = '/Users/hiliyeh/Desktop/project/Janssens'

# Services with localized slugs
SERVICES = [
    {'id': 'door-opening', 'fr': 'ouverture-porte', 'en': 'door-opening', 'nl': 'deuropening'},
    {'id': 'lock-replacement', 'fr': 'remplacement-serrure', 'en': 'lock-replacement', 'nl': 'slotvervanging'},
    {'id': 'key-duplication', 'fr': 'double-cles', 'en': 'key-duplication', 'nl': 'sleutel-kopie'},
    {'id': 'door-reinforcement', 'fr': 'blindage-porte', 'en': 'door-reinforcement', 'nl': 'deurbepantsering'},
    {'id': 'safe', 'fr': 'coffre-fort', 'en': 'safe', 'nl': 'kluis'},
    {'id': 'automotive', 'fr': 'serrurerie-automobile', 'en': 'automotive-locksmith', 'nl': 'auto-slotenmaker'},
]

# Brands (same slug for all languages)
BRANDS = [
    {'id': 'fichet', 'slug': 'fichet', 'name': 'Fichet'},
    {'id': 'bricard', 'slug': 'bricard', 'name': 'Bricard'},
    {'id': 'vachette', 'slug': 'vachette', 'name': 'Vachette'},
    {'id': 'mul-t-lock', 'slug': 'mul-t-lock', 'name': 'Mul-T-Lock'},
    {'id': 'picard', 'slug': 'picard', 'name': 'Picard'},
]

# Language config
LANG_CONFIG = {
    'fr': {'services_folder': 'services', 'brands_folder': 'marques'},
    'en': {'services_folder': 'services', 'brands_folder': 'brands'},
    'nl': {'services_folder': 'diensten', 'brands_folder': 'merken'},
}

def generate_service_page(service, lang):
    """Generate a single service page"""
    config = LANG_CONFIG[lang]
    slug = service[lang]

    # Build alternate URLs
    alternates = []
    for l, cfg in LANG_CONFIG.items():
        s = service[l]
        alternates.append(f"  {l}: \"/{l}/{cfg['services_folder']}/{s}/\"")

    content = f"""---
layout: service
lang: {lang}
title: "{service['id'].replace('-', ' ').title()} | Janssens"
description: "Service description"
service_id: "{service['id']}"
alternate:
{chr(10).join(alternates)}
---
"""

    # Create directory
    folder_path = os.path.join(BASE_PATH, lang, config['services_folder'], slug)
    os.makedirs(folder_path, exist_ok=True)

    # Write file
    file_path = os.path.join(folder_path, 'index.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return file_path

def generate_brand_page(brand, lang):
    """Generate a single brand page"""
    config = LANG_CONFIG[lang]

    # Build alternate URLs
    alternates = []
    for l, cfg in LANG_CONFIG.items():
        alternates.append(f"  {l}: \"/{l}/{cfg['brands_folder']}/{brand['slug']}/\"")

    content = f"""---
layout: brand
lang: {lang}
title: "Expert {brand['name']} | Janssens"
description: "{brand['name']} locksmith expert"
brand_id: "{brand['id']}"
alternate:
{chr(10).join(alternates)}
---
"""

    # Create directory
    folder_path = os.path.join(BASE_PATH, lang, config['brands_folder'], brand['slug'])
    os.makedirs(folder_path, exist_ok=True)

    # Write file
    file_path = os.path.join(folder_path, 'index.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return file_path

def main():
    print("Generating service pages...")
    for service in SERVICES:
        for lang in ['fr', 'en', 'nl']:
            path = generate_service_page(service, lang)
            print(f"  Created: {path}")

    print(f"\nGenerated {len(SERVICES) * 3} service pages")

    print("\nGenerating brand pages...")
    for brand in BRANDS:
        for lang in ['fr', 'en', 'nl']:
            path = generate_brand_page(brand, lang)
            print(f"  Created: {path}")

    print(f"\nGenerated {len(BRANDS) * 3} brand pages")

if __name__ == '__main__':
    main()
