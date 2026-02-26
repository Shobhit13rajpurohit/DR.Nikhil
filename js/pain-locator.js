document.addEventListener('DOMContentLoaded', () => {
    const painPoints = document.querySelectorAll('.pain-point');
    const detailsPanel = document.getElementById('pain-details');

    // Data for each body part
    const conditions = {
        neck: {
            title: "Neck Pain & Stiffness",
            symptoms: "Stiffness looking down/up, headaches, radiating pain to arms.",
            causes: "Cervical Spondylosis, Text Neck, Whiplash.",
            solution: "Manual Therapy, Posture Correction, Strengthening.",
            link: "services.html#neck"
        },
        shoulder: {
            title: "Shoulder Pain",
            symptoms: "Limited movement, sharp pain when lifting arm, night pain.",
            causes: "Rotator Cuff Tears, Frozen Shoulder, Impingement.",
            solution: "Mobilization, rotator cuff strengthening, electrotherapy.",
            link: "services.html#shoulder"
        },
        back: {
            title: "Back Pain (Lower/Upper)",
            symptoms: "Sharp shooting pain (Sciatica), stiffness in morning, trouble bending.",
            causes: "Herniated Disc, Muscle Strain, Poor Posture.",
            solution: "Core strengthening, McKenzie method, ergonomic advice.",
            link: "services.html#back"
        },
        knee: {
            title: "Knee Pain",
            symptoms: "Clicking sound, swelling, instability, pain on stairs.",
            causes: "ACL/MCL Injury, Osteoarthritis, Runner's Knee.",
            solution: "Post-op Rehab, quad strengthening, taping.",
            link: "services.html#knee"
        },
        ankle: {
            title: "Ankle & Foot Pain",
            symptoms: "Heel pain in morning, swelling after twisting, instability.",
            causes: "Ankle Sprains, Plantar Fasciitis, Achilles Tendonitis.",
            solution: "Balance training, soft tissue release, orthotics advice.",
            link: "services.html#ankle"
        }
    };

    // Add click listeners
    painPoints.forEach(point => {
        point.addEventListener('click', (e) => {
            // Remove active class from all points
            painPoints.forEach(p => p.classList.remove('active'));

            // Add active class to clicked point
            e.currentTarget.classList.add('active');

            // Get data key
            const part = e.currentTarget.getAttribute('data-part');
            const data = conditions[part];

            if (data) {
                // Update Details Panel with animation
                detailsPanel.style.opacity = '0';
                detailsPanel.style.transform = 'translateY(10px)';

                setTimeout(() => {
                    detailsPanel.innerHTML = `
                        <h3>${data.title}</h3>
                        <div class="detail-group">
                            <strong><i class="fas fa-notes-medical"></i> Symptoms:</strong>
                            <p>${data.symptoms}</p>
                        </div>
                        <div class="detail-group">
                            <strong><i class="fas fa-search-plus"></i> Common Causes:</strong>
                            <p>${data.causes}</p>
                        </div>
                        <div class="detail-group">
                            <strong><i class="fas fa-user-md"></i> How We Help:</strong>
                            <p>${data.solution}</p>
                        </div>
                        <a href="contact.html" class="btn btn-primary mt-3">Book for ${data.title.split(' ')[0]} <i class="fas fa-arrow-right"></i></a>
                    `;

                    // Fade in
                    detailsPanel.style.opacity = '1';
                    detailsPanel.style.transform = 'translateY(0)';
                }, 300);

                // Scroll to details on mobile if needed
                if (window.innerWidth < 768) {
                    detailsPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    });
});
