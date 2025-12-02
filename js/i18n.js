/* =====================================================
   JANSSENS SERRURIER - Internationalization System
   Languages: FR (default) | NL | EN
   ===================================================== */

const i18n = {
    currentLang: 'fr',

    translations: {
        // =====================================================
        // FRENCH (Default)
        // =====================================================
        fr: {
            // Navigation
            'nav.services': 'Services',
            'nav.pourquoi': 'Pourquoi nous',
            'nav.confiance': 'Engagements',
            'nav.zones': 'Intervention',
            'nav.contact': 'Contact',
            'nav.call': 'Appeler',
            'nav.whatsapp': 'WhatsApp',

            // Hero
            'hero.title.1': 'Votre serrurier',
            'hero.title.2': 'Bruxelles, Brabant wallon & flamand',
            'hero.text': 'Porte claquée ? Clé perdue ? Nous arrivons en <strong>30 minutes</strong>, sans abîmer votre porte. Plus de <strong>10 ans</strong> d\'expérience, entreprise enregistrée, prix annoncé avant intervention.',
            'hero.cta.call': 'Appeler maintenant',
            'hero.cta.whatsapp': 'WhatsApp',
            'hero.trust.1': 'Sans dégât',
            'hero.trust.2': 'Prix fixe annoncé',
            'hero.trust.3': 'Paiement après service',

            // Stats
            'stat.delay': 'Délai moyen',
            'stat.experience': 'Ans d\'expérience',
            'stat.communes': 'Communes couvertes',

            // Urgence Banner
            'urgence.title': 'Porte claquée ? Clé perdue ou cassée ?',
            'urgence.text': 'Un serrurier qualifié arrive chez vous en moins de 30 minutes.',
            'urgence.btn': 'Appel d\'urgence',

            // Services Section
            'services.tag': 'Nos services',
            'services.title': 'Solutions de serrurerie professionnelles',
            'services.desc': 'Des interventions rapides et soignées pour tous vos besoins en sécurité',

            // Service Cards
            'service.door.title': 'Ouverture de porte',
            'service.door.text': 'Porte claquée ou bloquée ? Intervention rapide sans endommager votre serrure ni votre porte.',
            'service.door.tag1': 'Urgence 24/7',
            'service.door.tag2': 'Sans dégât',
            'service.door.tag3': 'Toutes portes',

            'service.install.title': 'Installation de serrures',
            'service.install.text': 'Pose de serrures haute sécurité, cylindres européens, serrures multipoints et verrous.',
            'service.install.tag1': 'Haute sécurité',
            'service.install.tag2': 'Multipoints',
            'service.install.tag3': 'Toutes marques',

            'service.repair.title': 'Réparation de serrures',
            'service.repair.text': 'Diagnostic et réparation de serrures défectueuses. Remplacement de cylindres et mécanismes.',
            'service.repair.tag1': 'Diagnostic',
            'service.repair.tag2': 'Cylindres',
            'service.repair.tag3': 'Mécanismes',

            'service.keys.title': 'Duplication de clés',
            'service.keys.text': 'Copie de clés en 1 minute. Clés plates, à gorges, haute sécurité et clés de voiture.',
            'service.keys.tag1': 'Express',
            'service.keys.tag2': 'Toutes clés',
            'service.keys.tag3': 'Sur place',

            'service.auto.title': 'Serrurerie automobile',
            'service.auto.text': 'Ouverture de véhicule, duplication de clés auto, programmation de télécommandes.',
            'service.auto.tag1': 'Ouverture auto',
            'service.auto.tag2': 'Clés voiture',
            'service.auto.tag3': 'Télécommandes',

            'service.safe.title': 'Coffres-forts',
            'service.safe.text': 'Vente, installation et ouverture de coffres-forts. Marque Burg Wächter.',
            'service.safe.tag1': 'Burg Wächter',
            'service.safe.tag2': 'Installation',
            'service.safe.tag3': 'Ouverture',

            // Pourquoi Section
            'pourquoi.tag': 'Pourquoi Janssens ?',
            'pourquoi.title': 'La confiance se construit',
            'pourquoi.intro': 'Depuis plus de 10 ans, nous intervenons auprès des particuliers, entreprises et institutions de Bruxelles et du Brabant. Notre réputation repose sur trois engagements.',

            'pillar.speed.title': 'Rapidité',
            'pillar.speed.text': 'Intervention garantie en moins de 30 minutes, 24h/24 et 7j/7, jours fériés inclus.',
            'pillar.expertise.title': 'Expertise',
            'pillar.expertise.text': 'Techniciens certifiés, équipement professionnel, travail soigné et sans dégât.',
            'pillar.transparency.title': 'Transparence',
            'pillar.transparency.text': 'Prix annoncé avant intervention. Aucune surprise. Paiement uniquement après service.',

            'trust.available.title': 'Disponible 24h/24',
            'trust.available.text': 'Jours fériés et weekends inclus',
            'trust.registered.title': 'Entreprise enregistrée',
            'trust.registered.text': 'TVA BE0712.625.742 · LAMRO GROUP',
            'trust.certified.title': 'Techniciens certifiés',
            'trust.certified.text': 'Formation continue sur toutes les marques',

            // Confiance Section
            'confiance.tag': 'Notre couverture',
            'confiance.title': 'Toujours proche de vous',
            'live.title': 'Interventions en direct',
            'live.today': 'Aujourd\'hui:',
            'badge.registered': 'Entreprise enregistrée',

            // Intervention statuses
            'status.enroute': 'En route',
            'status.ongoing': 'En cours',
            'status.completed': 'Terminé',

            // Zones Section
            'zones.tag': 'Zones d\'intervention',
            'zones.title': 'Êtes-vous dans notre zone ?',
            'zones.desc': 'Vérifiez en 1 seconde si nous intervenons chez vous',
            'zones.placeholder': 'Entrez votre commune...',
            'zones.initial': 'Tapez le nom de votre commune pour vérifier',
            'zones.success.title': 'Bonne nouvelle !',
            'zones.success.text': 'Nous intervenons à',
            'zones.success.delay': 'Intervention en <strong>~30 min</strong>',
            'zones.success.available': 'Disponible <strong>24h/24</strong>',
            'zones.success.cta': 'Appeler maintenant',
            'zones.notfound.title': 'Zone non listée',
            'zones.notfound.text': 'Contactez-nous, nous pouvons peut-être intervenir.',
            'zones.notfound.cta': 'Nous contacter',
            'zones.regions.title': 'Nos 96 communes couvertes :',
            'zones.region.brussels': 'Bruxelles-Capitale',
            'zones.region.brabant.wallon': 'Brabant wallon',
            'zones.region.brabant.flamand': 'Brabant flamand',

            // FAQ Section
            'faq.tag': 'FAQ',
            'faq.title': 'Questions fréquentes',

            'faq.q1': 'Quelle est la différence entre une serrure standard et haute sécurité ?',
            'faq.a1': 'La serrure haute sécurité offre une meilleure protection contre les effractions grâce à des mécanismes renforcés, des cylindres anti-crochetage et anti-perçage. Elle est recommandée pour les portes d\'entrée.',

            'faq.q2': 'Quels sont vos horaires d\'intervention ?',
            'faq.a2': 'Nous sommes disponibles 24h/24 et 7j/7, y compris les jours fériés. Une urgence n\'attend pas, et nous non plus.',

            'faq.q3': 'Comment savoir si ma serrure doit être remplacée ?',
            'faq.a3': 'Si votre serrure est difficile à ouvrir, grince, montre des signes d\'usure ou ne sécurise plus correctement votre porte, il est temps de la remplacer. Nous pouvons effectuer un diagnostic gratuit.',

            'faq.q4': 'Intervenez-vous sur toutes les marques de serrures ?',
            'faq.a4': 'Oui, nos techniciens sont formés pour intervenir sur toutes les marques et tous les types de serrures du marché : Vachette, Bricard, Fichet, Yale, Abus, et bien d\'autres.',

            'faq.q5': 'Pouvez-vous ouvrir les portes blindées ?',
            'faq.a5': 'Oui, nous avons l\'expertise et l\'équipement nécessaires pour ouvrir, réparer et installer des serrures sur portes blindées, sans les endommager.',

            'faq.q6': 'Combien coûte un serrurier de nuit à Bruxelles ?',
            'faq.a6': 'Nos tarifs sont transparents et communiqués avant intervention, même la nuit. Pas de supplément caché. Appelez le 0495 205 400 pour un devis immédiat gratuit.',

            'faq.q7': 'Comment ouvrir une porte claquée sans clé ?',
            'faq.a7': 'N\'essayez pas d\'ouvrir vous-même, vous risquez d\'endommager la serrure. Appelez un serrurier professionnel comme Janssens Serrurier qui utilise des techniques non-destructives pour ouvrir votre porte en quelques minutes.',

            'faq.q8': 'Quel serrurier appeler en urgence à Uccle, Ixelles ou Waterloo ?',
            'faq.a8': 'Janssens Serrurier intervient à Uccle, Ixelles, Waterloo et toutes les communes de Bruxelles et du Brabant en moins de 30 minutes. Appelez le 0495 205 400, disponible 24h/24.',

            'faq.q9': 'Changement de serrure après cambriolage : que faire ?',
            'faq.a9': 'Après un cambriolage, appelez d\'abord la police puis contactez Janssens Serrurier au 0495 205 400. Nous intervenons en urgence pour sécuriser votre domicile avec une serrure haute sécurité certifiée.',

            // Contact Section
            'contact.tag': 'Contact',
            'contact.title': 'Besoin d\'un serrurier ?',
            'contact.text': 'Appelez-nous directement ou envoyez-nous un message. Nous répondons en quelques minutes.',
            'contact.phone': 'Téléphone',
            'contact.whatsapp': 'WhatsApp',
            'contact.whatsapp.text': 'Réponse rapide',
            'contact.email': 'Email',
            'contact.address': 'Adresse',

            // Footer
            'footer.desc': 'Votre expert en serrurerie à Bruxelles depuis plus de 10 ans. Disponible 24h/24, 7j/7 pour toutes vos urgences.',
            'footer.services': 'Services',
            'footer.services.door': 'Ouverture de porte',
            'footer.services.install': 'Installation serrure',
            'footer.services.keys': 'Duplication clés',
            'footer.services.auto': 'Serrurerie auto',
            'footer.services.safe': 'Coffres-forts',
            'footer.company': 'Entreprise',
            'footer.company.about': 'À propos',
            'footer.company.partners': 'Partenaires',
            'footer.company.zones': 'Intervention',
            'footer.company.faq': 'FAQ',
            'footer.company.contact': 'Contact',
            'footer.contact': 'Contact',
            'footer.terms': 'Conditions d\'utilisation',
            'footer.privacy': 'Politique de confidentialité',
            'footer.credit': 'Conçu par',

            // Floating CTA
            'floating.call': 'Appeler',

            // Language selector
            'lang.select': 'Langue',

            // Dynamic interventions
            'intervention.door': 'Ouverture de porte',
            'intervention.slam': 'Porte claquée',
            'intervention.replace': 'Remplacement serrure',
            'intervention.cylinder': 'Installation cylindre',
            'intervention.multipoint': 'Serrure multipoints',
            'intervention.keys': 'Duplication clés',
            'intervention.car': 'Ouverture véhicule',
            'intervention.ago': 'Il y a',
            'intervention.now': 'À l\'instant',
            'intervention.min': 'min',
            'intervention.hour': 'h',

            // Legal pages - Common
            'legal.back': 'Retour à l\'accueil',
            'legal.updated': 'Dernière mise à jour : Décembre 2024',

            // Conditions page
            'conditions.title': 'Conditions d\'utilisation',
            'conditions.1.title': '1. Présentation',
            'conditions.1.text1': 'Les présentes conditions générales d\'utilisation régissent l\'accès et l\'utilisation du site web <strong>janssensserrurier.be</strong>, exploité par <strong>LAMRO GROUP</strong>, société enregistrée en Belgique sous le numéro TVA BE0712.625.742, dont le siège social est situé Chaussée de Louvain 629, 1030 Bruxelles.',
            'conditions.1.text2': 'En accédant à ce site, vous acceptez sans réserve les présentes conditions d\'utilisation.',
            'conditions.2.title': '2. Services proposés',
            'conditions.2.text': 'Janssens Serrurier propose des services de serrurerie professionnels, incluant notamment :',
            'conditions.2.li1': 'Ouverture de portes claquées ou bloquées',
            'conditions.2.li2': 'Installation et remplacement de serrures',
            'conditions.2.li3': 'Duplication de clés',
            'conditions.2.li4': 'Serrurerie automobile',
            'conditions.2.li5': 'Installation de coffres-forts',
            'conditions.2.li6': 'Dépannage d\'urgence 24h/24',
            'conditions.3.title': '3. Tarification et paiement',
            'conditions.3.text1': 'Les tarifs de nos interventions sont communiqués avant toute prestation. Un devis gratuit et sans engagement est systématiquement proposé.',
            'conditions.3.text2': 'Le paiement s\'effectue à la fin de l\'intervention par les moyens suivants : espèces, carte bancaire (Bancontact), ou virement.',
            'conditions.3.text3': 'Aucun acompte n\'est demandé avant l\'intervention.',
            'conditions.4.title': '4. Zone d\'intervention',
            'conditions.4.text': 'Nos services couvrent l\'ensemble de la Région de Bruxelles-Capitale (19 communes), le Brabant wallon et le Brabant flamand, soit 96 communes au total.',
            'conditions.5.title': '5. Garanties',
            'conditions.5.text1': 'Toutes nos interventions sont garanties. Les pièces installées (serrures, cylindres) bénéficient de la garantie fabricant.',
            'conditions.5.text2': 'En cas de problème suite à une intervention, contactez-nous dans les meilleurs délais pour une prise en charge rapide.',
            'conditions.6.title': '6. Responsabilité',
            'conditions.6.text1': 'Janssens Serrurier s\'engage à fournir des services de qualité professionnelle. Notre responsabilité est limitée au montant de la prestation en cas de dommage direct prouvé.',
            'conditions.6.text2': 'Nous ne pouvons être tenus responsables des dommages indirects ou des circonstances de force majeure.',
            'conditions.7.title': '7. Propriété intellectuelle',
            'conditions.7.text': 'L\'ensemble des contenus du site (textes, images, logo, design) sont la propriété exclusive de LAMRO GROUP ou de ses partenaires. Toute reproduction sans autorisation préalable est interdite.',
            'conditions.8.title': '8. Modification des conditions',
            'conditions.8.text': 'Nous nous réservons le droit de modifier ces conditions à tout moment. Les modifications prennent effet dès leur publication sur le site.',
            'conditions.9.title': '9. Droit applicable et juridiction',
            'conditions.9.text': 'Les présentes conditions sont régies par le droit belge. En cas de litige, les tribunaux de Bruxelles seront seuls compétents.',
            'conditions.10.title': '10. Contact',
            'conditions.10.text': 'Pour toute question concernant ces conditions d\'utilisation :',

            // Privacy page
            'privacy.title': 'Politique de confidentialité',
            'privacy.1.title': '1. Introduction',
            'privacy.1.text1': '<strong>LAMRO GROUP</strong> (ci-après "nous", "notre" ou "Janssens Serrurier"), en tant que responsable du traitement, s\'engage à protéger la vie privée des utilisateurs de son site web janssensserrurier.be.',
            'privacy.1.text2': 'Cette politique de confidentialité explique comment nous collectons, utilisons et protégeons vos données personnelles, conformément au Règlement Général sur la Protection des Données (RGPD).',
            'privacy.1.box': '<strong>Responsable du traitement :</strong><br>LAMRO GROUP - TVA BE0712.625.742<br>Chaussée de Louvain 629, 1030 Bruxelles<br>Email : info@janssensserrurier.be',
            'privacy.2.title': '2. Données collectées',
            'privacy.2.text': 'Dans le cadre de nos activités, nous pouvons collecter les données suivantes :',
            'privacy.2.li1': '<strong>Données d\'identification :</strong> nom, prénom, adresse',
            'privacy.2.li2': '<strong>Données de contact :</strong> numéro de téléphone, adresse email',
            'privacy.2.li3': '<strong>Données de localisation :</strong> adresse d\'intervention',
            'privacy.2.li4': '<strong>Données techniques :</strong> adresse IP, type de navigateur, pages visitées (via cookies)',
            'privacy.3.title': '3. Finalités du traitement',
            'privacy.3.text': 'Vos données personnelles sont traitées pour les finalités suivantes :',
            'privacy.3.li1': 'Répondre à vos demandes de devis et d\'intervention',
            'privacy.3.li2': 'Fournir nos services de serrurerie',
            'privacy.3.li3': 'Établir et envoyer les factures',
            'privacy.3.li4': 'Assurer le suivi et la garantie des interventions',
            'privacy.3.li5': 'Améliorer la qualité de nos services et de notre site web',
            'privacy.3.li6': 'Respecter nos obligations légales et fiscales',
            'privacy.4.title': '4. Base légale du traitement',
            'privacy.4.text': 'Nous traitons vos données sur les bases légales suivantes :',
            'privacy.4.li1': '<strong>Exécution d\'un contrat :</strong> pour fournir les services demandés',
            'privacy.4.li2': '<strong>Obligation légale :</strong> pour respecter nos obligations fiscales',
            'privacy.4.li3': '<strong>Intérêt légitime :</strong> pour améliorer nos services',
            'privacy.4.li4': '<strong>Consentement :</strong> pour l\'envoi de communications marketing (le cas échéant)',
            'privacy.5.title': '5. Durée de conservation',
            'privacy.5.text': 'Vos données personnelles sont conservées :',
            'privacy.5.li1': '<strong>Données clients :</strong> pendant la durée de la relation commerciale, puis 10 ans pour les obligations comptables',
            'privacy.5.li2': '<strong>Données de prospects :</strong> 3 ans à compter du dernier contact',
            'privacy.5.li3': '<strong>Cookies :</strong> maximum 13 mois',
            'privacy.6.title': '6. Partage des données',
            'privacy.6.text': 'Vos données peuvent être partagées avec :',
            'privacy.6.li1': 'Nos techniciens pour les interventions sur site',
            'privacy.6.li2': 'Notre comptable pour la facturation',
            'privacy.6.li3': 'Les autorités compétentes si requis par la loi',
            'privacy.6.text2': 'Nous ne vendons jamais vos données à des tiers. Nous ne transférons pas vos données en dehors de l\'Espace Économique Européen.',
            'privacy.7.title': '7. Cookies',
            'privacy.7.text': 'Notre site utilise des cookies pour :',
            'privacy.7.li1': '<strong>Cookies essentiels :</strong> nécessaires au fonctionnement du site',
            'privacy.7.li2': '<strong>Cookies analytiques :</strong> pour comprendre l\'utilisation du site (anonymisés)',
            'privacy.7.text2': 'Vous pouvez gérer vos préférences de cookies via les paramètres de votre navigateur.',
            'privacy.8.title': '8. Vos droits',
            'privacy.8.text': 'Conformément au RGPD, vous disposez des droits suivants :',
            'privacy.8.li1': '<strong>Droit d\'accès :</strong> obtenir une copie de vos données',
            'privacy.8.li2': '<strong>Droit de rectification :</strong> corriger vos données inexactes',
            'privacy.8.li3': '<strong>Droit à l\'effacement :</strong> demander la suppression de vos données',
            'privacy.8.li4': '<strong>Droit à la portabilité :</strong> recevoir vos données dans un format structuré',
            'privacy.8.li5': '<strong>Droit d\'opposition :</strong> vous opposer au traitement de vos données',
            'privacy.8.li6': '<strong>Droit de limitation :</strong> limiter le traitement de vos données',
            'privacy.8.text2': 'Pour exercer ces droits, contactez-nous à info@janssensserrurier.be.',
            'privacy.9.title': '9. Sécurité des données',
            'privacy.9.text': 'Nous mettons en œuvre des mesures techniques et organisationnelles appropriées pour protéger vos données contre l\'accès non autorisé, la perte ou la destruction :',
            'privacy.9.li1': 'Connexion HTTPS sécurisée',
            'privacy.9.li2': 'Accès limité aux données sur une base "need-to-know"',
            'privacy.9.li3': 'Mises à jour régulières de sécurité',
            'privacy.10.title': '10. Réclamation',
            'privacy.10.text': 'Si vous estimez que vos droits ne sont pas respectés, vous pouvez introduire une réclamation auprès de l\'Autorité de Protection des Données (APD) :',
            'privacy.11.title': '11. Modifications',
            'privacy.11.text': 'Cette politique de confidentialité peut être mise à jour. Nous vous informerons de tout changement significatif via notre site web.',
            'privacy.12.title': '12. Contact',
            'privacy.12.text': 'Pour toute question relative à cette politique ou à vos données personnelles :'
        },

        // =====================================================
        // DUTCH (Nederlands)
        // =====================================================
        nl: {
            // Navigation
            'nav.services': 'Diensten',
            'nav.pourquoi': 'Waarom wij',
            'nav.confiance': 'Engagementen',
            'nav.zones': 'Interventie',
            'nav.contact': 'Contact',
            'nav.call': 'Bellen',
            'nav.whatsapp': 'WhatsApp',

            // Hero
            'hero.title.1': 'Uw slotenmaker',
            'hero.title.2': 'Brussel, Waals- & Vlaams-Brabant',
            'hero.text': 'Deur dichtgevallen? Sleutel verloren? Wij zijn er binnen <strong>30 minuten</strong>, zonder uw deur te beschadigen. Meer dan <strong>10 jaar</strong> ervaring, geregistreerd bedrijf, prijs meegedeeld voor interventie.',
            'hero.cta.call': 'Nu bellen',
            'hero.cta.whatsapp': 'WhatsApp',
            'hero.trust.1': 'Zonder schade',
            'hero.trust.2': 'Vaste prijs',
            'hero.trust.3': 'Betaling na service',

            // Stats
            'stat.delay': 'Gemiddelde tijd',
            'stat.experience': 'Jaar ervaring',
            'stat.communes': 'Gemeenten gedekt',

            // Urgence Banner
            'urgence.title': 'Deur dichtgevallen? Sleutel verloren of gebroken?',
            'urgence.text': 'Een gekwalificeerde slotenmaker is binnen 30 minuten bij u.',
            'urgence.btn': 'Noodoproep',

            // Services Section
            'services.tag': 'Onze diensten',
            'services.title': 'Professionele slotenmakeroplossingen',
            'services.desc': 'Snelle en zorgvuldige interventies voor al uw beveiligingsbehoeften',

            // Service Cards
            'service.door.title': 'Deuropening',
            'service.door.text': 'Deur dichtgevallen of geblokkeerd? Snelle interventie zonder uw slot of deur te beschadigen.',
            'service.door.tag1': 'Noodgeval 24/7',
            'service.door.tag2': 'Zonder schade',
            'service.door.tag3': 'Alle deuren',

            'service.install.title': 'Slotinstallatie',
            'service.install.text': 'Installatie van veiligheidssloten, Europese cilinders, meerpuntssloten en grendels.',
            'service.install.tag1': 'Hoge veiligheid',
            'service.install.tag2': 'Meerpunts',
            'service.install.tag3': 'Alle merken',

            'service.repair.title': 'Slotreparatie',
            'service.repair.text': 'Diagnose en reparatie van defecte sloten. Vervanging van cilinders en mechanismen.',
            'service.repair.tag1': 'Diagnose',
            'service.repair.tag2': 'Cilinders',
            'service.repair.tag3': 'Mechanismen',

            'service.keys.title': 'Sleutelduplicatie',
            'service.keys.text': 'Sleutelkopie in 1 minuut. Platte sleutels, baardsleutels, veiligheidssleutels en autosleutels.',
            'service.keys.tag1': 'Express',
            'service.keys.tag2': 'Alle sleutels',
            'service.keys.tag3': 'Ter plaatse',

            'service.auto.title': 'Auto-slotenmakerij',
            'service.auto.text': 'Voertuigopening, autosleutelduplicatie, afstandsbedieningprogrammering.',
            'service.auto.tag1': 'Auto-opening',
            'service.auto.tag2': 'Autosleutels',
            'service.auto.tag3': 'Afstandsbedieningen',

            'service.safe.title': 'Kluizen',
            'service.safe.text': 'Verkoop, installatie en opening van kluizen. Merk Burg Wächter.',
            'service.safe.tag1': 'Burg Wächter',
            'service.safe.tag2': 'Installatie',
            'service.safe.tag3': 'Opening',

            // Pourquoi Section
            'pourquoi.tag': 'Waarom Janssens?',
            'pourquoi.title': 'Vertrouwen bouw je op',
            'pourquoi.intro': 'Al meer dan 10 jaar werken wij voor particulieren, bedrijven en instellingen in Brussel en Brabant. Onze reputatie is gebaseerd op drie engagementen.',

            'pillar.speed.title': 'Snelheid',
            'pillar.speed.text': 'Gegarandeerde interventie binnen 30 minuten, 24/7, inclusief feestdagen.',
            'pillar.expertise.title': 'Expertise',
            'pillar.expertise.text': 'Gecertificeerde technici, professionele uitrusting, zorgvuldig werk zonder schade.',
            'pillar.transparency.title': 'Transparantie',
            'pillar.transparency.text': 'Prijs meegedeeld voor interventie. Geen verrassingen. Betaling alleen na service.',

            'trust.available.title': '24/7 beschikbaar',
            'trust.available.text': 'Feestdagen en weekends inbegrepen',
            'trust.registered.title': 'Geregistreerd bedrijf',
            'trust.registered.text': 'BTW BE0712.625.742 · LAMRO GROUP',
            'trust.certified.title': 'Gecertificeerde technici',
            'trust.certified.text': 'Continue opleiding op alle merken',

            // Confiance Section
            'confiance.tag': 'Onze dekking',
            'confiance.title': 'Altijd dichtbij',
            'live.title': 'Live interventies',
            'live.today': 'Vandaag:',
            'badge.registered': 'Geregistreerd bedrijf',

            // Intervention statuses
            'status.enroute': 'Onderweg',
            'status.ongoing': 'Bezig',
            'status.completed': 'Voltooid',

            // Zones Section
            'zones.tag': 'Interventiezones',
            'zones.title': 'Bent u in onze zone?',
            'zones.desc': 'Controleer in 1 seconde of wij bij u komen',
            'zones.placeholder': 'Voer uw gemeente in...',
            'zones.initial': 'Typ de naam van uw gemeente om te controleren',
            'zones.success.title': 'Goed nieuws!',
            'zones.success.text': 'Wij komen naar',
            'zones.success.delay': 'Interventie in <strong>~30 min</strong>',
            'zones.success.available': 'Beschikbaar <strong>24/7</strong>',
            'zones.success.cta': 'Nu bellen',
            'zones.notfound.title': 'Zone niet vermeld',
            'zones.notfound.text': 'Neem contact met ons op, misschien kunnen we toch komen.',
            'zones.notfound.cta': 'Contact opnemen',
            'zones.regions.title': 'Onze 96 gedekte gemeenten:',
            'zones.region.brussels': 'Brussels Hoofdstedelijk',
            'zones.region.brabant.wallon': 'Waals-Brabant',
            'zones.region.brabant.flamand': 'Vlaams-Brabant',

            // FAQ Section
            'faq.tag': 'FAQ',
            'faq.title': 'Veelgestelde vragen',

            'faq.q1': 'Wat is het verschil tussen een standaard en een veiligheidsslot?',
            'faq.a1': 'Het veiligheidsslot biedt betere bescherming tegen inbraak dankzij versterkte mechanismen, anti-picking en anti-boor cilinders. Het wordt aanbevolen voor voordeuren.',

            'faq.q2': 'Wat zijn uw interventie-uren?',
            'faq.a2': 'Wij zijn 24/7 beschikbaar, inclusief feestdagen. Een noodgeval wacht niet, en wij ook niet.',

            'faq.q3': 'Hoe weet ik of mijn slot moet worden vervangen?',
            'faq.a3': 'Als uw slot moeilijk te openen is, piept, tekenen van slijtage vertoont of uw deur niet meer goed beveiligt, is het tijd om het te vervangen. Wij kunnen een gratis diagnose stellen.',

            'faq.q4': 'Werkt u met alle slotmerken?',
            'faq.a4': 'Ja, onze technici zijn opgeleid om te werken met alle merken en soorten sloten op de markt: Vachette, Bricard, Fichet, Yale, Abus, en vele andere.',

            'faq.q5': 'Kunt u gepantserde deuren openen?',
            'faq.a5': 'Ja, wij hebben de expertise en uitrusting om sloten op gepantserde deuren te openen, repareren en installeren, zonder ze te beschadigen.',

            'faq.q6': 'Hoeveel kost een nachtslotenmaker in Brussel?',
            'faq.a6': 'Onze tarieven zijn transparant en worden voor interventie meegedeeld, ook \'s nachts. Geen verborgen kosten. Bel 0495 205 400 voor een gratis offerte.',

            'faq.q7': 'Hoe open ik een dichtgevallen deur zonder sleutel?',
            'faq.a7': 'Probeer niet zelf te openen, u riskeert het slot te beschadigen. Bel een professionele slotenmaker zoals Janssens Serrurier die niet-destructieve technieken gebruikt om uw deur in enkele minuten te openen.',

            'faq.q8': 'Welke slotenmaker bellen voor noodgevallen in Ukkel, Elsene of Waterloo?',
            'faq.a8': 'Janssens Serrurier komt binnen 30 minuten naar Ukkel, Elsene, Waterloo en alle gemeenten van Brussel en Brabant. Bel 0495 205 400, 24/7 beschikbaar.',

            'faq.q9': 'Slotvervanging na inbraak: wat te doen?',
            'faq.a9': 'Bel na een inbraak eerst de politie en neem dan contact op met Janssens Serrurier op 0495 205 400. Wij komen in noodgeval om uw woning te beveiligen met een gecertificeerd veiligheidsslot.',

            // Contact Section
            'contact.tag': 'Contact',
            'contact.title': 'Slotenmaker nodig?',
            'contact.text': 'Bel ons direct of stuur een bericht. Wij antwoorden binnen enkele minuten.',
            'contact.phone': 'Telefoon',
            'contact.whatsapp': 'WhatsApp',
            'contact.whatsapp.text': 'Snel antwoord',
            'contact.email': 'E-mail',
            'contact.address': 'Adres',

            // Footer
            'footer.desc': 'Uw slotenmaker-expert in Brussel sinds meer dan 10 jaar. 24/7 beschikbaar voor al uw noodgevallen.',
            'footer.services': 'Diensten',
            'footer.services.door': 'Deuropening',
            'footer.services.install': 'Slotinstallatie',
            'footer.services.keys': 'Sleutelduplicatie',
            'footer.services.auto': 'Auto-slotenmakerij',
            'footer.services.safe': 'Kluizen',
            'footer.company': 'Bedrijf',
            'footer.company.about': 'Over ons',
            'footer.company.partners': 'Partners',
            'footer.company.zones': 'Interventie',
            'footer.company.faq': 'FAQ',
            'footer.company.contact': 'Contact',
            'footer.contact': 'Contact',
            'footer.terms': 'Gebruiksvoorwaarden',
            'footer.privacy': 'Privacybeleid',
            'footer.credit': 'Ontworpen door',

            // Floating CTA
            'floating.call': 'Bellen',

            // Language selector
            'lang.select': 'Taal',

            // Dynamic interventions
            'intervention.door': 'Deuropening',
            'intervention.slam': 'Dichtgevallen deur',
            'intervention.replace': 'Slotvervanging',
            'intervention.cylinder': 'Cilinderinstallatie',
            'intervention.multipoint': 'Meerpuntsslot',
            'intervention.keys': 'Sleutelduplicatie',
            'intervention.car': 'Voertuigopening',
            'intervention.ago': 'Geleden',
            'intervention.now': 'Zojuist',
            'intervention.min': 'min',
            'intervention.hour': 'u',

            // Legal pages - Common
            'legal.back': 'Terug naar home',
            'legal.updated': 'Laatst bijgewerkt: December 2024',

            // Conditions page
            'conditions.title': 'Gebruiksvoorwaarden',
            'conditions.1.title': '1. Voorstelling',
            'conditions.1.text1': 'Deze algemene gebruiksvoorwaarden regelen de toegang tot en het gebruik van de website <strong>janssensserrurier.be</strong>, beheerd door <strong>LAMRO GROUP</strong>, een in België geregistreerd bedrijf met BTW-nummer BE0712.625.742, gevestigd aan de Leuvensesteenweg 629, 1030 Brussel.',
            'conditions.1.text2': 'Door toegang tot deze site accepteert u zonder voorbehoud deze gebruiksvoorwaarden.',
            'conditions.2.title': '2. Aangeboden diensten',
            'conditions.2.text': 'Janssens Serrurier biedt professionele slotenmakersdiensten aan, waaronder:',
            'conditions.2.li1': 'Opening van dichtgevallen of geblokkeerde deuren',
            'conditions.2.li2': 'Installatie en vervanging van sloten',
            'conditions.2.li3': 'Sleutelduplicatie',
            'conditions.2.li4': 'Auto-slotenmakerij',
            'conditions.2.li5': 'Installatie van kluizen',
            'conditions.2.li6': 'Noodhulp 24/7',
            'conditions.3.title': '3. Prijzen en betaling',
            'conditions.3.text1': 'De tarieven van onze interventies worden vóór elke dienst meegedeeld. Een gratis en vrijblijvende offerte wordt systematisch voorgesteld.',
            'conditions.3.text2': 'De betaling gebeurt aan het einde van de interventie via: contant, bankkaart (Bancontact), of overschrijving.',
            'conditions.3.text3': 'Er wordt geen voorschot gevraagd vóór de interventie.',
            'conditions.4.title': '4. Interventiegebied',
            'conditions.4.text': 'Onze diensten dekken het volledige Brussels Hoofdstedelijk Gewest (19 gemeenten), Waals-Brabant en Vlaams-Brabant, in totaal 96 gemeenten.',
            'conditions.5.title': '5. Garanties',
            'conditions.5.text1': 'Al onze interventies zijn gegarandeerd. De geïnstalleerde onderdelen (sloten, cilinders) vallen onder de fabrieksgarantie.',
            'conditions.5.text2': 'Bij een probleem na een interventie, neem zo snel mogelijk contact met ons op voor een snelle afhandeling.',
            'conditions.6.title': '6. Aansprakelijkheid',
            'conditions.6.text1': 'Janssens Serrurier verbindt zich ertoe professionele kwaliteitsdiensten te leveren. Onze aansprakelijkheid is beperkt tot het bedrag van de dienst in geval van bewezen directe schade.',
            'conditions.6.text2': 'Wij kunnen niet aansprakelijk worden gesteld voor indirecte schade of overmacht.',
            'conditions.7.title': '7. Intellectueel eigendom',
            'conditions.7.text': 'Alle inhoud van de site (teksten, afbeeldingen, logo, design) is het exclusieve eigendom van LAMRO GROUP of haar partners. Reproductie zonder voorafgaande toestemming is verboden.',
            'conditions.8.title': '8. Wijziging van de voorwaarden',
            'conditions.8.text': 'Wij behouden ons het recht voor deze voorwaarden op elk moment te wijzigen. Wijzigingen worden van kracht zodra ze op de site worden gepubliceerd.',
            'conditions.9.title': '9. Toepasselijk recht en jurisdictie',
            'conditions.9.text': 'Deze voorwaarden worden beheerst door het Belgisch recht. In geval van geschil zijn de rechtbanken van Brussel exclusief bevoegd.',
            'conditions.10.title': '10. Contact',
            'conditions.10.text': 'Voor vragen over deze gebruiksvoorwaarden:',

            // Privacy page
            'privacy.title': 'Privacybeleid',
            'privacy.1.title': '1. Inleiding',
            'privacy.1.text1': '<strong>LAMRO GROUP</strong> (hierna "wij", "ons" of "Janssens Serrurier"), als verantwoordelijke voor de verwerking, verbindt zich ertoe de privacy van de gebruikers van haar website janssensserrurier.be te beschermen.',
            'privacy.1.text2': 'Dit privacybeleid legt uit hoe wij uw persoonlijke gegevens verzamelen, gebruiken en beschermen, in overeenstemming met de Algemene Verordening Gegevensbescherming (AVG).',
            'privacy.1.box': '<strong>Verwerkingsverantwoordelijke:</strong><br>LAMRO GROUP - BTW BE0712.625.742<br>Leuvensesteenweg 629, 1030 Brussel<br>Email: info@janssensserrurier.be',
            'privacy.2.title': '2. Verzamelde gegevens',
            'privacy.2.text': 'In het kader van onze activiteiten kunnen wij de volgende gegevens verzamelen:',
            'privacy.2.li1': '<strong>Identificatiegegevens:</strong> naam, voornaam, adres',
            'privacy.2.li2': '<strong>Contactgegevens:</strong> telefoonnummer, e-mailadres',
            'privacy.2.li3': '<strong>Locatiegegevens:</strong> interventie-adres',
            'privacy.2.li4': '<strong>Technische gegevens:</strong> IP-adres, browsertype, bezochte pagina\'s (via cookies)',
            'privacy.3.title': '3. Verwerkingsdoeleinden',
            'privacy.3.text': 'Uw persoonsgegevens worden verwerkt voor de volgende doeleinden:',
            'privacy.3.li1': 'Beantwoorden van uw offerte- en interventieaanvragen',
            'privacy.3.li2': 'Leveren van onze slotenmakersdiensten',
            'privacy.3.li3': 'Opstellen en verzenden van facturen',
            'privacy.3.li4': 'Opvolging en garantie van interventies',
            'privacy.3.li5': 'Verbeteren van de kwaliteit van onze diensten en website',
            'privacy.3.li6': 'Nakomen van onze wettelijke en fiscale verplichtingen',
            'privacy.4.title': '4. Rechtsgrond voor de verwerking',
            'privacy.4.text': 'Wij verwerken uw gegevens op basis van de volgende rechtsgronden:',
            'privacy.4.li1': '<strong>Uitvoering van een contract:</strong> om de gevraagde diensten te leveren',
            'privacy.4.li2': '<strong>Wettelijke verplichting:</strong> om onze fiscale verplichtingen na te komen',
            'privacy.4.li3': '<strong>Gerechtvaardigd belang:</strong> om onze diensten te verbeteren',
            'privacy.4.li4': '<strong>Toestemming:</strong> voor het verzenden van marketingcommunicatie (indien van toepassing)',
            'privacy.5.title': '5. Bewaartermijn',
            'privacy.5.text': 'Uw persoonsgegevens worden bewaard:',
            'privacy.5.li1': '<strong>Klantgegevens:</strong> gedurende de commerciële relatie, daarna 10 jaar voor boekhoudkundige verplichtingen',
            'privacy.5.li2': '<strong>Prospectgegevens:</strong> 3 jaar vanaf het laatste contact',
            'privacy.5.li3': '<strong>Cookies:</strong> maximaal 13 maanden',
            'privacy.6.title': '6. Delen van gegevens',
            'privacy.6.text': 'Uw gegevens kunnen worden gedeeld met:',
            'privacy.6.li1': 'Onze technici voor interventies ter plaatse',
            'privacy.6.li2': 'Onze boekhouder voor facturatie',
            'privacy.6.li3': 'De bevoegde autoriteiten indien wettelijk vereist',
            'privacy.6.text2': 'Wij verkopen uw gegevens nooit aan derden. Wij dragen uw gegevens niet over buiten de Europese Economische Ruimte.',
            'privacy.7.title': '7. Cookies',
            'privacy.7.text': 'Onze website gebruikt cookies voor:',
            'privacy.7.li1': '<strong>Essentiële cookies:</strong> noodzakelijk voor de werking van de site',
            'privacy.7.li2': '<strong>Analytische cookies:</strong> om het gebruik van de site te begrijpen (geanonimiseerd)',
            'privacy.7.text2': 'U kunt uw cookievoorkeuren beheren via de instellingen van uw browser.',
            'privacy.8.title': '8. Uw rechten',
            'privacy.8.text': 'Overeenkomstig de AVG heeft u de volgende rechten:',
            'privacy.8.li1': '<strong>Recht op toegang:</strong> een kopie van uw gegevens verkrijgen',
            'privacy.8.li2': '<strong>Recht op rectificatie:</strong> uw onjuiste gegevens corrigeren',
            'privacy.8.li3': '<strong>Recht op wissing:</strong> verzoeken om verwijdering van uw gegevens',
            'privacy.8.li4': '<strong>Recht op overdraagbaarheid:</strong> uw gegevens ontvangen in een gestructureerd formaat',
            'privacy.8.li5': '<strong>Recht van bezwaar:</strong> bezwaar maken tegen de verwerking van uw gegevens',
            'privacy.8.li6': '<strong>Recht op beperking:</strong> de verwerking van uw gegevens beperken',
            'privacy.8.text2': 'Om deze rechten uit te oefenen, contacteer ons via info@janssensserrurier.be.',
            'privacy.9.title': '9. Gegevensbeveiliging',
            'privacy.9.text': 'Wij implementeren passende technische en organisatorische maatregelen om uw gegevens te beschermen tegen ongeoorloofde toegang, verlies of vernietiging:',
            'privacy.9.li1': 'Beveiligde HTTPS-verbinding',
            'privacy.9.li2': 'Beperkte toegang tot gegevens op basis van "need-to-know"',
            'privacy.9.li3': 'Regelmatige beveiligingsupdates',
            'privacy.10.title': '10. Klacht',
            'privacy.10.text': 'Als u van mening bent dat uw rechten niet worden gerespecteerd, kunt u een klacht indienen bij de Gegevensbeschermingsautoriteit (GBA):',
            'privacy.11.title': '11. Wijzigingen',
            'privacy.11.text': 'Dit privacybeleid kan worden bijgewerkt. Wij zullen u informeren over belangrijke wijzigingen via onze website.',
            'privacy.12.title': '12. Contact',
            'privacy.12.text': 'Voor vragen over dit beleid of uw persoonsgegevens:'
        },

        // =====================================================
        // ENGLISH
        // =====================================================
        en: {
            // Navigation
            'nav.services': 'Services',
            'nav.pourquoi': 'Why us',
            'nav.confiance': 'Commitments',
            'nav.zones': 'Coverage',
            'nav.contact': 'Contact',
            'nav.call': 'Call',
            'nav.whatsapp': 'WhatsApp',

            // Hero
            'hero.title.1': 'Your locksmith',
            'hero.title.2': 'Brussels, Walloon & Flemish Brabant',
            'hero.text': 'Locked out? Lost key? We arrive in <strong>30 minutes</strong>, without damaging your door. Over <strong>10 years</strong> of experience, registered company, price quoted before intervention.',
            'hero.cta.call': 'Call now',
            'hero.cta.whatsapp': 'WhatsApp',
            'hero.trust.1': 'No damage',
            'hero.trust.2': 'Fixed price',
            'hero.trust.3': 'Pay after service',

            // Stats
            'stat.delay': 'Average time',
            'stat.experience': 'Years experience',
            'stat.communes': 'Areas covered',

            // Urgence Banner
            'urgence.title': 'Locked out? Key lost or broken?',
            'urgence.text': 'A qualified locksmith arrives at your place in less than 30 minutes.',
            'urgence.btn': 'Emergency call',

            // Services Section
            'services.tag': 'Our services',
            'services.title': 'Professional locksmith solutions',
            'services.desc': 'Fast and careful interventions for all your security needs',

            // Service Cards
            'service.door.title': 'Door opening',
            'service.door.text': 'Locked out or door stuck? Quick intervention without damaging your lock or door.',
            'service.door.tag1': 'Emergency 24/7',
            'service.door.tag2': 'No damage',
            'service.door.tag3': 'All doors',

            'service.install.title': 'Lock installation',
            'service.install.text': 'Installation of high-security locks, European cylinders, multipoint locks and deadbolts.',
            'service.install.tag1': 'High security',
            'service.install.tag2': 'Multipoint',
            'service.install.tag3': 'All brands',

            'service.repair.title': 'Lock repair',
            'service.repair.text': 'Diagnosis and repair of faulty locks. Replacement of cylinders and mechanisms.',
            'service.repair.tag1': 'Diagnosis',
            'service.repair.tag2': 'Cylinders',
            'service.repair.tag3': 'Mechanisms',

            'service.keys.title': 'Key duplication',
            'service.keys.text': 'Key copy in 1 minute. Flat keys, bit keys, security keys and car keys.',
            'service.keys.tag1': 'Express',
            'service.keys.tag2': 'All keys',
            'service.keys.tag3': 'On site',

            'service.auto.title': 'Automotive locksmith',
            'service.auto.text': 'Vehicle opening, car key duplication, remote programming.',
            'service.auto.tag1': 'Car opening',
            'service.auto.tag2': 'Car keys',
            'service.auto.tag3': 'Remotes',

            'service.safe.title': 'Safes',
            'service.safe.text': 'Sale, installation and opening of safes. Burg Wächter brand.',
            'service.safe.tag1': 'Burg Wächter',
            'service.safe.tag2': 'Installation',
            'service.safe.tag3': 'Opening',

            // Pourquoi Section
            'pourquoi.tag': 'Why Janssens?',
            'pourquoi.title': 'Trust is built',
            'pourquoi.intro': 'For over 10 years, we have been serving individuals, businesses and institutions in Brussels and Brabant. Our reputation is based on three commitments.',

            'pillar.speed.title': 'Speed',
            'pillar.speed.text': 'Guaranteed intervention in less than 30 minutes, 24/7, including holidays.',
            'pillar.expertise.title': 'Expertise',
            'pillar.expertise.text': 'Certified technicians, professional equipment, careful work without damage.',
            'pillar.transparency.title': 'Transparency',
            'pillar.transparency.text': 'Price quoted before intervention. No surprises. Payment only after service.',

            'trust.available.title': 'Available 24/7',
            'trust.available.text': 'Holidays and weekends included',
            'trust.registered.title': 'Registered company',
            'trust.registered.text': 'VAT BE0712.625.742 · LAMRO GROUP',
            'trust.certified.title': 'Certified technicians',
            'trust.certified.text': 'Continuous training on all brands',

            // Confiance Section
            'confiance.tag': 'Our coverage',
            'confiance.title': 'Always close to you',
            'live.title': 'Live interventions',
            'live.today': 'Today:',
            'badge.registered': 'Registered company',

            // Intervention statuses
            'status.enroute': 'En route',
            'status.ongoing': 'In progress',
            'status.completed': 'Completed',

            // Zones Section
            'zones.tag': 'Service areas',
            'zones.title': 'Are you in our zone?',
            'zones.desc': 'Check in 1 second if we serve your area',
            'zones.placeholder': 'Enter your municipality...',
            'zones.initial': 'Type your municipality name to check',
            'zones.success.title': 'Good news!',
            'zones.success.text': 'We serve',
            'zones.success.delay': 'Intervention in <strong>~30 min</strong>',
            'zones.success.available': 'Available <strong>24/7</strong>',
            'zones.success.cta': 'Call now',
            'zones.notfound.title': 'Area not listed',
            'zones.notfound.text': 'Contact us, we may still be able to help.',
            'zones.notfound.cta': 'Contact us',
            'zones.regions.title': 'Our 96 covered municipalities:',
            'zones.region.brussels': 'Brussels-Capital',
            'zones.region.brabant.wallon': 'Walloon Brabant',
            'zones.region.brabant.flamand': 'Flemish Brabant',

            // FAQ Section
            'faq.tag': 'FAQ',
            'faq.title': 'Frequently asked questions',

            'faq.q1': 'What is the difference between a standard and high-security lock?',
            'faq.a1': 'The high-security lock offers better protection against break-ins thanks to reinforced mechanisms, anti-pick and anti-drill cylinders. It is recommended for front doors.',

            'faq.q2': 'What are your intervention hours?',
            'faq.a2': 'We are available 24/7, including holidays. An emergency doesn\'t wait, and neither do we.',

            'faq.q3': 'How do I know if my lock needs to be replaced?',
            'faq.a3': 'If your lock is difficult to open, squeaks, shows signs of wear or no longer properly secures your door, it\'s time to replace it. We can perform a free diagnosis.',

            'faq.q4': 'Do you work with all lock brands?',
            'faq.a4': 'Yes, our technicians are trained to work with all brands and types of locks on the market: Vachette, Bricard, Fichet, Yale, Abus, and many others.',

            'faq.q5': 'Can you open armored doors?',
            'faq.a5': 'Yes, we have the expertise and equipment to open, repair and install locks on armored doors without damaging them.',

            'faq.q6': 'How much does a night locksmith cost in Brussels?',
            'faq.a6': 'Our rates are transparent and communicated before intervention, even at night. No hidden fees. Call 0495 205 400 for a free quote.',

            'faq.q7': 'How to open a locked door without a key?',
            'faq.a7': 'Don\'t try to open it yourself, you risk damaging the lock. Call a professional locksmith like Janssens Serrurier who uses non-destructive techniques to open your door in minutes.',

            'faq.q8': 'Which locksmith to call for emergencies in Uccle, Ixelles or Waterloo?',
            'faq.a8': 'Janssens Serrurier comes to Uccle, Ixelles, Waterloo and all municipalities of Brussels and Brabant in less than 30 minutes. Call 0495 205 400, available 24/7.',

            'faq.q9': 'Lock change after burglary: what to do?',
            'faq.a9': 'After a burglary, first call the police then contact Janssens Serrurier at 0495 205 400. We intervene urgently to secure your home with a certified high-security lock.',

            // Contact Section
            'contact.tag': 'Contact',
            'contact.title': 'Need a locksmith?',
            'contact.text': 'Call us directly or send us a message. We respond within minutes.',
            'contact.phone': 'Phone',
            'contact.whatsapp': 'WhatsApp',
            'contact.whatsapp.text': 'Quick response',
            'contact.email': 'Email',
            'contact.address': 'Address',

            // Footer
            'footer.desc': 'Your locksmith expert in Brussels for over 10 years. Available 24/7 for all your emergencies.',
            'footer.services': 'Services',
            'footer.services.door': 'Door opening',
            'footer.services.install': 'Lock installation',
            'footer.services.keys': 'Key duplication',
            'footer.services.auto': 'Auto locksmith',
            'footer.services.safe': 'Safes',
            'footer.company': 'Company',
            'footer.company.about': 'About',
            'footer.company.partners': 'Partners',
            'footer.company.zones': 'Coverage',
            'footer.company.faq': 'FAQ',
            'footer.company.contact': 'Contact',
            'footer.contact': 'Contact',
            'footer.terms': 'Terms of use',
            'footer.privacy': 'Privacy policy',
            'footer.credit': 'Designed by',

            // Floating CTA
            'floating.call': 'Call',

            // Language selector
            'lang.select': 'Language',

            // Dynamic interventions
            'intervention.door': 'Door opening',
            'intervention.slam': 'Locked out',
            'intervention.replace': 'Lock replacement',
            'intervention.cylinder': 'Cylinder installation',
            'intervention.multipoint': 'Multipoint lock',
            'intervention.keys': 'Key duplication',
            'intervention.car': 'Vehicle opening',
            'intervention.ago': 'ago',
            'intervention.now': 'Just now',
            'intervention.min': 'min',
            'intervention.hour': 'h',

            // Legal pages - Common
            'legal.back': 'Back to home',
            'legal.updated': 'Last updated: December 2024',

            // Conditions page
            'conditions.title': 'Terms of Use',
            'conditions.1.title': '1. Introduction',
            'conditions.1.text1': 'These general terms of use govern access to and use of the website <strong>janssensserrurier.be</strong>, operated by <strong>LAMRO GROUP</strong>, a company registered in Belgium under VAT number BE0712.625.742, with registered office at Chaussée de Louvain 629, 1030 Brussels.',
            'conditions.1.text2': 'By accessing this site, you unconditionally accept these terms of use.',
            'conditions.2.title': '2. Services offered',
            'conditions.2.text': 'Janssens Serrurier offers professional locksmith services, including:',
            'conditions.2.li1': 'Opening of locked or blocked doors',
            'conditions.2.li2': 'Installation and replacement of locks',
            'conditions.2.li3': 'Key duplication',
            'conditions.2.li4': 'Automotive locksmith services',
            'conditions.2.li5': 'Safe installation',
            'conditions.2.li6': '24/7 emergency service',
            'conditions.3.title': '3. Pricing and payment',
            'conditions.3.text1': 'The rates for our services are communicated before any work begins. A free, no-obligation quote is systematically offered.',
            'conditions.3.text2': 'Payment is made at the end of the intervention by the following means: cash, bank card (Bancontact), or bank transfer.',
            'conditions.3.text3': 'No deposit is required before the intervention.',
            'conditions.4.title': '4. Service area',
            'conditions.4.text': 'Our services cover the entire Brussels-Capital Region (19 municipalities), Walloon Brabant and Flemish Brabant, totaling 96 municipalities.',
            'conditions.5.title': '5. Guarantees',
            'conditions.5.text1': 'All our interventions are guaranteed. Installed parts (locks, cylinders) are covered by the manufacturer\'s warranty.',
            'conditions.5.text2': 'In case of a problem following an intervention, contact us as soon as possible for quick resolution.',
            'conditions.6.title': '6. Liability',
            'conditions.6.text1': 'Janssens Serrurier is committed to providing professional quality services. Our liability is limited to the amount of the service in case of proven direct damage.',
            'conditions.6.text2': 'We cannot be held responsible for indirect damages or force majeure circumstances.',
            'conditions.7.title': '7. Intellectual property',
            'conditions.7.text': 'All content on the site (texts, images, logo, design) is the exclusive property of LAMRO GROUP or its partners. Reproduction without prior authorization is prohibited.',
            'conditions.8.title': '8. Modification of terms',
            'conditions.8.text': 'We reserve the right to modify these terms at any time. Changes take effect as soon as they are published on the site.',
            'conditions.9.title': '9. Applicable law and jurisdiction',
            'conditions.9.text': 'These terms are governed by Belgian law. In case of dispute, the courts of Brussels shall have exclusive jurisdiction.',
            'conditions.10.title': '10. Contact',
            'conditions.10.text': 'For any questions regarding these terms of use:',

            // Privacy page
            'privacy.title': 'Privacy Policy',
            'privacy.1.title': '1. Introduction',
            'privacy.1.text1': '<strong>LAMRO GROUP</strong> (hereinafter "we", "our" or "Janssens Serrurier"), as data controller, is committed to protecting the privacy of users of its website janssensserrurier.be.',
            'privacy.1.text2': 'This privacy policy explains how we collect, use and protect your personal data, in accordance with the General Data Protection Regulation (GDPR).',
            'privacy.1.box': '<strong>Data Controller:</strong><br>LAMRO GROUP - VAT BE0712.625.742<br>Chaussée de Louvain 629, 1030 Brussels<br>Email: info@janssensserrurier.be',
            'privacy.2.title': '2. Data collected',
            'privacy.2.text': 'As part of our activities, we may collect the following data:',
            'privacy.2.li1': '<strong>Identification data:</strong> name, first name, address',
            'privacy.2.li2': '<strong>Contact data:</strong> phone number, email address',
            'privacy.2.li3': '<strong>Location data:</strong> intervention address',
            'privacy.2.li4': '<strong>Technical data:</strong> IP address, browser type, pages visited (via cookies)',
            'privacy.3.title': '3. Processing purposes',
            'privacy.3.text': 'Your personal data is processed for the following purposes:',
            'privacy.3.li1': 'Responding to your quote and intervention requests',
            'privacy.3.li2': 'Providing our locksmith services',
            'privacy.3.li3': 'Preparing and sending invoices',
            'privacy.3.li4': 'Follow-up and warranty of interventions',
            'privacy.3.li5': 'Improving the quality of our services and website',
            'privacy.3.li6': 'Complying with our legal and tax obligations',
            'privacy.4.title': '4. Legal basis for processing',
            'privacy.4.text': 'We process your data on the following legal bases:',
            'privacy.4.li1': '<strong>Contract execution:</strong> to provide requested services',
            'privacy.4.li2': '<strong>Legal obligation:</strong> to comply with our tax obligations',
            'privacy.4.li3': '<strong>Legitimate interest:</strong> to improve our services',
            'privacy.4.li4': '<strong>Consent:</strong> for sending marketing communications (where applicable)',
            'privacy.5.title': '5. Retention period',
            'privacy.5.text': 'Your personal data is retained:',
            'privacy.5.li1': '<strong>Customer data:</strong> during the commercial relationship, then 10 years for accounting obligations',
            'privacy.5.li2': '<strong>Prospect data:</strong> 3 years from last contact',
            'privacy.5.li3': '<strong>Cookies:</strong> maximum 13 months',
            'privacy.6.title': '6. Data sharing',
            'privacy.6.text': 'Your data may be shared with:',
            'privacy.6.li1': 'Our technicians for on-site interventions',
            'privacy.6.li2': 'Our accountant for billing',
            'privacy.6.li3': 'Competent authorities if required by law',
            'privacy.6.text2': 'We never sell your data to third parties. We do not transfer your data outside the European Economic Area.',
            'privacy.7.title': '7. Cookies',
            'privacy.7.text': 'Our website uses cookies for:',
            'privacy.7.li1': '<strong>Essential cookies:</strong> necessary for site functionality',
            'privacy.7.li2': '<strong>Analytical cookies:</strong> to understand site usage (anonymized)',
            'privacy.7.text2': 'You can manage your cookie preferences through your browser settings.',
            'privacy.8.title': '8. Your rights',
            'privacy.8.text': 'Under GDPR, you have the following rights:',
            'privacy.8.li1': '<strong>Right of access:</strong> obtain a copy of your data',
            'privacy.8.li2': '<strong>Right to rectification:</strong> correct your inaccurate data',
            'privacy.8.li3': '<strong>Right to erasure:</strong> request deletion of your data',
            'privacy.8.li4': '<strong>Right to portability:</strong> receive your data in a structured format',
            'privacy.8.li5': '<strong>Right to object:</strong> object to the processing of your data',
            'privacy.8.li6': '<strong>Right to restriction:</strong> restrict the processing of your data',
            'privacy.8.text2': 'To exercise these rights, contact us at info@janssensserrurier.be.',
            'privacy.9.title': '9. Data security',
            'privacy.9.text': 'We implement appropriate technical and organizational measures to protect your data against unauthorized access, loss or destruction:',
            'privacy.9.li1': 'Secure HTTPS connection',
            'privacy.9.li2': 'Limited access to data on a "need-to-know" basis',
            'privacy.9.li3': 'Regular security updates',
            'privacy.10.title': '10. Complaint',
            'privacy.10.text': 'If you believe your rights are not being respected, you can file a complaint with the Data Protection Authority (DPA):',
            'privacy.11.title': '11. Modifications',
            'privacy.11.text': 'This privacy policy may be updated. We will inform you of any significant changes via our website.',
            'privacy.12.title': '12. Contact',
            'privacy.12.text': 'For any questions regarding this policy or your personal data:'
        }
    },

    // =====================================================
    // METHODS
    // =====================================================

    init() {
        // Check for saved language preference
        let savedLang = null;
        try {
            savedLang = localStorage.getItem('janssens-lang');
        } catch (e) {
            // localStorage not available (private browsing, etc.)
        }

        if (savedLang && this.translations[savedLang]) {
            this.currentLang = savedLang;
        } else {
            // Try to detect from browser
            const browserLang = navigator.language.split('-')[0];
            if (this.translations[browserLang]) {
                this.currentLang = browserLang;
            }
        }

        // Update HTML lang attribute
        document.documentElement.lang = this.currentLang === 'fr' ? 'fr-BE' :
                                        this.currentLang === 'nl' ? 'nl-BE' : 'en';

        // Apply translations
        this.applyTranslations();

        // Setup language switcher
        this.setupSwitcher();
    },

    t(key) {
        // Use i18n directly to avoid 'this' binding issues when called from other scripts
        const lang = i18n.currentLang || 'fr';
        const translations = i18n.translations[lang] || i18n.translations['fr'];
        return (translations && translations[key]) || (i18n.translations['fr'] && i18n.translations['fr'][key]) || key;
    },

    setLang(lang) {
        if (!this.translations[lang]) return;

        this.currentLang = lang;
        try {
            localStorage.setItem('janssens-lang', lang);
        } catch (e) {
            // localStorage not available
        }

        // Update HTML lang attribute
        document.documentElement.lang = lang === 'fr' ? 'fr-BE' :
                                        lang === 'nl' ? 'nl-BE' : 'en';

        // Apply translations
        this.applyTranslations();

        // Re-render dynamic content (interventions feed)
        if (typeof window.rerenderInterventions === 'function') {
            window.rerenderInterventions();
        }

        // Update switcher UI
        this.updateSwitcherUI();
    },

    applyTranslations() {
        // Translate all elements with data-i18n attribute
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            const translation = this.t(key);

            // Check if element has HTML content
            if (translation.includes('<')) {
                el.innerHTML = translation;
            } else {
                el.textContent = translation;
            }
        });

        // Translate placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            el.placeholder = this.t(key);
        });

        // Translate aria-labels
        document.querySelectorAll('[data-i18n-aria]').forEach(el => {
            const key = el.getAttribute('data-i18n-aria');
            el.setAttribute('aria-label', this.t(key));
        });
    },

    setupSwitcher() {
        const switchers = document.querySelectorAll('.lang-switcher');

        switchers.forEach(switcher => {
            const buttons = switcher.querySelectorAll('[data-lang]');

            buttons.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    const lang = btn.getAttribute('data-lang');
                    this.setLang(lang);
                });
            });
        });

        this.updateSwitcherUI();
    },

    updateSwitcherUI() {
        document.querySelectorAll('.lang-switcher [data-lang]').forEach(btn => {
            const isActive = btn.getAttribute('data-lang') === this.currentLang;
            btn.classList.toggle('active', isActive);
        });
    }
};

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    i18n.init();
});

// Export for use in other scripts
window.i18n = i18n;
