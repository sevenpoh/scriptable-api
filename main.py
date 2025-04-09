from fastapi import FastAPI
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import asyncio

# Instância do FastAPI
app = FastAPI()

# Token do bot (pegando da variável de ambiente para segurança)
BOT_TOKEN = os.getenv("BOT_TOKEN", "COLOQUE_SEU_TOKEN_AQUI")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Olá {user.first_name}, seja bem-vindo(a) ao bot!")

# Função para rodar o bot do Telegram
async def run_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

# Iniciando o bot com asyncio no FastAPI
@app.on_event("startup")
async def on_startup():
    asyncio.create_task(run_bot())

# Rota teste para garantir que o Render está funcionando
@app.get("/")
def read_root():
    return {"status": "Bot está rodando!"}

# Rodar localmente se for direto no terminal
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
