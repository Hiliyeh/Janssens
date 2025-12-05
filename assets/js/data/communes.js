/* =====================================================
   COMMUNES DATA - Centralized municipality data
   ===================================================== */

const COMMUNES = [
    // Bruxelles-Capitale (19 communes)
    { name: 'Anderlecht', region: 'Bruxelles' },
    { name: 'Auderghem', region: 'Bruxelles' },
    { name: 'Berchem-Sainte-Agathe', region: 'Bruxelles' },
    { name: 'Bruxelles-Ville', region: 'Bruxelles' },
    { name: 'Etterbeek', region: 'Bruxelles' },
    { name: 'Evere', region: 'Bruxelles' },
    { name: 'Forest', region: 'Bruxelles' },
    { name: 'Ganshoren', region: 'Bruxelles' },
    { name: 'Ixelles', region: 'Bruxelles' },
    { name: 'Jette', region: 'Bruxelles' },
    { name: 'Koekelberg', region: 'Bruxelles' },
    { name: 'Molenbeek-Saint-Jean', region: 'Bruxelles' },
    { name: 'Saint-Gilles', region: 'Bruxelles' },
    { name: 'Saint-Josse-ten-Noode', region: 'Bruxelles' },
    { name: 'Schaerbeek', region: 'Bruxelles' },
    { name: 'Uccle', region: 'Bruxelles' },
    { name: 'Watermael-Boitsfort', region: 'Bruxelles' },
    { name: 'Woluwe-Saint-Lambert', region: 'Bruxelles' },
    { name: 'Woluwe-Saint-Pierre', region: 'Bruxelles' },
    // Brabant wallon (25 communes)
    { name: 'Beauvechain', region: 'Brabant wallon' },
    { name: 'Braine-l\'Alleud', region: 'Brabant wallon' },
    { name: 'Braine-le-Château', region: 'Brabant wallon' },
    { name: 'Chastre', region: 'Brabant wallon' },
    { name: 'Chaumont-Gistoux', region: 'Brabant wallon' },
    { name: 'Court-Saint-Étienne', region: 'Brabant wallon' },
    { name: 'Genappe', region: 'Brabant wallon' },
    { name: 'Grez-Doiceau', region: 'Brabant wallon' },
    { name: 'Hélécine', region: 'Brabant wallon' },
    { name: 'Incourt', region: 'Brabant wallon' },
    { name: 'Jodoigne', region: 'Brabant wallon' },
    { name: 'La Hulpe', region: 'Brabant wallon' },
    { name: 'Lasne', region: 'Brabant wallon' },
    { name: 'Mont-Saint-Guibert', region: 'Brabant wallon' },
    { name: 'Nivelles', region: 'Brabant wallon' },
    { name: 'Orp-Jauche', region: 'Brabant wallon' },
    { name: 'Ottignies-Louvain-la-Neuve', region: 'Brabant wallon' },
    { name: 'Perwez', region: 'Brabant wallon' },
    { name: 'Ramillies', region: 'Brabant wallon' },
    { name: 'Rixensart', region: 'Brabant wallon' },
    { name: 'Tubize', region: 'Brabant wallon' },
    { name: 'Villers-la-Ville', region: 'Brabant wallon' },
    { name: 'Walhain', region: 'Brabant wallon' },
    { name: 'Waterloo', region: 'Brabant wallon' },
    { name: 'Wavre', region: 'Brabant wallon' },
    // Brabant flamand (52 communes)
    { name: 'Aarschot', region: 'Brabant flamand' },
    { name: 'Asse', region: 'Brabant flamand' },
    { name: 'Beersel', region: 'Brabant flamand' },
    { name: 'Begijnendijk', region: 'Brabant flamand' },
    { name: 'Bekkevoort', region: 'Brabant flamand' },
    { name: 'Bertem', region: 'Brabant flamand' },
    { name: 'Bierbeek', region: 'Brabant flamand' },
    { name: 'Boortmeerbeek', region: 'Brabant flamand' },
    { name: 'Boutersem', region: 'Brabant flamand' },
    { name: 'Diest', region: 'Brabant flamand' },
    { name: 'Dilbeek', region: 'Brabant flamand' },
    { name: 'Drogenbos', region: 'Brabant flamand' },
    { name: 'Geetbets', region: 'Brabant flamand' },
    { name: 'Glabbeek', region: 'Brabant flamand' },
    { name: 'Grimbergen', region: 'Brabant flamand' },
    { name: 'Haacht', region: 'Brabant flamand' },
    { name: 'Halle', region: 'Brabant flamand' },
    { name: 'Herent', region: 'Brabant flamand' },
    { name: 'Hoegaarden', region: 'Brabant flamand' },
    { name: 'Hoeilaart', region: 'Brabant flamand' },
    { name: 'Holsbeek', region: 'Brabant flamand' },
    { name: 'Huldenberg', region: 'Brabant flamand' },
    { name: 'Kampenhout', region: 'Brabant flamand' },
    { name: 'Kapelle-op-den-Bos', region: 'Brabant flamand' },
    { name: 'Keerbergen', region: 'Brabant flamand' },
    { name: 'Kortenaken', region: 'Brabant flamand' },
    { name: 'Kortenberg', region: 'Brabant flamand' },
    { name: 'Kraainem', region: 'Brabant flamand' },
    { name: 'Landen', region: 'Brabant flamand' },
    { name: 'Lennik', region: 'Brabant flamand' },
    { name: 'Leuven', region: 'Brabant flamand' },
    { name: 'Linkebeek', region: 'Brabant flamand' },
    { name: 'Londerzeel', region: 'Brabant flamand' },
    { name: 'Lubbeek', region: 'Brabant flamand' },
    { name: 'Machelen', region: 'Brabant flamand' },
    { name: 'Meise', region: 'Brabant flamand' },
    { name: 'Oud-Heverlee', region: 'Brabant flamand' },
    { name: 'Overijse', region: 'Brabant flamand' },
    { name: 'Rotselaar', region: 'Brabant flamand' },
    { name: 'Scherpenheuvel-Zichem', region: 'Brabant flamand' },
    { name: 'Sint-Genesius-Rode', region: 'Brabant flamand' },
    { name: 'Sint-Pieters-Leeuw', region: 'Brabant flamand' },
    { name: 'Steenokkerzeel', region: 'Brabant flamand' },
    { name: 'Tervuren', region: 'Brabant flamand' },
    { name: 'Tielt-Winge', region: 'Brabant flamand' },
    { name: 'Tienen', region: 'Brabant flamand' },
    { name: 'Tremelo', region: 'Brabant flamand' },
    { name: 'Vilvoorde', region: 'Brabant flamand' },
    { name: 'Wemmel', region: 'Brabant flamand' },
    { name: 'Wezembeek-Oppem', region: 'Brabant flamand' },
    { name: 'Zaventem', region: 'Brabant flamand' },
    { name: 'Zemst', region: 'Brabant flamand' },
    { name: 'Zoutleeuw', region: 'Brabant flamand' }
];

// Location names for interventions (subset for display)
const LOCATIONS = COMMUNES.map(c => c.name);

// Intervention types with weights and i18n keys
const INTERVENTION_TYPES = [
    { i18nKey: 'intervention.door', icon: 'door-open', iconClass: 'door', weight: 35 },
    { i18nKey: 'intervention.slam', icon: 'door-open', iconClass: 'door', weight: 25 },
    { i18nKey: 'intervention.replace', icon: 'lock', iconClass: 'lock', weight: 15 },
    { i18nKey: 'intervention.cylinder', icon: 'lock', iconClass: 'lock', weight: 8 },
    { i18nKey: 'intervention.multipoint', icon: 'lock', iconClass: 'lock', weight: 5 },
    { i18nKey: 'intervention.keys', icon: 'key', iconClass: 'key', weight: 7 },
    { i18nKey: 'intervention.car', icon: 'car', iconClass: 'car', weight: 5 }
];

// Hourly intervention rates (realistic for a small business)
const HOURLY_RATES = [
    0.4, 0.3, 0.2, 0.2, 0.3, 0.5,  // 00h-05h (very quiet night)
    0.6, 0.8, 1.2, 1.3, 1.3, 1.2,  // 06h-11h (morning)
    1.3, 1.3, 1.2, 1.3, 1.3, 1.4,  // 12h-17h (afternoon)
    1.4, 1.3, 1.0, 0.7, 0.5, 0.4   // 18h-23h (evening then quiet)
];

// Export for use in other modules
window.COMMUNES = COMMUNES;
window.LOCATIONS = LOCATIONS;
window.INTERVENTION_TYPES = INTERVENTION_TYPES;
window.HOURLY_RATES = HOURLY_RATES;
