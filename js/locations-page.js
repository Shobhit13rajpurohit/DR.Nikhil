document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Map
    // Center on Ahmedabad by default
    const map = L.map('map').setView([23.0225, 72.5714], 12);

    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 20
    }).addTo(map);

    // 2. Data
    const data = window.locationsData || {};
    // Hardcoded list of online cities based on generate_seo_pages.py
    const onlineCities = [
        "Surat", "Vadodara", "Rajkot", "Gandhinagar", "Bhavnagar", "Jamnagar",
        "Junagadh", "Anand", "Nadiad", "Mehsana", "Morbi", "Bharuch", "Vapi", "Navsari"
    ];

    const listContainer = document.getElementById('locationsList');
    const searchInput = document.getElementById('locationSearch');
    const markers = {};

    // Create Markers initially but don't add to map yet? Or add all?
    // Let's create them and store them.
    Object.keys(data).forEach(key => {
        const loc = data[key];
        if (loc.coordinates) {
            const link = `physiotherapist-in-${key.toLowerCase().replace(/ /g, '-').replace('&', 'and')}.html`;
            const marker = L.marker(loc.coordinates);
            marker.bindPopup(`
                <div style="text-align: center;">
                    <h4 style="margin: 0; color: #003366;">${key}</h4>
                    <span style="display: inline-block; background: #d4edda; color: #155724; padding: 2px 6px; border-radius: 4px; font-size: 10px; margin: 5px 0;">Home Visit Available</span><br>
                    <a href="${link}" style="color: #00A86B; font-weight: bold; text-decoration: none;">View Details</a>
                </div>
            `);

            marker.on('click', () => {
                highlightListItem(key);
            });

            markers[key] = marker;
        }
    });

    function highlightListItem(key) {
        // Only if item is in the current filtered list
        const item = document.querySelector(`.location-item[data-key="${key}"]`);
        if (item) {
            document.querySelectorAll('.location-item').forEach(i => i.classList.remove('active'));
            item.classList.add('active');
            item.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    // 3. Render List & Update Map
    function renderList(filterText = '') {
        listContainer.innerHTML = '';
        let matchCount = 0;
        const normalizedFilter = filterText.toLowerCase().trim();

        // Clear all markers first
        Object.values(markers).forEach(marker => map.removeLayer(marker));

        // 3a. Home Visit Matches
        Object.keys(data).sort().forEach(key => {
            const loc = data[key];

            if (normalizedFilter && !key.toLowerCase().includes(normalizedFilter)) {
                return; // Skip if filtered out
            }
            matchCount++;

            // Add marker back to map
            if (markers[key]) {
                markers[key].addTo(map);
            }

            const li = document.createElement('li');
            li.className = 'location-item';
            li.dataset.key = key; // For reverse lookup
            li.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                    <h4 style="margin:0; font-size: 1rem;">${key}</h4>
                    <i class="fas fa-chevron-right" style="color: #ccc; font-size: 0.8rem;"></i>
                </div>
                <span class="status-badge status-home"><i class="fas fa-home"></i> Home Visit Available</span>
            `;

            li.addEventListener('click', () => {
                if (markers[key]) {
                    map.setView(markers[key].getLatLng(), 15);
                    markers[key].openPopup();
                }
                // Highlight
                document.querySelectorAll('.location-item').forEach(i => i.classList.remove('active'));
                li.classList.add('active');
            });

            listContainer.appendChild(li);
        });

        // 3b. Online Consultation Matches (if search is active)
        if (normalizedFilter) {
            onlineCities.forEach(city => {
                if (city.toLowerCase().includes(normalizedFilter)) {
                    matchCount++;
                    const li = document.createElement('li');
                    li.className = 'location-item';
                    li.innerHTML = `
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                            <h4 style="margin:0; font-size: 1rem;">${city}</h4>
                        </div>
                        <span class="status-badge status-online"><i class="fas fa-laptop-medical"></i> Online Consultation</span>
                    `;
                    // Redirect to generic or specific online page
                    const onlineLink = `online-physiotherapy-${city.toLowerCase()}.html`;
                    li.addEventListener('click', () => {
                        window.location.href = onlineLink;
                    });
                    listContainer.appendChild(li);
                }
            });
        }

        // 3c. No Match -> Coming Soon
        if (matchCount === 0 && normalizedFilter) {
             const li = document.createElement('li');
             li.className = 'location-item';
             li.style.cursor = 'default';
             li.innerHTML = `
                <h4 style="color: #666; margin-bottom: 5px;">${filterText}</h4>
                <span class="status-badge status-soon"><i class="fas fa-clock"></i> Coming Soon</span>
                <p style="font-size: 0.85rem; margin-top: 10px; color: #555;">
                    We don't have home visits in this area yet, but you can join our waiting list or book an online consultation.
                </p>
                <div style="margin-top: 10px;">
                    <a href="contact.html" class="btn btn-sm btn-primary" style="font-size: 0.8rem;">Notify Me</a>
                    <a href="contact.html" class="btn btn-sm btn-outline-primary" style="font-size: 0.8rem; margin-left: 5px;">Book Online</a>
                </div>
            `;
            listContainer.appendChild(li);
        } else if (matchCount === 0 && !normalizedFilter) {
             // Should not happen if data is present, but just in case
        }
    }

    // Initial Render
    renderList();

    // 4. Search Listener
    searchInput.addEventListener('input', (e) => {
        renderList(e.target.value);
    });
});
