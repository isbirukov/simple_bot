from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from api_key import API_KEY

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='bot.log')

def greet_user(update, context):
    #context.bot.send_message(chat_id=update.effective_chat.id, text = "Hi")
    update.message.reply_text('What???')

def talk_to_me(update, context):
    user_text = 'Привет {}! Ты написал {}'.format(update.message.chat.first_name, update.message.text)
    print(user_text)
    update.message.reply_text(user_text)

    

def main():
    mybot = Updater(API_KEY)
    mybot.start_polling()
    #mybot.idle()

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    



main()
