document.addEventListener('DOMContentLoaded', async () => {
    // 1. Initialize Map
    // Default center India
    const map = L.map('map').setView([20.5937, 78.9629], 5);
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 20
    }).addTo(map);

    const listContainer = document.getElementById('locationsList');
    const searchInput = document.getElementById('locationSearch');
    const markers = {};

    // 2. Fetch Index
    let searchIndex = [];
    try {
        const response = await fetch('js/location-index.json');
        if (!response.ok) throw new Error('Failed to load index');
        searchIndex = await response.json();
    } catch (e) {
        console.error(e);
        listContainer.innerHTML = '<li class="location-item" style="padding:15px; color:red;">Error loading locations. Please try again later.</li>';
        return;
    }

    // 3. Merge with local map data (if available in global scope from locations.html)
    const localData = window.locationsData || {};

    // Add markers for items that have coords in localData
    searchIndex.forEach(item => {
        // Try to find matching key in localData
        // localData keys are like "Bopal", "Satellite", etc.
        const local = localData[item.name];

        if (local && local.coordinates) {
            item.coordinates = local.coordinates;
            // Create marker
            const marker = L.marker(local.coordinates);
            marker.bindPopup(`
                <div style="text-align: center;">
                    <h5 style="margin: 0; color: #003366; font-family: 'Montserrat', sans-serif;">${item.name}</h5>
                    <span style="display: inline-block; background: #d4edda; color: #155724; padding: 2px 6px; border-radius: 4px; font-size: 10px; margin: 5px 0;">Home Visit Available</span><br>
                    <a href="${item.url}" style="color: #00A86B; font-weight: bold; text-decoration: none; font-size: 0.9rem;">View Page</a>
                </div>
            `);
            marker.on('click', () => {
                // Optional: Scroll list to item
            });
            markers[item.name] = marker;
            item.marker = marker;
        }
    });

    // 4. Render List Function
    function renderList(filterText = '') {
        listContainer.innerHTML = '';
        const normalizedFilter = filterText.toLowerCase().trim();
        let matchCount = 0;

        // Clear all markers from map first
        Object.values(markers).forEach(m => map.removeLayer(m));

        // Filter items
        const matches = searchIndex.filter(item => {
            if (!normalizedFilter) return true;
            // Search in name and keywords
            const inName = item.name.toLowerCase().includes(normalizedFilter);
            const inKeywords = item.keywords && item.keywords.some(k => k.toLowerCase().includes(normalizedFilter));
            return inName || inKeywords;
        });

        // Sort: Exact matches first, then starts with, then contains
        matches.sort((a, b) => {
             const aName = a.name.toLowerCase();
             const bName = b.name.toLowerCase();
             if (aName === normalizedFilter) return -1;
             if (bName === normalizedFilter) return 1;
             if (aName.startsWith(normalizedFilter) && !bName.startsWith(normalizedFilter)) return -1;
             if (bName.startsWith(normalizedFilter) && !aName.startsWith(normalizedFilter)) return 1;
             return 0;
        });

        // Determine what to display
        // If no filter, show States and Ahmedabad locations (as "Featured") to avoid 100+ items list
        let displayItems = matches;
        if (!normalizedFilter) {
            displayItems = matches.filter(i => i.type === 'State' || i.parent === 'Ahmedabad');
        }

        displayItems.forEach(item => {
            matchCount++;

            // Add marker to map if displayed and exists
            if (item.marker) {
                item.marker.addTo(map);
            }

            const li = document.createElement('li');
            li.className = 'location-item';

            // Determine badge style
            let badgeClass = 'status-online';
            let badgeText = 'Online Consultation';
            let icon = 'fa-laptop-medical';

            if (item.type.includes('Home Visit') || item.type.includes('Clinic')) {
                badgeClass = 'status-home';
                badgeText = 'Home Visit Available';
                icon = 'fa-home';
            } else if (item.type === 'State') {
                badgeClass = 'status-online';
                badgeText = 'Statewide Service';
                icon = 'fa-map';
            }

            li.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                    <h4 style="margin:0; font-size: 1rem;">${item.name}</h4>
                    <i class="fas fa-chevron-right" style="color: #ccc; font-size: 0.8rem;"></i>
                </div>
                <div style="display:flex; justify-content: space-between; align-items: center;">
                    <span class="status-badge ${badgeClass}"><i class="fas ${icon}"></i> ${badgeText}</span>
                    <small style="color: #888;">${item.parent}</small>
                </div>
            `;

            li.addEventListener('click', () => {
                if (item.coordinates) {
                    map.setView(item.coordinates, 15);
                    item.marker.openPopup();
                }
                // Redirect logic
                window.location.href = item.url;
            });

            listContainer.appendChild(li);
        });

        // No Match -> Coming Soon
        if (matchCount === 0 && normalizedFilter) {
             const li = document.createElement('li');
             li.className = 'location-item';
             li.style.cursor = 'default';
             li.innerHTML = `
                <h4 style="color: #666; margin-bottom: 5px;">${filterText}</h4>
                <span class="status-badge status-soon"><i class="fas fa-clock"></i> Coming Soon</span>
                <p style="font-size: 0.85rem; margin-top: 10px; color: #555;">
                    We are expanding! Join our waiting list or book an online consultation.
                </p>
                <div style="margin-top: 10px;">
                    <a href="contact.html" class="btn btn-sm btn-primary" style="font-size: 0.8rem;">Request Service</a>
                </div>
            `;
            listContainer.appendChild(li);
        }
    }

    // Initial Render
    renderList();

    // Search Listener
    searchInput.addEventListener('input', (e) => {
        renderList(e.target.value);
    });
});
