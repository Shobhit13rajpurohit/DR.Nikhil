document.addEventListener('DOMContentLoaded', async () => {
    // Inject CSS for our component
    const style = document.createElement('style');
    style.textContent = `
        .il-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }
        .il-btn {
            display: block;
            padding: 10px 15px;
            background: #fff;
            border: 1px solid #eee;
            border-radius: 8px;
            text-align: center;
            color: #003366;
            text-decoration: none;
            transition: all 0.2s;
            font-size: 0.9rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        .il-btn:hover {
            background: #f0f8ff;
            border-color: #00A86B;
            transform: translateY(-2px);
            box-shadow: 0 5px 10px rgba(0,0,0,0.1);
        }
        .il-section {
            margin-bottom: 30px;
        }
        .il-title {
            color: #003366;
            font-size: 1.25rem;
            margin-bottom: 15px;
            font-weight: 700;
            border-bottom: 2px solid #00A86B;
            display: inline-block;
            padding-bottom: 5px;
        }
        .il-container {
            padding: 30px;
            background: #f8f9fa;
            border-radius: 12px;
            margin-top: 50px;
            border: 1px solid #e9ecef;
        }
        @media (max-width: 768px) {
            .il-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    `;
    document.head.appendChild(style);

    const container = document.getElementById('nearby-locations');
    if (!container) return;

    // Add container class if not present
    container.classList.add('il-container');

    try {
        const response = await fetch('js/location-index.json');
        if (!response.ok) throw new Error('Failed to load location index');
        const locations = await response.json();

        // 1. Identify Current Page
        const currentPath = window.location.pathname.split('/').pop() || 'index.html';
        const currentLocation = locations.find(loc => loc.url === currentPath);

        let html = '';

        if (!currentLocation) {
            // Check for special data attribute on body (e.g. for India page)
            const specialLoc = document.body.getAttribute('data-location');
            if (specialLoc === 'India') {
                 renderIndiaLinks(locations, container);
                 return;
            }
             // If generic page and not India page, maybe we are on locations.html or similar?
             // If container exists but no location match, fallback to "Explore Popular"
             if (container.id === 'nearby-locations') {
                 // Optional: Render something generic
             }
             return;
        }

        const { name, parent, type } = currentLocation;

        // 2. Find Related Locations
        // Children: Locations where parent is this location
        const children = locations.filter(loc => loc.parent === name);

        // Siblings: Locations where parent is same as this location's parent
        // Exclude self.
        const siblings = locations.filter(loc => loc.parent === parent && loc.name !== name);

        // Parent Object
        const parentLoc = locations.find(loc => loc.name === parent);


        // Section: Specific Areas in {Name} (Children) - e.g. Areas in Ahmedabad
        if (children.length > 0) {
            html += `
                <div class="il-section">
                    <h3 class="il-title">Locations in ${name}</h3>
                    <div class="il-grid">
                        ${children.map(loc => `
                            <a href="${loc.url}" class="il-btn">
                                <i class="fas fa-map-pin" style="color: #00A86B;"></i> ${loc.name}
                            </a>
                        `).join('')}
                    </div>
                </div>
            `;
        }

        // Section: Nearby Areas (Siblings) - e.g. Other districts in Rajasthan
        if (siblings.length > 0) {
            // Pick random 12 to avoid overcrowding
            const shuffledSiblings = siblings.sort(() => 0.5 - Math.random()).slice(0, 12);
            html += `
                <div class="il-section">
                    <h3 class="il-title">Nearby Areas in ${parent}</h3>
                    <div class="il-grid">
                        ${shuffledSiblings.map(loc => `
                            <a href="${loc.url}" class="il-btn">
                                ${loc.name}
                            </a>
                        `).join('')}
                    </div>
                    ${siblings.length > 12 ? `<p style="text-align:center; margin-top:15px;"><a href="locations.html" style="color:#003366; font-weight:600; text-decoration: underline;">View all ${siblings.length} locations</a></p>` : ''}
                </div>
            `;
        }

        // Section: Back to Parent
        html += `<div style="text-align: center; margin-top: 30px; display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">`;

        if (parentLoc) {
             html += `
                <a href="${parentLoc.url}" class="btn btn-primary">
                    <i class="fas fa-arrow-up"></i> Go to ${parent}
                </a>
            `;
        }

        html += `
            <a href="locations.html" class="btn btn-secondary">
                <i class="fas fa-search"></i> Search All Locations
            </a>
        </div>`;

        container.innerHTML = html;

    } catch (error) {
        console.error('Error loading internal links:', error);
    }
});

function renderIndiaLinks(locations, container) {
    const states = locations.filter(loc => loc.type === 'State');
    const shuffled = states.sort(() => 0.5 - Math.random()).slice(0, 12);

    container.innerHTML = `
        <div class="il-section" style="text-align:center;">
            <h3 class="il-title">Our Presence Across India</h3>
            <p style="margin-bottom: 20px;">We offer specialized online physiotherapy consultations in these states:</p>
            <div class="il-grid">
                 ${shuffled.map(loc => `
                    <a href="${loc.url}" class="il-btn">
                        ${loc.name}
                    </a>
                `).join('')}
            </div>
            <div style="margin-top: 30px;">
                <a href="locations.html" class="btn btn-primary pulse-btn">Find Your City</a>
            </div>
        </div>
    `;
}
