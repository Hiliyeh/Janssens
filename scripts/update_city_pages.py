#!/usr/bin/env python3
"""
Script to update city pages with region_name and remove duplicate content
"""
import os
import re
import yaml

# Define regions and their cities
REGIONS = {
    'brussels': {
        'region_names': {'fr': 'Bruxelles', 'en': 'Brussels', 'nl': 'Brussel'},
        'cities': [
            'anderlecht', 'auderghem', 'berchem-sainte-agathe', 'bruxelles-ville',
            'etterbeek', 'evere', 'forest', 'ganshoren', 'ixelles', 'jette',
            'koekelberg', 'molenbeek-saint-jean', 'saint-gilles', 'saint-josse-ten-noode',
            'schaerbeek', 'uccle', 'watermael-boitsfort', 'woluwe-saint-lambert',
            'woluwe-saint-pierre'
        ]
    },
    'walloon_brabant': {
        'region_names': {'fr': 'Brabant wallon', 'en': 'Walloon Brabant', 'nl': 'Waals-Brabant'},
        'cities': [
            'beauvechain', 'braine-lalleud', 'braine-le-chateau', 'chastre',
            'chaumont-gistoux', 'court-saint-etienne', 'genappe', 'grez-doiceau',
            'helecine', 'incourt', 'jodoigne', 'la-hulpe', 'lasne', 'mont-saint-guibert',
            'nivelles', 'orp-jauche', 'ottignies-louvain-la-neuve', 'perwez',
            'ramillies', 'rixensart', 'tubize', 'villers-la-ville', 'walhain',
            'waterloo', 'wavre'
        ]
    },
    'flemish_brabant': {
        'region_names': {'fr': 'Brabant flamand', 'en': 'Flemish Brabant', 'nl': 'Vlaams-Brabant'},
        'cities': [
            'aarschot', 'asse', 'beersel', 'begijnendijk', 'bekkevoort', 'bertem',
            'bierbeek', 'boortmeerbeek', 'boutersem', 'diest', 'dilbeek', 'drogenbos',
            'geetbets', 'glabbeek', 'grimbergen', 'haacht', 'halle', 'herent',
            'hoegaarden', 'hoeilaart', 'holsbeek', 'huldenberg', 'kampenhout',
            'kapelle-op-den-bos', 'keerbergen', 'kortenaken', 'kortenberg', 'kraainem',
            'landen', 'lennik', 'leuven', 'linkebeek', 'londerzeel', 'lubbeek',
            'machelen', 'meise', 'oud-heverlee', 'overijse', 'rotselaar',
            'scherpenheuvel-zichem', 'sint-genesius-rode', 'sint-pieters-leeuw',
            'steenokkerzeel', 'tervuren', 'tielt-winge', 'tienen', 'tremelo',
            'vilvoorde', 'wemmel', 'wezembeek-oppem', 'zaventem', 'zemst', 'zoutleeuw'
        ]
    }
}

# Build city to region mapping
CITY_REGIONS = {}
for region_key, region_data in REGIONS.items():
    for city in region_data['cities']:
        CITY_REGIONS[city] = region_data['region_names']

def get_region_name(slug, lang):
    """Get region name for a city slug and language"""
    if slug in CITY_REGIONS:
        return CITY_REGIONS[slug].get(lang, CITY_REGIONS[slug]['fr'])
    return ''

def update_city_file(filepath, lang):
    """Update a city file with region_name and remove duplicate content"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split front matter and content
    match = re.match(r'^---\n(.*?)\n---\n?(.*)?$', content, re.DOTALL)
    if not match:
        print(f"  Skipping {filepath}: No front matter found")
        return False

    fm_content = match.group(1)
    body_content = match.group(2) or ''

    # Parse front matter
    try:
        fm = yaml.safe_load(fm_content)
    except:
        print(f"  Error parsing YAML in {filepath}")
        return False

    # Get slug from front matter or filename
    slug = fm.get('slug', os.path.basename(filepath).replace('.html', ''))

    # Add region_name if not present
    if 'region_name' not in fm:
        region_name = get_region_name(slug, lang)
        if region_name:
            fm['region_name'] = region_name

    # Reconstruct front matter
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # Write back (without body content - all content comes from layout)
    new_content = f"---\n{new_fm}---\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    base_path = '/Users/hiliyeh/Desktop/project/Janssens'

    # Process each language
    for lang, folder in [('fr', 'fr/cities'), ('en', 'en/cities'), ('nl', 'nl/cities')]:
        cities_path = os.path.join(base_path, folder)
        if not os.path.exists(cities_path):
            print(f"Skipping {folder}: directory not found")
            continue

        print(f"\nProcessing {folder}...")
        files = [f for f in os.listdir(cities_path) if f.endswith('.html')]
        updated = 0

        for filename in sorted(files):
            filepath = os.path.join(cities_path, filename)
            if update_city_file(filepath, lang):
                updated += 1

        print(f"  Updated {updated}/{len(files)} files")

if __name__ == '__main__':
    main()
