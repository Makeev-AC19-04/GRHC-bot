import telebot
from telebot import types

token = '5589670914:AAGZFaTykB0AelTJFO1T0v63WdAlF-ylMt4'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #клавиатура
    item1 = types.KeyboardButton("Привет")
    item2 = types.KeyboardButton("Я повторю любой текст")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, создан помочь найти тебе работу в нашей компании!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_handler(message):
    if message.text.lower()=='привет':
        bot.send_message(message.chat.id, 'хааай')
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
