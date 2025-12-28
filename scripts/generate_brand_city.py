#!/usr/bin/env python3
"""
Generate Brand + City pages for Janssens Serrurier
Creates 645 pages (5 brands × 43 cities × 3 languages)
"""

import os
import yaml

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '_data')

# Load data
with open(os.path.join(DATA_DIR, 'brands.yml'), 'r', encoding='utf-8') as f:
    brands = yaml.safe_load(f)

with open(os.path.join(DATA_DIR, 'cities.yml'), 'r', encoding='utf-8') as f:
    cities_data = yaml.safe_load(f)

# Get cities with subpages
cities_with_subpages = cities_data.get('cities_with_subpages', [])

# Build city list from all regions
all_cities = []
for region in ['brussels', 'walloon_brabant', 'flemish_brabant']:
    if region in cities_data:
        for city in cities_data[region]:
            if city.get('slug') in cities_with_subpages or city.get('has_subpages'):
                all_cities.append(city)

# Language configurations with SEO phone number
languages = {
    'fr': {
        'folder': 'fr',
        'brands_folder': 'marques',
        'title_template': 'Expert {brand} {city} | Serrurier 24h/24 | 0495 205 400',
        'description_template': 'Serrurier expert {brand} à {city}. Intervention 24h/24 en 30 min. Cylindres, serrures, clés {brand}. Devis gratuit. Appelez 0495 205 400.'
    },
    'en': {
        'folder': 'en',
        'brands_folder': 'brands',
        'title_template': '{brand} Expert {city} | Locksmith 24/7 | 0495 205 400',
        'description_template': '{brand} expert locksmith in {city}. 24/7 service within 30 min. {brand} cylinders, locks, keys. Free quote. Call 0495 205 400.'
    },
    'nl': {
        'folder': 'nl',
        'brands_folder': 'merken',
        'title_template': '{brand} Expert {city} | Slotenmaker 24/7 | 0495 205 400',
        'description_template': '{brand} expert slotenmaker in {city}. 24/7 service binnen 30 min. {brand} cilinders, sloten, sleutels. Gratis offerte. Bel 0495 205 400.'
    }
}

def get_city_slug(city, lang):
    """Get the appropriate slug for a city in a given language"""
    if lang == 'nl' and city.get('slug_nl'):
        return city['slug_nl']
    elif lang == 'en' and city.get('slug_en'):
        return city['slug_en']
    return city['slug']

def get_city_name(city, lang):
    """Get the appropriate name for a city in a given language"""
    if lang == 'nl' and city.get('name_nl'):
        return city['name_nl']
    elif lang == 'en' and city.get('name_en'):
        return city['name_en']
    return city['name']

def generate_page(brand, city, lang, lang_config):
    """Generate a single brand-city page"""
    city_slug = get_city_slug(city, lang)
    city_name = get_city_name(city, lang)

    # Build alternates for hreflang
    alternates = {
        'fr': f"/fr/{languages['fr']['brands_folder']}/{brand['slug']}/{get_city_slug(city, 'fr')}/",
        'en': f"/en/{languages['en']['brands_folder']}/{brand['slug']}/{get_city_slug(city, 'en')}/",
        'nl': f"/nl/{languages['nl']['brands_folder']}/{brand['slug']}/{get_city_slug(city, 'nl')}/"
    }

    content = f"""---
layout: brand-city
lang: {lang}
brand_id: {brand['id']}
city_name: "{city_name}"
city_slug: "{city_slug}"
title: "{lang_config['title_template'].format(brand=brand['name'], city=city_name)}"
description: "{lang_config['description_template'].format(brand=brand['name'], city=city_name)}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---
"""
    return content

def main():
    total_created = 0

    for lang, lang_config in languages.items():
        lang_folder = lang_config['folder']
        brands_folder = lang_config['brands_folder']

        for brand in brands:
            # Create brand folder if not exists
            brand_dir = os.path.join(BASE_DIR, lang_folder, brands_folder, brand['slug'])
            os.makedirs(brand_dir, exist_ok=True)

            for city in all_cities:
                city_slug = get_city_slug(city, lang)

                # Create city folder under brand
                city_dir = os.path.join(brand_dir, city_slug)
                os.makedirs(city_dir, exist_ok=True)

                # Generate page content
                content = generate_page(brand, city, lang, lang_config)

                # Write file
                filepath = os.path.join(city_dir, 'index.html')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

                total_created += 1

    print(f"Created {total_created} brand-city pages")
    print(f"  - {len(brands)} brands")
    print(f"  - {len(all_cities)} cities")
    print(f"  - {len(languages)} languages")

if __name__ == '__main__':
    main()
