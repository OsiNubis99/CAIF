from env import token
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

updater = Updater(token)
bot = updater.dispatcher

# if (env.node_env == "production") bot.setWebHook(`${env.url}/bot${env.token}`);

# bot.onText(/\/saluda(.*)/, (msg, match) => {
# 	let chatId = msg.chat.id;
# 	let resp =
# 		"Hola " +
# 		(msg.from.username ? "@" + msg.from.username : msg.from.first_name) +
# 		(match[1] ? "\nTu mensaje fue: " + match[1] : "");
# 	bot.sendMessage(chatId, resp);
# });

def version(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def sayHi(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

bot.add_handler(CommandHandler('version', version))

bot.add_handler(CommandHandler('start', sayHi))

bot.add_handler(CommandHandler('help', sayHi))

updater.start_polling()

print(" * Bot Running")
