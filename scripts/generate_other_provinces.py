#!/usr/bin/env python3
"""
Generate cities data and pages for the 8 other Belgian provinces.
Uses the same structure as existing Brussels/Brabant cities.
"""

import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# All communes of Belgium by province (official data)
# Format: name, slug, postal_code, lat, lng

PROVINCES_DATA = {
    # Province d'Anvers (69 communes)
    "antwerp": [
        ("Antwerpen", "antwerpen", "2000", 51.2194, 4.4025),
        ("Mechelen", "mechelen", "2800", 51.0259, 4.4776),
        ("Turnhout", "turnhout", "2300", 51.3226, 4.9443),
        ("Lier", "lier", "2500", 51.1314, 4.5697),
        ("Heist-op-den-Berg", "heist-op-den-berg", "2220", 51.0750, 4.7264),
        ("Mortsel", "mortsel", "2640", 51.1667, 4.4500),
        ("Brasschaat", "brasschaat", "2930", 51.2917, 4.4917),
        ("Schoten", "schoten", "2900", 51.2500, 4.5000),
        ("Boom", "boom", "2850", 51.0833, 4.3667),
        ("Willebroek", "willebroek", "2830", 51.0667, 4.3667),
        ("Kontich", "kontich", "2550", 51.1333, 4.4500),
        ("Edegem", "edegem", "2650", 51.1500, 4.4333),
        ("Aartselaar", "aartselaar", "2630", 51.1333, 4.3833),
        ("Lint", "lint", "2547", 51.1333, 4.4833),
        ("Hove", "hove", "2540", 51.1500, 4.4667),
        ("Boechout", "boechout", "2530", 51.1500, 4.5000),
        ("Borsbeek", "borsbeek", "2150", 51.1833, 4.4833),
        ("Wijnegem", "wijnegem", "2110", 51.2333, 4.5167),
        ("Wommelgem", "wommelgem", "2160", 51.2167, 4.5333),
        ("Ranst", "ranst", "2520", 51.2000, 4.5667),
        ("Zandhoven", "zandhoven", "2240", 51.2167, 4.6667),
        ("Zoersel", "zoersel", "2980", 51.2667, 4.7000),
        ("Malle", "malle", "2390", 51.3000, 4.7000),
        ("Brecht", "brecht", "2960", 51.3500, 4.6333),
        ("Schilde", "schilde", "2970", 51.2500, 4.5833),
        ("Kapellen", "kapellen", "2950", 51.3167, 4.4333),
        ("Stabroek", "stabroek", "2940", 51.3333, 4.3667),
        ("Kalmthout", "kalmthout", "2920", 51.3833, 4.4667),
        ("Essen", "essen", "2910", 51.4667, 4.4667),
        ("Wuustwezel", "wuustwezel", "2990", 51.3833, 4.6000),
        ("Hoogstraten", "hoogstraten", "2320", 51.4000, 4.7667),
        ("Merksplas", "merksplas", "2330", 51.3667, 4.8667),
        ("Beerse", "beerse", "2340", 51.3167, 4.8500),
        ("Vosselaar", "vosselaar", "2350", 51.3167, 4.8833),
        ("Oud-Turnhout", "oud-turnhout", "2360", 51.3167, 4.9833),
        ("Arendonk", "arendonk", "2370", 51.3333, 5.0833),
        ("Ravels", "ravels", "2380", 51.4000, 5.0167),
        ("Baarle-Hertog", "baarle-hertog", "2387", 51.4333, 4.9333),
        ("Rijkevorsel", "rijkevorsel", "2310", 51.3500, 4.7667),
        ("Geel", "geel", "2440", 51.1667, 4.9833),
        ("Meerhout", "meerhout", "2450", 51.1333, 5.0833),
        ("Laakdal", "laakdal", "2430", 51.0833, 5.0000),
        ("Westerlo", "westerlo", "2260", 51.0833, 4.9167),
        ("Hulshout", "hulshout", "2235", 51.0667, 4.7833),
        ("Herenthout", "herenthout", "2270", 51.1333, 4.7500),
        ("Herentals", "herentals", "2200", 51.1833, 4.8333),
        ("Olen", "olen", "2250", 51.1500, 4.8500),
        ("Grobbendonk", "grobbendonk", "2280", 51.1833, 4.7333),
        ("Vorselaar", "vorselaar", "2290", 51.2000, 4.7667),
        ("Lille", "lille", "2275", 51.2333, 4.8167),
        ("Kasterlee", "kasterlee", "2460", 51.2500, 4.9667),
        ("Retie", "retie", "2470", 51.2667, 5.0833),
        ("Dessel", "dessel", "2480", 51.2333, 5.1167),
        ("Mol", "mol", "2400", 51.1833, 5.1167),
        ("Balen", "balen", "2490", 51.1667, 5.1833),
        ("Berlaar", "berlaar", "2590", 51.1167, 4.6500),
        ("Nijlen", "nijlen", "2560", 51.1500, 4.6667),
        ("Duffel", "duffel", "2570", 51.0833, 4.5000),
        ("Sint-Katelijne-Waver", "sint-katelijne-waver", "2860", 51.0667, 4.5333),
        ("Putte", "putte", "2580", 51.0500, 4.6333),
        ("Bonheiden", "bonheiden", "2820", 51.0167, 4.5333),
        ("Puurs-Sint-Amands", "puurs-sint-amands", "2870", 51.0667, 4.2833),
        ("Bornem", "bornem", "2880", 51.1000, 4.2333),
        ("Rumst", "rumst", "2840", 51.0833, 4.4167),
        ("Niel", "niel", "2845", 51.1000, 4.3333),
        ("Schelle", "schelle", "2627", 51.1333, 4.3333),
        ("Hemiksem", "hemiksem", "2620", 51.1500, 4.3333),
        ("Zwijndrecht", "zwijndrecht", "2070", 51.2167, 4.3333),
        ("Beveren", "beveren", "9120", 51.2167, 4.2500),
    ],

    # Province du Limbourg (42 communes)
    "limburg": [
        ("Hasselt", "hasselt", "3500", 50.9311, 5.3378),
        ("Genk", "genk", "3600", 50.9653, 5.5000),
        ("Sint-Truiden", "sint-truiden", "3800", 50.8167, 5.1833),
        ("Beringen", "beringen", "3580", 51.0500, 5.2167),
        ("Lommel", "lommel", "3920", 51.2333, 5.3167),
        ("Tongeren", "tongeren", "3700", 50.7833, 5.4667),
        ("Maasmechelen", "maasmechelen", "3630", 50.9667, 5.7000),
        ("Heusden-Zolder", "heusden-zolder", "3550", 51.0333, 5.2833),
        ("Bilzen", "bilzen", "3740", 50.8667, 5.5167),
        ("Diepenbeek", "diepenbeek", "3590", 50.9167, 5.4167),
        ("Lanaken", "lanaken", "3620", 50.9000, 5.6500),
        ("Bree", "bree", "3960", 51.1500, 5.6000),
        ("Leopoldsburg", "leopoldsburg", "3970", 51.1167, 5.2500),
        ("Peer", "peer", "3990", 51.1333, 5.4667),
        ("Hamont-Achel", "hamont-achel", "3930", 51.2667, 5.5333),
        ("Houthalen-Helchteren", "houthalen-helchteren", "3530", 51.0333, 5.3833),
        ("Tessenderlo", "tessenderlo", "3980", 51.0667, 5.0833),
        ("Ham", "ham", "3945", 51.1000, 5.1667),
        ("Zonhoven", "zonhoven", "3520", 50.9833, 5.3667),
        ("As", "as", "3665", 51.0000, 5.5833),
        ("Zutendaal", "zutendaal", "3690", 50.9333, 5.5667),
        ("Oudsbergen", "oudsbergen", "3670", 51.0667, 5.5833),
        ("Dilsen-Stokkem", "dilsen-stokkem", "3650", 51.0333, 5.7167),
        ("Maaseik", "maaseik", "3680", 51.0833, 5.7833),
        ("Kinrooi", "kinrooi", "3640", 51.1500, 5.7500),
        ("Bocholt", "bocholt", "3950", 51.1667, 5.5833),
        ("Hechtel-Eksel", "hechtel-eksel", "3940", 51.1333, 5.3667),
        ("Pelt", "pelt", "3900", 51.2167, 5.4333),
        ("Herk-de-Stad", "herk-de-stad", "3540", 50.9333, 5.1667),
        ("Lummen", "lummen", "3560", 50.9833, 5.2000),
        ("Nieuwerkerken", "nieuwerkerken", "3850", 50.8500, 5.1333),
        ("Gingelom", "gingelom", "3890", 50.7500, 5.1333),
        ("Borgloon", "borgloon", "3840", 50.8000, 5.3500),
        ("Heers", "heers", "3870", 50.7500, 5.3000),
        ("Kortessem", "kortessem", "3720", 50.8500, 5.4000),
        ("Hoeselt", "hoeselt", "3730", 50.8500, 5.4833),
        ("Riemst", "riemst", "3770", 50.8167, 5.6000),
        ("Voeren", "voeren", "3790", 50.7500, 5.8167),
        ("Alken", "alken", "3570", 50.8833, 5.3000),
        ("Wellen", "wellen", "3830", 50.8500, 5.3500),
        ("Herstappe", "herstappe", "3717", 50.7500, 5.4167),
        ("Boutersem", "boutersem-limburg", "3370", 50.8333, 4.8333),
    ],

    # Province de Flandre orientale (60 communes)
    "east_flanders": [
        ("Gent", "gent", "9000", 51.0543, 3.7174),
        ("Aalst", "aalst", "9300", 50.9367, 4.0400),
        ("Sint-Niklaas", "sint-niklaas", "9100", 51.1667, 4.1333),
        ("Dendermonde", "dendermonde", "9200", 51.0333, 4.1000),
        ("Lokeren", "lokeren", "9160", 51.1000, 3.9833),
        ("Wetteren", "wetteren", "9230", 51.0000, 3.8833),
        ("Ronse", "ronse", "9600", 50.7500, 3.6000),
        ("Eeklo", "eeklo", "9900", 51.1833, 3.5667),
        ("Zottegem", "zottegem", "9620", 50.8667, 3.8167),
        ("Geraardsbergen", "geraardsbergen", "9500", 50.7667, 3.8833),
        ("Ninove", "ninove", "9400", 50.8333, 4.0333),
        ("Temse", "temse", "9140", 51.1333, 4.2167),
        ("Hamme", "hamme", "9220", 51.1000, 4.1333),
        ("Zele", "zele", "9240", 51.0667, 4.0333),
        ("Buggenhout", "buggenhout", "9255", 51.0167, 4.2000),
        ("Lebbeke", "lebbeke", "9280", 51.0000, 4.1333),
        ("Berlare", "berlare", "9290", 51.0333, 4.0000),
        ("Wichelen", "wichelen", "9260", 51.0000, 3.9667),
        ("Laarne", "laarne", "9270", 51.0333, 3.8500),
        ("Destelbergen", "destelbergen", "9070", 51.0500, 3.8000),
        ("Melle", "melle", "9090", 51.0000, 3.8000),
        ("Merelbeke", "merelbeke", "9820", 51.0000, 3.7500),
        ("De Pinte", "de-pinte", "9840", 50.9833, 3.6500),
        ("Nazareth", "nazareth", "9810", 50.9500, 3.6000),
        ("Gavere", "gavere", "9890", 50.9333, 3.6667),
        ("Kruisem", "kruisem", "9770", 50.9167, 3.5167),
        ("Zwalm", "zwalm", "9630", 50.8833, 3.7167),
        ("Lierde", "lierde", "9570", 50.8500, 3.8500),
        ("Brakel", "brakel", "9660", 50.8000, 3.7500),
        ("Kluisbergen", "kluisbergen", "9690", 50.7833, 3.5167),
        ("Oudenaarde", "oudenaarde", "9700", 50.8500, 3.6000),
        ("Wortegem-Petegem", "wortegem-petegem", "9790", 50.8667, 3.5333),
        ("Horebeke", "horebeke", "9667", 50.8333, 3.6833),
        ("Maarkedal", "maarkedal", "9680", 50.8000, 3.6000),
        ("Deinze", "deinze", "9800", 50.9833, 3.5333),
        ("Lievegem", "lievegem", "9930", 51.1000, 3.5667),
        ("Aalter", "aalter", "9880", 51.0833, 3.4500),
        ("Zelzate", "zelzate", "9060", 51.2000, 3.8167),
        ("Wachtebeke", "wachtebeke", "9185", 51.1667, 3.8833),
        ("Moerbeke", "moerbeke", "9180", 51.1833, 3.9500),
        ("Stekene", "stekene", "9190", 51.2167, 4.0333),
        ("Sint-Gillis-Waas", "sint-gillis-waas", "9170", 51.2167, 4.1167),
        ("Kruibeke", "kruibeke", "9150", 51.1667, 4.3000),
        ("Assenede", "assenede", "9960", 51.2333, 3.7500),
        ("Kaprijke", "kaprijke", "9970", 51.2000, 3.6167),
        ("Evergem", "evergem", "9940", 51.1167, 3.6833),
        ("Lochristi", "lochristi", "9080", 51.1000, 3.8333),
        ("Lochristie", "lochristie", "9080", 51.1000, 3.8333),
        ("Oosterzele", "oosterzele", "9860", 50.9500, 3.8000),
        ("Sint-Lievens-Houtem", "sint-lievens-houtem", "9520", 50.9167, 3.8667),
        ("Herzele", "herzele", "9550", 50.8833, 3.8833),
        ("Haaltert", "haaltert", "9450", 50.9000, 4.0000),
        ("Erpe-Mere", "erpe-mere", "9420", 50.9333, 3.9667),
        ("Lede", "lede", "9340", 50.9667, 3.9833),
        ("Denderleeuw", "denderleeuw", "9470", 50.8833, 4.0667),
        ("Affligem", "affligem", "1790", 50.9167, 4.1167),
        ("Sint-Martens-Latem", "sint-martens-latem", "9830", 51.0000, 3.6333),
        ("Maldegem", "maldegem", "9990", 51.2000, 3.4500),
        ("Damme", "damme", "8340", 51.2500, 3.2833),
        ("Knesselare", "knesselare", "9910", 51.1333, 3.4167),
    ],

    # Province de Flandre occidentale (64 communes)
    "west_flanders": [
        ("Brugge", "brugge", "8000", 51.2093, 3.2247),
        ("Oostende", "oostende", "8400", 51.2250, 2.9167),
        ("Kortrijk", "kortrijk", "8500", 50.8283, 3.2650),
        ("Roeselare", "roeselare", "8800", 50.9500, 3.1167),
        ("Knokke-Heist", "knokke-heist", "8300", 51.3500, 3.2833),
        ("Ieper", "ieper", "8900", 50.8500, 2.8833),
        ("Waregem", "waregem", "8790", 50.8833, 3.4167),
        ("Izegem", "izegem", "8870", 50.9167, 3.2167),
        ("Harelbeke", "harelbeke", "8530", 50.8500, 3.3000),
        ("Menen", "menen", "8930", 50.7833, 3.1167),
        ("Wevelgem", "wevelgem", "8560", 50.8000, 3.1833),
        ("Kuurne", "kuurne", "8520", 50.8500, 3.2833),
        ("Torhout", "torhout", "8820", 51.0667, 3.1000),
        ("Tielt", "tielt", "8700", 51.0000, 3.3333),
        ("Blankenberge", "blankenberge", "8370", 51.3167, 3.1333),
        ("Middelkerke", "middelkerke", "8430", 51.1833, 2.8167),
        ("De Haan", "de-haan", "8420", 51.2833, 3.0333),
        ("Bredene", "bredene", "8450", 51.2500, 2.9667),
        ("Oudenburg", "oudenburg", "8460", 51.2000, 3.0000),
        ("Gistel", "gistel", "8470", 51.1500, 2.9667),
        ("Jabbeke", "jabbeke", "8490", 51.1833, 3.1000),
        ("Zedelgem", "zedelgem", "8210", 51.1333, 3.1333),
        ("Oostkamp", "oostkamp", "8020", 51.1500, 3.2333),
        ("Beernem", "beernem", "8730", 51.1333, 3.3333),
        ("Wingene", "wingene", "8750", 51.0667, 3.2667),
        ("Ruiselede", "ruiselede", "8755", 51.0667, 3.3833),
        ("Dentergem", "dentergem", "8720", 50.9667, 3.4167),
        ("Wielsbeke", "wielsbeke", "8710", 50.9167, 3.3833),
        ("Oostrozebeke", "oostrozebeke", "8780", 50.9333, 3.3500),
        ("Meulebeke", "meulebeke", "8760", 50.9500, 3.2833),
        ("Ingelmunster", "ingelmunster", "8770", 50.9167, 3.2500),
        ("Lendelede", "lendelede", "8860", 50.8833, 3.2333),
        ("Moorslede", "moorslede", "8890", 50.8833, 3.0833),
        ("Ledegem", "ledegem", "8880", 50.8500, 3.1167),
        ("Zwevegem", "zwevegem", "8550", 50.8000, 3.3333),
        ("Avelgem", "avelgem", "8580", 50.7667, 3.4500),
        ("Spiere-Helkijn", "spiere-helkijn", "8587", 50.7167, 3.3500),
        ("Deerlijk", "deerlijk", "8540", 50.8500, 3.3500),
        ("Anzegem", "anzegem", "8570", 50.8333, 3.4833),
        ("Poperinge", "poperinge", "8970", 50.8500, 2.7167),
        ("Vleteren", "vleteren", "8640", 50.9167, 2.7333),
        ("Lo-Reninge", "lo-reninge", "8647", 50.9833, 2.7500),
        ("Alveringem", "alveringem", "8690", 51.0167, 2.7167),
        ("Veurne", "veurne", "8630", 51.0667, 2.6667),
        ("De Panne", "de-panne", "8660", 51.1000, 2.5833),
        ("Koksijde", "koksijde", "8670", 51.1167, 2.6500),
        ("Nieuwpoort", "nieuwpoort", "8620", 51.1333, 2.7500),
        ("Diksmuide", "diksmuide", "8600", 51.0333, 2.8667),
        ("Koekelare", "koekelare", "8680", 51.0833, 2.9667),
        ("Kortemark", "kortemark", "8610", 51.0333, 3.0333),
        ("Houthulst", "houthulst", "8650", 50.9833, 2.9500),
        ("Langemark-Poelkapelle", "langemark-poelkapelle", "8920", 50.9167, 2.9167),
        ("Zonnebeke", "zonnebeke", "8980", 50.8667, 3.0000),
        ("Wervik", "wervik", "8940", 50.7833, 3.0333),
        ("Heuvelland", "heuvelland", "8950", 50.7667, 2.8167),
        ("Messines", "messines", "8957", 50.7667, 2.9000),
        ("Staden", "staden", "8840", 50.9833, 3.0167),
        ("Hooglede", "hooglede", "8830", 51.0000, 3.0833),
        ("Lichtervelde", "lichtervelde", "8810", 51.0333, 3.1500),
        ("Ardooie", "ardooie", "8850", 50.9667, 3.2000),
        ("Pittem", "pittem", "8740", 51.0000, 3.2667),
        ("Ichtegem", "ichtegem", "8480", 51.1000, 3.0167),
        ("De Moeren", "de-moeren", "8630", 51.0167, 2.6333),
        ("Zuienkerke", "zuienkerke", "8377", 51.2667, 3.1500),
    ],

    # Province du Hainaut (69 communes)
    "hainaut": [
        ("Charleroi", "charleroi", "6000", 50.4108, 4.4447),
        ("Mons", "mons", "7000", 50.4542, 3.9567),
        ("La Louvière", "la-louviere", "7100", 50.4833, 4.1833),
        ("Tournai", "tournai", "7500", 50.6056, 3.3878),
        ("Mouscron", "mouscron", "7700", 50.7333, 3.2167),
        ("Binche", "binche", "7130", 50.4167, 4.1667),
        ("Soignies", "soignies", "7060", 50.5833, 4.0667),
        ("Châtelet", "chatelet", "6200", 50.4000, 4.5333),
        ("Manage", "manage", "7170", 50.5000, 4.2333),
        ("Courcelles", "courcelles", "6180", 50.4667, 4.3667),
        ("Frameries", "frameries", "7080", 50.4000, 3.8833),
        ("Quaregnon", "quaregnon", "7390", 50.4500, 3.8667),
        ("Boussu", "boussu", "7300", 50.4333, 3.7833),
        ("Saint-Ghislain", "saint-ghislain", "7330", 50.4500, 3.8167),
        ("Dour", "dour", "7370", 50.3833, 3.7833),
        ("Quiévrain", "quievrain", "7380", 50.4000, 3.6833),
        ("Hensies", "hensies", "7350", 50.4333, 3.6833),
        ("Colfontaine", "colfontaine", "7340", 50.4000, 3.8500),
        ("Jurbise", "jurbise", "7050", 50.5333, 3.9167),
        ("Lens", "lens", "7870", 50.5500, 3.9000),
        ("Chièvres", "chievres", "7950", 50.5833, 3.8000),
        ("Brugelette", "brugelette", "7940", 50.5833, 3.8500),
        ("Ath", "ath", "7800", 50.6333, 3.7667),
        ("Lessines", "lessines", "7860", 50.7167, 3.8333),
        ("Ellezelles", "ellezelles", "7890", 50.7333, 3.6833),
        ("Flobecq", "flobecq", "7880", 50.7500, 3.7333),
        ("Enghien", "enghien", "7850", 50.7000, 4.0333),
        ("Silly", "silly", "7830", 50.6500, 3.9167),
        ("Braine-le-Comte", "braine-le-comte", "7090", 50.6167, 4.1333),
        ("Écaussinnes", "ecaussinnes", "7190", 50.5667, 4.1667),
        ("Seneffe", "seneffe", "7180", 50.5333, 4.2667),
        ("Le Roeulx", "le-roeulx", "7070", 50.5000, 4.1167),
        ("Estinnes", "estinnes", "7120", 50.4000, 4.1000),
        ("Anderlues", "anderlues", "6150", 50.4000, 4.2667),
        ("Fontaine-l'Évêque", "fontaine-leveque", "6140", 50.4167, 4.3333),
        ("Chapelle-lez-Herlaimont", "chapelle-lez-herlaimont", "7160", 50.4667, 4.2833),
        ("Morlanwelz", "morlanwelz", "7140", 50.4500, 4.2333),
        ("Mont-Sainte-Aldegonde", "mont-sainte-aldegonde", "7141", 50.4333, 4.2333),
        ("Fleurus", "fleurus", "6220", 50.4833, 4.5500),
        ("Farciennes", "farciennes", "6240", 50.4333, 4.5500),
        ("Aiseau-Presles", "aiseau-presles", "6250", 50.4000, 4.5833),
        ("Pont-à-Celles", "pont-a-celles", "6230", 50.5000, 4.3667),
        ("Les Bons Villers", "les-bons-villers", "6210", 50.5167, 4.4167),
        ("Gerpinnes", "gerpinnes", "6280", 50.3333, 4.5167),
        ("Ham-sur-Heure-Nalinnes", "ham-sur-heure-nalinnes", "6120", 50.3167, 4.3833),
        ("Montigny-le-Tilleul", "montigny-le-tilleul", "6110", 50.3667, 4.3667),
        ("Thuin", "thuin", "6530", 50.3333, 4.2833),
        ("Lobbes", "lobbes", "6540", 50.3500, 4.2667),
        ("Merbes-le-Château", "merbes-le-chateau", "6567", 50.3333, 4.1667),
        ("Erquelinnes", "erquelinnes", "6560", 50.3167, 4.1167),
        ("Beaumont", "beaumont", "6500", 50.2333, 4.2333),
        ("Sivry-Rance", "sivry-rance", "6470", 50.1667, 4.2167),
        ("Froidchapelle", "froidchapelle", "6440", 50.1500, 4.3167),
        ("Chimay", "chimay", "6460", 50.0500, 4.3167),
        ("Momignies", "momignies", "6590", 50.0333, 4.1667),
        ("Comines-Warneton", "comines-warneton", "7780", 50.7667, 3.0167),
        ("Estaimpuis", "estaimpuis", "7730", 50.7000, 3.2833),
        ("Pecq", "pecq", "7740", 50.6833, 3.3333),
        ("Celles", "celles", "7760", 50.7000, 3.4500),
        ("Mont-de-l'Enclus", "mont-de-lenclus", "7750", 50.7500, 3.5000),
        ("Rumes", "rumes", "7610", 50.5167, 3.3000),
        ("Brunehaut", "brunehaut", "7620", 50.5000, 3.4000),
        ("Antoing", "antoing", "7640", 50.5667, 3.4500),
        ("Péruwelz", "peruwelz", "7600", 50.5167, 3.5833),
        ("Beloeil", "beloeil", "7970", 50.5500, 3.7333),
        ("Bernissart", "bernissart", "7320", 50.4833, 3.6500),
        ("Leuze-en-Hainaut", "leuze-en-hainaut", "7900", 50.6000, 3.6167),
        ("Frasnes-lez-Anvaing", "frasnes-lez-anvaing", "7910", 50.6667, 3.5833),
    ],

    # Province de Liège (84 communes)
    "liege": [
        ("Liège", "liege-ville", "4000", 50.6333, 5.5667),
        ("Seraing", "seraing", "4100", 50.5833, 5.5000),
        ("Verviers", "verviers", "4800", 50.5833, 5.8667),
        ("Herstal", "herstal", "4040", 50.6667, 5.6333),
        ("Visé", "vise", "4600", 50.7333, 5.7000),
        ("Ans", "ans", "4430", 50.6667, 5.5167),
        ("Saint-Nicolas", "saint-nicolas-liege", "4420", 50.6333, 5.5333),
        ("Grâce-Hollogne", "grace-hollogne", "4460", 50.6333, 5.5000),
        ("Flémalle", "flemalle", "4400", 50.6000, 5.4667),
        ("Chaudfontaine", "chaudfontaine", "4050", 50.5833, 5.6500),
        ("Beyne-Heusay", "beyne-heusay", "4610", 50.6167, 5.6667),
        ("Fléron", "fleron", "4620", 50.6167, 5.6833),
        ("Soumagne", "soumagne", "4630", 50.6167, 5.7500),
        ("Blegny", "blegny", "4670", 50.6667, 5.7167),
        ("Dalhem", "dalhem", "4607", 50.7000, 5.7333),
        ("Oupeye", "oupeye", "4680", 50.7167, 5.6500),
        ("Bassenge", "bassenge", "4690", 50.7667, 5.6167),
        ("Juprelle", "juprelle", "4450", 50.7167, 5.5333),
        ("Awans", "awans", "4340", 50.6667, 5.4500),
        ("Crisnée", "crisnee", "4367", 50.7000, 5.5000),
        ("Fexhe-le-Haut-Clocher", "fexhe-le-haut-clocher", "4347", 50.7000, 5.4167),
        ("Remicourt", "remicourt", "4350", 50.6833, 5.3167),
        ("Oreye", "oreye", "4360", 50.7167, 5.3500),
        ("Waremme", "waremme", "4300", 50.7000, 5.2500),
        ("Berloz", "berloz", "4257", 50.7000, 5.2167),
        ("Geer", "geer", "4250", 50.7000, 5.1667),
        ("Faimes", "faimes", "4317", 50.6667, 5.2667),
        ("Braives", "braives", "4260", 50.6333, 5.1333),
        ("Burdinne", "burdinne", "4210", 50.5833, 5.0833),
        ("Héron", "heron", "4217", 50.5500, 5.1000),
        ("Wanze", "wanze", "4520", 50.5333, 5.2000),
        ("Huy", "huy", "4500", 50.5167, 5.2333),
        ("Amay", "amay", "4540", 50.5500, 5.3167),
        ("Engis", "engis", "4480", 50.5667, 5.4000),
        ("Neupré", "neupre", "4120", 50.5333, 5.4667),
        ("Esneux", "esneux", "4130", 50.5333, 5.5667),
        ("Comblain-au-Pont", "comblain-au-pont", "4170", 50.4833, 5.5833),
        ("Aywaille", "aywaille", "4920", 50.4667, 5.6667),
        ("Sprimont", "sprimont", "4140", 50.5000, 5.6667),
        ("Trooz", "trooz", "4870", 50.5667, 5.7000),
        ("Olne", "olne", "4877", 50.5833, 5.7500),
        ("Pepinster", "pepinster", "4860", 50.5667, 5.8000),
        ("Theux", "theux", "4910", 50.5333, 5.8167),
        ("Spa", "spa", "4900", 50.4833, 5.8667),
        ("Jalhay", "jalhay", "4845", 50.5500, 5.9667),
        ("Baelen", "baelen", "4837", 50.6167, 5.9667),
        ("Limbourg", "limbourg", "4830", 50.6167, 5.9333),
        ("Welkenraedt", "welkenraedt", "4840", 50.6500, 5.9667),
        ("Plombières", "plombieres", "4850", 50.7333, 5.9667),
        ("Aubel", "aubel", "4880", 50.7000, 5.8500),
        ("Thimister-Clermont", "thimister-clermont", "4890", 50.6667, 5.8500),
        ("Herve", "herve", "4650", 50.6333, 5.8000),
        ("Dison", "dison", "4820", 50.6000, 5.8500),
        ("Eupen", "eupen", "4700", 50.6333, 6.0333),
        ("La Calamine", "la-calamine", "4720", 50.7167, 6.0000),
        ("Lontzen", "lontzen", "4710", 50.6833, 6.0000),
        ("Raeren", "raeren", "4730", 50.6667, 6.1167),
        ("Butgenbach", "butgenbach", "4750", 50.4333, 6.2000),
        ("Büllingen", "bullingen", "4760", 50.4167, 6.2833),
        ("Amel", "amel", "4770", 50.3500, 6.1833),
        ("Sankt Vith", "sankt-vith", "4780", 50.2833, 6.1167),
        ("Burg-Reuland", "burg-reuland", "4790", 50.1833, 6.1333),
        ("Malmedy", "malmedy", "4960", 50.4167, 6.0333),
        ("Waimes", "waimes", "4950", 50.4167, 6.1167),
        ("Stavelot", "stavelot", "4970", 50.3833, 5.9333),
        ("Trois-Ponts", "trois-ponts", "4980", 50.3667, 5.8667),
        ("Stoumont", "stoumont", "4987", 50.4167, 5.8167),
        ("Lierneux", "lierneux", "4990", 50.2833, 5.7833),
        ("Ferrières", "ferrieres", "4190", 50.4000, 5.6167),
        ("Hamoir", "hamoir", "4180", 50.4333, 5.5333),
        ("Ouffet", "ouffet", "4590", 50.4333, 5.4500),
        ("Clavier", "clavier", "4560", 50.4000, 5.3667),
        ("Anthisnes", "anthisnes", "4160", 50.4833, 5.5167),
        ("Nandrin", "nandrin", "4550", 50.5000, 5.4167),
        ("Tinlot", "tinlot", "4557", 50.4667, 5.3667),
        ("Modave", "modave", "4577", 50.4500, 5.3000),
        ("Marchin", "marchin", "4570", 50.4667, 5.2333),
        ("Villers-le-Bouillet", "villers-le-bouillet", "4530", 50.5667, 5.2667),
        ("Verlaine", "verlaine", "4537", 50.6000, 5.3167),
        ("Saint-Georges-sur-Meuse", "saint-georges-sur-meuse", "4470", 50.5833, 5.3333),
        ("Donceel", "donceel", "4357", 50.6500, 5.3333),
        ("Wasseiges", "wasseiges", "4219", 50.6000, 5.0000),
        ("Hannut", "hannut", "4280", 50.6667, 5.0833),
        ("Lincent", "lincent", "4287", 50.7167, 5.0333),
    ],

    # Province de Namur (38 communes)
    "namur": [
        ("Namur", "namur-ville", "5000", 50.4667, 4.8667),
        ("Sambreville", "sambreville", "5060", 50.4333, 4.6000),
        ("Gembloux", "gembloux", "5030", 50.5667, 4.7000),
        ("Andenne", "andenne", "5300", 50.4833, 5.1000),
        ("Ciney", "ciney", "5590", 50.3000, 5.1000),
        ("Dinant", "dinant", "5500", 50.2667, 4.9167),
        ("Rochefort", "rochefort", "5580", 50.1667, 5.2167),
        ("Couvin", "couvin", "5660", 50.0500, 4.5000),
        ("Philippeville", "philippeville", "5600", 50.2000, 4.5500),
        ("Florennes", "florennes", "5620", 50.2500, 4.6000),
        ("Walcourt", "walcourt", "5650", 50.2500, 4.4333),
        ("Fosses-la-Ville", "fosses-la-ville", "5070", 50.4000, 4.6833),
        ("Jemeppe-sur-Sambre", "jemeppe-sur-sambre", "5190", 50.4333, 4.6667),
        ("Floreffe", "floreffe", "5150", 50.4333, 4.7500),
        ("Profondeville", "profondeville", "5170", 50.3833, 4.8667),
        ("Anhée", "anhee", "5537", 50.3167, 4.8833),
        ("Yvoir", "yvoir", "5530", 50.3333, 4.8833),
        ("Onhaye", "onhaye", "5520", 50.2500, 4.8333),
        ("Hastière", "hastiere", "5540", 50.2167, 4.8333),
        ("Houyet", "houyet", "5560", 50.1833, 5.0000),
        ("Beauraing", "beauraing", "5570", 50.1167, 5.0667),
        ("Gedinne", "gedinne", "5575", 49.9833, 4.9333),
        ("Bièvre", "bievre", "5555", 49.9667, 5.0000),
        ("Vresse-sur-Semois", "vresse-sur-semois", "5550", 49.8667, 4.9333),
        ("Doische", "doische", "5680", 50.1167, 4.7500),
        ("Viroinval", "viroinval", "5670", 50.0833, 4.6000),
        ("Cerfontaine", "cerfontaine", "5630", 50.1667, 4.4000),
        ("La Bruyère", "la-bruyere", "5080", 50.5167, 4.7667),
        ("Eghezée", "eghezee", "5310", 50.6000, 4.9167),
        ("Fernelmont", "fernelmont", "5380", 50.5500, 4.9667),
        ("Ohey", "ohey", "5350", 50.4333, 5.1333),
        ("Gesves", "gesves", "5340", 50.4000, 5.0667),
        ("Assesse", "assesse", "5330", 50.3667, 5.0167),
        ("Hamois", "hamois", "5360", 50.3333, 5.1667),
        ("Havelange", "havelange", "5370", 50.4000, 5.2333),
        ("Somme-Leuze", "somme-leuze", "5377", 50.3333, 5.3167),
        ("Mettet", "mettet", "5640", 50.3167, 4.6667),
        ("Sombreffe", "sombreffe", "5140", 50.5333, 4.6000),
    ],

    # Province du Luxembourg (44 communes)
    "luxembourg": [
        ("Arlon", "arlon", "6700", 49.6833, 5.8167),
        ("Marche-en-Famenne", "marche-en-famenne", "6900", 50.2333, 5.3500),
        ("Bastogne", "bastogne", "6600", 50.0000, 5.7167),
        ("Virton", "virton", "6760", 49.5667, 5.5333),
        ("Durbuy", "durbuy", "6940", 50.3500, 5.4500),
        ("Aubange", "aubange", "6790", 49.5667, 5.8000),
        ("Bertrix", "bertrix", "6880", 49.8500, 5.2667),
        ("Bouillon", "bouillon", "6830", 49.7833, 5.0667),
        ("Libramont-Chevigny", "libramont-chevigny", "6800", 49.9333, 5.3833),
        ("Neufchâteau", "neufchateau", "6840", 49.8500, 5.4333),
        ("Saint-Hubert", "saint-hubert", "6870", 50.0333, 5.3833),
        ("La Roche-en-Ardenne", "la-roche-en-ardenne", "6980", 50.1833, 5.5833),
        ("Vielsalm", "vielsalm", "6690", 50.2833, 5.9167),
        ("Houffalize", "houffalize", "6660", 50.1333, 5.7833),
        ("Gouvy", "gouvy", "6670", 50.1833, 5.9500),
        ("Manhay", "manhay", "6960", 50.2833, 5.6833),
        ("Érezée", "erezee", "6997", 50.3000, 5.5500),
        ("Hotton", "hotton", "6990", 50.2667, 5.4500),
        ("Rendeux", "rendeux", "6987", 50.2333, 5.5000),
        ("Nassogne", "nassogne", "6950", 50.1333, 5.3500),
        ("Tenneville", "tenneville", "6970", 50.1000, 5.5333),
        ("Sainte-Ode", "sainte-ode", "6680", 50.0167, 5.5167),
        ("Bertogne", "bertogne", "6687", 50.0833, 5.6667),
        ("Fauvillers", "fauvillers", "6637", 49.8667, 5.6667),
        ("Léglise", "leglise", "6860", 49.8000, 5.5333),
        ("Vaux-sur-Sûre", "vaux-sur-sure", "6640", 49.9167, 5.5667),
        ("Paliseul", "paliseul", "6850", 49.9000, 5.1333),
        ("Wellin", "wellin", "6920", 50.0833, 5.1167),
        ("Tellin", "tellin", "6927", 50.0833, 5.2167),
        ("Daverdisse", "daverdisse", "6929", 50.0167, 5.1167),
        ("Libin", "libin", "6890", 49.9833, 5.2500),
        ("Saint-Léger", "saint-leger", "6747", 49.6167, 5.6500),
        ("Messancy", "messancy", "6780", 49.5833, 5.8167),
        ("Attert", "attert", "6717", 49.7500, 5.7833),
        ("Habay", "habay", "6720", 49.7167, 5.6333),
        ("Étalle", "etalle", "6740", 49.6667, 5.6000),
        ("Tintigny", "tintigny", "6730", 49.6833, 5.5167),
        ("Meix-devant-Virton", "meix-devant-virton", "6769", 49.6167, 5.4833),
        ("Rouvroy", "rouvroy", "6767", 49.5333, 5.4833),
        ("Musson", "musson", "6750", 49.5500, 5.7000),
        ("Chiny", "chiny", "6810", 49.7333, 5.3333),
        ("Florenville", "florenville", "6820", 49.7000, 5.3000),
        ("Herbeumont", "herbeumont", "6887", 49.7833, 5.2333),
        ("Martelange", "martelange", "6630", 49.8333, 5.7333),
    ],
}

# Nom des provinces par langue
PROVINCE_NAMES = {
    "antwerp": {"fr": "Anvers", "nl": "Antwerpen", "en": "Antwerp"},
    "limburg": {"fr": "Limbourg", "nl": "Limburg", "en": "Limburg"},
    "east_flanders": {"fr": "Flandre orientale", "nl": "Oost-Vlaanderen", "en": "East Flanders"},
    "west_flanders": {"fr": "Flandre occidentale", "nl": "West-Vlaanderen", "en": "West Flanders"},
    "hainaut": {"fr": "Hainaut", "nl": "Henegouwen", "en": "Hainaut"},
    "liege": {"fr": "Liège", "nl": "Luik", "en": "Liège"},
    "namur": {"fr": "Namur", "nl": "Namen", "en": "Namur"},
    "luxembourg": {"fr": "Luxembourg", "nl": "Luxemburg", "en": "Luxembourg"},
}

def generate_cities_yaml_section():
    """Generate YAML content for cities.yml"""
    yaml_content = "\n# =====================================================\n"
    yaml_content += "# AUTRES PROVINCES (générées automatiquement)\n"
    yaml_content += "# =====================================================\n\n"

    for province_key, cities in PROVINCES_DATA.items():
        province_name = PROVINCE_NAMES[province_key]["fr"]
        yaml_content += f"# {province_name} ({len(cities)} communes)\n"
        yaml_content += f"{province_key}:\n"

        for name, slug, postal, lat, lng in cities:
            yaml_content += f'  - name: "{name}"\n'
            yaml_content += f'    slug: "{slug}"\n'
            yaml_content += f'    postal: "{postal}"\n'
            yaml_content += f'    has_subpages: false\n'
            yaml_content += f'    geo:\n'
            yaml_content += f'      lat: {lat}\n'
            yaml_content += f'      lng: {lng}\n'
            yaml_content += f'    province: "{province_key}"\n\n'

    return yaml_content

def generate_city_pages():
    """Generate HTML pages for each city - same structure as existing cities"""
    count = 0

    for province_key, cities in PROVINCES_DATA.items():
        province_names = PROVINCE_NAMES[province_key]

        for name, slug, postal, lat, lng in cities:
            # French page - /fr/communes/{slug}.html
            content_fr = f"""---
layout: city
lang: fr
title: "Serrurier {name} | Dépannage 24/24 | Janssens"
description: "Serrurier à {name} : intervention urgente en 30 min. Porte claquée, serrure bloquée ? Dépannage 24h/24 sans dégât. Devis gratuit."
city_name: {name}
slug: {slug}
postal: "{postal}"
region_name: {province_names['fr']}
province: "{province_key}"
breadcrumb:
- name: Zones d'intervention
  url: /fr/#zones
- name: {name}
alternate:
  fr: /fr/communes/{slug}/
  en: /en/cities/{slug}/
  nl: /nl/gemeenten/{slug}/
---
"""
            path_fr = os.path.join(BASE_DIR, "fr", "communes", f"{slug}.html")
            os.makedirs(os.path.dirname(path_fr), exist_ok=True)
            with open(path_fr, 'w', encoding='utf-8') as f:
                f.write(content_fr)
            count += 1

            # Dutch page - /nl/gemeenten/{slug}.html
            content_nl = f"""---
layout: city
lang: nl
title: "Slotenmaker {name} | 24/24 Hulpdienst | Janssens"
description: "Slotenmaker in {name}: dringende interventie in 30 min. Deur dichtgeslagen, slot geblokkeerd? 24u/24 hulpdienst zonder schade."
city_name: {name}
slug: {slug}
postal: "{postal}"
region_name: {province_names['nl']}
province: "{province_key}"
breadcrumb:
- name: Interventiezones
  url: /nl/#zones
- name: {name}
alternate:
  fr: /fr/communes/{slug}/
  en: /en/cities/{slug}/
  nl: /nl/gemeenten/{slug}/
---
"""
            path_nl = os.path.join(BASE_DIR, "nl", "gemeenten", f"{slug}.html")
            os.makedirs(os.path.dirname(path_nl), exist_ok=True)
            with open(path_nl, 'w', encoding='utf-8') as f:
                f.write(content_nl)
            count += 1

            # English page - /en/cities/{slug}.html
            content_en = f"""---
layout: city
lang: en
title: "Locksmith {name} | 24/24 Emergency | Janssens"
description: "Locksmith in {name}: emergency intervention in 30 min. Locked out, broken lock? 24/7 service without damage."
city_name: {name}
slug: {slug}
postal: "{postal}"
region_name: {province_names['en']}
province: "{province_key}"
breadcrumb:
- name: Service areas
  url: /en/#zones
- name: {name}
alternate:
  fr: /fr/communes/{slug}/
  en: /en/cities/{slug}/
  nl: /nl/gemeenten/{slug}/
---
"""
            path_en = os.path.join(BASE_DIR, "en", "cities", f"{slug}.html")
            os.makedirs(os.path.dirname(path_en), exist_ok=True)
            with open(path_en, 'w', encoding='utf-8') as f:
                f.write(content_en)
            count += 1

    return count

def main():
    print("=== Generating Other Provinces Data & Pages ===\n")

    # 1. Generate YAML section
    yaml_section = generate_cities_yaml_section()
    yaml_path = os.path.join(BASE_DIR, "_data", "other_provinces_cities.yml")
    with open(yaml_path, 'w', encoding='utf-8') as f:
        f.write(yaml_section)
    print(f"Generated: {yaml_path}")

    # 2. Generate city pages
    page_count = generate_city_pages()
    print(f"Generated: {page_count} city pages")

    # Summary
    total_cities = sum(len(cities) for cities in PROVINCES_DATA.values())
    print(f"\nTotal: {total_cities} cities across 8 provinces")
    print("Pages: 3 languages x {total_cities} = {page_count} pages")

if __name__ == "__main__":
    main()
