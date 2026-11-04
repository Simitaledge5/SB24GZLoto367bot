import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Enable logging to see errors in Railway logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello! The Loto bot is running."
    )

if __name__ == '__main__':
    # Railway injects environment variables automatically
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is missing!")

    application = ApplicationBuilder().token(TOKEN).build()

    # Add your commands here (e.g., /start, /loto)
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Start the bot (Long Polling mode)
    print("Bot is starting...")
    application.run_polling()
