import telebot
from mysql.connector import connect, Error

import keyboards
from keyboards import *

token = '5589670914:AAGZFaTykB0AelTJFO1T0v63WdAlF-ylMt4' #токен бота
bot = telebot.TeleBot(token)

class Response: # Класс посылаемого ботом сообщения
    def __init__(self, text, keyboard, upperLayer, func):
        self.text = text  # Определяем текст сообщения
        self.keyboard = keyboard # Загружаем нужную клавиатуру
        self.upperLayer = upperLayer # Предыдущий пункт меню
        self.func = func

class SearchFilters: # Класс для хранения параметров поиска
    def __init__(self):
        self.keywords = []
        isSearching = False
        enteringKeywords = False
        pass
    def setKeywords(self, keywords):
        self.keywords = keywords

class CurrentMenu():
    def __init__(self):
        self.key = 'главное меню'
currentMenu = CurrentMenu()

searchFilters=SearchFilters()

def Pass(key): # Функция смены меню
    global currentMenu
    if key == 'назад':
        currentMenu.key = menuResponses[currentMenu.key].upperLayer
    else:
        currentMenu.key=key

mainMenuResponse = Response('Главное меню', keyboards.mainMenu, None, Pass) # Ответы бота
vacanciesResponse = Response('Поиск вакансий: ', keyboards.vacanciesMenu, 'главное меню', Pass)
resumeResponse = Response('Меню резюме', keyboards.resumeMenu, 'главное меню', Pass)
aboutResponse = Response('Информация о компании: ', keyboards.aboutMenu, 'главное меню', Pass)
searchByResumeResponse = Response('Выберите резюме: ', keyboards.searchByResumeMenu, 'вакансии', Pass)
filtersReponse = Response('Фильтры: ', keyboards.filtersMenu, 'вакансии', Pass)
createResumeResponse = Response('Заполнение резюме', keyboards.createResumeMenu, 'мои резюме', Pass)
keywordsResponse = Response('Введите ключевые слова для поиска', None, 'мои резюме', Pass)
backResponse = Response('Назад', None, None, Pass)

menuResponses = { #Словарь ответов
    'главное меню': mainMenuResponse,
        'вакансии': vacanciesResponse,
            'по моему резюме': searchByResumeResponse,
            'фильтры': filtersReponse,
                'ключевые слова': keywordsResponse,
        'мои резюме': resumeResponse,
            'создать': createResumeResponse,
        'о компании': aboutResponse,
    'назад': backResponse
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

@bot.message_handler(content_types=['text'])
def message_handler(message):
    global currentMenu
    key = message.text.lower()
    if key in menuResponses: # Если сообщение содержит ключ из словаря ответов, то отправляем ответ, соответствующий ключу
        menuResponses[currentMenu.key].func(key)
        bot.send_message(message.chat.id, menuResponses[currentMenu.key].text, reply_markup=menuResponses[currentMenu.key].keyboard)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял, введи /menu чтобы вернуться в главное меню')


bot.polling(none_stop=True) # Непрерывно проверяем новые сообщения
