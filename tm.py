import telebot
import sqlite3
bot = telebot.TeleBot("354151340:AAEnLGjyv9CEl1TAwNkimzOCVsyI-P_2oZM")

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id,"Введите вопрос. ")
@bot.message_handler(content_types=["text"])
def repeat_allconn_messages(message): # Название функции не играет никакой роли, в принципе
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM albums WHERE question=?"
    for row in cursor.execute(sql,([message.text.upper()])):
            bot.send_message(message.chat.id,"Ваш ответ - "+row[-1])
    
    bot.send_message(message.chat.id,"Введите вопрос. ")
      
if __name__ == "__main__":
    
    bot.polling()
