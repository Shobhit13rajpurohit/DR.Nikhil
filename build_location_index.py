import os
import json

# ==========================================
# DATA: Locations
# ==========================================
rajasthan_districts = [
    "Ajmer", "Alwar", "Banswara", "Baran", "Barmer", "Bharatpur", "Bhilwara",
    "Bikaner", "Bundi", "Chittorgarh", "Churu", "Dausa", "Dholpur", "Dungarpur",
    "Hanumangarh", "Jaipur", "Jaisalmer", "Jalore", "Jhalawar", "Jhunjhunu",
    "Jodhpur", "Karauli", "Kota", "Nagaur", "Pali", "Pratapgarh", "Rajsamand",
    "Sawai Madhopur", "Sikar", "Sirohi", "Sri Ganganagar", "Tonk", "Udaipur"
]

bikaner_tehsils = [
    "Nokha", "Kolayat", "Lunkaransar", "Khajuwala", "Sri Dungargarh",
    "Bikaner City", "Pugal", "Chhatargarh", "Bajju"
]

gujarat_districts = [
    "Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar", "Bhavnagar",
    "Jamnagar", "Junagadh", "Anand", "Nadiad", "Mehsana", "Morbi", "Bharuch",
    "Vapi", "Navsari"
]

india_states = [
    "Delhi", "Punjab", "Haryana", "Himachal Pradesh", "Uttarakhand",
    "Jammu & Kashmir", "Ladakh", "Chandigarh", "Rajasthan", "Maharashtra",
    "Goa", "Dadra & Nagar Haveli and Daman & Diu", "Karnataka", "Tamil Nadu",
    "Kerala", "Telangana", "Andhra Pradesh", "Puducherry", "Lakshadweep",
    "Andaman & Nicobar Islands", "West Bengal", "Odisha", "Bihar", "Jharkhand",
    "Madhya Pradesh", "Chhattisgarh", "Assam", "Sikkim", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Tripura", "Arunachal Pradesh",
    "Uttar Pradesh", "Gujarat"
]

def build_index():
    index = []

    # Track existing URLs to avoid duplicates
    existing_urls = set()

    # 1. State Pages (Online)
    for state in india_states:
        slug = state.lower().replace(" & ", "-").replace(" ", "-")
        filename = f"online-physiotherapist-{slug}.html"

        # Check special cases based on generate_india_seo_pages.py
        if state == "Gujarat":
            filename = "best-physiotherapist-gujarat.html"
        elif state == "Dadra & Nagar Haveli and Daman & Diu":
             filename = "online-physiotherapist-daman-diu.html"

        if os.path.exists(filename):
            index.append({
                "name": state,
                "type": "State",
                "url": filename,
                "parent": "India",
                "keywords": [state, "Physiotherapist in " + state]
            })
            existing_urls.add(filename)

    # 2. Gujarat Districts (Online)
    for city in gujarat_districts:
        slug = city.lower().replace(" ", "-")
        filename_online = f"online-physiotherapy-{slug}.html"

        if os.path.exists(filename_online):
            index.append({
                "name": city,
                "type": "City (Online)",
                "url": filename_online,
                "parent": "Gujarat",
                "keywords": [city, "Physiotherapist in " + city, "Online Physio " + city]
            })
            existing_urls.add(filename_online)

    # 3. Rajasthan Districts (Home Visit)
    for district in rajasthan_districts:
        slug = district.lower().replace(" ", "-")
        filename_local = f"physiotherapist-in-{slug}.html"

        if os.path.exists(filename_local):
             index.append({
                "name": district,
                "type": "City (Home Visit)",
                "url": filename_local,
                "parent": "Rajasthan",
                "keywords": [district, "Physiotherapist in " + district]
            })
             existing_urls.add(filename_local)

    # 4. Bikaner Tehsils (Home Visit)
    for tehsil in bikaner_tehsils:
        slug = tehsil.lower().replace(" ", "-")
        filename_local = f"physiotherapist-in-{slug}.html"

        if os.path.exists(filename_local):
             index.append({
                "name": tehsil,
                "type": "Tehsil (Home Visit)",
                "url": filename_local,
                "parent": "Bikaner",
                "keywords": [tehsil, "Physiotherapist in " + tehsil]
            })
             existing_urls.add(filename_local)

    # 5. Scan for other local pages (likely Ahmedabad areas)
    for filename in os.listdir("."):
        if filename.endswith(".html"):
            if filename.startswith("physiotherapist-in-") and filename not in existing_urls:
                # Extract name
                name_part = filename.replace("physiotherapist-in-", "").replace(".html", "")
                name = name_part.replace("-", " ").title()

                # Assume parent is Ahmedabad for leftover files (mostly areas like Navrangpura, etc.)
                parent = "Ahmedabad"

                index.append({
                    "name": name,
                    "type": "Area (Home Visit)",
                    "url": filename,
                    "parent": parent,
                    "keywords": [name, "Physiotherapist in " + name]
                })
                existing_urls.add(filename)

    # Output
    # Ensure js directory exists
    if not os.path.exists("js"):
        os.makedirs("js")

    with open("js/location-index.json", "w") as f:
        json.dump(index, f, indent=4)

    print(f"Index built with {len(index)} entries.")

if __name__ == "__main__":
    build_index()
