import telebot
bot=telebot.TeleBot("354151340:AAEnLGjyv9CEl1TAwNkimzOCVsyI-P_2oZM")
f = open('text.txt','r',encoding='latin-1')
keys={}
for line in f:
    arr=line.split("$$")
    keys[arr[0]]=arr[-1]
    
@bot.message_handler(commands=["start"])
def send_message2(message):
    bot.send_message(message.chat.id,"Введите вопрос")

@bot.message_handler(content_types=["text"])
def mes_handler(message):
    global keys
    for i in keys.keys():
        questions=message.chat.id
        if questions == i:
            bot.send_message(message.chat.id,"Ваш ответ - %s"%( keys[i]))
        else:
            bot.send_message(message.chat.id,'Вопрос не найден')
            
    
    
