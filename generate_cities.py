#!/usr/bin/env python3
"""
Generate all city pages for Jekyll migration
"""

import os
import yaml

# City data (extracted from cities.yml)
cities = {
    "brussels": [
        {"name": "Anderlecht", "slug": "anderlecht", "postal": "1070"},
        {"name": "Auderghem", "slug": "auderghem", "slug_nl": "oudergem", "postal": "1160"},
        {"name": "Berchem-Sainte-Agathe", "slug": "berchem-sainte-agathe", "slug_nl": "sint-agatha-berchem", "postal": "1082"},
        {"name": "Bruxelles-Ville", "slug": "bruxelles-ville", "slug_en": "city-of-brussels", "slug_nl": "brussel-stad", "postal": "1000"},
        {"name": "Etterbeek", "slug": "etterbeek", "postal": "1040"},
        {"name": "Evere", "slug": "evere", "postal": "1140"},
        {"name": "Forest", "slug": "forest", "slug_nl": "vorst", "postal": "1190"},
        {"name": "Ganshoren", "slug": "ganshoren", "postal": "1083"},
        {"name": "Ixelles", "slug": "ixelles", "slug_nl": "elsene", "postal": "1050"},
        {"name": "Jette", "slug": "jette", "postal": "1090"},
        {"name": "Koekelberg", "slug": "koekelberg", "postal": "1081"},
        {"name": "Molenbeek-Saint-Jean", "slug": "molenbeek-saint-jean", "slug_nl": "sint-jans-molenbeek", "postal": "1080"},
        {"name": "Saint-Gilles", "slug": "saint-gilles", "slug_nl": "sint-gillis", "postal": "1060"},
        {"name": "Saint-Josse-ten-Noode", "slug": "saint-josse-ten-noode", "slug_nl": "sint-joost-ten-node", "postal": "1210"},
        {"name": "Schaerbeek", "slug": "schaerbeek", "slug_nl": "schaarbeek", "postal": "1030"},
        {"name": "Uccle", "slug": "uccle", "slug_nl": "ukkel", "postal": "1180"},
        {"name": "Watermael-Boitsfort", "slug": "watermael-boitsfort", "slug_nl": "watermaal-bosvoorde", "postal": "1170"},
        {"name": "Woluwe-Saint-Lambert", "slug": "woluwe-saint-lambert", "slug_nl": "sint-lambrechts-woluwe", "postal": "1200"},
        {"name": "Woluwe-Saint-Pierre", "slug": "woluwe-saint-pierre", "slug_nl": "sint-pieters-woluwe", "postal": "1150"},
    ],
    "walloon_brabant": [
        {"name": "Beauvechain", "slug": "beauvechain", "postal": "1320"},
        {"name": "Braine-l'Alleud", "slug": "braine-lalleud", "postal": "1420"},
        {"name": "Braine-le-Château", "slug": "braine-le-chateau", "postal": "1440"},
        {"name": "Chastre", "slug": "chastre", "postal": "1450"},
        {"name": "Chaumont-Gistoux", "slug": "chaumont-gistoux", "postal": "1325"},
        {"name": "Court-Saint-Étienne", "slug": "court-saint-etienne", "postal": "1490"},
        {"name": "Genappe", "slug": "genappe", "postal": "1470"},
        {"name": "Grez-Doiceau", "slug": "grez-doiceau", "postal": "1390"},
        {"name": "Hélécine", "slug": "helecine", "postal": "1357"},
        {"name": "Incourt", "slug": "incourt", "postal": "1315"},
        {"name": "Jodoigne", "slug": "jodoigne", "postal": "1370"},
        {"name": "La Hulpe", "slug": "la-hulpe", "postal": "1310"},
        {"name": "Lasne", "slug": "lasne", "postal": "1380"},
        {"name": "Mont-Saint-Guibert", "slug": "mont-saint-guibert", "postal": "1435"},
        {"name": "Nivelles", "slug": "nivelles", "postal": "1400"},
        {"name": "Orp-Jauche", "slug": "orp-jauche", "postal": "1350"},
        {"name": "Ottignies-Louvain-la-Neuve", "slug": "ottignies-louvain-la-neuve", "postal": "1340"},
        {"name": "Perwez", "slug": "perwez", "postal": "1360"},
        {"name": "Ramillies", "slug": "ramillies", "postal": "1367"},
        {"name": "Rixensart", "slug": "rixensart", "postal": "1330"},
        {"name": "Tubize", "slug": "tubize", "postal": "1480"},
        {"name": "Villers-la-Ville", "slug": "villers-la-ville", "postal": "1495"},
        {"name": "Walhain", "slug": "walhain", "postal": "1457"},
        {"name": "Waterloo", "slug": "waterloo", "postal": "1410"},
        {"name": "Wavre", "slug": "wavre", "postal": "1300"},
    ],
    "flemish_brabant": [
        {"name": "Aarschot", "slug": "aarschot", "postal": "3200"},
        {"name": "Asse", "slug": "asse", "postal": "1730"},
        {"name": "Beersel", "slug": "beersel", "postal": "1650"},
        {"name": "Begijnendijk", "slug": "begijnendijk", "postal": "3130"},
        {"name": "Bekkevoort", "slug": "bekkevoort", "postal": "3460"},
        {"name": "Bertem", "slug": "bertem", "postal": "3060"},
        {"name": "Bierbeek", "slug": "bierbeek", "postal": "3360"},
        {"name": "Boortmeerbeek", "slug": "boortmeerbeek", "postal": "3190"},
        {"name": "Boutersem", "slug": "boutersem", "postal": "3370"},
        {"name": "Diest", "slug": "diest", "postal": "3290"},
        {"name": "Dilbeek", "slug": "dilbeek", "postal": "1700"},
        {"name": "Drogenbos", "slug": "drogenbos", "postal": "1620"},
        {"name": "Geetbets", "slug": "geetbets", "postal": "3450"},
        {"name": "Glabbeek", "slug": "glabbeek", "postal": "3380"},
        {"name": "Grimbergen", "slug": "grimbergen", "postal": "1850"},
        {"name": "Haacht", "slug": "haacht", "postal": "3150"},
        {"name": "Halle", "slug": "halle", "postal": "1500"},
        {"name": "Herent", "slug": "herent", "postal": "3020"},
        {"name": "Hoegaarden", "slug": "hoegaarden", "postal": "3320"},
        {"name": "Hoeilaart", "slug": "hoeilaart", "postal": "1560"},
        {"name": "Holsbeek", "slug": "holsbeek", "postal": "3220"},
        {"name": "Huldenberg", "slug": "huldenberg", "postal": "3040"},
        {"name": "Kampenhout", "slug": "kampenhout", "postal": "1910"},
        {"name": "Kapelle-op-den-Bos", "slug": "kapelle-op-den-bos", "postal": "1880"},
        {"name": "Keerbergen", "slug": "keerbergen", "postal": "3140"},
        {"name": "Kortenaken", "slug": "kortenaken", "postal": "3470"},
        {"name": "Kortenberg", "slug": "kortenberg", "postal": "3070"},
        {"name": "Kraainem", "slug": "kraainem", "postal": "1950"},
        {"name": "Landen", "slug": "landen", "postal": "3400"},
        {"name": "Lennik", "slug": "lennik", "postal": "1750"},
        {"name": "Leuven", "slug": "leuven", "postal": "3000"},
        {"name": "Linkebeek", "slug": "linkebeek", "postal": "1630"},
        {"name": "Londerzeel", "slug": "londerzeel", "postal": "1840"},
        {"name": "Lubbeek", "slug": "lubbeek", "postal": "3210"},
        {"name": "Machelen", "slug": "machelen", "postal": "1830"},
        {"name": "Meise", "slug": "meise", "postal": "1860"},
        {"name": "Oud-Heverlee", "slug": "oud-heverlee", "postal": "3050"},
        {"name": "Overijse", "slug": "overijse", "postal": "3090"},
        {"name": "Rotselaar", "slug": "rotselaar", "postal": "3110"},
        {"name": "Scherpenheuvel-Zichem", "slug": "scherpenheuvel-zichem", "postal": "3270"},
        {"name": "Sint-Genesius-Rode", "slug": "sint-genesius-rode", "postal": "1640"},
        {"name": "Sint-Pieters-Leeuw", "slug": "sint-pieters-leeuw", "postal": "1600"},
        {"name": "Steenokkerzeel", "slug": "steenokkerzeel", "postal": "1820"},
        {"name": "Tervuren", "slug": "tervuren", "postal": "3080"},
        {"name": "Tielt-Winge", "slug": "tielt-winge", "postal": "3390"},
        {"name": "Tienen", "slug": "tienen", "postal": "3300"},
        {"name": "Tremelo", "slug": "tremelo", "postal": "3120"},
        {"name": "Vilvoorde", "slug": "vilvoorde", "postal": "1800"},
        {"name": "Wemmel", "slug": "wemmel", "postal": "1780"},
        {"name": "Wezembeek-Oppem", "slug": "wezembeek-oppem", "postal": "1970"},
        {"name": "Zaventem", "slug": "zaventem", "postal": "1930"},
        {"name": "Zemst", "slug": "zemst", "postal": "1980"},
        {"name": "Zoutleeuw", "slug": "zoutleeuw", "postal": "3440"},
    ]
}

# Language configurations
lang_config = {
    "fr": {
        "title_prefix": "Serrurier",
        "title_suffix": "Dépannage 24/24",
        "desc_template": "Serrurier à {city} : intervention urgente en 30 min. Porte claquée, serrure bloquée ? Dépannage 24h/24 sans dégât. Devis gratuit.",
        "breadcrumb_zones": "Zones d'intervention",
        "faq_title": "Questions fréquentes sur nos services à {city}",
        "faq": [
            {"q": "Combien coûte un serrurier à {city} ?", "a": "Nos tarifs à {city} sont transparents et communiqués avant intervention. Appelez le 0495 205 400 pour un devis gratuit immédiat."},
            {"q": "En combien de temps intervenez-vous à {city} ?", "a": "Notre serrurier arrive à {city} en 30 minutes maximum, 24h/24 et 7j/7."},
            {"q": "Intervenez-vous la nuit à {city} ?", "a": "Oui, nous sommes disponibles 24h/24 à {city}, y compris la nuit, les weekends et jours fériés."},
        ]
    },
    "en": {
        "title_prefix": "Locksmith",
        "title_suffix": "Emergency 24/7",
        "desc_template": "Locksmith in {city}: urgent intervention in 30 min. Locked out, jammed lock? 24/7 service without damage. Free quote.",
        "breadcrumb_zones": "Service areas",
        "faq_title": "FAQ about our services in {city}",
        "faq": [
            {"q": "How much does a locksmith cost in {city}?", "a": "Our rates in {city} are transparent and communicated before intervention. Call 0495 205 400 for a free immediate quote."},
            {"q": "How quickly do you arrive in {city}?", "a": "Our locksmith arrives in {city} within 30 minutes maximum, 24/7."},
            {"q": "Do you work at night in {city}?", "a": "Yes, we are available 24/7 in {city}, including nights, weekends and holidays."},
        ]
    },
    "nl": {
        "title_prefix": "Slotenmaker",
        "title_suffix": "Noodhulp 24/7",
        "desc_template": "Slotenmaker in {city}: dringende interventie in 30 min. Buitengesloten, slot geblokkeerd? 24/7 service zonder schade. Gratis offerte.",
        "breadcrumb_zones": "Interventiezones",
        "faq_title": "Veelgestelde vragen over onze diensten in {city}",
        "faq": [
            {"q": "Hoeveel kost een slotenmaker in {city}?", "a": "Onze tarieven in {city} zijn transparant en worden voor interventie meegedeeld. Bel 0495 205 400 voor een gratis offerte."},
            {"q": "Hoe snel komt u in {city}?", "a": "Onze slotenmaker is binnen 30 minuten in {city}, 24/7."},
            {"q": "Werkt u 's nachts in {city}?", "a": "Ja, wij zijn 24/7 beschikbaar in {city}, inclusief nachten, weekends en feestdagen."},
        ]
    }
}

def get_slug_for_lang(city, lang):
    """Get the appropriate slug for a city in a given language"""
    if lang == "en" and "slug_en" in city:
        return city["slug_en"]
    elif lang == "nl" and "slug_nl" in city:
        return city["slug_nl"]
    return city["slug"]

def get_nearby_cities(all_cities, current_city, region):
    """Get 4 nearby cities from the same region"""
    region_cities = all_cities[region]
    nearby = []
    for c in region_cities:
        if c["slug"] != current_city["slug"] and len(nearby) < 4:
            nearby.append({"name": c["name"], "slug": c["slug"]})
    return nearby

def generate_city_page(city, region, lang, all_cities):
    """Generate a single city page"""
    config = lang_config[lang]
    slug = get_slug_for_lang(city, lang)

    # Get slugs for all languages for alternates
    slug_fr = city["slug"]
    slug_en = city.get("slug_en", city["slug"])
    slug_nl = city.get("slug_nl", city["slug"])

    nearby = get_nearby_cities(all_cities, city, region)

    content = f'''---
layout: city
lang: {lang}
title: "{config["title_prefix"]} {city["name"]} | {config["title_suffix"]} | Janssens"
description: "{config["desc_template"].format(city=city["name"])}"
city_name: "{city["name"]}"
slug: "{slug}"
postal: "{city["postal"]}"
breadcrumb:
  - name: "{config["breadcrumb_zones"]}"
    url: "/{lang}/#zones"
  - name: "{city["name"]}"
alternate:
  fr: "/fr/cities/{slug_fr}/"
  en: "/en/cities/{slug_en}/"
  nl: "/nl/cities/{slug_nl}/"
nearby_cities:
'''

    for nc in nearby:
        nc_slug = nc["slug"]
        content += f'  - name: "{nc["name"]}"\n    slug: "{nc_slug}"\n'

    content += f'''---

<!-- FAQ Section -->
<section class="commune-faq" id="faq">
    <div class="commune-container">
        <h2 class="section-title">{config["faq_title"].format(city=city["name"])}</h2>

        <div class="faq-list">
'''

    for faq in config["faq"]:
        q = faq["q"].format(city=city["name"])
        a = faq["a"].format(city=city["name"])
        content += f'''            <details class="faq-item">
                <summary>{q}</summary>
                <p>{a}</p>
            </details>
'''

    content += '''        </div>
    </div>
</section>
'''

    return content

def main():
    base_path = "/Users/hiliyeh/Desktop/project/Janssens"

    # Create directories
    for lang in ["fr", "en", "nl"]:
        os.makedirs(f"{base_path}/{lang}/cities", exist_ok=True)

    # Flatten all cities for reference
    all_cities = cities

    # Generate pages
    count = 0
    for region, city_list in cities.items():
        for city in city_list:
            for lang in ["fr", "en", "nl"]:
                slug = get_slug_for_lang(city, lang)
                filepath = f"{base_path}/{lang}/cities/{slug}.html"
                content = generate_city_page(city, region, lang, all_cities)

                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)

                count += 1
                print(f"Created: {lang}/cities/{slug}.html")

    print(f"\n✅ Generated {count} city pages!")

if __name__ == "__main__":
    main()
