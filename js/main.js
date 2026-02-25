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

// ==========================================
// Floating Buttons & Chatbot Logic
// ==========================================

document.addEventListener('DOMContentLoaded', () => {
    // 1. Inject CSS
    const style = document.createElement('style');
    style.innerHTML = `
        /* Floating Buttons Container */
        .floating-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .float-btn {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-size: 30px;
            text-decoration: none;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            transition: transform 0.3s;
            cursor: pointer;
            position: relative;
        }

        .float-btn:hover {
            transform: scale(1.1);
        }

        .whatsapp-btn {
            background-color: #25D366;
        }

        .chat-btn {
            background-color: #003366;
        }

        /* Chat Window */
        .chat-window {
            position: fixed;
            bottom: 170px;
            right: 20px;
            width: 350px;
            max-width: 90%;
            height: 450px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
            z-index: 1001;
            display: none;
            flex-direction: column;
            overflow: hidden;
            font-family: 'Open Sans', sans-serif;
            border: 1px solid #eee;
        }

        .chat-window.active {
            display: flex;
            animation: slideIn 0.3s ease-out;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .chat-header {
            background: #003366;
            color: white;
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .chat-header h4 {
            margin: 0;
            font-size: 1.1rem;
            font-family: 'Montserrat', sans-serif;
        }

        .close-chat {
            background: none;
            border: none;
            color: white;
            font-size: 20px;
            cursor: pointer;
        }

        .chat-body {
            flex: 1;
            padding: 15px;
            overflow-y: auto;
            background: #f9f9f9;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .message {
            max-width: 80%;
            padding: 10px 15px;
            border-radius: 15px;
            font-size: 0.95rem;
            line-height: 1.4;
        }

        .bot-message {
            background: #e9ecef;
            color: #333;
            align-self: flex-start;
            border-bottom-left-radius: 2px;
        }

        .user-message {
            background: #00A86B;
            color: white;
            align-self: flex-end;
            border-bottom-right-radius: 2px;
        }

        .chat-input-area {
            padding: 10px;
            border-top: 1px solid #ddd;
            background: white;
            display: flex;
            gap: 10px;
        }

        .chat-input-area input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 20px;
            outline: none;
        }

        .chat-input-area button {
            background: #003366;
            color: white;
            border: none;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .chat-input-area button:hover {
            background: #002244;
        }
    `;
    document.head.appendChild(style);

    // 2. Create Elements
    const floatContainer = document.createElement('div');
    floatContainer.className = 'floating-container';

    // WhatsApp Button
    const waBtn = document.createElement('a');
    waBtn.href = 'https://wa.me/918094767023';
    waBtn.className = 'float-btn whatsapp-btn';
    waBtn.target = '_blank';
    waBtn.setAttribute('aria-label', 'Chat on WhatsApp');
    waBtn.innerHTML = '<i class="fab fa-whatsapp"></i>';

    // Chatbot Button
    const chatBtn = document.createElement('div');
    chatBtn.className = 'float-btn chat-btn';
    chatBtn.innerHTML = '<i class="fas fa-comment-dots"></i>';
    chatBtn.setAttribute('aria-label', 'Open Chatbot');

    floatContainer.appendChild(waBtn);
    floatContainer.appendChild(chatBtn);
    document.body.appendChild(floatContainer);

    // Chat Window HTML
    const chatWindow = document.createElement('div');
    chatWindow.className = 'chat-window';
    chatWindow.innerHTML = `
        <div class="chat-header">
            <h4><i class="fas fa-user-md"></i> Dr. Nikhil's Assistant</h4>
            <button class="close-chat">&times;</button>
        </div>
        <div class="chat-body" id="chatBody">
            <div class="message bot-message">Hello! I am Dr. Nikhil's virtual assistant. How can I help you today?</div>
        </div>
        <div class="chat-input-area">
            <input type="text" id="chatInput" placeholder="Type your question...">
            <button id="sendBtn"><i class="fas fa-paper-plane"></i></button>
        </div>
    `;
    document.body.appendChild(chatWindow);

    // 3. Logic
    const chatBody = document.getElementById('chatBody');
    const chatInput = document.getElementById('chatInput');
    const sendBtn = document.getElementById('sendBtn');
    const closeBtn = chatWindow.querySelector('.close-chat');

    // Knowledge Base
    const knowledgeBase = {
        "greetings": ["hello", "hi", "hey", "start", "good morning", "good evening"],
        "services": ["service", "treatment", "pain", "back", "neck", "knee", "sports", "neuro", "online", "home visit", "paralysis", "sciatica", "frozen shoulder"],
        "location": ["location", "address", "where", "visit", "clinic", "ahmedabad", "area", "map"],
        "contact": ["contact", "phone", "email", "number", "call", "whatsapp", "mobile"],
        "appointment": ["book", "appointment", "schedule", "consultation", "time", "slot"],
        "price": ["price", "cost", "fees", "charges", "money", "rate"],
        "dr": ["doctor", "nikhil", "experience", "qualification", "about"]
    };

    const responses = {
        "greetings": "Hello! I can help you with services, location details, appointment booking, and more. What would you like to know?",
        "services": "We specialize in <strong>Home Physiotherapy</strong> (Ahmedabad) and <strong>Online Consultations</strong> (Global). We treat Back Pain, Neck Pain, Knee Arthritis, Sports Injuries, Neuro Rehab (Paralysis), and Post-Surgery stiffness.",
        "location": "We provide <strong>Home Visits</strong> across Ahmedabad. Our registered office is at 233/1/B Mukhivas, Jehangirpura, Ahmedabad 380016. For other cities, we offer video consultations.",
        "contact": "You can call or WhatsApp Dr. Nikhil at <strong>+91-8094767023</strong> or email info@drnikhilphysio.in.",
        "appointment": "To book a session, please click the 'Book Appointment' button in the menu or call us directly at <strong>+91-8094767023</strong>.",
        "price": "Our fees depend on the type of service (Home Visit or Online) and the duration. Please contact us at +91-8094767023 for a personalized quote.",
        "dr": "Dr. Nikhil Rajpurohit (PT) is a highly experienced Physiotherapist (B.P.T, GPC-21467) with expertise in musculoskeletal and neurological rehabilitation. He has served at Civil Hospital Ahmedabad.",
        "default": "I'm not sure about that. Please contact Dr. Nikhil directly at <strong>+91-8094767023</strong> for expert medical advice."
    };

    // Toggle Chat
    chatBtn.addEventListener('click', () => {
        chatWindow.classList.toggle('active');
        if (chatWindow.classList.contains('active')) {
            chatInput.focus();
        }
    });

    closeBtn.addEventListener('click', () => {
        chatWindow.classList.remove('active');
    });

    // Send Message Logic
    const sendMessage = () => {
        const text = chatInput.value.trim().toLowerCase();
        if (text === "") return;

        // Add User Message
        addMessage(chatInput.value, 'user-message', false);
        chatInput.value = '';

        // Generate Response
        setTimeout(() => {
            const response = getResponse(text);
            addMessage(response, 'bot-message', true);
        }, 500);
    };

    const addMessage = (text, className, isHtml = false) => {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${className}`;
        if (isHtml) {
            msgDiv.innerHTML = text;
        } else {
            msgDiv.textContent = text;
        }
        chatBody.appendChild(msgDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    };

    const getResponse = (text) => {
        let bestMatch = "default";

        // Simple keyword matching
        for (const [key, keywords] of Object.entries(knowledgeBase)) {
            for (const keyword of keywords) {
                if (text.includes(keyword)) {
                    bestMatch = key;
                    break;
                }
            }
            if (bestMatch !== "default") break;
        }

        return responses[bestMatch];
    };

    // Event Listeners for Input
    sendBtn.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });
});
