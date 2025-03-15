from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7849280605:AAHvsAGaGFJoz-KSNk1-ppqi-_NpAIRd4Bc"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! मैं आपका Telegram बॉट हूँ।")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
