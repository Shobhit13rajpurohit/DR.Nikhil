from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Ensure verification directory exists
        os.makedirs('/home/jules/verification', exist_ok=True)

        # Verify Index
        page.goto('file:///app/index.html')
        page.screenshot(path='/home/jules/verification/index_page.png', full_page=True)
        print("Captured index.html")

        # Verify About
        page.goto('file:///app/about.html')
        page.screenshot(path='/home/jules/verification/about_page.png', full_page=True)
        print("Captured about.html")

        # Verify Tips (expand details)
        page.goto('file:///app/tips.html')
        # Click the first summary to ensure it's open (though it has 'open' attribute)
        # We can try to click others to expand them too, but full page screenshot might not capture all if they are long.
        # Let's just capture the default state which has the first one open.
        page.screenshot(path='/home/jules/verification/tips_page.png', full_page=True)
        print("Captured tips.html")

        # Verify Contact
        page.goto('file:///app/contact.html')
        page.screenshot(path='/home/jules/verification/contact_page.png', full_page=True)
        print("Captured contact.html")

        browser.close()

if __name__ == "__main__":
    run()
