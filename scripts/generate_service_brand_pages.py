#!/usr/bin/env python3
"""
Generate service and brand pages for FR, EN, NL with localized URLs
"""
import os

BASE_PATH = '/Users/hiliyeh/Desktop/project/Janssens'

# Services with localized slugs and names for SEO
SERVICES = [
    {'id': 'door-opening', 'fr': 'ouverture-porte', 'en': 'door-opening', 'nl': 'deuropening',
     'name_fr': 'Ouverture de Porte', 'name_en': 'Door Opening', 'name_nl': 'Deuropening',
     'desc_fr': "Service d'ouverture de porte à Bruxelles et Brabant. Porte claquée, serrure bloquée ? Intervention rapide 24h/24, ouverture sans dégât. Devis gratuit. Appelez 0495 205 400.",
     'desc_en': 'Door opening service in Brussels and Brabant. Locked out, jammed lock? Fast 24/7 response, damage-free entry. Free quote. Call 0495 205 400.',
     'desc_nl': 'Deuropening service in Brussel en Brabant. Deur dichtgevallen, slot geblokkeerd? Snelle 24/7 interventie, opening zonder schade. Gratis offerte. Bel 0495 205 400.'},
    {'id': 'lock-replacement', 'fr': 'remplacement-serrure', 'en': 'lock-replacement', 'nl': 'slotvervanging',
     'name_fr': 'Remplacement Serrure', 'name_en': 'Lock Replacement', 'name_nl': 'Slotvervanging',
     'desc_fr': 'Remplacement de serrure à Bruxelles et Brabant. Installation serrures haute sécurité, cylindres européens, serrures multipoints. Devis gratuit. Appelez 0495 205 400.',
     'desc_en': 'Lock replacement in Brussels and Brabant. High-security lock installation, European cylinders, multipoint locks. Free quote. Call 0495 205 400.',
     'desc_nl': 'Slotvervanging in Brussel en Brabant. Installatie beveiligde sloten, Europese cilinders, meerpuntssloten. Gratis offerte. Bel 0495 205 400.'},
    {'id': 'key-duplication', 'fr': 'double-cles', 'en': 'key-duplication', 'nl': 'sleutel-kopie',
     'name_fr': 'Double de Clés', 'name_en': 'Key Duplication', 'name_nl': 'Sleutel Kopie',
     'desc_fr': 'Double de clés à Bruxelles et Brabant. Reproduction clés maison, immeuble, boîte aux lettres, voiture. Service rapide sur place. Appelez 0495 205 400.',
     'desc_en': 'Key duplication in Brussels and Brabant. Copy house keys, building keys, mailbox keys, car keys. Fast on-site service. Call 0495 205 400.',
     'desc_nl': 'Sleutel kopie in Brussel en Brabant. Duplicaat huissleutels, gebouwsleutels, brievenbussleutels, autosleutels. Snelle service ter plaatse. Bel 0495 205 400.'},
    {'id': 'door-reinforcement', 'fr': 'blindage-porte', 'en': 'door-reinforcement', 'nl': 'deurbepantsering',
     'name_fr': 'Blindage de Porte', 'name_en': 'Door Reinforcement', 'name_nl': 'Deurbepantsering',
     'desc_fr': 'Blindage de porte à Bruxelles et Brabant. Renforcement porte existante, installation porte blindée, serrures haute sécurité. Devis gratuit. Appelez 0495 205 400.',
     'desc_en': 'Door reinforcement in Brussels and Brabant. Strengthen existing door, armored door installation, high-security locks. Free quote. Call 0495 205 400.',
     'desc_nl': 'Deurbepantsering in Brussel en Brabant. Versterking bestaande deur, gepantserde deur installatie, beveiligde sloten. Gratis offerte. Bel 0495 205 400.'},
    {'id': 'safe', 'fr': 'coffre-fort', 'en': 'safe', 'nl': 'kluis',
     'name_fr': 'Coffre-Fort', 'name_en': 'Safe Services', 'name_nl': 'Kluisdiensten',
     'desc_fr': 'Service coffre-fort à Bruxelles et Brabant. Ouverture coffre bloqué, installation, dépannage. Toutes marques. Devis gratuit. Appelez 0495 205 400.',
     'desc_en': 'Safe services in Brussels and Brabant. Locked safe opening, installation, repair. All brands. Free quote. Call 0495 205 400.',
     'desc_nl': 'Kluisdiensten in Brussel en Brabant. Geblokkeerde kluis opening, installatie, reparatie. Alle merken. Gratis offerte. Bel 0495 205 400.'},
    {'id': 'automotive', 'fr': 'serrurerie-automobile', 'en': 'automotive-locksmith', 'nl': 'auto-slotenmaker',
     'name_fr': 'Serrurerie Automobile', 'name_en': 'Automotive Locksmith', 'name_nl': 'Auto Slotenmaker',
     'desc_fr': 'Serrurerie automobile à Bruxelles et Brabant. Ouverture voiture, remplacement clé, réparation serrure auto. Intervention 24h/24. Appelez 0495 205 400.',
     'desc_en': 'Automotive locksmith in Brussels and Brabant. Car door opening, key replacement, auto lock repair. 24/7 service. Call 0495 205 400.',
     'desc_nl': 'Auto slotenmaker in Brussel en Brabant. Auto deur opening, sleutel vervanging, auto slot reparatie. 24/7 service. Bel 0495 205 400.'},
]

# Brands (same slug for all languages)
BRANDS = [
    {'id': 'fichet', 'slug': 'fichet', 'name': 'Fichet'},
    {'id': 'bricard', 'slug': 'bricard', 'name': 'Bricard'},
    {'id': 'vachette', 'slug': 'vachette', 'name': 'Vachette'},
    {'id': 'mul-t-lock', 'slug': 'mul-t-lock', 'name': 'Mul-T-Lock'},
    {'id': 'picard', 'slug': 'picard', 'name': 'Picard'},
]

# Language config
LANG_CONFIG = {
    'fr': {'services_folder': 'services', 'brands_folder': 'marques'},
    'en': {'services_folder': 'services', 'brands_folder': 'brands'},
    'nl': {'services_folder': 'diensten', 'brands_folder': 'merken'},
}

def generate_service_page(service, lang):
    """Generate a single service page"""
    config = LANG_CONFIG[lang]
    slug = service[lang]

    # Build alternate URLs
    alternates = []
    for l, cfg in LANG_CONFIG.items():
        s = service[l]
        alternates.append(f"  {l}: \"/{l}/{cfg['services_folder']}/{s}/\"")

    # Get localized name and description
    service_name = service[f'name_{lang}']
    service_desc = service[f'desc_{lang}']

    # SEO title suffix per language with phone number
    if lang == "fr":
        title = f"{service_name} Bruxelles | Serrurier 24h/24 | 0495 205 400"
    elif lang == "en":
        title = f"{service_name} Brussels | Locksmith 24/7 | 0495 205 400"
    else:
        title = f"{service_name} Brussel | Slotenmaker 24/7 | 0495 205 400"

    content = f"""---
layout: service
lang: {lang}
title: "{title}"
description: "{service_desc}"
service_id: "{service['id']}"
alternate:
{chr(10).join(alternates)}
---
"""

    # Create directory
    folder_path = os.path.join(BASE_PATH, lang, config['services_folder'], slug)
    os.makedirs(folder_path, exist_ok=True)

    # Write file
    file_path = os.path.join(folder_path, 'index.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return file_path

def generate_brand_page(brand, lang):
    """Generate a single brand page"""
    config = LANG_CONFIG[lang]

    # Build alternate URLs
    alternates = []
    for l, cfg in LANG_CONFIG.items():
        alternates.append(f"  {l}: \"/{l}/{cfg['brands_folder']}/{brand['slug']}/\"")

    # SEO title suffix per language with phone number
    if lang == "fr":
        title = f"Expert {brand['name']} Bruxelles | Serrurier 24h/24 | 0495 205 400"
        description = f"Expert {brand['name']} agréé à Bruxelles. Installation, dépannage, remplacement serrures {brand['name']}. Intervention 24h/24. Appelez 0495 205 400."
    elif lang == "en":
        title = f"Expert {brand['name']} Brussels | Locksmith 24/7 | 0495 205 400"
        description = f"Certified {brand['name']} expert in Brussels. Installation, repair, replacement of {brand['name']} locks. 24/7 service. Call 0495 205 400."
    else:
        title = f"Expert {brand['name']} Brussel | Slotenmaker 24/7 | 0495 205 400"
        description = f"Erkende {brand['name']} expert in Brussel. Installatie, reparatie, vervanging {brand['name']} sloten. 24/7 dienst. Bel 0495 205 400."

    content = f"""---
layout: brand
lang: {lang}
title: "{title}"
description: "{description}"
brand_id: "{brand['id']}"
alternate:
{chr(10).join(alternates)}
---
"""

    # Create directory
    folder_path = os.path.join(BASE_PATH, lang, config['brands_folder'], brand['slug'])
    os.makedirs(folder_path, exist_ok=True)

    # Write file
    file_path = os.path.join(folder_path, 'index.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return file_path

def main():
    print("Generating service pages...")
    for service in SERVICES:
        for lang in ['fr', 'en', 'nl']:
            path = generate_service_page(service, lang)
            print(f"  Created: {path}")

    print(f"\nGenerated {len(SERVICES) * 3} service pages")

    print("\nGenerating brand pages...")
    for brand in BRANDS:
        for lang in ['fr', 'en', 'nl']:
            path = generate_brand_page(brand, lang)
            print(f"  Created: {path}")

    print(f"\nGenerated {len(BRANDS) * 3} brand pages")

if __name__ == '__main__':
    main()
