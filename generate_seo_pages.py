import os

# Define the HTML template
template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_description}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="Dr. Nikhil Rajpurohit">
    <title>{title}</title>
    <link rel="icon" type="image/jpeg" href="Public/fevicon.jpeg">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" integrity="sha512-9usAa10IRO0HhonpyAIVpjrylPvoDwiPUiKdWk5t3PyolY1cOd4DSE0Ga+ri4AuTroPR5aQvXU9xC6qOPnzFeg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        .location-hero {{
            background: linear-gradient(rgba(0, 34, 68, 0.85), rgba(0, 86, 179, 0.7)), url('Public/hero-bg.jpg'); /* Fallback or generic image */
            background-size: cover;
            background-position: center;
            color: white;
            padding: 100px 0;
            text-align: center;
        }}
        .location-content h2 {{
            color: #003366;
            margin-bottom: 20px;
        }}
        .location-content p {{
            margin-bottom: 15px;
            font-size: 1.1rem;
            line-height: 1.6;
        }}
        .local-landmark {{
            background-color: #f8f9fa;
            padding: 20px;
            border-left: 5px solid #00A86B;
            margin: 30px 0;
        }}
    </style>
</head>
<body>

    <!-- Header -->
    <header class="header">
        <div class="container">
            <nav class="navbar">
                <a href="index.html" class="logo"><img src="Public/bgremove_logo.png" alt="Dr. Nikhil Physio Logo"></a>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About Dr. Nikhil</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="tips.html">Tips & Exercises</a></li>
                    <li><a href="testimonials.html">Testimonials</a></li>
                    <li><a href="contact.html" class="btn btn-primary nav-btn">Book Appointment</a></li>
                </ul>
                <div class="hamburger">
                    <i class="fas fa-bars"></i>
                </div>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="location-hero">
        <div class="container">
            <h1>Best Physiotherapist in {area_name}, Ahmedabad</h1>
            <p>Expert Pain Relief & Rehabilitation by Dr. Nikhil Rajpurohit</p>
            <div class="mt-4">
                <a href="contact.html" class="btn btn-primary btn-lg">Book Home Visit in {area_name}</a>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <section class="location-content section-padding">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <h2>Physiotherapy Services in {area_name}</h2>
                    <p>{intro_text}</p>

                    <div class="local-landmark">
                        <h4>Serving Patients Near {landmark}</h4>
                        <p>{landmark_text}</p>
                    </div>

                    <h2>Why {area_name} Residents Choose Dr. Nikhil</h2>
                    <p>{why_choose_text}</p>

                    <h3>Common Conditions Treated in {area_name}</h3>
                    <p>{common_conditions_text}</p>

                    <ul class="check-list mt-3">
                        <li><i class="fas fa-check-circle"></i> <strong>Home Visits:</strong> We come to your home in {area_name}, saving you travel time and pain.</li>
                        <li><i class="fas fa-check-circle"></i> <strong>Personalized Care:</strong> Treatment plans designed around your lifestyle in {area_name}.</li>
                        <li><i class="fas fa-check-circle"></i> <strong>Expertise:</strong> Dr. Nikhil brings years of experience treating complex cases.</li>
                    </ul>

                    <div class="mt-5 text-center">
                        <h3>Ready to Live Pain-Free?</h3>
                        <p>Don't let pain control your life. Get world-class physiotherapy right here in {area_name}.</p>
                        <a href="contact.html" class="btn btn-primary btn-lg">Schedule Your Assessment</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-about">
                    <img src="Public/whitebglogo.jpeg" alt="Dr. Nikhil Physio Logo" class="footer-logo">
                    <p>Providing expert physiotherapy care with a human touch. Dedicated to restoring movement and improving quality of life.</p>
                </div>
                <div class="footer-links">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="locations.html">Areas We Serve</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-services">
                    <h4>Our Services</h4>
                    <ul>
                        <li><a href="services.html#home-physio">Home Physiotherapy</a></li>
                        <li><a href="services.html#online-physio">Online Consultation</a></li>
                        <li><a href="services.html#sports-rehab">Sports Rehab</a></li>
                        <li><a href="services.html#neuro-rehab">Neuro Rehab</a></li>
                        <li><a href="services.html#pain-management">Pain Management</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Contact Us</h4>
                    <p><i class="fas fa-map-marker-alt"></i> Ahmedabad, Gujarat, India</p>
                    <p><i class="fas fa-envelope"></i> info@drnikhilphysio.in</p>

                    <h4 class="mt-4">Opening Hours</h4>
                    <p><i class="far fa-clock"></i> Mon - Sat: 9:00 AM - 8:00 PM</p>
                    <p><i class="far fa-clock"></i> Sunday: By Appointment</p>

                    <div class="social-links mt-3">
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom text-center">
                <p>&copy; <span id="year"></span> Dr. Nikhil Rajpurohit. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <script src="js/main.js"></script>
    <script>
        document.getElementById('year').textContent = new Date().getFullYear();
    </script>
</body>
</html>
"""

# Data Dictionary
areas_data = {
    "Navrangpura": {
        "title": "Best Physiotherapist in Navrangpura, Ahmedabad – Dr. Nikhil Rajpurohit",
        "meta_description": "Top-rated Physiotherapist in Navrangpura, Ahmedabad. Expert home visits for back pain, sports injuries & post-surgery rehab. Dr. Nikhil Rajpurohit brings clinic-quality care to you.",
        "keywords": "Physiotherapist in Navrangpura, best physio Navrangpura, home physiotherapy Navrangpura, back pain treatment Navrangpura, sports injury rehab Navrangpura",
        "intro_text": "Navrangpura is the heartbeat of Ahmedabad, bustling with educational institutions and commerce. However, the fast-paced lifestyle often leads to health neglects. Residents of Navrangpura deserve the best medical care without the hassle of navigating heavy traffic. Dr. Nikhil Rajpurohit offers premier physiotherapy services directly to your doorstep, ensuring you receive focused, high-quality rehabilitation in the comfort of your home.",
        "landmark": "Gujarat University & Law Garden",
        "landmark_text": "Whether you are a student near Gujarat University suffering from 'text neck' or a professional near C.G. Road dealing with chronic back pain, our services are just a call away. We understand the specific needs of this vibrant community.",
        "why_choose_text": "Residents of Navrangpura choose Dr. Nikhil for his punctuality, professional demeanor, and evidence-based approach. We know that time is valuable for the busy professionals and students in this area. Our home visits are scheduled to fit your routine, minimizing disruption while maximizing recovery.",
        "common_conditions_text": "In Navrangpura, we frequently treat posture-related issues among students and desk workers, as well as age-related joint pain in the elderly population residing in the classic bungalows of the area."
    },
    "Maninagar": {
        "title": "Physiotherapist in Maninagar, Ahmedabad – Pain Relief & Rehab",
        "meta_description": "Looking for a Physiotherapist in Maninagar? Dr. Nikhil Rajpurohit provides expert home physiotherapy for knee pain, sciatica, and paralysis in Maninagar, Ahmedabad.",
        "keywords": "Physiotherapist in Maninagar, Physiotherapy at home Maninagar, knee pain treatment Maninagar, paralysis treatment Maninagar, Dr. Nikhil Rajpurohit Maninagar",
        "intro_text": "Maninagar, the southern gem of Ahmedabad, is known for its strong community spirit and vibrant lifestyle. But whether you are enjoying a walk at Kankaria or managing a busy household, pain shouldn't hold you back. Dr. Nikhil Rajpurohit brings specialized physiotherapy care to Maninagar, focusing on personalized recovery plans that help you get back to what you love.",
        "landmark": "Kankaria Lake & Nagina Wadi",
        "landmark_text": "For the active walkers of Kankaria Lake and the residents around the railway station, we provide targeted therapies. If your morning walk is becoming painful due to knee or heel pain, our expert assessment can identify the root cause.",
        "why_choose_text": "Maninagar residents appreciate our warm, patient-centric approach. Dr. Nikhil is known for his ability to explain complex medical conditions in simple language, empowering patients to take charge of their recovery. Our home visit service in Maninagar is reliable and efficient.",
        "common_conditions_text": "We see a high volume of knee osteoarthritis cases in Maninagar's senior community, as well as sciatica and lower back pain among the working population commuting to industrial zones."
    },
    "Satellite": {
        "title": "Top Physiotherapist in Satellite, Ahmedabad – Dr. Nikhil Rajpurohit",
        "meta_description": "Expert Physiotherapy in Satellite, Ahmedabad. Dr. Nikhil Rajpurohit specializes in sports injuries, neck pain, and post-op rehab. Book a home visit in Satellite today.",
        "keywords": "Physiotherapist in Satellite Ahmedabad, sports physio Satellite, neck pain relief Satellite, home visit physiotherapy Satellite, Dr. Nikhil Rajpurohit",
        "intro_text": "Satellite is synonymous with modern living in Ahmedabad. With its high-rise apartments and corporate offices, the lifestyle here is upscale but demanding. Long hours at desks and high-stress environments can take a toll on your body. Dr. Nikhil Rajpurohit offers elite physiotherapy services tailored for the residents of Satellite, blending advanced techniques with the convenience of home care.",
        "landmark": "ISRO & Star Bazaar",
        "landmark_text": "From the busy streets near Star Bazaar to the residential pockets near ISRO, we cover the entire Satellite area. We bring all necessary equipment to your apartment, ensuring a clinic-like experience without the commute.",
        "why_choose_text": "Satellite's discerning residents demand quality and results. Dr. Nikhil delivers both with his certification in advanced manual therapy and a track record of successful recoveries. We offer flexible evening slots perfect for corporate employees returning from work.",
        "common_conditions_text": "Our Satellite patients often seek help for 'Corporate Athlete' injuries: chronic neck pain, repetitive strain injuries (RSI), and stress-induced muscle tension. We also provide specialized post-surgical rehab for joint replacements."
    },
    "Bopal": {
        "title": "Best Physiotherapist in Bopal & South Bopal – Dr. Nikhil Rajpurohit",
        "meta_description": "Leading Physiotherapist in Bopal and South Bopal. Specialized care for back pain, pregnancy rehab, and sports injuries. Home visits available in Bopal, Ahmedabad.",
        "keywords": "Physiotherapist in Bopal, Physiotherapist in South Bopal, pregnancy physiotherapy Bopal, back pain doctor Bopal, home physio Bopal",
        "intro_text": "Bopal and South Bopal have rapidly emerged as the new residential hubs for young families and professionals. While the area offers great amenities, the commute to the city center can be long and tiring, often exacerbating back and neck issues. Dr. Nikhil Rajpurohit bridges this gap by bringing top-tier physiotherapy services directly to your home in Bopal.",
        "landmark": "TRP Mall & Sobo Center",
        "landmark_text": "Serving the expanding communities around TRP Mall, Sobo Center, and the new residential societies along the ring road. We ensure that quality healthcare is accessible without you having to travel miles into the city.",
        "why_choose_text": "Families in Bopal choose us for our comprehensive care. From young parents dealing with lifting strains to grandparents needing mobility support, Dr. Nikhil provides holistic care for the whole family. Our punctual home service is a boon for Bopal residents.",
        "common_conditions_text": "We frequently treat commute-related back pain, sports injuries from weekend cricket/football, and provide pre/post-natal physiotherapy for new mothers in the Bopal area."
    },
    "Gota": {
        "title": "Physiotherapist in Gota, Ahmedabad – Expert Home Visits",
        "meta_description": "Reliable Physiotherapist in Gota, Ahmedabad. Dr. Nikhil Rajpurohit treats knee pain, frozen shoulder, and more. Convenient home physiotherapy services in Gota.",
        "keywords": "Physiotherapist in Gota, best physio Gota, frozen shoulder treatment Gota, home physiotherapy Gota Ahmedabad, Dr. Nikhil Rajpurohit",
        "intro_text": "Gota is one of Ahmedabad's fastest-developing corridors, strategically located near the SG Highway. As new residential townships rise, so does the need for accessible healthcare. Dr. Nikhil Rajpurohit serves the Gota community with dedication, ensuring that world-class physiotherapy is available right at your doorstep.",
        "landmark": "Vandemataram City & SG Highway",
        "landmark_text": "Whether you reside in Vandemataram City, Godrej Garden City, or near the Gota Flyover, our team is equipped to reach you. We understand the specific health challenges of this growing suburb.",
        "why_choose_text": "Gota residents value our commitment to affordable yet premium care. Dr. Nikhil's honest advice and effective treatment plans mean you recover faster and spend less time in pain. We focus on teaching you self-management techniques.",
        "common_conditions_text": "Common issues in Gota include construction-related occupational injuries, lifestyle ailments like frozen shoulder in the middle-aged population, and post-fracture rehabilitation."
    },
    "Thaltej": {
        "title": "Premium Physiotherapist in Thaltej, Ahmedabad – Dr. Nikhil Rajpurohit",
        "meta_description": "Elite Physiotherapy services in Thaltej. Dr. Nikhil Rajpurohit offers specialized geriatric care, arthritis treatment, and pain management in Thaltej, Ahmedabad.",
        "keywords": "Physiotherapist in Thaltej, geriatric physiotherapy Thaltej, arthritis treatment Thaltej, best physio Thaltej, home visit doctor Thaltej",
        "intro_text": "Thaltej is known for its serene environment, spacious bungalows, and affluent community. Maintaining an active, pain-free lifestyle is a priority for the residents here. Dr. Nikhil Rajpurohit provides premium, discreet, and highly effective home physiotherapy services tailored to the sophisticated needs of Thaltej residents.",
        "landmark": "Acropolis Mall & Thaltej Shilaj Road",
        "landmark_text": "Serving the prestigious localities around Thaltej Shilaj Road, Hebatpur, and near Acropolis Mall. We bring the clinic to your living room, ensuring privacy and comfort during your rehabilitation sessions.",
        "why_choose_text": "Dr. Nikhil is the preferred choice in Thaltej for his experience with complex geriatric conditions and chronic pain management. We offer longer session durations and detailed attention that goes beyond standard care.",
        "common_conditions_text": "We specialize in treating Osteoarthritis, Rheumatoid Arthritis, and balance disorders in seniors. We also manage chronic lifestyle diseases like Fibromyalgia and chronic fatigue for Thaltej residents."
    },
    "Vastrapur": {
        "title": "Best Physiotherapist in Vastrapur, Ahmedabad – Sports & Spine Care",
        "meta_description": "Top Physiotherapist in Vastrapur. Expert care for sports injuries, gym strains, and spine pain. Dr. Nikhil Rajpurohit offers home visits near Vastrapur Lake.",
        "keywords": "Physiotherapist in Vastrapur, sports injury clinic Vastrapur, back pain doctor Vastrapur, gym injury rehab Vastrapur, Dr. Nikhil Rajpurohit",
        "intro_text": "Vastrapur is the energetic soul of Ahmedabad, buzzing with youth, shopping, and recreation. With a high concentration of gyms and sports activities, injuries are common. Dr. Nikhil Rajpurohit brings specialized sports and spine care to Vastrapur, helping you bounce back to your active lifestyle stronger than before.",
        "landmark": "Vastrapur Lake & Alpha One Mall",
        "landmark_text": "Located near the iconic Vastrapur Lake and Alpha One Mall? We are in your neighborhood. We help joggers, gym-goers, and shoppers alike to overcome pain and regain mobility.",
        "why_choose_text": "The young and active population of Vastrapur prefers Dr. Nikhil for his modern, active-rehab approach. We don't just use machines; we use functional training to get you back to the gym or the track safely.",
        "common_conditions_text": "High incidence of gym-related injuries (rotator cuff strains, lower back spasms), runner's knee, and ankle sprains are what we treat daily in Vastrapur."
    },
    "Paldi": {
        "title": "Trusted Physiotherapist in Paldi, Ahmedabad – Dr. Nikhil Rajpurohit",
        "meta_description": "Experienced Physiotherapist in Paldi. Specializing in joint pain, post-surgery care, and neurological rehab. Home visits available in Paldi, Ahmedabad.",
        "keywords": "Physiotherapist in Paldi, joint pain treatment Paldi, neuro rehab Paldi, home physiotherapy Paldi, Dr. Nikhil Rajpurohit",
        "intro_text": "Paldi is a cultural melting pot, blending the charm of old Ahmedabad with modern amenities. Home to a large community that values health and tradition, Paldi requires physiotherapy services that are respectful and effective. Dr. Nikhil Rajpurohit offers compassionate, expert care to the families of Paldi.",
        "landmark": "Sanskar Kendra & NID",
        "landmark_text": "Serving the areas around Sanskar Kendra, Mahalaxmi Cross Roads, and Bhatta. We understand the community's needs and provide care that integrates well with your daily routine and values.",
        "why_choose_text": "Paldi residents trust Dr. Nikhil for his ethical practice and proven results. We are particularly skilled in handling post-surgical recovery for joint replacements, a common need in the area's senior demographic.",
        "common_conditions_text": "Our practice in Paldi sees a lot of frozen shoulder, knee replacement rehabilitation, and neurological cases like stroke recovery or Parkinson's management."
    },
    "Naranpura": {
        "title": "Physiotherapist in Naranpura, Ahmedabad – Effective Pain Relief",
        "meta_description": "Best Physiotherapist in Naranpura. Dr. Nikhil Rajpurohit treats neck pain, back pain, and sciatica. Affordable home physiotherapy in Naranpura, Ahmedabad.",
        "keywords": "Physiotherapist in Naranpura, sciatica treatment Naranpura, neck pain doctor Naranpura, home physio Naranpura, Dr. Nikhil Rajpurohit",
        "intro_text": "Naranpura is a well-established residential area with a strong sense of community. From young professionals to retired government officials, the residents here seek reliable and effective healthcare. Dr. Nikhil Rajpurohit is dedicated to keeping Naranpura pain-free with his expert home physiotherapy services.",
        "landmark": "Naranpura Crossing & AEC",
        "landmark_text": "Covering the neighborhoods near Naranpura Crossing, AEC, and Parasnagar. We bring professional physiotherapy equipment to your home, ensuring you don't have to travel in pain.",
        "why_choose_text": "Patients in Naranpura appreciate Dr. Nikhil's straightforward, results-oriented approach. We focus on reducing pain quickly and preventing recurrence through education and exercise.",
        "common_conditions_text": "Common ailments we treat in Naranpura include Cervical Spondylosis (neck pain), Lumbar Spondylosis (back pain), and heel pain (Plantar Fasciitis)."
    },
    "Chandkheda": {
        "title": "Physiotherapist in Chandkheda & Motera – Dr. Nikhil Rajpurohit",
        "meta_description": "Top Physiotherapist in Chandkheda and Motera. Expert care for sports injuries and occupational pain near Narendra Modi Stadium. Home visits available.",
        "keywords": "Physiotherapist in Chandkheda, Physiotherapist in Motera, sports injury rehab Motera, back pain Chandkheda, Dr. Nikhil Rajpurohit",
        "intro_text": "Chandkheda and Motera have transformed into vibrant hubs, especially with the world's largest cricket stadium putting the area on the map. This growth brings a mix of active sports enthusiasts and hardworking professionals. Dr. Nikhil Rajpurohit provides specialized physiotherapy services to keep the residents of Chandkheda and Motera moving.",
        "landmark": "Narendra Modi Stadium & ONGC",
        "landmark_text": "Whether you are near the ONGC colony or the bustling areas around the Stadium, we are here for you. We provide specialized ergonomic advice for office workers and sports rehab for athletes.",
        "why_choose_text": "With a large population of government employees and young professionals, the demand for scientific, evidence-based physio is high. Dr. Nikhil meets this demand with precise diagnoses and effective treatment plans.",
        "common_conditions_text": "We treat a lot of occupational overuse syndromes (wrist pain, back pain) in ONGC employees, as well as sports injuries like ACL tears and meniscus issues in the local youth."
    },
    "Prahlad Nagar": {
        "title": "Best Physiotherapist in Prahlad Nagar, Ahmedabad – Corporate Wellness",
        "meta_description": "Corporate & Home Physiotherapy in Prahlad Nagar. Dr. Nikhil Rajpurohit treats desk-job injuries, posture issues, and back pain. Book now in Prahlad Nagar.",
        "keywords": "Physiotherapist in Prahlad Nagar, corporate physiotherapy Ahmedabad, posture correction Prahlad Nagar, back pain specialist Prahlad Nagar",
        "intro_text": "Prahlad Nagar is the corporate powerhouse of Ahmedabad. While the area drives the city's economy, the long hours sitting in ergonomic chairs often lead to 'sitting disease'. Dr. Nikhil Rajpurohit specializes in combating the side effects of the corporate lifestyle with targeted physiotherapy in Prahlad Nagar.",
        "landmark": "Prahlad Nagar Garden & Corporate Road",
        "landmark_text": "Serving the high-rises along Corporate Road and the residences near Prahlad Nagar Garden. We offer flexible scheduling to fit into your pre-office or post-office hours.",
        "why_choose_text": "Professionals in Prahlad Nagar choose us because we understand the mechanics of desk work. We don't just treat the pain; we assess your workstation and posture to prevent it from coming back.",
        "common_conditions_text": "Our Prahlad Nagar clinic (home visits) specializes in 'Tech Neck', lower back pain from prolonged sitting, and carpal tunnel syndrome."
    },
    "Isanpur": {
        "title": "Physiotherapist in Isanpur, Ahmedabad – Dr. Nikhil Rajpurohit",
        "meta_description": "Expert Physiotherapy in Isanpur. Treating work injuries, joint pain, and paralysis. Affordable home visits by Dr. Nikhil Rajpurohit in Isanpur.",
        "keywords": "Physiotherapist in Isanpur, work injury treatment Isanpur, paralysis doctor Isanpur, home physio Isanpur, Dr. Nikhil Rajpurohit",
        "intro_text": "Isanpur is a bustling mix of residential and industrial zones in eastern Ahmedabad. The hardworking residents here often face physical challenges due to demanding jobs. Dr. Nikhil Rajpurohit is committed to providing accessible, high-quality physiotherapy to the Isanpur community.",
        "landmark": "Isanpur Highway & Govindwadi",
        "landmark_text": "We cover the entire Isanpur area, from the highway to the internal residential societies. Our goal is to ensure that quality healthcare reaches every corner of Ahmedabad.",
        "why_choose_text": "Isanpur residents value Dr. Nikhil's honest and effective treatment methods. We focus on manual therapy and exercises that can be easily done at home, reducing the need for expensive equipment.",
        "common_conditions_text": "We frequently treat heavy-lifting injuries, shoulder strain, and chronic knee pain in Isanpur. Neurological rehabilitation for stroke survivors is also a key service here."
    },
    "Shahibaug": {
        "title": "Physiotherapist in Shahibaug, Ahmedabad – Elite Care",
        "meta_description": "Best Physiotherapist in Shahibaug. Dr. Nikhil Rajpurohit offers premium home visits for arthritis, sports injuries, and post-op care in Shahibaug.",
        "keywords": "Physiotherapist in Shahibaug, arthritis treatment Shahibaug, sports physio Shahibaug, home visit physiotherapy Shahibaug",
        "intro_text": "Shahibaug, with its lush greenery and historic charm, is one of Ahmedabad's most prestigious areas. Home to the cantonment and the beautiful riverfront, it fosters an active lifestyle. Dr. Nikhil Rajpurohit complements this lifestyle with elite physiotherapy services tailored for Shahibaug's residents.",
        "landmark": "Riverfront & Circuit House",
        "landmark_text": "Serving the serene localities near the Circuit House and the active walkers of the Riverfront. We help you maintain your mobility so you can continue to enjoy the beautiful surroundings.",
        "why_choose_text": "Dr. Nikhil's professional and discreet service is highly valued in Shahibaug. We provide comprehensive care that addresses not just the symptoms but the overall well-being of the patient.",
        "common_conditions_text": "We treat many walkers and runners for shin splints and knee pain. We also manage age-related arthritis and provide post-surgical care for joint replacements."
    },
    "Ranip": {
        "title": "Physiotherapist in Ranip & New Ranip – Dr. Nikhil Rajpurohit",
        "meta_description": "Reliable Physiotherapist in Ranip. Expert care for back pain, neck pain, and sciatica. Home visits available in Ranip and New Ranip, Ahmedabad.",
        "keywords": "Physiotherapist in Ranip, Physiotherapist in New Ranip, sciatica doctor Ranip, back pain relief Ranip, Dr. Nikhil Rajpurohit",
        "intro_text": "Ranip and New Ranip are rapidly developing areas connecting North Ahmedabad to the city center. As a transport and residential hub, the area is always on the move. Dr. Nikhil Rajpurohit ensures that the residents of Ranip have access to top-tier physiotherapy without having to travel far.",
        "landmark": "GST Crossing & Railway Museum",
        "landmark_text": "Covering the areas near GST Crossing and New Ranip. We bring the clinic to your doorstep, saving you the hassle of commuting in traffic while in pain.",
        "why_choose_text": "Residents of Ranip appreciate our practical and effective approach to pain relief. Dr. Nikhil creates customized exercise plans that fit into your daily routine.",
        "common_conditions_text": "Common issues in Ranip include commuter-related back pain, cervical issues from two-wheeler driving, and general geriatric mobility problems."
    },
    "Nikol": {
        "title": "Physiotherapist in Nikol, Ahmedabad – Advanced Rehab",
        "meta_description": "Top Physiotherapist in Nikol. Specialized in shoulder pain, neck pain, and diamond worker injuries. Home visits in Nikol by Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Nikol, shoulder pain Nikol, neck pain treatment Nikol, home physio Nikol, Dr. Nikhil Rajpurohit",
        "intro_text": "Nikol has transformed into a vibrant residential and commercial hub in East Ahmedabad. With a large community involved in the diamond and textile industries, occupational health is a major concern. Dr. Nikhil Rajpurohit offers specialized ergonomic and rehabilitation services to the Nikol community.",
        "landmark": "Nikol Naroda Road & Raspan Cross Road",
        "landmark_text": "We serve the bustling neighborhoods around Raspan Cross Road and Nikol Gam. Our home visits ensure that you get expert care without taking too much time off work.",
        "why_choose_text": "Nikol residents trust Dr. Nikhil for his understanding of occupational hazards. We provide specific exercises to counteract the strain of repetitive work.",
        "common_conditions_text": "We see a high prevalence of 'Diamond Polisher's Neck' (cervical pain), frozen shoulder, and repetitive strain injuries in Nikol."
    },
    "Odhav": {
        "title": "Physiotherapist in Odhav, Ahmedabad – Industrial Rehab",
        "meta_description": "Expert Physiotherapy in Odhav. Treatment for industrial injuries, back pain, and joint stiffness. Home visits by Dr. Nikhil Rajpurohit in Odhav.",
        "keywords": "Physiotherapist in Odhav, industrial injury rehab Odhav, back pain doctor Odhav, home physiotherapy Odhav",
        "intro_text": "Odhav is the industrial backbone of Ahmedabad. The physical demands placed on workers and residents here are immense. Dr. Nikhil Rajpurohit brings focused physiotherapy services to Odhav, helping the workforce stay healthy and productive.",
        "landmark": "GIDC & Odhav Ring Road",
        "landmark_text": "Serving the residential pockets near GIDC and Odhav Ring Road. We understand that physical fitness is your livelihood, and we aim to get you back to work safely and quickly.",
        "why_choose_text": "We offer robust rehabilitation plans that focus on strength and endurance. Dr. Nikhil's guidance helps prevent future injuries, which is crucial for the hardworking people of Odhav.",
        "common_conditions_text": "We treat lumbar strain (lifting injuries), slip discs, and chronic joint stiffness in the Odhav population."
    },
    "Ellis Bridge": {
        "title": "Physiotherapist in Ellis Bridge, Ahmedabad – Dr. Nikhil Rajpurohit",
        "meta_description": "Best Physiotherapist in Ellis Bridge. Central Ahmedabad's top choice for pain relief and post-op rehab. Home visits near VS Hospital and Law Garden.",
        "keywords": "Physiotherapist in Ellis Bridge, post-op rehab Ellis Bridge, pain relief Ahmedabad, Dr. Nikhil Rajpurohit",
        "intro_text": "Ellis Bridge is not just a landmark; it's the connector between the old and new city. This central area is home to many long-standing residents and key institutions. Dr. Nikhil Rajpurohit provides respectful, high-quality physiotherapy services to the families residing in this historic part of Ahmedabad.",
        "landmark": "VS Hospital & MJ Library",
        "landmark_text": "Serving the prestigious lanes near MJ Library and the residential colonies behind VS Hospital. We bring modern physiotherapy techniques to your heritage homes.",
        "why_choose_text": "Dr. Nikhil is preferred in Ellis Bridge for his blend of traditional patient care values and modern medical knowledge. We take the time to listen and treat the person, not just the pain.",
        "common_conditions_text": "We manage a lot of geriatric conditions here, including Parkinson's disease, balance issues, and general debility, helping seniors maintain their independence."
    },
    "Law Garden": {
        "title": "Physiotherapist near Law Garden, Ahmedabad – Dr. Nikhil Rajpurohit",
        "meta_description": "Physiotherapy near Law Garden. Expert care for walkers, joggers, and shoppers. Knee pain, back pain, and sports injury treatment by Dr. Nikhil.",
        "keywords": "Physiotherapist Law Garden, knee pain treatment Law Garden, sports injury rehab Ahmedabad, Dr. Nikhil Rajpurohit",
        "intro_text": "Law Garden is the recreational heart of the city, famous for its morning joggers and evening market. But an active lifestyle can sometimes lead to injuries. Dr. Nikhil Rajpurohit is the go-to physiotherapist for the fitness enthusiasts and residents around the Law Garden area.",
        "landmark": "Law Garden & NCC Ground",
        "landmark_text": "Whether you injured your knee jogging at the track or have back pain from long shopping sprees, we are right around the corner. We offer home visits to the apartments surrounding this green lung.",
        "why_choose_text": "Fitness enthusiasts choose Dr. Nikhil because he understands the biomechanics of running and exercise. We help you correct your form and recover without giving up your passion.",
        "common_conditions_text": "Runner's knee, plantar fasciitis (heel pain), and shin splints are very common among our patients from the Law Garden area."
    },
     "Motera": {
        "title": "Physiotherapist in Motera, Ahmedabad – Sports & Spine Specialist",
        "meta_description": "Top Physiotherapist in Motera. Near Narendra Modi Stadium. Expert in sports injuries, back pain, and post-op rehab. Book Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Motera, sports physio Motera, back pain Motera, home visit physiotherapy Motera",
        "intro_text": "Motera is globally known for cricket, but for its residents, it's a rapidly growing community needing top-tier healthcare. Dr. Nikhil Rajpurohit brings specialized sports and spine physiotherapy to Motera, ensuring world-class care is available right next to the world's biggest stadium.",
        "landmark": "Narendra Modi Stadium & Visat",
        "landmark_text": "Serving the vibrant communities from Visat to the Stadium road. We provide elite sports rehabilitation protocols used by professional athletes to the residents of Motera.",
        "why_choose_text": "Dr. Nikhil's expertise in sports injuries makes him the top choice in Motera. Whether you play tennis, cricket, or just want to stay fit, we help you move better and pain-free.",
        "common_conditions_text": "ACL injuries, rotator cuff tears, and tennis elbow are frequently treated here, along with lifestyle-related back pain."
    }
}

# Function to generate pages
def generate_pages():
    # 1. Generate individual area pages
    for area, data in areas_data.items():
        # Create a safe filename
        filename = f"physiotherapist-in-{area.lower().replace(' ', '-').replace('&', 'and')}.html"

        # Fill the template
        page_content = template.format(
            title=data["title"],
            meta_description=data["meta_description"],
            keywords=data["keywords"],
            area_name=area,
            intro_text=data["intro_text"],
            landmark=data["landmark"],
            landmark_text=data["landmark_text"],
            why_choose_text=data["why_choose_text"],
            common_conditions_text=data["common_conditions_text"]
        )

        # Write the file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_content)
        print(f"Generated {filename}")

    # 2. Generate locations.html (Hub Page)
    locations_template_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Find expert physiotherapy services across all major areas of Ahmedabad. Dr. Nikhil Rajpurohit offers home visits and clinic care near you.">
    <meta name="keywords" content="Physiotherapist near me, Physiotherapy locations Ahmedabad, Dr. Nikhil Rajpurohit service areas">
    <title>Areas We Serve - Dr. Nikhil Rajpurohit</title>
    <link rel="icon" type="image/jpeg" href="Public/fevicon.jpeg">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
    <style>
        .locations-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .location-card {
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }
        .location-card:hover {
            transform: translateY(-5px);
        }
        .location-card a {
            text-decoration: none;
            color: #003366;
            font-weight: bold;
            font-size: 1.1rem;
        }
        .location-card i {
            font-size: 2rem;
            color: #00A86B;
            margin-bottom: 15px;
            display: block;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <nav class="navbar">
                <a href="index.html" class="logo"><img src="Public/bgremove_logo.png" alt="Dr. Nikhil Physio Logo"></a>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About Dr. Nikhil</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="locations.html" class="active">Areas We Serve</a></li>
                    <li><a href="contact.html" class="btn btn-primary nav-btn">Book Appointment</a></li>
                </ul>
                <div class="hamburger"><i class="fas fa-bars"></i></div>
            </nav>
        </div>
    </header>

    <section class="page-header section-padding bg-light">
        <div class="container text-center">
            <h1>Areas We Serve in Ahmedabad</h1>
            <p>Bringing World-Class Physiotherapy to Your Doorstep</p>
        </div>
    </section>

    <section class="section-padding">
        <div class="container">
            <div class="locations-grid">
"""

    locations_content = ""
    for area in sorted(areas_data.keys()):
        link = f"physiotherapist-in-{area.lower().replace(' ', '-').replace('&', 'and')}.html"
        locations_content += f"""
                <div class="location-card">
                    <i class="fas fa-map-marker-alt"></i>
                    <a href="{link}">Physiotherapist in {area}</a>
                </div>"""

    locations_template_end = """
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-about">
                    <img src="Public/whitebglogo.jpeg" alt="Dr. Nikhil Physio Logo" class="footer-logo">
                    <p>Providing expert physiotherapy care with a human touch.</p>
                </div>
                <div class="footer-links">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="locations.html">Areas We Serve</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Contact Us</h4>
                    <p><i class="fas fa-map-marker-alt"></i> Ahmedabad, Gujarat, India</p>
                    <p><i class="fas fa-envelope"></i> info@drnikhilphysio.in</p>
                </div>
            </div>
            <div class="footer-bottom text-center">
                <p>&copy; <span id="year"></span> Dr. Nikhil Rajpurohit. All Rights Reserved.</p>
            </div>
        </div>
    </footer>
    <script src="js/main.js"></script>
    <script>document.getElementById('year').textContent = new Date().getFullYear();</script>
</body>
</html>
"""

    with open('locations.html', 'w', encoding='utf-8') as f:
        f.write(locations_template_start + locations_content + locations_template_end)
    print("Generated locations.html")

if __name__ == "__main__":
    generate_pages()
