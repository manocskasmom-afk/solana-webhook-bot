from telegram import Update
from telegram.ext import ContextTypes
from config.settings import AUTO_TRADING

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Hello! Your Solana Trading Bot is online."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):

    trading_status = "ON" if AUTO_TRADING else "OFF"

    await update.message.reply_text(
        f"🟢 Status: ONLINE\n"
        f"🤖 Auto Trading: {trading_status}"
    )

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available Commands:\n\n"
        "/start\n"
        "/status\n"
        "/ping\n"
        "/help"
    )
