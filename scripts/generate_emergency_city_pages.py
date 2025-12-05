#!/usr/bin/env python3
"""
Generate emergency city pages for all languages.
19 cities x 6 emergency types x 3 languages = 342 pages
"""

import os

BASE_DIR = "/Users/hiliyeh/Desktop/project/Janssens"

# Cities with emergency pages (from archive)
CITIES = [
    {"slug": "anderlecht", "name": "Anderlecht"},
    {"slug": "braine-lalleud", "name": "Braine-l'Alleud"},
    {"slug": "bruxelles-ville", "name": "Bruxelles-Ville", "name_en": "City of Brussels", "name_nl": "Stad Brussel"},
    {"slug": "etterbeek", "name": "Etterbeek"},
    {"slug": "forest", "name": "Forest", "name_nl": "Vorst"},
    {"slug": "ixelles", "name": "Ixelles", "name_nl": "Elsene"},
    {"slug": "leuven", "name": "Leuven", "name_fr": "Louvain"},
    {"slug": "molenbeek-saint-jean", "name": "Molenbeek-Saint-Jean", "name_nl": "Sint-Jans-Molenbeek"},
    {"slug": "nivelles", "name": "Nivelles", "name_nl": "Nijvel"},
    {"slug": "ottignies-louvain-la-neuve", "name": "Ottignies-Louvain-la-Neuve"},
    {"slug": "saint-gilles", "name": "Saint-Gilles", "name_nl": "Sint-Gillis"},
    {"slug": "schaerbeek", "name": "Schaerbeek", "name_nl": "Schaarbeek"},
    {"slug": "uccle", "name": "Uccle", "name_nl": "Ukkel"},
    {"slug": "vilvoorde", "name": "Vilvoorde", "name_fr": "Vilvorde"},
    {"slug": "waterloo", "name": "Waterloo"},
    {"slug": "wavre", "name": "Wavre", "name_nl": "Waver"},
    {"slug": "woluwe-saint-lambert", "name": "Woluwe-Saint-Lambert", "name_nl": "Sint-Lambrechts-Woluwe"},
    {"slug": "woluwe-saint-pierre", "name": "Woluwe-Saint-Pierre", "name_nl": "Sint-Pieters-Woluwe"},
    {"slug": "zaventem", "name": "Zaventem"},
]

# Emergency types with slugs for each language
EMERGENCIES = [
    {
        "id": "locked-out",
        "fr": {"slug": "porte-claquee"},
        "en": {"slug": "locked-out"},
        "nl": {"slug": "dichtgevallen-deur"}
    },
    {
        "id": "broken-key",
        "fr": {"slug": "cle-cassee-serrure"},
        "en": {"slug": "broken-key-lock"},
        "nl": {"slug": "gebroken-sleutel-slot"}
    },
    {
        "id": "burglary",
        "fr": {"slug": "cambriolage"},
        "en": {"slug": "burglary"},
        "nl": {"slug": "inbraak"}
    },
    {
        "id": "armored-door",
        "fr": {"slug": "porte-blindee-bloquee"},
        "en": {"slug": "armored-door-locked"},
        "nl": {"slug": "gepantserde-deur-geblokkeerd"}
    },
    {
        "id": "night-locksmith",
        "fr": {"slug": "serrurier-nuit"},
        "en": {"slug": "night-locksmith"},
        "nl": {"slug": "nacht-slotenmaker"}
    },
    {
        "id": "sunday-locksmith",
        "fr": {"slug": "serrurier-dimanche"},
        "en": {"slug": "sunday-locksmith"},
        "nl": {"slug": "zondag-slotenmaker"}
    }
]

# Language config
LANGS = [
    {"code": "fr", "folder": "urgence"},
    {"code": "en", "folder": "emergency"},
    {"code": "nl", "folder": "noodgeval"}
]

def get_city_name(city, lang):
    """Get city name for specific language"""
    if lang == "fr":
        return city.get("name_fr", city["name"])
    elif lang == "en":
        return city.get("name_en", city["name"])
    elif lang == "nl":
        return city.get("name_nl", city["name"])
    return city["name"]

def generate_page(city, emergency, lang_config):
    """Generate a single emergency city page"""
    lang = lang_config["code"]
    folder = lang_config["folder"]
    city_slug = city["slug"]
    city_name = get_city_name(city, lang)
    emergency_slug = emergency[lang]["slug"]
    emergency_id = emergency["id"]

    # Build alternates
    alternates = {}
    for l in LANGS:
        l_code = l["code"]
        l_folder = l["folder"]
        l_emergency_slug = emergency[l_code]["slug"]
        if l_code == "fr":
            alternates[l_code] = f"/fr/{l_folder}/{city_slug}/{l_emergency_slug}/"
        else:
            alternates[l_code] = f"/{l_code}/{l_folder}/{city_slug}/{l_emergency_slug}/"

    # Build title
    if lang == "fr":
        title = f"{emergency_slug.replace('-', ' ').title()} {city_name} | Janssens Serrurier"
    elif lang == "en":
        title = f"{emergency_slug.replace('-', ' ').title()} {city_name} | Janssens Locksmith"
    else:
        title = f"{emergency_slug.replace('-', ' ').title()} {city_name} | Janssens Slotenmaker"

    content = f'''---
layout: emergency-city
lang: {lang}
title: "{title}"
description: "{emergency_slug.replace('-', ' ').title()} {city_name}"
emergency_id: "{emergency_id}"
city_slug: "{city_slug}"
city_name: "{city_name}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---

'''
    return content

def main():
    count = 0

    for lang_config in LANGS:
        lang = lang_config["code"]
        folder = lang_config["folder"]

        for city in CITIES:
            city_slug = city["slug"]

            for emergency in EMERGENCIES:
                emergency_slug = emergency[lang]["slug"]

                # Determine base path
                if lang == "fr":
                    dir_path = os.path.join(BASE_DIR, "fr", folder, city_slug)
                else:
                    dir_path = os.path.join(BASE_DIR, lang, folder, city_slug)

                # Create directory
                os.makedirs(dir_path, exist_ok=True)

                # Generate page content
                content = generate_page(city, emergency, lang_config)

                # Write file
                file_path = os.path.join(dir_path, "index.html") if emergency_slug == emergency[lang]["slug"] else os.path.join(dir_path, f"{emergency_slug}.html")
                # Use subfolder with index.html for clean URLs
                sub_dir = os.path.join(dir_path, emergency_slug)
                os.makedirs(sub_dir, exist_ok=True)
                file_path = os.path.join(sub_dir, "index.html")

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

                count += 1
                print(f"Created: {file_path}")

    print(f"\n=== Generated {count} emergency city pages ===")

if __name__ == "__main__":
    main()
