from fastapi import FastAPI
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
import os

# Ativa logs
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Inicia FastAPI
app = FastAPI()

# Token do seu bot
BOT_TOKEN = os.getenv("BOT_TOKEN", "SEU_TOKEN_AQUI")

# Inicia o bot
bot_app = Application.builder().token(BOT_TOKEN).build()

# Comando /start
async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Bem-vindo(a) ao bot!")

bot_app.add_handler(CommandHandler("start", start))

# Inicializa o bot com FastAPI
@app.on_event("startup")
async def startup():
    bot_app.create_task(bot_app.run_polling())

# Rota raiz só pra teste
@app.get("/")
def read_root():
    return {"status": "ok"}

# Para deploy local (Render)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
