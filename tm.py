import telebot
bot=telebot.TeleBot("354151340:AAEnLGjyv9CEl1TAwNkimzOCVsyI-P_2oZM")

    
@bot.message_handler(commands=["start"])
def send_message2(message):
    bot.send_message(message.chat.id,"Введите вопрос")

@bot.message_handler(content_types=["text"])
def mes_handler(message):
    with open('out.txt','rb') as inp:
        d_in = pickle.load(inp)
    print(d_in)

    for i in d_in.keys():
        questions=message.chat.id
        if questions == i:
            bot.send_message(message.chat.id,"Ваш ответ - %s"%( keys[i]))
        else:
            bot.send_message(message.chat.id,'Вопрос не найден')
            
    
    
