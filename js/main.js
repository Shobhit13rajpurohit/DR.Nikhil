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

    // Pain Decoder Logic
    const bodyParts = document.querySelectorAll('.body-part');
    const resultContent = document.querySelector('.result-content');
    const placeholderText = document.querySelector('.placeholder-text');

    // Data for the decoder
    const painData = {
        neck: {
            title: "Neck Pain & Stiffness",
            desc: "Often caused by poor posture ('Tech Neck'), stress, or sleeping wrong.",
            tip: "Try gentle chin tucks. Ensure your screen is at eye level."
        },
        shoulder: {
            title: "Shoulder Impingement / Pain",
            desc: "Can be Rotator Cuff strain or Frozen Shoulder from overuse.",
            tip: "Avoid sleeping on the painful side. Do pendulum swings."
        },
        back: {
            title: "Lower Back Pain",
            desc: "Commonly due to prolonged sitting, muscle strain, or disc issues.",
            tip: "Use lumbar support while sitting. Do 'Cat-Cow' stretches."
        },
        knee: {
            title: "Knee Pain (Runner's Knee)",
            desc: "Could be Meniscus wear, Ligament strain, or Arthritis.",
            tip: "Avoid deep squats/lunges. Apply ice for 15 mins to reduce swelling."
        }
    };

    if (bodyParts.length > 0) {
        bodyParts.forEach(part => {
            part.addEventListener('click', () => {
                // Remove active class from all
                bodyParts.forEach(p => p.classList.remove('active'));
                // Add to clicked
                part.classList.add('active');

                // Get Data
                const partKey = part.getAttribute('data-part');
                const data = painData[partKey];

                if (data) {
                    // Update Content
                    document.getElementById('result-title').textContent = data.title;
                    document.getElementById('result-desc').textContent = data.desc;
                    document.getElementById('result-tip').textContent = data.tip;

                    // Show Result, Hide Placeholder
                    placeholderText.style.display = 'none';
                    resultContent.style.display = 'block';
                    resultContent.classList.add('animate-on-scroll'); // Re-trigger fade
                    resultContent.classList.add('visible');
                }
            });
        });
    }

    // Create Floating Particles
    const particlesContainer = document.getElementById('particles');
    if (particlesContainer) {
        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.classList.add('particle');

            // Random positioning
            const size = Math.random() * 20 + 5;
            particle.style.width = `${size}px`;
            particle.style.height = `${size}px`;
            particle.style.left = `${Math.random() * 100}%`;
            particle.style.animationDuration = `${Math.random() * 10 + 10}s`;
            particle.style.animationDelay = `${Math.random() * 5}s`;

            particlesContainer.appendChild(particle);
        }
    }
});
