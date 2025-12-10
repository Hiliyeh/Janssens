/* =====================================================
   JANSSENS SERRURIER - Application Script
   Compiled version without ES modules for browser compatibility
   ===================================================== */

(function() {
    'use strict';

    // =====================================================
    // UTILITY FUNCTIONS
    // =====================================================

    function setCurrentYear() {
        const yearEl = document.getElementById('currentYear');
        if (yearEl) {
            yearEl.textContent = new Date().getFullYear();
        }
    }

    // Phone tracking removed - implement with analytics if needed

    // =====================================================
    // ICONS
    // =====================================================

    function initIcons() {
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    }

    // =====================================================
    // MOBILE MENU
    // =====================================================

    function initMobileMenu() {
        const menuBtn = document.getElementById('menuBtn');
        const nav = document.getElementById('nav');
        const headerCta = document.querySelector('.header-cta');

        if (!menuBtn || !nav) return;

        menuBtn.addEventListener('click', () => {
            nav.classList.toggle('open');
            menuBtn.classList.toggle('active');

            if (headerCta) {
                headerCta.style.display = menuBtn.classList.contains('active') ? 'none' : '';
            }
        });

        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                nav.classList.remove('open');
                menuBtn.classList.remove('active');
                if (headerCta) {
                    headerCta.style.display = '';
                }
            });
        });
    }

    // =====================================================
    // HEADER SCROLL
    // =====================================================

    function initHeaderScroll() {
        const header = document.querySelector('.header');
        if (!header) return;

        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }, { passive: true });
    }

    // =====================================================
    // FLOATING CTA
    // =====================================================

    function initFloatingCta() {
        const floatingCta = document.getElementById('floatingCta');
        const hero = document.querySelector('.hero');

        if (!floatingCta || !hero) return;

        window.addEventListener('scroll', () => {
            const isMobile = window.innerWidth <= 768;
            const scrollY = window.pageYOffset;
            const heroBottom = hero.getBoundingClientRect().bottom;

            if (isMobile ? scrollY > 100 : heroBottom < 0) {
                floatingCta.classList.add('visible');
            } else {
                floatingCta.classList.remove('visible');
            }
        }, { passive: true });
    }

    // =====================================================
    // SMOOTH SCROLL
    // =====================================================

    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    }

    // =====================================================
    // FAQ ACCORDION
    // =====================================================

    function initFaqAccordion() {
        const faqItems = document.querySelectorAll('.faq-item');

        faqItems.forEach(item => {
            const summary = item.querySelector('summary');
            if (!summary) return;

            summary.addEventListener('click', (e) => {
                e.preventDefault();

                faqItems.forEach(other => {
                    if (other !== item && other.hasAttribute('open')) {
                        other.removeAttribute('open');
                    }
                });

                item.toggleAttribute('open');
            });
        });
    }

    // =====================================================
    // INTERVENTIONS FEED
    // =====================================================

    function initInterventionsFeed() {
        const interventionsList = document.getElementById('interventionsList');
        const interventionCountEl = document.getElementById('interventionCount');

        if (!interventionsList) return;

        // Show skeleton loader initially
        const showSkeletonLoader = () => {
            interventionsList.innerHTML = Array(4).fill('').map(() => `
                <div class="skeleton-intervention">
                    <div class="skeleton skeleton-icon"></div>
                    <div class="skeleton-intervention-content">
                        <div class="skeleton skeleton-text medium"></div>
                        <div class="skeleton skeleton-text short"></div>
                    </div>
                    <div class="skeleton-intervention-meta">
                        <div class="skeleton skeleton-text short"></div>
                        <div class="skeleton skeleton-badge"></div>
                    </div>
                </div>
            `).join('');
            interventionsList.classList.add('loading');
        };

        // Get translated text helper
        const t = (key) => {
            return window.i18n && window.i18n.t ? window.i18n.t(key) : key;
        };

        // Use centralized data from communes.js
        const interventionTypes = window.INTERVENTION_TYPES;
        const locations = window.LOCATIONS;
        const hourlyRate = window.HOURLY_RATES;

        // Day cycle starts at 3 AM instead of midnight
        // This prevents the counter from resetting to 0 at midnight
        const DAY_START_HOUR = 3;

        // Calculate the "logical date" seed - if before 3 AM, use yesterday's date
        const calculateDateSeed = () => {
            const now = new Date();
            const currentHour = now.getHours();
            const logicalDate = new Date(now);
            if (currentHour < DAY_START_HOUR) {
                logicalDate.setDate(logicalDate.getDate() - 1);
            }
            return logicalDate.getFullYear() * 10000 + (logicalDate.getMonth() + 1) * 100 + logicalDate.getDate();
        };

        let dateSeed = calculateDateSeed();

        const seededRandom = (seed) => {
            const x = Math.sin(seed) * 10000;
            return x - Math.floor(x);
        };

        const weightedRandom = (items, seed) => {
            const totalWeight = items.reduce((sum, item) => sum + item.weight, 0);
            let random = seededRandom(seed) * totalWeight;
            for (const item of items) {
                random -= item.weight;
                if (random <= 0) return item;
            }
            return items[0];
        };

        const generateDayInterventions = () => {
            const nowTime = new Date();
            const nowHour = nowTime.getHours();
            const nowMinute = nowTime.getMinutes();
            const interventions = [];
            let seed = dateSeed;

            // Determine the hours to generate interventions for
            // If before 3 AM: generate from 3h yesterday to current hour (crossing midnight)
            // If after 3 AM: generate from 3h to current hour
            let hoursToGenerate = [];

            if (nowHour < DAY_START_HOUR) {
                // Before 3 AM: include hours 3-23 from "yesterday" and 0 to nowHour from "today"
                for (let h = DAY_START_HOUR; h < 24; h++) {
                    hoursToGenerate.push({ hour: h, isYesterday: true });
                }
                for (let h = 0; h <= nowHour; h++) {
                    hoursToGenerate.push({ hour: h, isYesterday: false });
                }
            } else {
                // After 3 AM: just 3h to nowHour
                for (let h = DAY_START_HOUR; h <= nowHour; h++) {
                    hoursToGenerate.push({ hour: h, isYesterday: false });
                }
            }

            hoursToGenerate.forEach(({ hour, isYesterday }) => {
                const rate = hourlyRate[hour];
                // For the current hour, only generate up to current minute
                const isCurrentHour = !isYesterday && hour === nowHour;
                const maxMinute = isCurrentHour ? nowMinute : 60;

                const hasIntervention = seededRandom(seed++) < rate;
                const numInterventions = hasIntervention ? 1 : 0;

                for (let i = 0; i < numInterventions; i++) {
                    const minute = Math.floor(seededRandom(seed++) * maxMinute);

                    let intervention;
                    let attempts = 0;
                    do {
                        intervention = weightedRandom(interventionTypes, seed++);
                        attempts++;
                    } while (
                        interventions.length > 0 &&
                        intervention.i18nKey === interventions[interventions.length - 1].i18nKey &&
                        attempts < 5
                    );

                    let location;
                    attempts = 0;
                    do {
                        location = locations[Math.floor(seededRandom(seed++) * locations.length)];
                        attempts++;
                    } while (
                        interventions.length > 0 &&
                        location === interventions[interventions.length - 1].location &&
                        attempts < 5
                    );

                    // Calculate the correct date for the timestamp
                    const interventionDate = new Date(nowTime);
                    if (isYesterday) {
                        interventionDate.setDate(interventionDate.getDate() - 1);
                    }
                    interventionDate.setHours(hour, minute, 0, 0);

                    interventions.push({
                        hour,
                        minute,
                        i18nKey: intervention.i18nKey,
                        icon: intervention.icon,
                        iconClass: intervention.iconClass,
                        location,
                        timestamp: interventionDate
                    });
                }
            });

            interventions.sort((a, b) => b.timestamp - a.timestamp);
            return interventions;
        };

        const formatTimeDiff = (timestamp) => {
            const now = new Date();
            const diff = Math.floor((now - timestamp) / 1000 / 60);

            if (diff < 1) return t('intervention.now');
            if (diff < 60) return `${t('intervention.ago')} ${diff} ${t('intervention.min')}`;
            const hours = Math.floor(diff / 60);
            return `${t('intervention.ago')} ${hours}${t('intervention.hour')}`;
        };

        const getStatus = (index) => {
            if (index === 0) return { label: t('status.enroute'), class: 'enroute', icon: 'truck' };
            if (index === 1) return { label: t('status.ongoing'), class: 'ongoing', icon: 'loader' };
            return { label: t('status.completed'), class: 'completed', icon: 'check-circle' };
        };

        const renderIntervention = (intervention, index, isNew) => {
            const status = getStatus(index);
            const timeStr = formatTimeDiff(intervention.timestamp);
            const typeName = t(intervention.i18nKey);

            return `
                <div class="intervention-item${isNew ? ' new' : ''} fade-in">
                    <div class="intervention-icon ${intervention.iconClass}">
                        <i data-lucide="${intervention.icon}"></i>
                    </div>
                    <div class="intervention-info">
                        <div class="intervention-type">${typeName}</div>
                        <div class="intervention-location">
                            <i data-lucide="map-pin"></i>
                            ${intervention.location}
                        </div>
                    </div>
                    <div class="intervention-meta">
                        <div class="intervention-time">${timeStr}</div>
                        <div class="intervention-status ${status.class}">
                            <i data-lucide="${status.icon}"></i>
                            ${status.label}
                        </div>
                    </div>
                </div>
            `;
        };

        // Store interventions in module scope for re-rendering
        let dayInterventions = [];

        const renderList = () => {
            interventionsList.classList.remove('loading');
            const visibleInterventions = dayInterventions.slice(0, 6);
            interventionsList.innerHTML = visibleInterventions.map((int, i) =>
                renderIntervention(int, i, i === 0 && int.isNew)
            ).join('');
            initIcons();
        };

        // Expose re-render function globally for language switching
        window.rerenderInterventions = renderList;

        // Show skeleton loader first
        showSkeletonLoader();

        // Small delay to simulate loading and show skeleton
        setTimeout(() => {
            dayInterventions = generateDayInterventions();

            if (interventionCountEl) {
                interventionCountEl.textContent = dayInterventions.length;
            }

            renderList();

            setInterval(() => renderList(), 60000);

            setInterval(() => {
                const now = new Date();
                const hour = now.getHours();
                const rate = hourlyRate[hour];
                const probability = (rate / 60) * 2;

                if (Math.random() < probability) {
                    let intervention;
                    let attempts = 0;
                    do {
                        intervention = weightedRandom(interventionTypes, Date.now() + attempts);
                        attempts++;
                    } while (
                        dayInterventions.length > 0 &&
                        intervention.i18nKey === dayInterventions[0].i18nKey &&
                        attempts < 5
                    );

                    let location;
                    attempts = 0;
                    do {
                        location = locations[Math.floor(Math.random() * locations.length)];
                        attempts++;
                    } while (
                        dayInterventions.length > 0 &&
                        location === dayInterventions[0].location &&
                        attempts < 5
                    );

                    const newIntervention = {
                        hour: now.getHours(),
                        minute: now.getMinutes(),
                        i18nKey: intervention.i18nKey,
                        icon: intervention.icon,
                        iconClass: intervention.iconClass,
                        location,
                        timestamp: now,
                        isNew: true
                    };

                    dayInterventions.unshift(newIntervention);

                    if (interventionCountEl) {
                        interventionCountEl.textContent = dayInterventions.length;
                    }

                    if (dayInterventions[1]) dayInterventions[1].isNew = false;

                    renderList();

                    setTimeout(() => {
                        newIntervention.isNew = false;
                    }, 3000);
                }
            }, 120000);

            // Mobile fix: regenerate interventions when user returns to page
            // This handles cases where phone was in sleep mode and day cycle changed
            document.addEventListener('visibilitychange', () => {
                if (document.visibilityState === 'visible') {
                    const newSeed = calculateDateSeed();
                    if (newSeed !== dateSeed) {
                        // Day cycle has changed (crossed 3 AM), regenerate everything
                        dateSeed = newSeed;
                        dayInterventions = generateDayInterventions();
                        if (interventionCountEl) {
                            interventionCountEl.textContent = dayInterventions.length;
                        }
                        renderList();
                    } else {
                        // Same day cycle, just refresh the display (update time diffs)
                        renderList();
                    }
                }
            });
        }, 400); // End of initial setTimeout for skeleton
    }

    // =====================================================
    // ZONE CHECKER
    // =====================================================

    function initZoneChecker() {
        // Use centralized data from communes.js
        const communes = window.COMMUNES;

        // Validate data is loaded
        if (!communes || !Array.isArray(communes) || communes.length === 0) {
            return;
        }

        const zoneInput = document.getElementById('zoneInput');
        const zoneSuggestions = document.getElementById('zoneSuggestions');
        const checkerResult = document.getElementById('checkerResult');

        if (!zoneInput || !zoneSuggestions || !checkerResult) return;

        let selectedIndex = -1;

        const normalize = (str) => str.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
        const isPostalQuery = (query) => /^\d+$/.test(query);

        const filterCommunes = (query) => {
            if (!query || query.length < 2) return [];
            const normalizedQuery = normalize(query);

            // Search by postal code if query is numeric
            if (isPostalQuery(query)) {
                return communes.filter(c =>
                    c.postal && c.postal.some(p => p.startsWith(query))
                ).slice(0, 8);
            }

            // Search by name or alternative names
            return communes.filter(c => {
                if (normalize(c.name).includes(normalizedQuery)) return true;
                if (c.altNames && c.altNames.some(alt => normalize(alt).includes(normalizedQuery))) return true;
                return false;
            }).slice(0, 8);
        };

        const highlightMatch = (text, query) => {
            const normalizedText = normalize(text);
            const normalizedQuery = normalize(query);
            const index = normalizedText.indexOf(normalizedQuery);
            if (index === -1) return text;
            return text.slice(0, index) +
                   `<span class="suggestion-highlight">${text.slice(index, index + query.length)}</span>` +
                   text.slice(index + query.length);
        };

        const renderSuggestions = (filtered, query) => {
            if (filtered.length === 0) {
                zoneSuggestions.classList.remove('active');
                return;
            }

            zoneSuggestions.innerHTML = filtered.map((c, i) => {
                const postalDisplay = c.postal ? c.postal[0] : '';
                const coveredClass = c.covered ? 'covered' : 'not-covered';
                return `
                <div class="suggestion-item ${coveredClass}${i === selectedIndex ? ' active' : ''}" data-index="${i}">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                    <span class="suggestion-name">${highlightMatch(c.name, query)} <span class="suggestion-postal">(${postalDisplay})</span></span>
                    <span class="suggestion-region">${c.region}</span>
                </div>
            `}).join('');
            zoneSuggestions.classList.add('active');
            selectedIndex = -1;
        };

        const showResult = (commune) => {
            const initial = checkerResult.querySelector('.result-initial');
            const success = checkerResult.querySelector('.result-success');
            const notfound = checkerResult.querySelector('.result-notfound');
            const outside = checkerResult.querySelector('.result-outside');

            initial.style.display = 'none';
            success.style.display = 'none';
            notfound.style.display = 'none';
            if (outside) outside.style.display = 'none';

            if (commune) {
                const postalDisplay = commune.postal ? commune.postal[0] : '';
                if (commune.covered) {
                    // Zone covered - show success
                    success.style.display = 'flex';
                    const successText = window.i18n && window.i18n.t ? window.i18n.t('zones.success.text') : 'Nous intervenons à';
                    success.querySelector('.result-commune').textContent =
                        `${successText} ${commune.name} (${postalDisplay}) - ${commune.region}`;
                } else {
                    // Zone not covered - show outside message
                    if (outside) {
                        outside.style.display = 'flex';
                        const outsideText = window.i18n && window.i18n.t ? window.i18n.t('zones.outside.text') : 'Zone hors couverture standard';
                        outside.querySelector('.result-commune').textContent =
                            `${commune.name} (${postalDisplay}) - ${commune.region}`;
                    } else {
                        // Fallback to notfound if outside element doesn't exist
                        notfound.style.display = 'flex';
                    }
                }
                initIcons();
            } else {
                notfound.style.display = 'flex';
                initIcons();
            }
        };

        const selectCommune = (commune) => {
            zoneInput.value = commune.name;
            zoneSuggestions.classList.remove('active');
            showResult(commune);
        };

        zoneInput.addEventListener('input', (e) => {
            const query = e.target.value.trim();
            const filtered = filterCommunes(query);
            renderSuggestions(filtered, query);
        });

        zoneSuggestions.addEventListener('click', (e) => {
            const item = e.target.closest('.suggestion-item');
            if (item) {
                const index = parseInt(item.dataset.index);
                const filtered = filterCommunes(zoneInput.value.trim());
                if (filtered[index]) {
                    selectCommune(filtered[index]);
                }
            }
        });

        zoneInput.addEventListener('keydown', (e) => {
            const items = zoneSuggestions.querySelectorAll('.suggestion-item');

            if (items.length) {
                if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    selectedIndex = Math.min(selectedIndex + 1, items.length - 1);
                    items.forEach((item, i) => item.classList.toggle('active', i === selectedIndex));
                } else if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    selectedIndex = Math.max(selectedIndex - 1, 0);
                    items.forEach((item, i) => item.classList.toggle('active', i === selectedIndex));
                } else if (e.key === 'Enter' && selectedIndex >= 0) {
                    e.preventDefault();
                    const filtered = filterCommunes(zoneInput.value.trim());
                    if (filtered[selectedIndex]) {
                        selectCommune(filtered[selectedIndex]);
                    }
                } else if (e.key === 'Escape') {
                    zoneSuggestions.classList.remove('active');
                }
            }

            if (e.key === 'Enter' && selectedIndex === -1) {
                const query = zoneInput.value.trim();
                if (query.length >= 2) {
                    const filtered = filterCommunes(query);
                    if (filtered.length === 1) {
                        selectCommune(filtered[0]);
                    } else if (filtered.length === 0) {
                        showResult(null);
                        zoneSuggestions.classList.remove('active');
                    }
                }
            }
        });

        document.addEventListener('click', (e) => {
            if (!e.target.closest('.checker-input-wrapper')) {
                zoneSuggestions.classList.remove('active');
            }
        });
    }

    // =====================================================
    // ANIMATIONS
    // =====================================================

    function initScrollAnimations() {
        if (!('IntersectionObserver' in window)) return;

        const animatedElements = document.querySelectorAll(
            '.service-card, .pillar, .trust-card, .zone-region, .faq-item, .contact-card, .partner-card'
        );

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, index * 50);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        animatedElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            observer.observe(el);
        });
    }

    function initAnimatedCounters() {
        if (!('IntersectionObserver' in window)) return;

        const animateCounter = (element) => {
            const target = parseInt(element.getAttribute('data-count'), 10);
            const duration = 2000;
            const increment = target / (duration / 16);
            let current = 0;

            const updateCounter = () => {
                current += increment;
                if (current < target) {
                    element.textContent = Math.floor(current);
                    requestAnimationFrame(updateCounter);
                } else {
                    element.textContent = target;
                }
            };

            updateCounter();
        };

        const counterElements = document.querySelectorAll('[data-count]');
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        counterElements.forEach(el => counterObserver.observe(el));
    }

    // =====================================================
    // INIT
    // =====================================================

    document.addEventListener('DOMContentLoaded', () => {
        initIcons();
        setCurrentYear();
        initMobileMenu();
        initHeaderScroll();
        initSmoothScroll();
        initFloatingCta();
        initFaqAccordion();
        initInterventionsFeed();
        initZoneChecker();
        initScrollAnimations();
        initAnimatedCounters();
    });

})();
