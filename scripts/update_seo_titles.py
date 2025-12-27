#!/usr/bin/env python3
"""
Script to update SEO titles across all city pages with phone number
Format: "{Service} {City} | {Type} 24h/24 | 0489 24 73 64"
"""
import os
import re
import yaml

PHONE = "0489 24 73 64"

# Language-specific settings
LANG_CONFIG = {
    'fr': {
        'folder': 'fr/communes',
        'service': 'Serrurier',
        'suffix': f'Serrurier 24h/24 | {PHONE}'
    },
    'en': {
        'folder': 'en/cities',
        'service': 'Locksmith',
        'suffix': f'Locksmith 24/7 | {PHONE}'
    },
    'nl': {
        'folder': 'nl/gemeenten',
        'service': 'Slotenmaker',
        'suffix': f'Slotenmaker 24/7 | {PHONE}'
    }
}

def update_city_title(filepath, lang):
    """Update a city page title with SEO format including phone number"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split front matter and content
    match = re.match(r'^---\n(.*?)\n---\n?(.*)?$', content, re.DOTALL)
    if not match:
        print(f"  Skipping {filepath}: No front matter found")
        return False

    fm_content = match.group(1)
    body_content = match.group(2) or ''

    # Parse front matter
    try:
        fm = yaml.safe_load(fm_content)
    except:
        print(f"  Error parsing YAML in {filepath}")
        return False

    # Get city name
    city_name = fm.get('city_name', '')
    if not city_name:
        print(f"  Skipping {filepath}: No city_name found")
        return False

    config = LANG_CONFIG[lang]

    # Build new title: "Serrurier CityName | Serrurier 24h/24 | 0489 24 73 64"
    new_title = f"{config['service']} {city_name} | {config['suffix']}"

    # Only update if different
    if fm.get('title') == new_title:
        return False

    fm['title'] = new_title

    # Reconstruct front matter
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # Write back
    new_content = f"---\n{new_fm}---\n{body_content}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    base_path = '/Users/hiliyeh/Desktop/project/Janssens'

    for lang, config in LANG_CONFIG.items():
        folder_path = os.path.join(base_path, config['folder'])
        if not os.path.exists(folder_path):
            print(f"Skipping {config['folder']}: directory not found")
            continue

        print(f"\nProcessing {config['folder']}...")
        updated = 0
        total = 0

        # Process both direct .html files AND city subdirectories with index.html
        for entry in sorted(os.listdir(folder_path)):
            entry_path = os.path.join(folder_path, entry)

            # Direct .html file
            if entry.endswith('.html') and os.path.isfile(entry_path):
                total += 1
                if update_city_title(entry_path, lang):
                    updated += 1

            # Subdirectory with index.html (city page)
            elif os.path.isdir(entry_path):
                index_path = os.path.join(entry_path, 'index.html')
                if os.path.exists(index_path):
                    total += 1
                    if update_city_title(index_path, lang):
                        updated += 1

        print(f"  Updated {updated}/{total} files")

if __name__ == '__main__':
    main()
