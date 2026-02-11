document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const links = document.querySelectorAll('.nav-links li');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.querySelector('i').classList.toggle('fa-times');
            hamburger.querySelector('i').classList.toggle('fa-bars');
        });
    }

    // Close menu when a link is clicked
    links.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            hamburger.querySelector('i').classList.add('fa-bars');
            hamburger.querySelector('i').classList.remove('fa-times');
        });
    });

    // Scroll Animations using Intersection Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Select elements to animate
    const animateElements = document.querySelectorAll('.service-card, .intro-text, .intro-image, .content-block, .tip-card, .testimonial-box, .section-title, .hero-content h1, .hero-content p, .hero-btns, details, .step-list li, .info-item, .contact-form-wrapper, .pathway-card, .problem-card');

    // Add base class and observe
    animateElements.forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });

    // Contact Form Handling (Demo)
    const form = document.getElementById('appointmentForm');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = form.querySelector('button');
            const originalText = btn.innerText;

            btn.innerText = 'Sending...';
            btn.disabled = true;

            // Simulate API call
            setTimeout(() => {
                alert('Thank you! Your appointment request has been sent. We will contact you shortly.');
                form.reset();
                btn.innerText = originalText;
                btn.disabled = false;
            }, 1500);
        });
    }

    // Dynamic Header Background on Scroll (Optional polish)
    window.addEventListener('scroll', () => {
        const header = document.querySelector('.header');
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.boxShadow = 'none'; // Or keep it if you want it always there
        }
    });

    // Dynamic Copyright Year
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // Stats Counter Animation
    const counters = document.querySelectorAll('.counter');
    const speed = 50; // Speed of counting

    const animateCounters = () => {
        counters.forEach(counter => {
            const updateCount = () => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText;
                const inc = target / speed;

                if (count < target) {
                    counter.innerText = Math.ceil(count + inc);
                    setTimeout(updateCount, 40);
                } else {
                    counter.innerText = target + "+";
                }
            };
            updateCount();
        });
    };

    // Trigger counters when Stats section is visible
    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        const statsObserver = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                animateCounters();
                statsObserver.unobserve(statsSection);
            }
        }, { threshold: 0.5 });
        statsObserver.observe(statsSection);
    }

    // ==========================================
    // Locations Page Logic
    // ==========================================

    // 1. Search Functionality
    const searchInput = document.getElementById('locationSearch');
    const searchBtn = document.getElementById('searchBtn');

    if (searchInput) {
        const locationCards = document.querySelectorAll('.location-card');

        const performSearch = () => {
            const query = searchInput.value.toLowerCase().trim();

            locationCards.forEach(card => {
                const text = card.innerText.toLowerCase();
                if (text.includes(query)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        };

        searchInput.addEventListener('input', performSearch);
        if (searchBtn) {
            searchBtn.addEventListener('click', performSearch);
        }
    }

    // 2. Interactive Map Logic
    const stateTiles = document.querySelectorAll('.state-tile');
    const serviceStatus = document.getElementById('serviceStatus');

    if (stateTiles.length > 0 && serviceStatus) {
        stateTiles.forEach(tile => {
            tile.addEventListener('click', () => {
                // Remove active class from all
                stateTiles.forEach(t => t.classList.remove('active'));

                // Add active to clicked
                tile.classList.add('active');

                // Get data
                const stateName = tile.getAttribute('data-state');
                const linkUrl = tile.getAttribute('data-link');
                const isGujarat = stateName === 'Gujarat';

                // Update Status Panel
                serviceStatus.innerHTML = `
                    <h4>${stateName}</h4>
                    <p class="mb-2"><strong>Service Availability:</strong></p>
                    <div class="status-indicators mb-4">
                        ${isGujarat ?
                            `<div class="indicator home"><i class="fas fa-home"></i> Home Visits Available (Ahmedabad)</div>
                             <div class="indicator online"><i class="fas fa-laptop-medical"></i> Online Consultation Available</div>`
                            :
                            `<div class="indicator online"><i class="fas fa-laptop-medical"></i> Online Consultation Available</div>`
                        }
                    </div>
                    <a href="${linkUrl}" class="btn btn-primary btn-sm">View Details & Book <i class="fas fa-arrow-right ml-2"></i></a>
                `;

                // Add fade-in animation class to new content
                serviceStatus.classList.remove('fade-in');
                void serviceStatus.offsetWidth; // trigger reflow
                serviceStatus.classList.add('fade-in');
            });
        });
    }
});
