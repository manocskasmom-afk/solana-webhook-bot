from telegram.ext import Application, CommandHandler

from config.settings import TOKEN
from bot.commands import start, status, ping, help_command


def main():

    if TOKEN is None:
        print("❌ ERROR: Telegram Bot Token not found.")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("help", help_command))

    print("===================================")
    print("🤖 Solana Trading Bot is running...")
    print("Waiting for Telegram messages...")
    print("Press CTRL + C to stop.")
    print("===================================")

    app.run_polling()


if __name__ == "__main__":
    main()