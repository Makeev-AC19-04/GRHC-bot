import telebot
from mysql.connector import  connect, Error

import keyboards
from keyboards import *

token = '5589670914:AAGZFaTykB0AelTJFO1T0v63WdAlF-ylMt4' #токен бота
bot = telebot.TeleBot(token)

class Response: # Класс посылаемого ботом сообщения
    def __init__(self, text, keyboard, upperLayer):
        self.text = text  # Определяем текст сообщения
        self.keyboard = keyboard # Загружаем нужную клавиатуру
        self.upperLayer = upperLayer # Предыдущий пункт меню

menuResponse = Response('Главное меню', keyboards.mainMenu, None) # Ответы бота
vacanciesResponse = Response('Поиск вакансий: ', keyboards.vacanciesMenu, 'главное меню')
resumeResponse = Response('Меню резюме', keyboards.resumeMenu, 'главное меню')
aboutResponse = Response('Информация о компании: ', keyboards.aboutMenu, 'главное меню')
searchByResumeResponse = Response('Выберите резюме: ', keyboards.searchByResumeMenu, 'вакансии')
filtersReponse = Response('Фильтры: ', keyboards.filtersMenu, 'вакансии')
createResumeResponse = Response('Заполнение резюме', keyboards.createResumeMenu, 'мои резюме')

responses = { #Словарь ответов
    'главное меню': menuResponse,
        'вакансии': vacanciesResponse,
            'по моему резюме': searchByResumeResponse,
            'фильтры': filtersReponse,
        'мои резюме': resumeResponse,
            'создать': createResumeResponse,
        'о компании': aboutResponse
}

def DBadd(message):
    with connect(
            host="localhost",
            user="root",
            password="54321",
    ) as connection:
        addtobdcommand = 'INSERT INTO botdb.test_table VALUES ("' + str(message.chat.id) + '","' + str(message.text) + '");'
        with connection.cursor() as cursor:
            cursor.execute(addtobdcommand)
            connection.commit() # Подтверждение изменений в БД
            bot.send_message(message.chat.id, 'Запись добавлена: ' + addtobdcommand)

def DBread(message):
    with connect(
            host="localhost",
            user="root",
            password="54321",
    ) as connection:
        DBdata = 'select * from botdb.test_table;'
        msgtext = ''
        with connection.cursor() as cursor:
            cursor.execute(DBdata)
            for i in cursor:
                msgtext += 'id: ' + str(i[0]) + ' text: ' + str(i[1]) + '\n'
            bot.send_message(message.chat.id, msgtext)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, создан помочь найти тебе работу в нашей компании!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=mainMenu)

@bot.message_handler(commands=['menu'])
def LoadMenu(message):
    bot.send_message(message.chat.id, 'Главное меню', reply_markup=mainMenu)

currentMenu='' # Переменная, отвечающая за выбор нужной клавиатуры

@bot.message_handler(content_types=['text'])
def message_handler(message):
    global currentMenu
    key = message.text.lower()
    if key == 'назад':
        currentMenu = responses[currentMenu].upperLayer
        bot.send_message(message.chat.id,  responses[currentMenu].text, reply_markup=responses[currentMenu].keyboard)
    elif key in responses: # Если сообщение содержит ключ из словаря ответов, то отправляем ответ, соответствующий ключу
        currentMenu = key
        bot.send_message(message.chat.id, responses[currentMenu].text, reply_markup=responses[key].keyboard)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял, введи /menu чтобы вернуться в главное меню')


bot.polling(none_stop=True) # Непрерывно проверяем новые сообщения
