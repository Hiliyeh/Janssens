#!/usr/bin/env python3
"""
Generate emergency city pages for all languages.
43 cities x 6 emergency types x 3 languages = 774 pages
"""

import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '_data')

# Load cities from YAML
with open(os.path.join(DATA_DIR, 'cities.yml'), 'r', encoding='utf-8') as f:
    cities_data = yaml.safe_load(f)

# Get list of cities with subpages (43 cities)
CITIES_WITH_SUBPAGES = cities_data.get('cities_with_subpages', [])

# Build city info from all regions
ALL_CITIES = {}
for region in ['brussels', 'walloon_brabant', 'flemish_brabant']:
    if region in cities_data:
        for city in cities_data[region]:
            ALL_CITIES[city['slug']] = city

# Emergency types with slugs and SEO descriptions for each language
EMERGENCIES = [
    {
        "id": "locked-out",
        "fr": {"slug": "porte-claquee", "title": "Porte Claquée", "desc": "Porte claquée à {city} ? Serrurier urgence 24h/24. Intervention rapide 30 min, ouverture sans dégât. Appelez 0489 24 73 64."},
        "en": {"slug": "locked-out", "title": "Locked Out", "desc": "Locked out in {city}? 24/7 emergency locksmith. Fast 30-min response, damage-free entry. Call 0489 24 73 64."},
        "nl": {"slug": "dichtgevallen-deur", "title": "Dichtgevallen Deur", "desc": "Deur dichtgevallen in {city}? Nood slotenmaker 24/7. Snelle interventie 30 min, zonder schade. Bel 0489 24 73 64."}
    },
    {
        "id": "broken-key",
        "fr": {"slug": "cle-cassee-serrure", "title": "Clé Cassée dans Serrure", "desc": "Clé cassée dans la serrure à {city} ? Serrurier urgence extrait la clé et remplace si nécessaire. 24h/24. Appelez 0489 24 73 64."},
        "en": {"slug": "broken-key-lock", "title": "Broken Key in Lock", "desc": "Broken key stuck in lock in {city}? Emergency locksmith extracts key and replaces if needed. 24/7 service. Call 0489 24 73 64."},
        "nl": {"slug": "gebroken-sleutel-slot", "title": "Gebroken Sleutel in Slot", "desc": "Sleutel afgebroken in slot in {city}? Nood slotenmaker haalt sleutel eruit en vervangt indien nodig. 24/7. Bel 0489 24 73 64."}
    },
    {
        "id": "burglary",
        "fr": {"slug": "cambriolage", "title": "Cambriolage", "desc": "Victime de cambriolage à {city} ? Serrurier urgence sécurise votre domicile 24h/24. Remplacement serrure, blindage porte. Appelez 0489 24 73 64."},
        "en": {"slug": "burglary", "title": "Burglary", "desc": "Burglary victim in {city}? Emergency locksmith secures your home 24/7. Lock replacement, door reinforcement. Call 0489 24 73 64."},
        "nl": {"slug": "inbraak", "title": "Inbraak", "desc": "Slachtoffer van inbraak in {city}? Nood slotenmaker beveiligt uw woning 24/7. Slotvervanging, deurbepantsering. Bel 0489 24 73 64."}
    },
    {
        "id": "armored-door",
        "fr": {"slug": "porte-blindee-bloquee", "title": "Porte Blindée Bloquée", "desc": "Porte blindée bloquée à {city} ? Serrurier spécialisé portes sécurisées. Ouverture sans destruction 24h/24. Appelez 0489 24 73 64."},
        "en": {"slug": "armored-door-locked", "title": "Armored Door Locked", "desc": "Armored door locked in {city}? Specialist locksmith for security doors. Non-destructive opening 24/7. Call 0489 24 73 64."},
        "nl": {"slug": "gepantserde-deur-geblokkeerd", "title": "Gepantserde Deur Geblokkeerd", "desc": "Gepantserde deur geblokkeerd in {city}? Specialist slotenmaker voor beveiligde deuren. Opening zonder schade 24/7. Bel 0489 24 73 64."}
    },
    {
        "id": "night-locksmith",
        "fr": {"slug": "serrurier-nuit", "title": "Serrurier de Nuit", "desc": "Serrurier de nuit à {city}. Intervention urgente entre 22h et 6h. Porte claquée, clé perdue ? Disponible 7j/7. Appelez 0489 24 73 64."},
        "en": {"slug": "night-locksmith", "title": "Night Locksmith", "desc": "Night locksmith in {city}. Emergency service 10PM-6AM. Locked out, lost key? Available 7 days. Call 0489 24 73 64."},
        "nl": {"slug": "nacht-slotenmaker", "title": "Nacht Slotenmaker", "desc": "Nacht slotenmaker in {city}. Dringende interventie 22u-6u. Deur dichtgevallen, sleutel verloren? 7 dagen beschikbaar. Bel 0489 24 73 64."}
    },
    {
        "id": "sunday-locksmith",
        "fr": {"slug": "serrurier-dimanche", "title": "Serrurier Dimanche", "desc": "Serrurier dimanche à {city}. Intervention urgente le dimanche et jours fériés. Même tarif, même rapidité. Appelez 0489 24 73 64."},
        "en": {"slug": "sunday-locksmith", "title": "Sunday Locksmith", "desc": "Sunday locksmith in {city}. Emergency service on Sundays and holidays. Same rate, same speed. Call 0489 24 73 64."},
        "nl": {"slug": "zondag-slotenmaker", "title": "Zondag Slotenmaker", "desc": "Zondag slotenmaker in {city}. Dringende interventie op zondag en feestdagen. Zelfde tarief, zelfde snelheid. Bel 0489 24 73 64."}
    }
]

# Language config
LANGS = [
    {"code": "fr", "folder": "urgence"},
    {"code": "en", "folder": "emergency"},
    {"code": "nl", "folder": "noodgeval"}
]

def get_city_slug(city_data, lang):
    """Get the correct city slug for a language."""
    if lang == 'en' and city_data.get('slug_en'):
        return city_data['slug_en']
    elif lang == 'nl' and city_data.get('slug_nl'):
        return city_data['slug_nl']
    return city_data['slug']

def get_city_name(city_data, lang):
    """Get city name for specific language"""
    if lang == 'en' and city_data.get('name_en'):
        return city_data['name_en']
    elif lang == 'nl' and city_data.get('name_nl'):
        return city_data['name_nl']
    return city_data['name']

def generate_page(city_data, emergency, lang_config):
    """Generate a single emergency city page"""
    lang = lang_config["code"]
    folder = lang_config["folder"]
    city_slug = get_city_slug(city_data, lang)
    city_name = get_city_name(city_data, lang)
    emergency_data = emergency[lang]
    emergency_slug = emergency_data["slug"]
    emergency_title = emergency_data["title"]
    emergency_desc = emergency_data["desc"].format(city=city_name)
    emergency_id = emergency["id"]

    # Build alternates with correct slugs per language
    alternates = {}
    for l in LANGS:
        l_code = l["code"]
        l_folder = l["folder"]
        l_city_slug = get_city_slug(city_data, l_code)
        l_emergency_slug = emergency[l_code]["slug"]
        alternates[l_code] = f"/{l_code}/{l_folder}/{l_city_slug}/{l_emergency_slug}/"

    # Build title with proper brand name per language
    if lang == "fr":
        title = f"{emergency_title} {city_name} | Serrurier Urgence | Janssens"
    elif lang == "en":
        title = f"{emergency_title} {city_name} | Emergency Locksmith | Janssens"
    else:
        title = f"{emergency_title} {city_name} | Nood Slotenmaker | Janssens"

    content = f'''---
layout: emergency-city
lang: {lang}
title: "{title}"
description: "{emergency_desc}"
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

        for city_slug_fr in CITIES_WITH_SUBPAGES:
            city_data = ALL_CITIES.get(city_slug_fr)
            if not city_data:
                print(f"Warning: City {city_slug_fr} not found in cities.yml")
                continue

            city_slug = get_city_slug(city_data, lang)

            for emergency in EMERGENCIES:
                emergency_slug = emergency[lang]["slug"]

                # Determine base path
                dir_path = os.path.join(BASE_DIR, lang, folder, city_slug)

                # Create directory
                os.makedirs(dir_path, exist_ok=True)

                # Generate page content
                content = generate_page(city_data, emergency, lang_config)

                # Use subfolder with index.html for clean URLs
                sub_dir = os.path.join(dir_path, emergency_slug)
                os.makedirs(sub_dir, exist_ok=True)
                file_path = os.path.join(sub_dir, "index.html")

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

                count += 1

        print(f"{lang.upper()}: {count // len(EMERGENCIES)} cities processed")

    print(f"\n=== Generated {count} emergency city pages ===")
    print(f"  - {len(CITIES_WITH_SUBPAGES)} cities")
    print(f"  - {len(EMERGENCIES)} emergency types")
    print(f"  - {len(LANGS)} languages")

if __name__ == "__main__":
    main()
