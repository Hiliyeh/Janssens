#!/usr/bin/env python3
"""Update license plate page titles with SEO format including phone number."""

import os
import re

BASE_DIR = "/Users/hiliyeh/Desktop/project/Janssens"
PHONE = "0495 205 400"

# Language configurations
LANG_CONFIG = {
    'fr': {
        'folder': 'fr/plaque-immatriculation',
        'service_name': "Plaque d'immatriculation",
        'suffix': f'Serrurier 24h/24 | {PHONE}',
        'location': 'Bruxelles'
    },
    'en': {
        'folder': 'en/license-plate',
        'service_name': 'License Plate',
        'suffix': f'Locksmith 24/7 | {PHONE}',
        'location': 'Brussels'
    },
    'nl': {
        'folder': 'nl/nummerplaat',
        'service_name': 'Nummerplaat',
        'suffix': f'Slotenmaker 24/7 | {PHONE}',
        'location': 'Brussel'
    }
}

# City name mapping for display
CITY_NAMES = {
    'fr': {
        'bruxelles': 'Bruxelles',
        'ixelles': 'Ixelles',
        'uccle': 'Uccle',
        'forest': 'Forest',
        'schaerbeek': 'Schaerbeek',
        'saint-gilles': 'Saint-Gilles',
        'anderlecht': 'Anderlecht',
        'molenbeek-saint-jean': 'Molenbeek-Saint-Jean',
        'auderghem': 'Auderghem',
        'woluwe-saint-lambert': 'Woluwe-Saint-Lambert',
        'woluwe-saint-pierre': 'Woluwe-Saint-Pierre',
        'berchem-sainte-agathe': 'Berchem-Sainte-Agathe',
        'watermael-boitsfort': 'Watermael-Boitsfort',
        'etterbeek': 'Etterbeek',
        'evere': 'Evere',
        'ganshoren': 'Ganshoren',
        'jette': 'Jette',
        'koekelberg': 'Koekelberg',
        'saint-josse-ten-noode': 'Saint-Josse-ten-Noode',
    },
    'en': {
        'brussels': 'Brussels',
        'ixelles': 'Ixelles',
        'uccle': 'Uccle',
        'forest': 'Forest',
        'schaerbeek': 'Schaerbeek',
        'saint-gilles': 'Saint-Gilles',
        'anderlecht': 'Anderlecht',
        'molenbeek-saint-jean': 'Molenbeek-Saint-Jean',
        'auderghem': 'Auderghem',
        'woluwe-saint-lambert': 'Woluwe-Saint-Lambert',
        'woluwe-saint-pierre': 'Woluwe-Saint-Pierre',
        'berchem-sainte-agathe': 'Berchem-Sainte-Agathe',
        'watermael-boitsfort': 'Watermael-Boitsfort',
        'etterbeek': 'Etterbeek',
        'evere': 'Evere',
        'ganshoren': 'Ganshoren',
        'jette': 'Jette',
        'koekelberg': 'Koekelberg',
        'saint-josse-ten-noode': 'Saint-Josse-ten-Noode',
    },
    'nl': {
        'brussel': 'Brussel',
        'elsene': 'Elsene',
        'ukkel': 'Ukkel',
        'vorst': 'Vorst',
        'schaarbeek': 'Schaarbeek',
        'sint-gillis': 'Sint-Gillis',
        'anderlecht': 'Anderlecht',
        'sint-jans-molenbeek': 'Sint-Jans-Molenbeek',
        'oudergem': 'Oudergem',
        'sint-lambrechts-woluwe': 'Sint-Lambrechts-Woluwe',
        'sint-pieters-woluwe': 'Sint-Pieters-Woluwe',
        'sint-agatha-berchem': 'Sint-Agatha-Berchem',
        'watermaal-bosvoorde': 'Watermaal-Bosvoorde',
        'etterbeek': 'Etterbeek',
        'evere': 'Evere',
        'ganshoren': 'Ganshoren',
        'jette': 'Jette',
        'koekelberg': 'Koekelberg',
        'sint-joost-ten-node': 'Sint-Joost-ten-Node',
    }
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

def process_license_plate_pages():
    """Process all license plate pages."""
    updated = 0

    for lang, config in LANG_CONFIG.items():
        folder_path = os.path.join(BASE_DIR, config['folder'])

        if not os.path.exists(folder_path):
            print(f"Folder not found: {folder_path}")
            continue

        # Process index page
        index_file = os.path.join(folder_path, 'index.html')
        if os.path.exists(index_file):
            new_title = f"{config['service_name']} {config['location']} | {config['suffix']}"
            update_file_title(index_file, new_title)
            print(f"Updated: {index_file}")
            updated += 1

        # Process city pages
        city_names = CITY_NAMES.get(lang, {})
        for city_slug in os.listdir(folder_path):
            city_path = os.path.join(folder_path, city_slug)
            if os.path.isdir(city_path):
                city_file = os.path.join(city_path, 'index.html')
                if os.path.exists(city_file):
                    # Get proper city name or capitalize slug
                    city_name = city_names.get(city_slug, city_slug.replace('-', ' ').title())
                    new_title = f"{config['service_name']} {city_name} | {config['suffix']}"
                    update_file_title(city_file, new_title)
                    print(f"Updated: {city_file}")
                    updated += 1

    return updated

def main():
    print("Updating license plate page titles with SEO format...")
    count = process_license_plate_pages()
    print(f"\nTotal: {count} pages updated")

if __name__ == "__main__":
    main()
