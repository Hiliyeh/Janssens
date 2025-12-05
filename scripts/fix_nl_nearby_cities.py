#!/usr/bin/env python3
"""
Fix nearby_cities slugs in NL city pages to use Dutch slugs
"""
import os
import re
import yaml

# Mapping of French slugs to Dutch slugs
FR_TO_NL_SLUGS = {
    'auderghem': 'oudergem',
    'berchem-sainte-agathe': 'sint-agatha-berchem',
    'bruxelles-ville': 'brussel-stad',
    'forest': 'vorst',
    'ixelles': 'elsene',
    'molenbeek-saint-jean': 'sint-jans-molenbeek',
    'saint-gilles': 'sint-gillis',
    'saint-josse-ten-noode': 'sint-joost-ten-node',
    'schaerbeek': 'schaarbeek',
    'uccle': 'ukkel',
    'watermael-boitsfort': 'watermaal-bosvoorde',
    'woluwe-saint-lambert': 'sint-lambrechts-woluwe',
    'woluwe-saint-pierre': 'sint-pieters-woluwe',
}

# Region mapping for NL
REGIONS = {
    'brussels': {
        'region_name': 'Brussel',
        'cities': [
            'anderlecht', 'oudergem', 'sint-agatha-berchem', 'brussel-stad',
            'etterbeek', 'evere', 'vorst', 'ganshoren', 'elsene', 'jette',
            'koekelberg', 'sint-jans-molenbeek', 'sint-gillis', 'sint-joost-ten-node',
            'schaarbeek', 'ukkel', 'watermaal-bosvoorde', 'sint-lambrechts-woluwe',
            'sint-pieters-woluwe'
        ]
    },
    'walloon_brabant': {
        'region_name': 'Waals-Brabant',
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
        'region_name': 'Vlaams-Brabant',
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
        CITY_REGIONS[city] = region_data['region_name']

def get_nl_slug(fr_slug):
    """Convert French slug to Dutch slug"""
    return FR_TO_NL_SLUGS.get(fr_slug, fr_slug)

def get_region_name(slug):
    """Get NL region name for a city slug"""
    return CITY_REGIONS.get(slug, '')

def fix_nl_city_file(filepath):
    """Fix nearby_cities slugs and add region_name"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split front matter and content
    match = re.match(r'^---\n(.*?)\n---\n?(.*)?$', content, re.DOTALL)
    if not match:
        print(f"  Skipping {filepath}: No front matter found")
        return False

    fm_content = match.group(1)

    # Parse front matter
    try:
        fm = yaml.safe_load(fm_content)
    except:
        print(f"  Error parsing YAML in {filepath}")
        return False

    modified = False

    # Get the slug for region lookup
    slug = fm.get('slug', os.path.basename(filepath).replace('.html', ''))

    # Add region_name if missing
    if 'region_name' not in fm or not fm['region_name']:
        region = get_region_name(slug)
        if region:
            fm['region_name'] = region
            modified = True

    # Fix nearby_cities slugs
    if 'nearby_cities' in fm and fm['nearby_cities']:
        for city in fm['nearby_cities']:
            if 'slug' in city:
                old_slug = city['slug']
                new_slug = get_nl_slug(old_slug)
                if old_slug != new_slug:
                    city['slug'] = new_slug
                    modified = True

    if not modified:
        return False

    # Reconstruct front matter
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # Write back
    new_content = f"---\n{new_fm}---\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    nl_cities_path = '/Users/hiliyeh/Desktop/project/Janssens/nl/cities'

    if not os.path.exists(nl_cities_path):
        print(f"Directory not found: {nl_cities_path}")
        return

    print(f"Processing NL city pages...")
    files = [f for f in os.listdir(nl_cities_path) if f.endswith('.html')]
    updated = 0

    for filename in sorted(files):
        filepath = os.path.join(nl_cities_path, filename)
        if fix_nl_city_file(filepath):
            updated += 1
            print(f"  Fixed: {filename}")

    print(f"\nUpdated {updated}/{len(files)} files")

if __name__ == '__main__':
    main()
