#!/usr/bin/env python3
"""
Add arrondissement field to cities in other_provinces_cities.yml
Based on official Belgian postal code to arrondissement mapping
"""

import yaml
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Comprehensive postal code to arrondissement mapping
# Based on official Belgian administrative divisions
POSTAL_TO_ARRONDISSEMENT = {
    # ============================================
    # ANTWERP PROVINCE
    # ============================================
    # Arrondissement Antwerpen
    "2000": "antwerpen", "2018": "antwerpen", "2020": "antwerpen", "2030": "antwerpen",
    "2040": "antwerpen", "2050": "antwerpen", "2060": "antwerpen", "2070": "antwerpen",
    "2100": "antwerpen", "2140": "antwerpen", "2150": "antwerpen", "2160": "antwerpen",
    "2170": "antwerpen", "2180": "antwerpen", "2500": "antwerpen", "2520": "antwerpen",
    "2530": "antwerpen", "2540": "antwerpen", "2547": "antwerpen", "2550": "antwerpen",
    "2560": "antwerpen", "2570": "antwerpen", "2580": "antwerpen", "2590": "antwerpen",
    "2600": "antwerpen", "2610": "antwerpen", "2620": "antwerpen", "2627": "antwerpen",
    "2630": "antwerpen", "2640": "antwerpen", "2650": "antwerpen", "2660": "antwerpen",
    "2840": "antwerpen", "2845": "antwerpen", "2850": "antwerpen", "2860": "antwerpen",
    "2861": "antwerpen", "2870": "antwerpen", "2880": "antwerpen", "2890": "antwerpen",
    "2900": "antwerpen", "2910": "antwerpen", "2920": "antwerpen", "2930": "antwerpen",
    "2940": "antwerpen", "2950": "antwerpen", "2960": "antwerpen", "2970": "antwerpen",
    "2980": "antwerpen", "2990": "antwerpen",

    # Arrondissement Mechelen
    "2800": "mechelen", "2801": "mechelen", "2811": "mechelen", "2812": "mechelen",
    "2820": "mechelen", "2830": "mechelen", "2850": "mechelen",
    "1800": "mechelen", "1820": "mechelen", "1830": "mechelen", "1840": "mechelen",
    "1850": "mechelen", "1860": "mechelen", "1861": "mechelen", "1880": "mechelen",
    "2220": "mechelen", "2221": "mechelen", "2222": "mechelen", "2223": "mechelen",
    "2230": "mechelen", "2235": "mechelen", "2240": "mechelen", "2242": "mechelen",
    "2243": "mechelen", "2250": "mechelen", "2260": "mechelen", "2270": "mechelen",
    "2275": "mechelen", "2288": "mechelen",

    # Arrondissement Turnhout
    "2200": "turnhout", "2260": "turnhout", "2275": "turnhout", "2280": "turnhout",
    "2288": "turnhout", "2290": "turnhout", "2300": "turnhout", "2310": "turnhout",
    "2320": "turnhout", "2321": "turnhout", "2322": "turnhout", "2323": "turnhout",
    "2328": "turnhout", "2330": "turnhout", "2340": "turnhout", "2350": "turnhout",
    "2360": "turnhout", "2370": "turnhout", "2380": "turnhout", "2381": "turnhout",
    "2382": "turnhout", "2387": "turnhout", "2390": "turnhout", "2400": "turnhout",
    "2430": "turnhout", "2431": "turnhout", "2440": "turnhout", "2450": "turnhout",
    "2460": "turnhout", "2470": "turnhout", "2480": "turnhout", "2490": "turnhout",

    # ============================================
    # LIMBURG PROVINCE
    # ============================================
    # Arrondissement Hasselt
    "3500": "hasselt", "3501": "hasselt", "3510": "hasselt", "3511": "hasselt",
    "3512": "hasselt", "3520": "hasselt", "3530": "hasselt", "3540": "hasselt",
    "3545": "hasselt", "3550": "hasselt", "3560": "hasselt", "3570": "hasselt",
    "3580": "hasselt", "3581": "hasselt", "3582": "hasselt", "3583": "hasselt",
    "3590": "hasselt", "3600": "hasselt", "3620": "hasselt", "3621": "hasselt",
    "3630": "hasselt", "3631": "hasselt", "3640": "hasselt", "3650": "hasselt",
    "3660": "hasselt", "3665": "hasselt", "3668": "hasselt",

    # Arrondissement Maaseik
    "3670": "maaseik", "3680": "maaseik", "3690": "maaseik",
    "3900": "maaseik", "3910": "maaseik", "3920": "maaseik", "3930": "maaseik",
    "3940": "maaseik", "3941": "maaseik", "3945": "maaseik", "3950": "maaseik",
    "3960": "maaseik", "3970": "maaseik", "3971": "maaseik", "3980": "maaseik",
    "3990": "maaseik",

    # Arrondissement Tongeren
    "3700": "tongeren", "3717": "tongeren", "3720": "tongeren", "3721": "tongeren",
    "3722": "tongeren", "3723": "tongeren", "3724": "tongeren", "3730": "tongeren",
    "3732": "tongeren", "3740": "tongeren", "3746": "tongeren", "3770": "tongeren",
    "3790": "tongeren", "3791": "tongeren", "3792": "tongeren", "3793": "tongeren",
    "3798": "tongeren", "3800": "tongeren", "3803": "tongeren", "3806": "tongeren",
    "3830": "tongeren", "3831": "tongeren", "3832": "tongeren", "3840": "tongeren",
    "3850": "tongeren", "3870": "tongeren", "3890": "tongeren", "3891": "tongeren",

    # ============================================
    # EAST FLANDERS PROVINCE
    # ============================================
    # Arrondissement Aalst
    "9300": "aalst", "9308": "aalst", "9310": "aalst", "9320": "aalst",
    "9340": "aalst", "9400": "aalst", "9401": "aalst", "9402": "aalst",
    "9403": "aalst", "9404": "aalst", "9406": "aalst", "9420": "aalst",
    "9450": "aalst", "9451": "aalst", "9470": "aalst", "9472": "aalst",
    "9473": "aalst", "9500": "aalst", "9506": "aalst", "9520": "aalst",
    "9521": "aalst", "9550": "aalst", "9551": "aalst", "9552": "aalst",

    # Arrondissement Dendermonde
    "9200": "dendermonde", "9220": "dendermonde", "9230": "dendermonde",
    "9240": "dendermonde", "9250": "dendermonde", "9255": "dendermonde",
    "9260": "dendermonde", "9270": "dendermonde", "9280": "dendermonde",
    "9290": "dendermonde",

    # Arrondissement Eeklo
    "9900": "eeklo", "9910": "eeklo", "9920": "eeklo", "9921": "eeklo",
    "9930": "eeklo", "9931": "eeklo", "9932": "eeklo", "9940": "eeklo",
    "9950": "eeklo", "9960": "eeklo", "9968": "eeklo", "9970": "eeklo",
    "9971": "eeklo", "9980": "eeklo", "9981": "eeklo", "9982": "eeklo",
    "9988": "eeklo", "9990": "eeklo", "9991": "eeklo", "9992": "eeklo",

    # Arrondissement Gent
    "9000": "gent", "9030": "gent", "9031": "gent", "9032": "gent",
    "9040": "gent", "9041": "gent", "9042": "gent", "9050": "gent",
    "9051": "gent", "9052": "gent", "9060": "gent", "9070": "gent",
    "9080": "gent", "9090": "gent", "9100": "gent",
    "9800": "gent", "9810": "gent", "9820": "gent", "9830": "gent",
    "9831": "gent", "9840": "gent", "9850": "gent", "9860": "gent",
    "9870": "gent", "9880": "gent", "9881": "gent", "9890": "gent",

    # Arrondissement Oudenaarde
    "9600": "oudenaarde", "9620": "oudenaarde", "9630": "oudenaarde",
    "9636": "oudenaarde", "9660": "oudenaarde", "9661": "oudenaarde",
    "9667": "oudenaarde", "9680": "oudenaarde", "9681": "oudenaarde",
    "9688": "oudenaarde", "9690": "oudenaarde", "9700": "oudenaarde",

    # Arrondissement Sint-Niklaas
    "9100": "sint-niklaas", "9111": "sint-niklaas", "9112": "sint-niklaas",
    "9120": "sint-niklaas", "9130": "sint-niklaas", "9140": "sint-niklaas",
    "9150": "sint-niklaas", "9160": "sint-niklaas", "9170": "sint-niklaas",
    "9180": "sint-niklaas", "9185": "sint-niklaas", "9190": "sint-niklaas",

    # ============================================
    # WEST FLANDERS PROVINCE
    # ============================================
    # Arrondissement Brugge
    "8000": "brugge", "8020": "brugge", "8200": "brugge", "8210": "brugge",
    "8211": "brugge", "8300": "brugge", "8301": "brugge", "8310": "brugge",
    "8340": "brugge", "8370": "brugge", "8377": "brugge", "8380": "brugge",

    # Arrondissement Diksmuide
    "8600": "diksmuide", "8610": "diksmuide", "8620": "diksmuide",
    "8630": "diksmuide", "8640": "diksmuide", "8647": "diksmuide",
    "8650": "diksmuide", "8660": "diksmuide", "8670": "diksmuide",
    "8680": "diksmuide", "8690": "diksmuide", "8691": "diksmuide",

    # Arrondissement Ieper
    "8900": "ieper", "8902": "ieper", "8904": "ieper", "8906": "ieper",
    "8908": "ieper", "8920": "ieper", "8930": "ieper", "8940": "ieper",
    "8950": "ieper", "8951": "ieper", "8952": "ieper", "8953": "ieper",
    "8954": "ieper", "8956": "ieper", "8957": "ieper", "8958": "ieper",
    "8970": "ieper", "8972": "ieper", "8978": "ieper", "8980": "ieper",

    # Arrondissement Kortrijk
    "8500": "kortrijk", "8501": "kortrijk", "8510": "kortrijk",
    "8511": "kortrijk", "8520": "kortrijk", "8530": "kortrijk",
    "8531": "kortrijk", "8540": "kortrijk", "8550": "kortrijk",
    "8551": "kortrijk", "8552": "kortrijk", "8553": "kortrijk",
    "8554": "kortrijk", "8560": "kortrijk", "8570": "kortrijk",
    "8572": "kortrijk", "8573": "kortrijk", "8580": "kortrijk",
    "8581": "kortrijk", "8582": "kortrijk", "8583": "kortrijk",
    "8587": "kortrijk", "8590": "kortrijk", "8591": "kortrijk",
    "8770": "kortrijk", "8780": "kortrijk", "8790": "kortrijk",
    "8791": "kortrijk", "8792": "kortrijk", "8793": "kortrijk",
    "8794": "kortrijk",

    # Arrondissement Oostende
    "8400": "oostende", "8420": "oostende", "8430": "oostende",
    "8431": "oostende", "8432": "oostende", "8433": "oostende",
    "8434": "oostende", "8450": "oostende", "8460": "oostende",
    "8470": "oostende", "8480": "oostende",

    # Arrondissement Roeselare
    "8800": "roeselare", "8810": "roeselare", "8820": "roeselare",
    "8830": "roeselare", "8840": "roeselare", "8850": "roeselare",
    "8851": "roeselare", "8860": "roeselare", "8870": "roeselare",
    "8880": "roeselare",

    # Arrondissement Tielt
    "8700": "tielt", "8710": "tielt", "8720": "tielt",
    "8730": "tielt", "8740": "tielt", "8750": "tielt",
    "8755": "tielt", "8760": "tielt", "8780": "tielt",

    # Arrondissement Veurne
    "8620": "veurne", "8630": "veurne", "8640": "veurne",
    "8660": "veurne", "8670": "veurne", "8680": "veurne",
    "8690": "veurne", "8691": "veurne",

    # ============================================
    # HAINAUT PROVINCE
    # ============================================
    # Arrondissement Ath
    "7800": "ath", "7801": "ath", "7802": "ath", "7803": "ath",
    "7804": "ath", "7810": "ath", "7811": "ath", "7812": "ath",
    "7822": "ath", "7823": "ath", "7830": "ath", "7850": "ath",
    "7860": "ath", "7861": "ath", "7862": "ath", "7863": "ath",
    "7864": "ath", "7866": "ath", "7870": "ath", "7880": "ath",
    "7890": "ath", "7900": "ath", "7901": "ath", "7903": "ath",
    "7904": "ath", "7906": "ath", "7910": "ath", "7911": "ath",
    "7912": "ath", "7940": "ath", "7941": "ath", "7942": "ath",
    "7943": "ath", "7950": "ath", "7951": "ath", "7970": "ath",
    "7971": "ath", "7972": "ath", "7973": "ath",

    # Arrondissement Charleroi
    "6000": "charleroi", "6001": "charleroi", "6010": "charleroi",
    "6020": "charleroi", "6030": "charleroi", "6031": "charleroi",
    "6032": "charleroi", "6040": "charleroi", "6041": "charleroi",
    "6042": "charleroi", "6043": "charleroi", "6044": "charleroi",
    "6060": "charleroi", "6061": "charleroi", "6110": "charleroi",
    "6111": "charleroi", "6120": "charleroi", "6140": "charleroi",
    "6141": "charleroi", "6142": "charleroi", "6150": "charleroi",
    "6180": "charleroi", "6181": "charleroi", "6182": "charleroi",
    "6183": "charleroi", "6200": "charleroi", "6210": "charleroi",
    "6211": "charleroi", "6220": "charleroi", "6221": "charleroi",
    "6222": "charleroi", "6223": "charleroi", "6224": "charleroi",
    "6230": "charleroi", "6238": "charleroi", "6240": "charleroi",
    "6250": "charleroi", "6280": "charleroi", "6567": "charleroi",

    # Arrondissement La Louvière
    "7100": "la-louviere", "7110": "la-louviere", "7120": "la-louviere",
    "7130": "la-louviere", "7131": "la-louviere", "7134": "la-louviere",
    "7140": "la-louviere", "7141": "la-louviere", "7160": "la-louviere",
    "7170": "la-louviere", "7180": "la-louviere", "7181": "la-louviere",
    "7190": "la-louviere", "7191": "la-louviere",

    # Arrondissement Mons
    "7000": "mons", "7010": "mons", "7011": "mons", "7012": "mons",
    "7020": "mons", "7021": "mons", "7022": "mons", "7024": "mons",
    "7030": "mons", "7031": "mons", "7032": "mons", "7033": "mons",
    "7034": "mons", "7040": "mons", "7041": "mons", "7050": "mons",
    "7060": "mons", "7061": "mons", "7062": "mons", "7063": "mons",
    "7070": "mons", "7080": "mons", "7300": "mons", "7301": "mons",
    "7320": "mons", "7321": "mons", "7322": "mons", "7330": "mons",
    "7331": "mons", "7332": "mons", "7333": "mons", "7334": "mons",
    "7340": "mons", "7350": "mons", "7370": "mons", "7380": "mons",
    "7382": "mons", "7387": "mons", "7390": "mons",

    # Arrondissement Soignies
    "7060": "soignies", "7063": "soignies", "7070": "soignies",
    "7090": "soignies", "7190": "soignies",

    # Arrondissement Thuin
    "6440": "thuin", "6460": "thuin", "6461": "thuin", "6462": "thuin",
    "6463": "thuin", "6464": "thuin", "6470": "thuin", "6471": "thuin",
    "6472": "thuin", "6500": "thuin", "6510": "thuin", "6511": "thuin",
    "6530": "thuin", "6531": "thuin", "6532": "thuin", "6533": "thuin",
    "6534": "thuin", "6536": "thuin", "6540": "thuin", "6541": "thuin",
    "6542": "thuin", "6543": "thuin", "6560": "thuin", "6561": "thuin",
    "6567": "thuin", "6590": "thuin", "6591": "thuin", "6592": "thuin",
    "6593": "thuin", "6594": "thuin", "6596": "thuin",

    # Arrondissement Tournai-Mouscron
    "7500": "tournai", "7501": "tournai", "7502": "tournai", "7503": "tournai",
    "7504": "tournai", "7506": "tournai", "7510": "tournai", "7511": "tournai",
    "7512": "tournai", "7513": "tournai", "7520": "tournai", "7521": "tournai",
    "7522": "tournai", "7530": "tournai", "7531": "tournai", "7532": "tournai",
    "7533": "tournai", "7534": "tournai", "7536": "tournai", "7538": "tournai",
    "7540": "tournai", "7542": "tournai", "7543": "tournai", "7548": "tournai",
    "7600": "tournai", "7601": "tournai", "7602": "tournai", "7603": "tournai",
    "7604": "tournai", "7608": "tournai", "7610": "tournai", "7611": "tournai",
    "7618": "tournai", "7619": "tournai", "7620": "tournai", "7621": "tournai",
    "7622": "tournai", "7623": "tournai", "7624": "tournai", "7640": "tournai",
    "7641": "tournai", "7642": "tournai", "7643": "tournai", "7700": "tournai",
    "7711": "tournai", "7712": "tournai", "7730": "tournai", "7740": "tournai",
    "7742": "tournai", "7743": "tournai", "7750": "tournai", "7760": "tournai",
    "7780": "tournai", "7781": "tournai", "7782": "tournai", "7783": "tournai",
    "7784": "tournai",

    # ============================================
    # LIÈGE PROVINCE
    # ============================================
    # Arrondissement Huy
    "4500": "huy", "4520": "huy", "4530": "huy", "4537": "huy",
    "4540": "huy", "4550": "huy", "4557": "huy", "4560": "huy",
    "4570": "huy", "4577": "huy", "4590": "huy",

    # Arrondissement Liège
    "4000": "liege", "4020": "liege", "4030": "liege", "4031": "liege",
    "4032": "liege", "4040": "liege", "4041": "liege", "4042": "liege",
    "4050": "liege", "4051": "liege", "4052": "liege", "4053": "liege",
    "4100": "liege", "4101": "liege", "4102": "liege", "4120": "liege",
    "4121": "liege", "4122": "liege", "4130": "liege", "4140": "liege",
    "4141": "liege", "4160": "liege", "4161": "liege", "4162": "liege",
    "4163": "liege", "4170": "liege", "4180": "liege", "4181": "liege",
    "4190": "liege", "4210": "liege", "4217": "liege", "4218": "liege",
    "4219": "liege", "4250": "liege", "4252": "liege", "4253": "liege",
    "4254": "liege", "4257": "liege", "4260": "liege", "4261": "liege",
    "4263": "liege", "4280": "liege", "4287": "liege", "4300": "liege",
    "4340": "liege", "4341": "liege", "4342": "liege", "4347": "liege",
    "4350": "liege", "4351": "liege", "4357": "liege", "4360": "liege",
    "4367": "liege", "4400": "liege", "4420": "liege", "4430": "liege",
    "4431": "liege", "4432": "liege", "4450": "liege", "4451": "liege",
    "4452": "liege", "4453": "liege", "4458": "liege", "4460": "liege",
    "4470": "liege", "4480": "liege", "4600": "liege", "4601": "liege",
    "4602": "liege", "4607": "liege", "4608": "liege", "4610": "liege",
    "4620": "liege", "4621": "liege", "4623": "liege", "4624": "liege",
    "4630": "liege", "4631": "liege", "4632": "liege", "4633": "liege",
    "4650": "liege", "4651": "liege", "4652": "liege", "4653": "liege",
    "4654": "liege", "4670": "liege", "4671": "liege", "4672": "liege",
    "4680": "liege", "4681": "liege", "4682": "liege", "4683": "liege",
    "4684": "liege", "4690": "liege",

    # Arrondissement Verviers
    "4700": "verviers", "4701": "verviers", "4710": "verviers", "4711": "verviers",
    "4720": "verviers", "4721": "verviers", "4728": "verviers", "4730": "verviers",
    "4731": "verviers", "4750": "verviers", "4760": "verviers", "4761": "verviers",
    "4770": "verviers", "4771": "verviers", "4780": "verviers", "4781": "verviers",
    "4782": "verviers", "4783": "verviers", "4784": "verviers", "4790": "verviers",
    "4791": "verviers", "4800": "verviers", "4801": "verviers", "4802": "verviers",
    "4820": "verviers", "4821": "verviers", "4830": "verviers", "4831": "verviers",
    "4834": "verviers", "4837": "verviers", "4840": "verviers", "4841": "verviers",
    "4845": "verviers", "4850": "verviers", "4851": "verviers", "4852": "verviers",
    "4860": "verviers", "4861": "verviers", "4870": "verviers", "4877": "verviers",
    "4880": "verviers", "4890": "verviers", "4900": "verviers", "4910": "verviers",
    "4920": "verviers", "4950": "verviers", "4960": "verviers", "4970": "verviers",
    "4980": "verviers", "4983": "verviers", "4987": "verviers", "4990": "verviers",

    # Arrondissement Waremme
    "4280": "waremme", "4287": "waremme", "4350": "waremme", "4351": "waremme",
    "4357": "waremme", "4360": "waremme", "4367": "waremme",

    # ============================================
    # NAMUR PROVINCE
    # ============================================
    # Arrondissement Dinant
    "5500": "dinant", "5501": "dinant", "5502": "dinant", "5503": "dinant",
    "5504": "dinant", "5510": "dinant", "5520": "dinant", "5521": "dinant",
    "5522": "dinant", "5523": "dinant", "5524": "dinant", "5530": "dinant",
    "5537": "dinant", "5540": "dinant", "5541": "dinant", "5542": "dinant",
    "5543": "dinant", "5544": "dinant", "5550": "dinant", "5555": "dinant",
    "5560": "dinant", "5561": "dinant", "5562": "dinant", "5563": "dinant",
    "5564": "dinant", "5570": "dinant", "5571": "dinant", "5572": "dinant",
    "5573": "dinant", "5574": "dinant", "5575": "dinant", "5576": "dinant",
    "5580": "dinant", "5590": "dinant", "5600": "dinant", "5620": "dinant",
    "5621": "dinant", "5630": "dinant", "5640": "dinant", "5641": "dinant",
    "5644": "dinant", "5646": "dinant", "5650": "dinant", "5651": "dinant",
    "5660": "dinant", "5670": "dinant", "5680": "dinant",

    # Arrondissement Namur
    "5000": "namur", "5001": "namur", "5002": "namur", "5003": "namur",
    "5004": "namur", "5010": "namur", "5012": "namur", "5014": "namur",
    "5020": "namur", "5021": "namur", "5022": "namur", "5024": "namur",
    "5030": "namur", "5031": "namur", "5032": "namur", "5060": "namur",
    "5070": "namur", "5080": "namur", "5081": "namur", "5100": "namur",
    "5101": "namur", "5140": "namur", "5150": "namur", "5170": "namur",
    "5190": "namur", "5300": "namur", "5310": "namur", "5330": "namur",
    "5332": "namur", "5333": "namur", "5334": "namur", "5336": "namur",
    "5340": "namur", "5350": "namur", "5351": "namur", "5352": "namur",
    "5353": "namur", "5354": "namur", "5360": "namur", "5361": "namur",
    "5362": "namur", "5363": "namur", "5364": "namur", "5370": "namur",
    "5372": "namur", "5374": "namur", "5376": "namur", "5377": "namur",
    "5380": "namur", "5530": "namur", "5537": "namur",

    # Arrondissement Philippeville
    "5600": "philippeville", "5620": "philippeville", "5621": "philippeville",
    "5630": "philippeville", "5640": "philippeville", "5641": "philippeville",
    "5644": "philippeville", "5646": "philippeville", "5650": "philippeville",
    "5651": "philippeville", "5660": "philippeville", "5670": "philippeville",
    "5680": "philippeville",

    # ============================================
    # LUXEMBOURG PROVINCE
    # ============================================
    # Arrondissement Arlon
    "6700": "arlon", "6704": "arlon", "6706": "arlon", "6717": "arlon",
    "6720": "arlon", "6724": "arlon", "6730": "arlon", "6740": "arlon",
    "6741": "arlon", "6742": "arlon", "6743": "arlon", "6747": "arlon",
    "6750": "arlon", "6760": "arlon", "6761": "arlon", "6762": "arlon",
    "6767": "arlon", "6780": "arlon", "6781": "arlon", "6782": "arlon",
    "6790": "arlon", "6791": "arlon", "6792": "arlon",

    # Arrondissement Bastogne
    "6600": "bastogne", "6630": "bastogne", "6637": "bastogne",
    "6640": "bastogne", "6642": "bastogne", "6660": "bastogne",
    "6661": "bastogne", "6662": "bastogne", "6663": "bastogne",
    "6666": "bastogne", "6670": "bastogne", "6671": "bastogne",
    "6672": "bastogne", "6673": "bastogne", "6674": "bastogne",
    "6680": "bastogne", "6681": "bastogne", "6686": "bastogne",
    "6687": "bastogne", "6688": "bastogne", "6690": "bastogne",
    "6692": "bastogne", "6698": "bastogne",

    # Arrondissement Marche-en-Famenne
    "6900": "marche", "6920": "marche", "6921": "marche", "6922": "marche",
    "6924": "marche", "6927": "marche", "6929": "marche", "6940": "marche",
    "6941": "marche", "6950": "marche", "6951": "marche", "6952": "marche",
    "6953": "marche", "6960": "marche", "6970": "marche", "6971": "marche",
    "6972": "marche", "6980": "marche", "6982": "marche", "6983": "marche",
    "6984": "marche", "6986": "marche", "6987": "marche", "6990": "marche",
    "6997": "marche",

    # Arrondissement Neufchâteau
    "6800": "neufchateau", "6810": "neufchateau", "6811": "neufchateau",
    "6820": "neufchateau", "6821": "neufchateau", "6823": "neufchateau",
    "6824": "neufchateau", "6830": "neufchateau", "6831": "neufchateau",
    "6832": "neufchateau", "6833": "neufchateau", "6834": "neufchateau",
    "6836": "neufchateau", "6838": "neufchateau", "6840": "neufchateau",
    "6850": "neufchateau", "6851": "neufchateau", "6852": "neufchateau",
    "6853": "neufchateau", "6856": "neufchateau", "6857": "neufchateau",
    "6858": "neufchateau", "6860": "neufchateau", "6870": "neufchateau",
    "6880": "neufchateau", "6890": "neufchateau",

    # Arrondissement Virton
    "6760": "virton", "6761": "virton", "6762": "virton", "6767": "virton",
    "6769": "virton", "6780": "virton", "6781": "virton", "6782": "virton",
    "6790": "virton", "6791": "virton", "6792": "virton",
}


def get_arrondissement_by_postal(postal_code):
    """Get arrondissement ID based on postal code"""
    if postal_code in POSTAL_TO_ARRONDISSEMENT:
        return POSTAL_TO_ARRONDISSEMENT[postal_code]

    # Try first 2 digits for broader match
    prefix_2 = postal_code[:2] + "00"
    if prefix_2 in POSTAL_TO_ARRONDISSEMENT:
        return POSTAL_TO_ARRONDISSEMENT[prefix_2]

    return None


def add_arrondissements():
    """Add arrondissement field to cities in other_provinces_cities.yml"""

    yaml_path = os.path.join(BASE_DIR, "_data", "other_provinces_cities.yml")

    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    updated_count = 0
    missing_count = 0

    for province_key, cities in data.items():
        if not isinstance(cities, list):
            continue

        for city in cities:
            postal = str(city.get('postal', ''))
            arrondissement = get_arrondissement_by_postal(postal)

            if arrondissement:
                city['arrondissement'] = arrondissement
                updated_count += 1
            else:
                print(f"Warning: No arrondissement found for {city['name']} (postal: {postal})")
                missing_count += 1

    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Updated {updated_count} cities with arrondissement")
    print(f"Missing arrondissement for {missing_count} cities")

    return updated_count, missing_count


def main():
    print("=== Adding Arrondissements to Cities ===\n")
    updated, missing = add_arrondissements()
    print(f"\nDone! {updated} cities updated, {missing} cities without arrondissement")


if __name__ == "__main__":
    main()
