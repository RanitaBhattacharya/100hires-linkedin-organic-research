from playwright.sync_api import sync_playwright

profiles = [
    "https://www.linkedin.com/in/justinwelsh/",
    "https://www.linkedin.com/in/amandanat/",
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    for profile in profiles:
        page.goto(profile)
        print(profile)

    browser.close()