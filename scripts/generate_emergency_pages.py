#!/usr/bin/env python3
"""
Generate emergency pages for FR, EN, NL with localized URLs
"""
import os

# Emergency types with localized data
EMERGENCIES = [
    {
        'id': 'locked-out',
        'fr': {'slug': 'porte-claquee', 'title': 'Porte Claquee', 'desc': 'Porte claquee a Bruxelles ? Serrurier disponible 24h/24. Ouverture en 30 min sans degat.'},
        'en': {'slug': 'locked-out', 'title': 'Locked Out', 'desc': 'Locked out in Brussels? Locksmith available 24/7. Door opening in 30 min without damage.'},
        'nl': {'slug': 'dichtgevallen-deur', 'title': 'Dichtgevallen Deur', 'desc': 'Deur dichtgevallen in Brussel? Slotenmaker 24/7 beschikbaar. Deuropening in 30 min zonder schade.'},
    },
    {
        'id': 'broken-key',
        'fr': {'slug': 'cle-cassee-serrure', 'title': 'Cle Cassee dans la Serrure', 'desc': 'Cle cassee dans la serrure ? Extraction sans degat par notre serrurier professionnel.'},
        'en': {'slug': 'broken-key-lock', 'title': 'Broken Key in Lock', 'desc': 'Key broken in lock? Damage-free extraction by our professional locksmith.'},
        'nl': {'slug': 'gebroken-sleutel-slot', 'title': 'Gebroken Sleutel in Slot', 'desc': 'Sleutel gebroken in slot? Schadevrije extractie door onze professionele slotenmaker.'},
    },
    {
        'id': 'burglary',
        'fr': {'slug': 'cambriolage', 'title': 'Apres Cambriolage', 'desc': 'Victime d\'un cambriolage ? Securisation urgente et remplacement de serrure 24h/24.'},
        'en': {'slug': 'burglary', 'title': 'After Burglary', 'desc': 'Victim of burglary? Emergency securing and lock replacement 24/7.'},
        'nl': {'slug': 'inbraak', 'title': 'Na Inbraak', 'desc': 'Slachtoffer van inbraak? Dringende beveiliging en slotvervanging 24/7.'},
    },
    {
        'id': 'armored-door',
        'fr': {'slug': 'porte-blindee-bloquee', 'title': 'Porte Blindee Bloquee', 'desc': 'Porte blindee bloquee ? Specialiste portes blindees, intervention rapide 24h/24.'},
        'en': {'slug': 'armored-door-locked', 'title': 'Armored Door Locked', 'desc': 'Armored door locked? Armored door specialist, fast intervention 24/7.'},
        'nl': {'slug': 'gepantserde-deur-geblokkeerd', 'title': 'Gepantserde Deur Geblokkeerd', 'desc': 'Gepantserde deur geblokkeerd? Specialist gepantserde deuren, snelle interventie 24/7.'},
    },
    {
        'id': 'night-locksmith',
        'fr': {'slug': 'serrurier-nuit', 'title': 'Serrurier de Nuit', 'desc': 'Serrurier de nuit a Bruxelles. Intervention urgente 24h/24, 7j/7.'},
        'en': {'slug': 'night-locksmith', 'title': 'Night Locksmith', 'desc': 'Night locksmith in Brussels. Emergency intervention 24/7.'},
        'nl': {'slug': 'nacht-slotenmaker', 'title': 'Nacht Slotenmaker', 'desc': 'Nacht slotenmaker in Brussel. Dringende interventie 24/7.'},
    },
    {
        'id': 'sunday-locksmith',
        'fr': {'slug': 'serrurier-dimanche', 'title': 'Serrurier Dimanche', 'desc': 'Serrurier le dimanche et jours feries a Bruxelles. Disponible 24h/24.'},
        'en': {'slug': 'sunday-locksmith', 'title': 'Sunday Locksmith', 'desc': 'Sunday and holiday locksmith in Brussels. Available 24/7.'},
        'nl': {'slug': 'zondag-slotenmaker', 'title': 'Zondag Slotenmaker', 'desc': 'Zondag en feestdag slotenmaker in Brussel. Beschikbaar 24/7.'},
    },
]

# Language config
LANG_CONFIG = {
    'fr': {'folder': 'urgence', 'title_prefix': 'Serrurier'},
    'en': {'folder': 'emergency', 'title_prefix': 'Locksmith'},
    'nl': {'folder': 'noodgeval', 'title_prefix': 'Slotenmaker'},
}

BASE_PATH = '/Users/hiliyeh/Desktop/project/Janssens'

def generate_page(emergency, lang):
    """Generate a single emergency page"""
    config = LANG_CONFIG[lang]
    data = emergency[lang]

    # Build alternate URLs
    alternates = []
    for l, cfg in LANG_CONFIG.items():
        slug = emergency[l]['slug']
        alternates.append(f"  {l}: \"/{l}/{cfg['folder']}/{slug}/\"")

    content = f"""---
layout: emergency
lang: {lang}
title: "{data['title']} | {config['title_prefix']} Urgence | Janssens"
description: "{data['desc']}"
emergency_id: "{emergency['id']}"
alternate:
{chr(10).join(alternates)}
---
"""

    # Create directory
    folder_path = os.path.join(BASE_PATH, lang, config['folder'], data['slug'])
    os.makedirs(folder_path, exist_ok=True)

    # Write file
    file_path = os.path.join(folder_path, 'index.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return file_path

def main():
    print("Generating emergency pages...")

    for emergency in EMERGENCIES:
        for lang in ['fr', 'en', 'nl']:
            path = generate_page(emergency, lang)
            print(f"  Created: {path}")

    print(f"\nGenerated {len(EMERGENCIES) * 3} emergency pages")

if __name__ == '__main__':
    main()
