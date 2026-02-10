import os
import datetime

base_url = "https://www.drnikhilphysio.in/"

header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
footer = '</urlset>'

content = ""
today = datetime.date.today().isoformat()

# Get all HTML files
files = [f for f in os.listdir('.') if f.endswith('.html')]

# Ensure index.html is processed correctly if it's in the list
if "index.html" in files:
    # Handle index separately or just map it to root
    pass

for filename in sorted(files):
    # Skip potential google verification files if any
    if filename.startswith("google"):
        continue

    if filename == "index.html":
        url = base_url
        priority = "1.0"
    else:
        url = base_url + filename
        priority = "0.8"

    content += f"""
    <url>
        <loc>{url}</loc>
        <lastmod>{today}</lastmod>
        <priority>{priority}</priority>
    </url>"""

with open("sitemap.xml", "w") as f:
    f.write(header + content + "\n" + footer)

print(f"Generated sitemap.xml with {len(files)} URLs")
