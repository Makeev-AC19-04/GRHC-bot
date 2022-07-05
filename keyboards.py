###     Все клавиатуры      ###

from telebot import types

# клавиатура главного меню
mainMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(types.KeyboardButton("Вакансии"),
             types.KeyboardButton("Мои резюме"),
             types.KeyboardButton("О компании"),
             types.KeyboardButton("Работа с БД"))

# клавиатура поиска вакансий
vacanciesMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
vacanciesMenu.add(types.KeyboardButton("По моему резюме"),
                 types.KeyboardButton("Поиск"),
                 types.KeyboardButton("Назад"))

# меню резюме
resumeMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
resumeMenu.add(types.KeyboardButton("Мои резюме"),
                types.KeyboardButton("Создать"),
                types.KeyboardButton("Назад"))
# меню о компании
aboutMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
aboutMenu.add(types.KeyboardButton("Общая информация"),
            types.KeyboardButton("Полезные ссылки"),
            types.KeyboardButton("Назад"))

# клавиатура для работы с бд
dbMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
dbMenu.add(types.KeyboardButton("Добавить запись в БД"),
           types.KeyboardButton("Посмотреть записи в БД"),
           types.KeyboardButton("Назад"))
