import asyncio
from playwright.async_api import async_playwright

FOLDER_URL = "https://gofile.io/d/eSHaJU"  # Change this to your GoFile folder

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(FOLDER_URL)
        print("Page title:", await page.title())
        links = await page.eval_on_selector_all(
            'a[href*="/d/"]', 'elements => elements.map(e => e.href)'
        )
        print(f"Found {len(links)} download links")
        for link in links:
            print("Downloading:", link)
            await page.goto(link)
            await page.wait_for_timeout(2000)  # simulate stay
        await browser.close()

asyncio.run(run())