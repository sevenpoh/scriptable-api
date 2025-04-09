from fastapi import FastAPI, Request
from playwright.async_api import async_playwright
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "API Online"}

@app.post("/testar")
async def testar_cartao(request: Request):
    data = await request.json()
    numero = data.get("numero")
    validade = data.get("validade")
    cvv = data.get("cvv")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.guariguari.com/carrinho/pagamento")

        await page.fill('[name="cardNumber"]', numero)
        await page.fill('[name="cardExpiry"]', validade)
        await page.fill('[name="cardCVC"]', cvv)
        await page.wait_for_timeout(3000)

        content = await page.content()
        await browser.close()
        return {"resultado": "Testado", "html": content}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)