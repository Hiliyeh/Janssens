#!/usr/bin/env python3
"""Update province page titles with SEO format including phone number."""

import os
import re

BASE_DIR = "/Users/hiliyeh/Desktop/project/Janssens"
PHONE = "0495 205 400"

# Province configurations by language
PROVINCES = {
    'fr': {
        'folder': 'fr/provinces',
        'suffix': f'Serrurier 24h/24 | {PHONE}',
        'provinces': {
            'anvers': 'Anvers',
            'flandre-occidentale': 'Flandre-Occidentale',
            'flandre-orientale': 'Flandre-Orientale',
            'hainaut': 'Hainaut',
            'liege': 'Liège',
            'limbourg': 'Limbourg',
            'luxembourg': 'Luxembourg',
            'namur': 'Namur',
        }
    },
    'en': {
        'folder': 'en/provinces',
        'suffix': f'Locksmith 24/7 | {PHONE}',
        'provinces': {
            'antwerp': 'Antwerp',
            'east-flanders': 'East Flanders',
            'west-flanders': 'West Flanders',
            'hainaut': 'Hainaut',
            'liege': 'Liège',
            'limburg': 'Limburg',
            'luxembourg': 'Luxembourg',
            'namur': 'Namur',
        }
    },
    'nl': {
        'folder': 'nl/provincies',
        'suffix': f'Slotenmaker 24/7 | {PHONE}',
        'provinces': {
            'antwerpen': 'Antwerpen',
            'oost-vlaanderen': 'Oost-Vlaanderen',
            'west-vlaanderen': 'West-Vlaanderen',
            'henegouwen': 'Henegouwen',
            'luik': 'Luik',
            'limburg': 'Limburg',
            'luxemburg': 'Luxemburg',
            'namen': 'Namen',
        }
    }
}

SERVICE_NAMES = {
    'fr': 'Serrurier',
    'en': 'Locksmith',
    'nl': 'Slotenmaker'
}

def update_file_title(file_path, new_title):
    """Update the title in a Jekyll front matter file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace title line
    new_content = re.sub(
        r'^title:\s*["\'].*["\']',
        f'title: "{new_title}"',
        content,
        flags=re.MULTILINE
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def process_province_pages():
    """Process all province pages."""
    updated = 0

    for lang, config in PROVINCES.items():
        folder_path = os.path.join(BASE_DIR, config['folder'])
        service_name = SERVICE_NAMES[lang]

        if not os.path.exists(folder_path):
            print(f"Folder not found: {folder_path}")
            continue

        for province_slug, province_name in config['provinces'].items():
            file_path = os.path.join(folder_path, province_slug, 'index.html')
            if os.path.exists(file_path):
                new_title = f"{service_name} {province_name} | {config['suffix']}"
                update_file_title(file_path, new_title)
                print(f"Updated: {file_path}")
                updated += 1

    return updated

def main():
    print("Updating province page titles with SEO format...")
    count = process_province_pages()
    print(f"\nTotal: {count} pages updated")

if __name__ == "__main__":
    main()
