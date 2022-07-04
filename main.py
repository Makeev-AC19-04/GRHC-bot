import telebot
from telebot import types
from mysql.connector import  connect, Error

token = '5589670914:AAGZFaTykB0AelTJFO1T0v63WdAlF-ylMt4' #токен бота

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #клавиатура
    btn1 = types.KeyboardButton("Привет")
    btn2 = types.KeyboardButton("Я повторю любой текст") #кнопки клавиатуры
    btn3 = types.KeyboardButton("работа с БД")

    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, создан помочь найти тебе работу в нашей компании!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

addtobd = False

@bot.message_handler(content_types=['text'])
def message_handler(message):
    global addtobd
    if addtobd == True:
        with connect(
                host="localhost",
                user="root",
                password="54321",
        ) as connection:
            addtobdcommand='INSERT INTO botdb.test_table VALUES ("' + str(message.chat.id) + '","' + str(message.text) + '");'
            with connection.cursor() as cursor:
                cursor.execute(addtobdcommand)
                connection.commit()
                bot.send_message(message.chat.id, 'Запись добавлена: ' + addtobdcommand)
                addtobd = False
    else:
        if message.text.lower()=='привет':
            bot.send_message(message.chat.id, 'хааай')
        elif message.text.lower()=='работа с бд':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # клавиатура
            btn1 = types.KeyboardButton("Добавить запись в БД")
            btn2 = types.KeyboardButton("Посмотреть записи в БД")  # кнопки клавиатуры
            btn3 = types.KeyboardButton("Назад")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Что вы хотите сделать?', reply_markup=markup)
        elif message.text.lower() == 'добавить запись в бд':
            addtobd = True
            bot.send_message(message.chat.id, 'Напишите сообщение для записи в бд')
        elif message.text.lower() == 'посмотреть записи в бд':
            with connect(
                    host="localhost",
                    user="root",
                    password="54321",
            ) as connection:
                DBdata = 'select * from botdb.test_table;'
                msgtext = ''
                with connection.cursor() as cursor:
                    cursor.execute(DBdata)
                    #msgtext+=cursor;
                    #for row in result:
                    #    msgtext+=row[1]
                    for i in cursor:
                        msgtext += 'id: ' + str(i[0]) + ' text: ' + str(i[1]) + '\n'
                    bot.send_message(message.chat.id, msgtext)
        elif message.text.lower() == 'назад':
            welcome(message)
        else:
            bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
