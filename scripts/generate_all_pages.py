#!/usr/bin/env python3
"""
Unified page generator - reads from _data/*.yml files
Generates: city pages, city-service pages, emergency-city pages, service pages, brand pages, guide pages
"""

import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_yaml(filename):
    """Load a YAML file from _data folder."""
    path = os.path.join(BASE_DIR, '_data', filename)
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def write_page(path, content):
    """Write a page to disk."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Language configurations
LANGS = {
    'fr': {'cities': 'cities', 'services': 'services', 'emergency': 'urgence', 'brands': 'marques', 'guides': 'guides'},
    'en': {'cities': 'cities', 'services': 'services', 'emergency': 'emergency', 'brands': 'brands', 'guides': 'guides'},
    'nl': {'cities': 'cities', 'services': 'diensten', 'emergency': 'noodgeval', 'brands': 'merken', 'guides': 'gidsen'}
}

def generate_city_service_pages():
    """Generate city-service pages from cities.yml and services.yml."""
    cities_data = load_yaml('cities.yml')
    services = load_yaml('services.yml')

    # Get cities with subpages
    cities_with_subpages = cities_data.get('cities_with_subpages', [])

    # Build city name lookup from all regions
    city_names = {}
    for region in ['brussels', 'walloon_brabant', 'flemish_brabant']:
        for city in cities_data.get(region, []):
            city_names[city['slug']] = city['name']

    count = 0
    for lang in LANGS:
        cities_folder = LANGS[lang]['cities']
        for city_slug in cities_with_subpages:
            city_name = city_names.get(city_slug, city_slug.replace('-', ' ').title())

            for service in services:
                service_id = service['id']
                s_data = service[lang]
                service_slug = s_data['slug']
                service_name = s_data['name']

                # Build alternates
                alternates = {l: f"/{l}/{LANGS[l]['cities']}/{city_slug}/{service[l]['slug']}/" for l in LANGS}

                content = f"""---
layout: city-service
lang: {lang}
title: "{service_name} {city_name} | Janssens Serrurier"
description: "{service_name} à {city_name}. Intervention rapide 24h/24, 7j/7."
city_name: "{city_name}"
city_slug: "{city_slug}"
service_id: "{service_id}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---
"""
                path = os.path.join(BASE_DIR, lang, cities_folder, city_slug, f"{service_slug}.html")
                write_page(path, content)
                count += 1

    return count

def generate_emergency_city_pages():
    """Generate emergency-city pages from cities.yml and emergencies.yml."""
    cities_data = load_yaml('cities.yml')
    emergencies = load_yaml('emergencies.yml')

    # Cities with emergency pages (subset)
    emergency_cities = cities_data.get('cities_with_emergency_pages', cities_data.get('cities_with_subpages', [])[:19])

    # Build city name lookup
    city_names = {}
    for region in ['brussels', 'walloon_brabant', 'flemish_brabant']:
        for city in cities_data.get(region, []):
            city_names[city['slug']] = city['name']

    count = 0
    for lang in LANGS:
        emergency_folder = LANGS[lang]['emergency']
        for city_slug in emergency_cities:
            city_name = city_names.get(city_slug, city_slug.replace('-', ' ').title())

            for emergency in emergencies:
                emergency_id = emergency['id']
                e_data = emergency[lang]
                emergency_slug = e_data['slug']

                # Build alternates
                alternates = {l: f"/{l}/{LANGS[l]['emergency']}/{city_slug}/{emergency[l]['slug']}/" for l in LANGS}

                content = f"""---
layout: emergency-city
lang: {lang}
title: "{e_data['name']} {city_name} | Janssens Serrurier"
description: "{e_data['name']} à {city_name}. Intervention urgente 24h/24."
city_name: "{city_name}"
city_slug: "{city_slug}"
emergency_id: "{emergency_id}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---
"""
                path = os.path.join(BASE_DIR, lang, emergency_folder, city_slug, f"{emergency_slug}.html")
                write_page(path, content)
                count += 1

    return count

def generate_service_pages():
    """Generate main service pages from services.yml."""
    services = load_yaml('services.yml')

    count = 0
    for lang in LANGS:
        services_folder = LANGS[lang]['services']
        for service in services:
            service_id = service['id']
            s_data = service[lang]

            alternates = {l: f"/{l}/{LANGS[l]['services']}/{service[l]['slug']}/" for l in LANGS}

            content = f"""---
layout: service
lang: {lang}
title: "{s_data['title']} | Janssens Serrurier"
description: "{s_data['description']}"
service_id: "{service_id}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---
"""
            path = os.path.join(BASE_DIR, lang, services_folder, s_data['slug'], 'index.html')
            write_page(path, content)
            count += 1

    return count

def generate_brand_pages():
    """Generate brand pages from brands.yml."""
    brands = load_yaml('brands.yml')

    count = 0
    for lang in LANGS:
        brands_folder = LANGS[lang]['brands']
        for brand in brands:
            alternates = {l: f"/{l}/{LANGS[l]['brands']}/{brand['slug']}/" for l in LANGS}

            content = f"""---
layout: brand
lang: {lang}
title: "Serrurier {brand['name']} | Janssens Serrurier"
description: "{brand['description'][lang]}"
brand_id: "{brand['id']}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---
"""
            path = os.path.join(BASE_DIR, lang, brands_folder, brand['slug'], 'index.html')
            write_page(path, content)
            count += 1

    return count

def generate_emergency_pages():
    """Generate main emergency pages from emergencies.yml."""
    emergencies = load_yaml('emergencies.yml')

    count = 0
    for lang in LANGS:
        emergency_folder = LANGS[lang]['emergency']
        for emergency in emergencies:
            e_data = emergency[lang]

            alternates = {l: f"/{l}/{LANGS[l]['emergency']}/{emergency[l]['slug']}/" for l in LANGS}

            content = f"""---
layout: emergency
lang: {lang}
title: "{e_data['name']} | Janssens Serrurier"
description: "{e_data.get('description', e_data['name'])}"
emergency_id: "{emergency['id']}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---
"""
            path = os.path.join(BASE_DIR, lang, emergency_folder, e_data['slug'], 'index.html')
            write_page(path, content)
            count += 1

    return count

def main():
    """Run all generators."""
    print("=== Unified Page Generator ===\n")

    generators = [
        ("City-Service pages", generate_city_service_pages),
        ("Emergency-City pages", generate_emergency_city_pages),
        ("Service pages", generate_service_pages),
        ("Brand pages", generate_brand_pages),
        ("Emergency pages", generate_emergency_pages),
    ]

    total = 0
    for name, func in generators:
        try:
            count = func()
            print(f"{name}: {count}")
            total += count
        except Exception as e:
            print(f"{name}: ERROR - {e}")

    print(f"\nTotal: {total} pages generated")

if __name__ == "__main__":
    main()
