#!/usr/bin/env python3
"""Generate city-service pages for all 44 cities with subpages × 6 services × 3 languages."""

import os
import yaml

# Base path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '_data')

# Load cities from YAML
with open(os.path.join(DATA_DIR, 'cities.yml'), 'r', encoding='utf-8') as f:
    cities_data = yaml.safe_load(f)

# Get list of cities with subpages
CITIES_WITH_SUBPAGES = cities_data.get('cities_with_subpages', [])

# Brussels communes (19) - key-duplication only available here (in-store service)
BRUSSELS_CITIES = [
    'anderlecht', 'auderghem', 'berchem-sainte-agathe', 'bruxelles-ville',
    'etterbeek', 'evere', 'forest', 'ganshoren', 'ixelles', 'jette',
    'koekelberg', 'molenbeek-saint-jean', 'saint-gilles', 'saint-josse-ten-noode',
    'schaerbeek', 'uccle', 'watermael-boitsfort', 'woluwe-saint-lambert', 'woluwe-saint-pierre'
]

# Build city info from all regions
ALL_CITIES = {}
for region in ['brussels', 'walloon_brabant', 'flemish_brabant']:
    if region in cities_data:
        for city in cities_data[region]:
            ALL_CITIES[city['slug']] = city

# Services by language with SEO descriptions
SERVICES = {
    "door-opening": {
        "fr": {"slug": "ouverture-porte", "name": "Ouverture de porte", "desc": "Ouverture de porte à {city}. Serrurier professionnel, intervention 24h/24. Porte claquée, serrure bloquée ? Devis gratuit. Appelez 0495 205 400."},
        "en": {"slug": "door-opening", "name": "Door Opening", "desc": "Door opening service in {city}. Professional locksmith, 24/7 availability. Locked out, jammed lock? Free quote. Call 0495 205 400."},
        "nl": {"slug": "deuropening", "name": "Deuropening", "desc": "Deuropening in {city}. Professionele slotenmaker, 24/7 beschikbaar. Deur dichtgevallen, slot geblokkeerd? Gratis offerte. Bel 0495 205 400."}
    },
    "lock-replacement": {
        "fr": {"slug": "remplacement-serrure", "name": "Remplacement serrure", "desc": "Remplacement de serrure à {city}. Installation serrures haute sécurité, cylindres européens. Devis gratuit. Appelez 0495 205 400."},
        "en": {"slug": "lock-replacement", "name": "Lock Replacement", "desc": "Lock replacement in {city}. High-security lock installation, European cylinders. Free quote. Call 0495 205 400."},
        "nl": {"slug": "slotvervanging", "name": "Slotvervanging", "desc": "Slotvervanging in {city}. Installatie beveiligde sloten, Europese cilinders. Gratis offerte. Bel 0495 205 400."}
    },
    "key-duplication": {
        "fr": {"slug": "double-cles", "name": "Double de clés", "desc": "Double de clés à {city}. Reproduction clés maison, immeuble, boîte aux lettres. Service rapide. Appelez 0495 205 400."},
        "en": {"slug": "key-duplication", "name": "Key Duplication", "desc": "Key duplication in {city}. Copy house keys, building keys, mailbox keys. Fast service. Call 0495 205 400."},
        "nl": {"slug": "sleutel-kopie", "name": "Sleutel kopie", "desc": "Sleutel kopie in {city}. Duplicaat huissleutels, gebouwsleutels, brievenbussleutels. Snelle service. Bel 0495 205 400."}
    },
    "door-reinforcement": {
        "fr": {"slug": "blindage-porte", "name": "Blindage de porte", "desc": "Blindage de porte à {city}. Renforcement porte existante, installation porte blindée. Protection anti-effraction. Appelez 0495 205 400."},
        "en": {"slug": "door-reinforcement", "name": "Door Reinforcement", "desc": "Door reinforcement in {city}. Strengthen existing door, armored door installation. Anti-burglary protection. Call 0495 205 400."},
        "nl": {"slug": "deurbepantsering", "name": "Deurbepantsering", "desc": "Deurbepantsering in {city}. Versterking bestaande deur, gepantserde deur installatie. Anti-inbraak bescherming. Bel 0495 205 400."}
    },
    "safe": {
        "fr": {"slug": "coffre-fort", "name": "Coffre-fort", "desc": "Service coffre-fort à {city}. Ouverture, installation, dépannage coffres-forts. Toutes marques. Appelez 0495 205 400."},
        "en": {"slug": "safe", "name": "Safe Services", "desc": "Safe services in {city}. Safe opening, installation, repair. All brands. Call 0495 205 400."},
        "nl": {"slug": "kluis", "name": "Kluisdiensten", "desc": "Kluisdiensten in {city}. Kluis opening, installatie, reparatie. Alle merken. Bel 0495 205 400."}
    },
    "automotive": {
        "fr": {"slug": "serrurerie-automobile", "name": "Serrurerie automobile", "desc": "Serrurerie automobile à {city}. Ouverture voiture, remplacement clé, réparation serrure auto. 24h/24. Appelez 0495 205 400."},
        "en": {"slug": "automotive-locksmith", "name": "Automotive Locksmith", "desc": "Automotive locksmith in {city}. Car door opening, key replacement, auto lock repair. 24/7. Call 0495 205 400."},
        "nl": {"slug": "auto-slotenmaker", "name": "Auto slotenmaker", "desc": "Auto slotenmaker in {city}. Auto deur opening, sleutel vervanging, auto slot reparatie. 24/7. Bel 0495 205 400."}
    },
    "smart-lock": {
        "fr": {"slug": "serrure-connectee", "name": "Serrure connectée", "desc": "Installation serrure connectée à {city}. Nuki, Yale, Samsung. Domotique, contrôle smartphone. Devis gratuit. Appelez 0495 205 400."},
        "en": {"slug": "smart-lock", "name": "Smart Lock", "desc": "Smart lock installation in {city}. Nuki, Yale, Samsung. Home automation, smartphone control. Free quote. Call 0495 205 400."},
        "nl": {"slug": "slim-slot", "name": "Slim slot", "desc": "Slim slot installatie in {city}. Nuki, Yale, Samsung. Domotica, smartphone bediening. Gratis offerte. Bel 0495 205 400."}
    },
    "access-control": {
        "fr": {"slug": "digicode", "name": "Digicode", "desc": "Installation digicode à {city}. Clavier à code, contrôle d'accès, interphone. Immeubles et entreprises. Appelez 0495 205 400."},
        "en": {"slug": "access-control", "name": "Access Control", "desc": "Access control installation in {city}. Keypad locks, entry systems, intercoms. Buildings and businesses. Call 0495 205 400."},
        "nl": {"slug": "codeslot", "name": "Codeslot", "desc": "Codeslot installatie in {city}. Toetsenbordslot, toegangscontrole, intercom. Gebouwen en bedrijven. Bel 0495 205 400."}
    }
}

# Language folder configuration
LANG_CONFIG = {
    "fr": {"cities_folder": "communes"},
    "en": {"cities_folder": "cities"},
    "nl": {"cities_folder": "gemeenten"}
}

def get_city_slug(city_data, lang):
    """Get the correct city slug for a language."""
    if lang == 'en' and city_data.get('slug_en'):
        return city_data['slug_en']
    elif lang == 'nl' and city_data.get('slug_nl'):
        return city_data['slug_nl']
    return city_data['slug']

def get_city_name(city_data, lang):
    """Get the correct city name for a language."""
    if lang == 'en' and city_data.get('name_en'):
        return city_data['name_en']
    elif lang == 'nl' and city_data.get('name_nl'):
        return city_data['name_nl']
    return city_data['name']

def generate_page(lang, city_data, service_id, service_data):
    """Generate a city-service page."""

    city_slug = get_city_slug(city_data, lang)
    city_name = get_city_name(city_data, lang)
    service_slug = service_data["slug"]
    service_name = service_data["name"]
    service_desc = service_data["desc"].format(city=city_name)
    cities_folder = LANG_CONFIG[lang]["cities_folder"]

    # Generate alternate links with correct slugs per language
    alternates = {}
    for alt_lang in ["fr", "en", "nl"]:
        alt_city_slug = get_city_slug(city_data, alt_lang)
        alt_service = SERVICES[service_id][alt_lang]
        alt_folder = LANG_CONFIG[alt_lang]["cities_folder"]
        alternates[alt_lang] = f"/{alt_lang}/{alt_folder}/{alt_city_slug}/{alt_service['slug']}/"

    # SEO title suffix per language with phone number
    if lang == "fr":
        title_suffix = "Serrurier 24h/24 | 0495 205 400"
    elif lang == "en":
        title_suffix = "Locksmith 24/7 | 0495 205 400"
    else:
        title_suffix = "Slotenmaker 24/7 | 0495 205 400"

    # Create page content
    content = f"""---
layout: city-service
lang: {lang}
title: "{service_name} {city_name} | {title_suffix}"
description: "{service_desc}"
city_name: "{city_name}"
city_slug: "{city_slug}"
service_id: "{service_id}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---
"""

    # Determine output path
    output_dir = os.path.join(BASE_DIR, lang, cities_folder, city_slug)
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{service_slug}.html")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path

def main():
    """Generate all city-service pages."""

    total_created = 0

    for lang in ["fr", "en", "nl"]:
        lang_count = 0

        for city_slug_fr in CITIES_WITH_SUBPAGES:
            city_data = ALL_CITIES.get(city_slug_fr)
            if not city_data:
                print(f"Warning: City {city_slug_fr} not found in cities.yml")
                continue

            for service_id, service_langs in SERVICES.items():
                # Skip key-duplication for cities outside Brussels (in-store service only)
                if service_id == "key-duplication" and city_slug_fr not in BRUSSELS_CITIES:
                    continue

                service_data = service_langs[lang]

                path = generate_page(lang, city_data, service_id, service_data)
                lang_count += 1
                total_created += 1

        print(f"{lang.upper()}: {lang_count} pages created")

    print(f"\nTotal: {total_created} city-service pages created")

if __name__ == "__main__":
    main()
