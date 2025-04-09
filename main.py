from fastapi import FastAPI
from playwright.async_api import async_playwright

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API está rodando com sucesso!"}

@app.get("/test-playwright")
async def test_playwright():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto("https://example.com")
            title = await page.title()
            await browser.close()
            return {"status": "ok", "title": title}
    except Exception as e:
        return {"status": "erro", "detalhes": str(e)}
