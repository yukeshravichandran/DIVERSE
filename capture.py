import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 2000})
        try:
            await page.goto('http://localhost:8080', timeout=10000)
            await page.screenshot(path='screenshot.png', full_page=True)
            print("Screenshot saved to screenshot.png")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
