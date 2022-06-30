import telebot

token = '5589670914:AAGZFaTykB0AelTJFO1T0v63WdAlF-ylMt4' #git  сheck

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def message_handler(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)