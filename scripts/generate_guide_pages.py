#!/usr/bin/env python3
"""Generate guide pages for all languages."""

import os

BASE_DIR = "/Users/hiliyeh/Desktop/project/Janssens"

LANG_CONFIG = {
    'fr': {'guides_folder': 'guides'},
    'en': {'guides_folder': 'guides'},
    'nl': {'guides_folder': 'gidsen'},
}

# SEO suffixes per language
SEO_SUFFIX = {
    'fr': 'Serrurier 24h/24 | 0489 24 73 64',
    'en': 'Locksmith 24/7 | 0489 24 73 64',
    'nl': 'Slotenmaker 24/7 | 0489 24 73 64',
}

GUIDES = [
    {
        'id': 'locked-out-what-to-do',
        'fr': {'slug': 'porte-claquee-que-faire', 'title': 'Porte Claquée Bruxelles'},
        'en': {'slug': 'locked-out-what-to-do', 'title': 'Locked Out Brussels'},
        'nl': {'slug': 'buitengesloten-wat-te-doen', 'title': 'Buitengesloten Brussel'},
    },
    {
        'id': 'avoid-locksmith-scams',
        'fr': {'slug': 'eviter-arnaques-serrurier', 'title': 'Éviter Arnaques Serrurier'},
        'en': {'slug': 'avoid-locksmith-scams', 'title': 'Avoid Locksmith Scams'},
        'nl': {'slug': 'slotenmaker-oplichting-vermijden', 'title': 'Slotenmaker Oplichting Vermijden'},
    },
    {
        'id': 'choose-security-lock',
        'fr': {'slug': 'choisir-serrure-securite', 'title': 'Choisir Serrure Sécurité'},
        'en': {'slug': 'choose-security-lock', 'title': 'Choose Security Lock'},
        'nl': {'slug': 'veiligheidsslot-kiezen', 'title': 'Veiligheidsslot Kiezen'},
    },
    {
        'id': 'after-burglary',
        'fr': {'slug': 'cambriolage-que-faire', 'title': 'Après Cambriolage'},
        'en': {'slug': 'after-burglary-what-to-do', 'title': 'After Burglary'},
        'nl': {'slug': 'na-inbraak-wat-te-doen', 'title': 'Na Inbraak'},
    },
]

def get_alternate_urls(guide, current_lang):
    """Generate alternate URLs for all languages."""
    alternates = {}
    for lang, config in LANG_CONFIG.items():
        folder = config['guides_folder']
        slug = guide[lang]['slug']
        alternates[lang] = f"/{lang}/{folder}/{slug}/"
    return alternates

def create_guide_page(guide, lang):
    """Create a guide page for a specific language."""
    config = LANG_CONFIG[lang]
    folder = config['guides_folder']
    slug = guide[lang]['slug']
    title = guide[lang]['title']

    alternates = get_alternate_urls(guide, lang)

    content = f"""---
layout: guide
lang: {lang}
title: "{title} | {SEO_SUFFIX[lang]}"
description: "{title}"
guide_id: "{guide['id']}"
alternate:
  fr: "{alternates['fr']}"
  en: "{alternates['en']}"
  nl: "{alternates['nl']}"
---

"""

    # Create directory
    dir_path = os.path.join(BASE_DIR, lang, folder, slug)
    os.makedirs(dir_path, exist_ok=True)

    # Write file
    file_path = os.path.join(dir_path, "index.html")
    with open(file_path, 'w') as f:
        f.write(content)

    print(f"Created: {file_path}")

def create_guides_index(lang):
    """Create the guides index page for a specific language."""
    config = LANG_CONFIG[lang]
    folder = config['guides_folder']

    titles = {
        'fr': 'Guides Serrurerie',
        'en': 'Locksmith Guides',
        'nl': 'Slotenmaker Gidsen',
    }

    descs = {
        'fr': 'Guides pratiques sur la serrurerie',
        'en': 'Practical guides about locksmithing',
        'nl': 'Praktische gidsen over slotenmakerij',
    }

    content = f"""---
layout: guides-index
lang: {lang}
title: "{titles[lang]} | {SEO_SUFFIX[lang]}"
description: "{descs[lang]}"
alternate:
  fr: "/fr/guides/"
  en: "/en/guides/"
  nl: "/nl/gidsen/"
---
"""

    # Create directory
    dir_path = os.path.join(BASE_DIR, lang, folder)
    os.makedirs(dir_path, exist_ok=True)

    # Write file
    file_path = os.path.join(dir_path, "index.html")
    with open(file_path, 'w') as f:
        f.write(content)

    print(f"Created: {file_path}")

def main():
    print("Generating guide pages...")

    # Generate individual guide pages
    for guide in GUIDES:
        for lang in LANG_CONFIG.keys():
            create_guide_page(guide, lang)

    # Generate index pages
    for lang in LANG_CONFIG.keys():
        create_guides_index(lang)

    print(f"\nTotal: {len(GUIDES) * 3} guide pages + 3 index pages created")

if __name__ == "__main__":
    main()
