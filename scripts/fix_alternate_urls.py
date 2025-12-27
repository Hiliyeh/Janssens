#!/usr/bin/env python3
"""Fix alternate and canonical URLs in city pages to use correct folder structure."""
import os
import re

BASE_PATH = '/Users/hiliyeh/Desktop/project/Janssens'

# Correct folder names per language
LANG_FOLDERS = {
    'fr': 'communes',
    'en': 'cities', 
    'nl': 'gemeenten'
}

def fix_file(filepath, lang):
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # Fix canonical URL
    # /fr/cities/ -> /fr/communes/
    # /nl/cities/ -> /nl/gemeenten/
    if lang == 'fr':
        content = re.sub(r'canonical:\s*/fr/cities/', 'canonical: /fr/communes/', content)
    elif lang == 'nl':
        content = re.sub(r'canonical:\s*/nl/cities/', 'canonical: /nl/gemeenten/', content)
    
    # Fix alternate URLs
    content = re.sub(r'fr:\s*/fr/cities/', 'fr: /fr/communes/', content)
    content = re.sub(r'nl:\s*/nl/cities/', 'nl: /nl/gemeenten/', content)
    # en stays as /en/cities/ which is correct
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False

def main():
    updated = 0
    
    for lang, folder in LANG_FOLDERS.items():
        cities_path = os.path.join(BASE_PATH, lang, folder)
        if not os.path.exists(cities_path):
            continue
            
        for city in os.listdir(cities_path):
            city_path = os.path.join(cities_path, city)
            if os.path.isdir(city_path):
                index_path = os.path.join(city_path, 'index.html')
                if os.path.exists(index_path):
                    if fix_file(index_path, lang):
                        print(f"Fixed: {index_path}")
                        updated += 1
    
    print(f"\nTotal files updated: {updated}")

if __name__ == '__main__':
    main()
