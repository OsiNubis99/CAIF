# Imorts
from config.Env import TOKEN, URL, PORT
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# SetUp
updater = Updater(TOKEN)
bot = updater.dispatcher
if URL != "localhost":
	updater.start_webhook(
		listen="0.0.0.0",
		port=PORT,
		url_path=TOKEN,
		webhook_url= URL + "/" + TOKEN
	)

# Triggers
def start(update: Update, context: CallbackContext) -> None:
	update.message.reply_text(f'Hello {update.effective_user.first_name}')
def sayHi(update: Update, context: CallbackContext) -> None:
	update.message.reply_text(f'Hello {update.effective_user.first_name}')

bot.add_handler(CommandHandler('saluda', sayHi))
bot.add_handler(CommandHandler('start', start))
bot.add_handler(CommandHandler('help', start))

# Start the Bot
updater.start_polling()
print(" * Bot Running")
