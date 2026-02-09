import os

# HTML Template for Online Consultation Pages
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
        .online-hero {{
            background: linear-gradient(rgba(0, 51, 102, 0.9), rgba(0, 168, 107, 0.8)), url('Public/hero-bg.jpg'); /* distinct from local pages */
            background-size: cover;
            background-position: center;
            color: white;
            padding: 120px 0;
            text-align: center;
        }}
        .online-hero h1 {{
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }}
        .content-section {{
            padding: 60px 0;
        }}
        .content-section h2 {{
            color: #003366;
            margin-bottom: 25px;
            font-weight: 700;
        }}
        .content-section p {{
            font-size: 1.1rem;
            line-height: 1.8;
            color: #333;
            margin-bottom: 20px;
        }}
        .feature-box {{
            background: #f8f9fa;
            padding: 30px;
            border-radius: 8px;
            border-left: 5px solid #00A86B;
            margin-bottom: 30px;
            transition: transform 0.3s;
        }}
        .feature-box:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }}
        .feature-box h3 {{
            color: #003366;
            margin-bottom: 15px;
        }}
        .cta-box {{
            background: linear-gradient(135deg, #003366, #0055a5);
            color: white;
            padding: 40px;
            border-radius: 10px;
            text-align: center;
            margin-top: 40px;
        }}
        .cta-box h2 {{
            color: white;
        }}
        .btn-cta {{
            background-color: #FFC107;
            color: #003366;
            font-weight: bold;
            padding: 15px 30px;
            border-radius: 30px;
            text-decoration: none;
            display: inline-block;
            margin-top: 20px;
            transition: background 0.3s;
        }}
        .btn-cta:hover {{
            background-color: #ffca2c;
            color: #002244;
        }}
        ul.check-list li {{
            margin-bottom: 10px;
            font-size: 1.1rem;
        }}
        ul.check-list i {{
            color: #00A86B;
            margin-right: 10px;
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
    <section class="online-hero">
        <div class="container">
            <h1>{h1}</h1>
            <p class="lead">Expert Pain Relief & Virtual Rehabilitation across {location}</p>
            <div class="mt-4">
                <a href="contact.html" class="btn btn-cta">Book Online Consultation</a>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <section class="content-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-10 mx-auto">

                    <!-- Introduction -->
                    <h2>World-Class Physiotherapy, Now in {location}</h2>
                    <p>{intro_content}</p>

                    <!-- Why Online -->
                    <div class="feature-box">
                        <h3>Why Choose Online Physiotherapy in {location}?</h3>
                        <p>{why_online_content}</p>
                    </div>

                    <!-- Common Problems -->
                    <h2>Common Pain & Lifestyle Issues in {location}</h2>
                    <p>{problems_content}</p>
                    <ul class="check-list">
                        <li><i class="fas fa-check-circle"></i> <strong>Chronic Back Pain:</strong> Often caused by long commutes or sedentary desk jobs.</li>
                        <li><i class="fas fa-check-circle"></i> <strong>Neck & Shoulder Strain:</strong> Common in tech and diamond industry professionals.</li>
                        <li><i class="fas fa-check-circle"></i> <strong>Knee & Joint Pain:</strong> Affecting our seniors who want to stay active.</li>
                        <li><i class="fas fa-check-circle"></i> <strong>Sports Injuries:</strong> For the active youth and weekend athletes.</li>
                    </ul>

                    <!-- Target Audience -->
                    <h2 class="mt-5">Who Should Opt for Virtual Sessions?</h2>
                    <p>{audience_content}</p>

                    <!-- Approach -->
                    <h2>Dr. Nikhil Rajpurohit's Treatment Approach</h2>
                    <p>{approach_content}</p>

                    <!-- Technology -->
                    <div class="row mt-4">
                        <div class="col-md-6">
                            <h3><i class="fas fa-laptop-medical"></i> Advanced Tele-Rehab</h3>
                            <p>{tech_content}</p>
                        </div>
                        <div class="col-md-6">
                            <h3><i class="fas fa-user-md"></i> Expert Guidance</h3>
                            <p>{benefits_content}</p>
                        </div>
                    </div>

                    <!-- Trust & Outcomes -->
                    <h2 class="mt-5">Trusted by Patients Across Gujarat</h2>
                    <p>{trust_content}</p>

                    <!-- CTA -->
                    <div class="cta-box">
                        <h2>Start Your Recovery Today</h2>
                        <p>Don't let distance or traffic stop you from getting the best care. Experience professional physiotherapy from the comfort of your home in {location}.</p>
                        <a href="contact.html" class="btn btn-cta">Schedule Your Video Assessment</a>
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
                        <li><a href="tips.html">Tips & Exercises</a></li>
                        <li><a href="testimonials.html">Testimonials</a></li>
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
                    <p><strong>Dr. Nikhil Rajpurohit (PT)</strong></p>
                    <p>B.P.T, GPC-21467</p>
                    <p>Consultant Physiotherapist</p>
                    <p><i class="fas fa-map-marker-alt"></i> 233/1/B Mukhivas, Jehangirpura, Ahmedabad 380016</p>
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

# Common Content Blocks
common_approach = "Dr. Nikhil Rajpurohit follows a strict evidence-based protocol. Unlike generic advice found online, your session begins with a detailed assessment of your movement, pain history, and lifestyle factors. We use visual aids and real-time demonstrations to ensure you perform exercises correctly. The focus is not just on temporary relief, but on correcting the root cause—whether it's posture, muscle imbalance, or post-surgical stiffness."

common_tech = "We utilize high-definition video calls to conduct thorough assessments. You don't need expensive equipment; a smartphone or laptop is enough. We guide you through self-assessment tests that are clinically validated for remote diagnosis. Exercise plans are shared digitally with videos, so you never forget a step."

common_benefits = "Why visit a local clinic when you can consult a top-tier specialist from home? Local clinics often juggle multiple patients at once. In our online sessions, you get 100% dedicated one-on-one attention. We empower you to manage your condition independently, saving you time and travel costs while delivering superior outcomes."

common_trust = "With years of experience treating patients across Gujarat and internationally, Dr. Nikhil Rajpurohit has built a reputation for honesty and results. Patients from remote villages to bustling cities like Surat and Vadodara have found relief through our guided online programs. We prioritize your recovery goals, whether it's returning to work, playing sports, or simply walking without pain."

# Data Dictionary for Pages
pages_data = {
    "Gujarat": {
        "filename": "best-physiotherapist-gujarat.html",
        "title": "Best Physiotherapist in Gujarat – Online Consultation by Dr. Nikhil Rajpurohit",
        "h1": "Best Online Physiotherapist in Gujarat",
        "meta_description": "Leading Physiotherapist in Gujarat offering expert online consultations. Dr. Nikhil Rajpurohit provides specialized care for back pain, joint issues & post-op rehab across the state.",
        "keywords": "Best physiotherapist in Gujarat, Online physiotherapy consultation Gujarat, Virtual physiotherapy sessions Gujarat, Physiotherapy doctor in Gujarat, remote physical therapy",
        "intro_content": "Gujarat is a state of diverse landscapes and vibrant cultures, from the white deserts of Kutch to the lush greenery of the Dangs. However, access to specialized physiotherapy care is often concentrated in major cities. Residents in smaller towns or remote areas frequently struggle to find expert guidance for complex musculoskeletal issues. Dr. Nikhil Rajpurohit bridges this gap by bringing top-tier physiotherapy services to every corner of Gujarat through advanced online consultations.",
        "why_online_content": "For many in Gujarat, visiting a specialist means travelling hundreds of kilometers to Ahmedabad or Surat. This travel can worsen back pain and consume valuable time. Online physiotherapy eliminates these barriers. Whether you are a business owner in Rajkot unable to leave your shop or an elderly patient in a remote village, virtual sessions ensure you receive the same high-quality care as a patient in our Ahmedabad clinic. It’s convenient, cost-effective, and highly effective.",
        "problems_content": "Across Gujarat, we see a rise in lifestyle-related ailments. The entrepreneurial spirit of the state often leads to long working hours and high stress, resulting in chronic neck and back pain. In agricultural belts, repetitive strain injuries are common. Furthermore, the prevalence of diabetes and hypertension in the region complicates recovery from joint pains, requiring a specialized, holistic approach that Dr. Nikhil provides.",
        "audience_content": "Our online services are perfect for busy professionals, homemakers with tight schedules, and seniors who find travel difficult. It is also ideal for NRIs from Gujarat visiting home who need continuity of care, or residents in towns with limited medical infrastructure. If you have internet access, you have access to the best physiotherapy care in the state."
    },
    "Ahmedabad": {
        "filename": "online-physiotherapy-ahmedabad.html",
        "title": "Online Physiotherapy in Ahmedabad – Dr. Nikhil Rajpurohit",
        "h1": "Expert Online Physiotherapy in Ahmedabad",
        "meta_description": "Best Online Physiotherapist in Ahmedabad. Skip the traffic and get expert care for back pain, neck pain, and sports injuries from home. Dr. Nikhil Rajpurohit.",
        "keywords": "Online physiotherapy Ahmedabad, virtual physio Ahmedabad, best physiotherapist Ahmedabad online, remote rehab Ahmedabad",
        "intro_content": "Ahmedabad is a bustling metropolis, but its rapid growth has brought traffic congestion and a fast-paced lifestyle that leaves little time for self-care. While Dr. Nikhil Rajpurohit offers home visits in specific areas, our online consultation service is designed for those across the city who want immediate expert advice without the commute. We bring the clinic to your living room, ensuring your recovery fits seamlessly into your busy schedule.",
        "why_online_content": "Even within Ahmedabad, travelling from Bopal to Maninagar for a therapy session can take over an hour. Why spend time in traffic when you can spend it healing? Online physiotherapy allows you to connect with Dr. Nikhil instantly. It is particularly beneficial for corporate employees in SG Highway or Prahlad Nagar who can schedule sessions during lunch breaks or after work hours without leaving their office or home.",
        "problems_content": "The 'Amadavadi' lifestyle, often involving long hours of sitting for business or work, contributes significantly to posture-related issues like 'Text Neck' and lower back pain. We also see a high number of knee issues among the elderly population residing in flats without elevators. Our online guidance helps you modify your home and work environment to support your recovery.",
        "audience_content": "Ideal for IT professionals, business owners, and students preparing for exams who cannot afford to waste time. It is also excellent for post-operative patients who have been discharged from hospitals in Ahmedabad and need guided rehabilitation while recovering at home."
    },
    "Surat": {
        "filename": "online-physiotherapy-surat.html",
        "title": "Best Physiotherapist in Surat – Online Consultation",
        "h1": "Top-Rated Online Physiotherapy for Surat",
        "meta_description": "Expert Physiotherapist for Surat residents. Online consultation for diamond & textile workers, joint pain, and lifestyle injuries. Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Surat, Online physiotherapy Surat, best physio Surat, back pain treatment Surat, virtual doctor Surat",
        "intro_content": "Surat, the Diamond City, is known for its industrious people and vibrant food culture. However, the intense work culture in the textile and diamond industries often takes a toll on physical health. Dr. Nikhil Rajpurohit offers specialized online physiotherapy services tailored to the unique needs of Suratis, ensuring that you can continue your work and life without pain.",
        "why_online_content": "Surat is a fast-moving city. Taking time off work for daily clinic visits is often not an option for business owners and workers. Online physiotherapy offers the flexibility you need. We provide concise, effective exercise protocols that can be performed at your workplace or home, minimizing downtime. Dr. Nikhil's expertise is now accessible to every household in Adajan, Varachha, and beyond.",
        "problems_content": "We frequently treat 'Diamond Polisher’s Neck' and lower back pain among textile traders who sit for long hours. The food-loving culture also sometimes contributes to weight-related joint stress. Our online plans include lifestyle and ergonomic advice specifically designed for the Surat community to manage these issues effectively.",
        "audience_content": "This service is a boon for the busy diamond merchants, textile workers, and the active youth of Surat. It is also highly beneficial for homemakers who manage large joint families and often neglect their own health due to lack of time."
    },
    "Vadodara": {
        "filename": "online-physiotherapy-vadodara.html",
        "title": "Physiotherapist in Vadodara – Online & Virtual Rehab",
        "h1": "Expert Online Physiotherapy in Vadodara",
        "meta_description": "Best Physiotherapist for Vadodara. Online sessions for students, professionals, and seniors. Treat back pain & sports injuries from home with Dr. Nikhil.",
        "keywords": "Physiotherapist in Vadodara, Online physio Vadodara, sports injury Vadodara, back pain doctor Vadodara, virtual rehab",
        "intro_content": "Vadodara, the cultural capital of Gujarat, is home to a mix of heavy industries, educational institutions, and a rich heritage. Whether you are a student at MSU or an engineer in the industrial belt, health issues can arise. Dr. Nikhil Rajpurohit brings world-class physiotherapy to Vadodara via secure online platforms, ensuring that high-quality care is never far away.",
        "why_online_content": "For residents in Alkapuri, Manjalpur, or the outskirts near the industrial zones, finding a specialized physiotherapist nearby can be challenging. Online consultation bridges this gap. It provides access to Dr. Nikhil’s specialized musculoskeletal expertise without the need to travel, making it perfect for the culturally active and industrially busy population of Baroda.",
        "problems_content": "Vadodara's population faces a mix of industrial occupational hazards (like repetitive strain injuries) and student-related posture issues. We also see a significant number of geriatric patients needing support for osteoarthritis and balance issues. Our virtual sessions are adapted to address these specific demographic needs.",
        "audience_content": "Perfect for university students, industrial employees working shifts, and senior citizens who prefer the safety and comfort of their homes. We also support artists and performers in the city who face unique physical strains."
    },
    "Rajkot": {
        "filename": "online-physiotherapy-rajkot.html",
        "title": "Best Physiotherapist in Rajkot – Online Consultation",
        "h1": "Online Physiotherapy Services for Rajkot",
        "meta_description": "Top Physiotherapist for Rajkot. Online treatment for engineering workers, business owners, and seniors. Pain relief & rehab by Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Rajkot, Online physiotherapy Rajkot, joint pain Rajkot, sciatica treatment Rajkot, virtual doctor",
        "intro_content": "Rajkot is the engine of Saurashtra, famous for its engineering, casting, and jewelry industries. The hardworking people of Rajkot often ignore early signs of pain until it becomes severe. Dr. Nikhil Rajpurohit offers accessible online physiotherapy to the people of Rajkot, focusing on quick recovery and long-term prevention so you can keep the engines running.",
        "why_online_content": "In a busy industrial hub like Rajkot, time is money. Driving through traffic on 150 Feet Ring Road or Kalavad Road for therapy can be draining. Our virtual physiotherapy sessions respect your time. Get assessed, learn your exercises, and get back to your business. We bring the expertise of a top Ahmedabad physio directly to your screen in Rajkot.",
        "problems_content": "Heavy lifting injuries, lower back pain from standing in foundry units, and cervical spondylosis are rampant in Rajkot. We also treat many cases of knee pain in the elderly who enjoy their evening walks but suffer from arthritis. Our online guidance focuses on ergonomic corrections for factory owners and workers alike.",
        "audience_content": "Tailored for the industrial workforce, busy SME owners, and the large joint families where specialized care for the elderly is a priority. We provide clear, no-nonsense medical advice that the practical people of Rajkot appreciate."
    },
    "Gandhinagar": {
        "filename": "online-physiotherapy-gandhinagar.html",
        "title": "Physiotherapist in Gandhinagar – Online Consultation",
        "h1": "Premier Online Physiotherapy in Gandhinagar",
        "meta_description": "Best Physiotherapist for Gandhinagar. Online care for government employees, IT professionals & seniors. Expert neck & back pain relief by Dr. Nikhil.",
        "keywords": "Physiotherapist in Gandhinagar, Online physio Gandhinagar, neck pain treatment Gandhinagar, posture correction, Dr. Nikhil Rajpurohit",
        "intro_content": "Gandhinagar, the green capital, is a city of government officials, IT professionals, and peaceful residential sectors. The serene life here is sometimes disrupted by lifestyle diseases associated with desk jobs. Dr. Nikhil Rajpurohit provides specialized online physiotherapy consultations for Gandhinagar residents, ensuring you stay as fit and green as your city.",
        "why_online_content": "While Gandhinagar has wide roads, specialized healthcare often requires a trip to Ahmedabad. Why make that commute? Our online service brings the specialist to you. Whether you are in Sargasan, Raysan, or Sector 21, you can access expert advice for your aches and pains without leaving your sector.",
        "problems_content": "We see a high incidence of 'Desk Neck' and lower back pain among the secretariat staff and Infocity employees. Morning walkers in the city's many parks often report heel pain (plantar fasciitis) and knee issues. Our virtual rehab programs address these specific sedentary and active lifestyle clashes.",
        "audience_content": "Ideal for government employees with fixed schedules, IT professionals in Infocity, and retired seniors settled in the capital. We offer evening and weekend slots to suit your routine."
    },
    "Bhavnagar": {
        "filename": "online-physiotherapy-bhavnagar.html",
        "title": "Best Physiotherapist in Bhavnagar – Online Care",
        "h1": "Online Physiotherapy for Bhavnagar Residents",
        "meta_description": "Expert Physiotherapy for Bhavnagar. Online consultation for joint pain, diabetes-related stiffness, and post-op rehab. Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Bhavnagar, Online physiotherapy Bhavnagar, frozen shoulder Bhavnagar, diabetes physio, virtual clinic",
        "intro_content": "Bhavnagar, a city of culture, education, and trade, is known for its warm hospitality. However, residents often face challenges in accessing advanced physiotherapy techniques. Dr. Nikhil Rajpurohit extends his expert services to Bhavnagar through online platforms, ensuring that distance is no barrier to quality healthcare.",
        "why_online_content": "Residents of Bhavnagar no longer need to travel to larger metros for second opinions or specialized rehab. With our online consultation, you get a detailed assessment and a personalized recovery plan right at home. It is particularly useful for managing chronic conditions where regular monitoring is needed but daily clinic visits are impractical.",
        "problems_content": "Frozen shoulder and diabetic stiff hand syndrome are conditions we frequently encounter in patients from Bhavnagar, often linked to the high prevalence of diabetes in the region. We also treat back pain in traders and businessmen. Our online holistic approach integrates diet advice and exercise for better results.",
        "audience_content": "Great for the business community, educators, and the elderly population who cherish their independence. We provide easy-to-follow video instructions that can be done in the comfort of your home."
    },
    "Jamnagar": {
        "filename": "online-physiotherapy-jamnagar.html",
        "title": "Physiotherapist in Jamnagar – Online Consultation",
        "h1": "Expert Online Physiotherapy in Jamnagar",
        "meta_description": "Top Physiotherapist for Jamnagar. Online sessions for refinery workers, defense personnel & families. Treat pain effectively with Dr. Nikhil.",
        "keywords": "Physiotherapist in Jamnagar, Online physio Jamnagar, refinery injury rehab, back pain Jamnagar, Dr. Nikhil Rajpurohit",
        "intro_content": "Jamnagar, the Jewel of Kathiawar, is a unique blend of historical richness and modern industry, housing massive refineries and defense establishments. The diverse population here has diverse medical needs. Dr. Nikhil Rajpurohit brings specialized, evidence-based physiotherapy to Jamnagar via online consultations, serving both the civilian and industrial sectors.",
        "why_online_content": "For those working in the refinery townships or living in the old city, accessing specialized care can be time-consuming. Online physiotherapy offers a direct line to an expert. We understand the demanding schedules of industrial shifts and defense duties, offering flexible consultation times to fit your life.",
        "problems_content": "We often treat industrial fatigue injuries, lower back strain from heavy machinery operation, and lifestyle diseases in the affluent merchant community. Joint pain in seniors is also a major focus. Our virtual sessions emphasize strength and conditioning to prevent recurrence.",
        "audience_content": "Ideal for refinery employees, defense families, and local business owners. We provide a private, professional, and effective way to manage pain without disrupting your work or duties."
    },
    "Junagadh": {
        "filename": "online-physiotherapy-junagadh.html",
        "title": "Best Physiotherapist in Junagadh – Online Rehab",
        "h1": "Online Physiotherapy Services for Junagadh",
        "meta_description": "Physiotherapy for Junagadh. Online consultation for knee pain, trekking injuries, and back pain. Expert care by Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Junagadh, Online physiotherapy Junagadh, knee pain treatment, Girnar trekking injury, virtual doctor",
        "intro_content": "Junagadh, lying at the foot of the sacred Girnar, is a city steeped in history and spirituality. The terrain and lifestyle here are unique. Dr. Nikhil Rajpurohit offers dedicated online physiotherapy services to the people of Junagadh, helping them maintain the mobility needed to navigate their hilly and historic city.",
        "why_online_content": "Accessing specialized physiotherapy in Junagadh can sometimes be difficult. Our online service connects you with Dr. Nikhil, a leading expert, ensuring you get the best advice without travelling. Whether you are recovering from a pilgrimage strain or managing age-related arthritis, expert help is just a video call away.",
        "problems_content": "Knee pain is a primary complaint here, often exacerbated by the uneven terrain and the climbing of Girnar steps. We also treat back pain in the agricultural community surrounding the city. Our online plans focus heavily on knee strengthening and balance training.",
        "audience_content": "Perfect for the elderly devotees, agricultural workers, and the tourism-focused residents of Junagadh. We help you stay active so you can continue to serve and explore your beautiful city."
    },
    "Anand": {
        "filename": "online-physiotherapy-anand.html",
        "title": "Physiotherapist in Anand – Online Consultation",
        "h1": "Top Online Physiotherapy in Anand",
        "meta_description": "Best Physiotherapist for Anand & Vidhyanagar. Online care for students, dairy farmers & NRIs. Specialized pain relief by Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Anand, Online physio Anand, Vidhyanagar physiotherapy, NRI health services Gujarat, Dr. Nikhil Rajpurohit",
        "intro_content": "Anand, the Milk Capital of India, is a thriving hub of education and agriculture. With a significant NRI population and a large student base in Vidhyanagar, the demand for quality healthcare is high. Dr. Nikhil Rajpurohit delivers premium online physiotherapy services to Anand, meeting international standards of care.",
        "why_online_content": "Anand's residents are globally connected and value efficiency. Online physiotherapy fits perfectly with this mindset. It saves travel time and provides high-quality documentation and video guidance that appeals to the educated demographic. For NRIs visiting home, it ensures continuity of care even after they return abroad.",
        "problems_content": "We treat a mix of agricultural injuries (shoulder and back strain) and student-related posture issues. The NRI population often seeks help for chronic conditions accumulated over years of hard work abroad. We provide comprehensive, long-term management strategies.",
        "audience_content": "Tailored for the student community, dairy industry professionals, and NRI families. We offer consultations that bridge the gap between local needs and global healthcare standards."
    },
    "Nadiad": {
        "filename": "online-physiotherapy-nadiad.html",
        "title": "Physiotherapist in Nadiad – Online Consultation",
        "h1": "Expert Online Physiotherapy for Nadiad",
        "meta_description": "Physiotherapy for Nadiad. Online sessions for back pain, joint health, and post-surgery recovery. Trusted care by Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Nadiad, Online physiotherapy Nadiad, spine care Nadiad, virtual rehab Nadiad, Dr. Nikhil Rajpurohit",
        "intro_content": "Nadiad is a city of distinct character, known for its educational institutions and religious significance. As a key stop in Central Gujarat, it is a bustling center where health often takes a backseat. Dr. Nikhil Rajpurohit brings focused online physiotherapy services to Nadiad, making it easier for residents to prioritize their physical well-being.",
        "why_online_content": "For patients in Nadiad, finding specialized care often means travelling to Ahmedabad or Vadodara. Our online consultation service brings that expertise directly to your home. It empowers you to manage your pain and recovery without the stress of inter-city travel, providing a comfortable and effective healing environment.",
        "problems_content": "Common issues in Nadiad include geriatric joint pain (osteoarthritis) and lower back pain among the trading community. We also see sports injuries from the active youth in local colleges. Our virtual programs are designed to be simple, effective, and easy to integrate into daily life.",
        "audience_content": "Ideal for the senior citizens of Nadiad who prefer home care, as well as students and traders. We provide clear guidance and support, ensuring you feel cared for at every step."
    },
    "Mehsana": {
        "filename": "online-physiotherapy-mehsana.html",
        "title": "Best Physiotherapist in Mehsana – Online Care",
        "h1": "Online Physiotherapy Services in Mehsana",
        "meta_description": "Top Physiotherapist for Mehsana. Online consultation for back pain, knee pain, and water park injuries. Expert rehab by Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Mehsana, Online physio Mehsana, knee replacement rehab, back pain doctor Mehsana, virtual clinic",
        "intro_content": "Mehsana is a key economic hub in North Gujarat, known for its dairy, oil, and education. The industrious nature of its people drives the city forward. Dr. Nikhil Rajpurohit supports the hardworking residents of Mehsana with top-tier online physiotherapy, ensuring that physical pain doesn't slow down their progress.",
        "why_online_content": "Mehsana is growing fast, but specialized medical services are still centralized. Online physiotherapy gives you access to Ahmedabad's top physiotherapist without the travel. Whether you are in the city center or a nearby village, expert care is now accessible via your smartphone.",
        "problems_content": "We frequently treat knee pain and back pain associated with long hours of travel and agricultural management. We also see cases related to water park mishaps! Our online rehab focuses on functional recovery, helping you get back to your daily tasks quickly.",
        "audience_content": "Designed for the busy business owners, farmers managing large operations, and families who want the best care without travelling. We speak your language and understand your needs."
    },
    "Morbi": {
        "filename": "online-physiotherapy-morbi.html",
        "title": "Physiotherapist in Morbi – Online Consultation",
        "h1": "Expert Online Physiotherapy for Morbi",
        "meta_description": "Best Physiotherapist for Morbi. Online care for ceramic industry workers & business owners. Treat back & neck pain with Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Morbi, Online physiotherapy Morbi, ceramic industry health, back pain treatment Morbi, Dr. Nikhil Rajpurohit",
        "intro_content": "Morbi is the ceramic capital of India, a city that never sleeps. The intense industrial activity brings wealth but also physical strain. Dr. Nikhil Rajpurohit offers specialized online physiotherapy to the people of Morbi, understanding the unique occupational health challenges of the ceramic region.",
        "why_online_content": "In a city driven by production targets, taking time off for therapy is difficult. Online consultation is the solution. It allows factory owners and workers to get expert advice and exercise plans that can be done on-site or at home. We help you manage pain efficiently so you can focus on your business.",
        "problems_content": "Respiratory issues aside, the ceramic industry workforce suffers heavily from lower back pain, sciatica, and shoulder strain due to lifting and monitoring production lines. We provide targeted ergonomic advice and strengthening exercises to combat these industrial hazards.",
        "audience_content": "Essential for factory owners, managers, and workers in the ceramic hub. We provide no-nonsense, effective treatments that respect your time and keep your workforce healthy."
    },
    "Bharuch": {
        "filename": "online-physiotherapy-bharuch.html",
        "title": "Best Physiotherapist in Bharuch – Online Rehab",
        "h1": "Online Physiotherapy Services in Bharuch",
        "meta_description": "Top Physiotherapist for Bharuch & Ankleshwar. Online consultation for industrial injuries & chemical plant workers. Expert care by Dr. Nikhil.",
        "keywords": "Physiotherapist in Bharuch, Online physio Bharuch, Ankleshwar physiotherapy, industrial rehab Gujarat, Dr. Nikhil Rajpurohit",
        "intro_content": "Bharuch, the oldest city of Gujarat, is now a major industrial belt alongside Ankleshwar. The chemical and petrochemical industries here define the lifestyle. Dr. Nikhil Rajpurohit brings specialized occupational health and physiotherapy services to Bharuch via online platforms, serving the backbone of Gujarat's industry.",
        "why_online_content": "For professionals in the GNFC township or Ankleshwar GIDC, specialized physio care can be hard to find locally. Online consultation provides a bridge to expert care. We offer flexible timings to suit shift workers and professionals, ensuring you get the right care at the right time.",
        "problems_content": "Occupational overuse syndromes, chemical exposure-related fatigue, and standard desk-job ailments are common here. We also treat many cases of Ankylosing Spondylitis and chronic back pain in the region. Our online approach focuses on posture correction and core strengthening.",
        "audience_content": "Tailored for industrial professionals, engineers, and their families. We offer a scientific approach to pain management that appeals to the technical mindset of Bharuch's residents."
    },
    "Vapi": {
        "filename": "online-physiotherapy-vapi.html",
        "title": "Physiotherapist in Vapi – Online Consultation",
        "h1": "Expert Online Physiotherapy in Vapi",
        "meta_description": "Best Physiotherapist for Vapi. Online care for industrial workers & Valsad residents. Treat back pain & joint issues with Dr. Nikhil Rajpurohit.",
        "keywords": "Physiotherapist in Vapi, Online physiotherapy Vapi, Valsad physio, industrial health Vapi, virtual doctor",
        "intro_content": "Vapi, the Gateway of Gujarat, is a powerhouse of industry and trade. The fast-paced life here often leads to neglect of personal health. Dr. Nikhil Rajpurohit offers premier online physiotherapy services to Vapi, ensuring that the city's industrious population has access to top-quality pain relief and rehabilitation.",
        "why_online_content": "Vapi's connectivity is great, but traffic and work pressure often prevent regular clinic visits. Online physiotherapy solves this by bringing the clinic to you. Whether you are in the GIDC or the residential areas, Dr. Nikhil’s expert guidance is available at your fingertips, saving you hours of commute time.",
        "problems_content": "We see a high volume of lumbar spondylosis and repetitive strain injuries from the manufacturing sector. Stress-related muscle tension is also common. Our online sessions provide quick, effective relief strategies that can be implemented immediately.",
        "audience_content": "Ideal for the busy industrial workforce, business travelers, and families in Vapi and Valsad. We help you stay pain-free and productive with minimal disruption to your schedule."
    },
    "Navsari": {
        "filename": "online-physiotherapy-navsari.html",
        "title": "Best Physiotherapist in Navsari – Online Care",
        "h1": "Online Physiotherapy Services for Navsari",
        "meta_description": "Top Physiotherapist for Navsari. Online consultation for Parsi community & seniors. Gentle, expert care for arthritis & back pain by Dr. Nikhil.",
        "keywords": "Physiotherapist in Navsari, Online physio Navsari, geriatric care Navsari, arthritis treatment, Dr. Nikhil Rajpurohit",
        "intro_content": "Navsari, with its rich Parsi heritage and calm atmosphere, is a wonderful place to live. However, the aging population here requires specialized geriatric care. Dr. Nikhil Rajpurohit extends his compassionate, expert physiotherapy services to Navsari through online consultations, ensuring seniors get the care they deserve.",
        "why_online_content": "Travel can be physically taxing for the elderly. Online physiotherapy brings the doctor to the patient. For the residents of Navsari, this means accessing specialized arthritis and mobility care without the need to travel to Surat or Mumbai. It is safe, convenient, and highly personalized.",
        "problems_content": "Osteoarthritis, balance disorders, and post-fall recovery are the primary concerns we address in Navsari. We also manage chronic back pain and general frailty. Our online programs are gentle, focusing on maintaining independence and quality of life.",
        "audience_content": "Specially designed for the senior citizens and the peace-loving residents of Navsari. We provide patient, detailed, and respectful care that aligns with the values of the community."
    }
}

def generate_pages():
    for location, data in pages_data.items():
        # Fill the template
        page_content = template.format(
            title=data["title"],
            h1=data["h1"],
            meta_description=data["meta_description"],
            keywords=data["keywords"],
            location=location,
            intro_content=data["intro_content"],
            why_online_content=data["why_online_content"],
            problems_content=data["problems_content"],
            audience_content=data["audience_content"],
            approach_content=common_approach,
            tech_content=common_tech,
            benefits_content=common_benefits,
            trust_content=common_trust
        )

        # Write the file
        filename = data["filename"]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    generate_pages()
