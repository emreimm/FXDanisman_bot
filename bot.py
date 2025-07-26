import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Buraya senin bot tokenin
TOKEN = "7330074726:AAHbM-uzg6HVpTD49y1lM99DuReJfeo9-eg"

# Loglama ayarları
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# /start komutu
def start(update, context):
    update.message.reply_text("✅ Bot çalışıyor! Buradan mesaj gönderebilirsin.")

# Her mesaja cevap
def echo(update, context):
    update.message.reply_text(f"Mesajını aldım: {update.message.text}")

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
