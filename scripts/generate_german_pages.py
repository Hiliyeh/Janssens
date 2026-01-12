#!/usr/bin/env python3
"""Generate German pages for the 9 German-speaking municipalities in Belgium."""

import os
import yaml

# Base path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '_data')

# Load cities from YAML
with open(os.path.join(DATA_DIR, 'cities.yml'), 'r', encoding='utf-8') as f:
    cities_data = yaml.safe_load(f)

# Load services from YAML
with open(os.path.join(DATA_DIR, 'services.yml'), 'r', encoding='utf-8') as f:
    services_data = yaml.safe_load(f)

# Load brands from YAML
with open(os.path.join(DATA_DIR, 'brands.yml'), 'r', encoding='utf-8') as f:
    brands_data = yaml.safe_load(f)

# Get German-speaking cities
GERMAN_CITIES = cities_data.get('german_speaking', [])

# Services for German pages (exclude brussels_only services)
SERVICES = {}
for service in services_data:
    if not service.get('brussels_only', False):
        service_id = service['id']
        de_data = service.get('de', {})
        if de_data:
            SERVICES[service_id] = {
                "slug": de_data['slug'],
                "name": de_data['name'],
                "title": de_data['title'],
                "desc": f"{de_data['name']} in {{city}}. Professioneller Schlüsseldienst, 24/7 verfügbar. Kostenloser Kostenvoranschlag. Rufen Sie 0495 205 400 an."
            }

# German folder config
LANG = "de"
CITIES_FOLDER = "gemeinden"
SERVICES_FOLDER = "dienstleistungen"
BRANDS_FOLDER = "marken"

def generate_city_index(city_data):
    """Generate city index page."""
    city_name = city_data['name']
    city_slug = city_data['slug']

    content = f"""---
layout: city
lang: de
title: "Schlüsseldienst {city_name} | 24/7 Notdienst | 0495 205 400"
description: "Schlüsseldienst in {city_name}. Schneller Einsatz in 30 Minuten, 24/7 verfügbar. Türöffnung, Schlossaustausch. Kostenloser Kostenvoranschlag. Rufen Sie 0495 205 400 an."
city_name: "{city_name}"
city_slug: "{city_slug}"
alternate:
  de: "/de/{CITIES_FOLDER}/{city_slug}/"
---
"""

    output_dir = os.path.join(BASE_DIR, LANG, CITIES_FOLDER, city_slug)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "index.html")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path

def generate_city_service(city_data, service_id, service_info):
    """Generate city-service page."""
    city_name = city_data['name']
    city_slug = city_data['slug']
    service_slug = service_info['slug']
    service_name = service_info['name']
    service_desc = service_info['desc'].format(city=city_name)

    content = f"""---
layout: city-service
lang: de
title: "{service_name} {city_name} | Schlüsseldienst 24/7 | 0495 205 400"
description: "{service_desc}"
city_name: "{city_name}"
city_slug: "{city_slug}"
service_id: "{service_id}"
alternate:
  de: "/de/{CITIES_FOLDER}/{city_slug}/{service_slug}/"
---
"""

    output_dir = os.path.join(BASE_DIR, LANG, CITIES_FOLDER, city_slug)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{service_slug}.html")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path

def generate_brand_page(brand_data):
    """Generate brand index page."""
    brand_name = brand_data['name']
    brand_slug = brand_data['slug']
    brand_id = brand_data['id']
    brand_desc = brand_data['description'].get('de', brand_data['description'].get('en', ''))

    content = f"""---
layout: brand
lang: de
title: "{brand_name} Experte | Schlüsseldienst | 0495 205 400"
description: "{brand_desc}"
brand_id: "{brand_id}"
alternate:
  fr: "/fr/marques/{brand_slug}/"
  en: "/en/brands/{brand_slug}/"
  nl: "/nl/merken/{brand_slug}/"
  de: "/de/{BRANDS_FOLDER}/{brand_slug}/"
---
"""

    output_dir = os.path.join(BASE_DIR, LANG, BRANDS_FOLDER, brand_slug)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "index.html")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path

def generate_brand_city(brand_data, city_data):
    """Generate brand-city page."""
    brand_name = brand_data['name']
    brand_slug = brand_data['slug']
    brand_id = brand_data['id']
    city_name = city_data['name']
    city_slug = city_data['slug']

    content = f"""---
layout: brand-city
lang: de
brand_id: {brand_id}
city_name: "{city_name}"
city_slug: "{city_slug}"
title: "{brand_name} Experte {city_name} | Schlüsseldienst 24/7 | 0495 205 400"
description: "Zertifizierter {brand_name} Schlüsseldienst in {city_name}. Einsatz 24/7 in 30 Minuten. Kostenloser Kostenvoranschlag. Rufen Sie 0495 205 400 an."
alternate:
  de: "/de/{BRANDS_FOLDER}/{brand_slug}/{city_slug}/"
---
"""

    output_dir = os.path.join(BASE_DIR, LANG, BRANDS_FOLDER, brand_slug, city_slug)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "index.html")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path

def generate_service_index(service_id, service_info):
    """Generate service index page."""
    service_slug = service_info['slug']
    service_name = service_info['name']
    service_title = service_info.get('title', service_name)

    content = f"""---
layout: service
lang: de
title: "{service_title} | Schlüsseldienst 24/7 | 0495 205 400"
description: "{service_name} Service. Professioneller Schlüsseldienst in der Deutschsprachigen Gemeinschaft Belgiens. 24/7 verfügbar. Kostenloser Kostenvoranschlag."
service_id: "{service_id}"
alternate:
  de: "/de/{SERVICES_FOLDER}/{service_slug}/"
---
"""

    output_dir = os.path.join(BASE_DIR, LANG, SERVICES_FOLDER, service_slug)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "index.html")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path

def generate_german_index():
    """Generate German homepage."""
    content = """---
layout: home
lang: de
title: "Schlüsseldienst Deutschsprachige Gemeinschaft | 24/7 | 0495 205 400"
description: "Professioneller Schlüsseldienst in der Deutschsprachigen Gemeinschaft Belgiens. Eupen, Sankt Vith, Kelmis. Einsatz in 30 Minuten, 24/7 verfügbar."
alternate:
  fr: "/"
  en: "/en/"
  nl: "/nl/"
  de: "/de/"
---
"""

    output_dir = os.path.join(BASE_DIR, LANG)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "index.html")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path

def main():
    """Generate all German pages."""

    total_created = 0

    # Generate German homepage
    generate_german_index()
    print("Created: /de/index.html")
    total_created += 1

    # Generate city pages
    city_pages = 0
    for city in GERMAN_CITIES:
        # City index
        generate_city_index(city)
        city_pages += 1

        # City-service pages
        for service_id, service_info in SERVICES.items():
            generate_city_service(city, service_id, service_info)
            city_pages += 1

    print(f"Created: {city_pages} city & city-service pages")
    total_created += city_pages

    # Generate service pages
    service_pages = 0
    for service_id, service_info in SERVICES.items():
        generate_service_index(service_id, service_info)
        service_pages += 1

    print(f"Created: {service_pages} service pages")
    total_created += service_pages

    # Generate brand pages
    brand_pages = 0
    for brand in brands_data:
        # Brand index
        generate_brand_page(brand)
        brand_pages += 1

        # Brand-city pages
        for city in GERMAN_CITIES:
            generate_brand_city(brand, city)
            brand_pages += 1

    print(f"Created: {brand_pages} brand & brand-city pages")
    total_created += brand_pages

    print(f"\nTotal: {total_created} German pages created")

if __name__ == "__main__":
    main()
