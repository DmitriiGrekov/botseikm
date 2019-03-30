import telebot
bot = telebot.TeleBot("354151340:AAEnLGjyv9CEl1TAwNkimzOCVsyI-P_2oZM")
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id,"Enter the questions.")
