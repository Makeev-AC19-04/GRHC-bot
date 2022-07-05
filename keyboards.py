###     Все клавиатуры      ###

from telebot import types

# главное меню
mainMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(types.KeyboardButton("Вакансии"),
             types.KeyboardButton("Мои резюме"),
             types.KeyboardButton("О компании"))

# меню поиска вакансий
vacanciesMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
vacanciesMenu.add(types.KeyboardButton("По моему резюме"),
                  types.KeyboardButton("Фильтры"),
                  types.KeyboardButton("Все"),
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

# меню поиска по вакансиям
searchByResumeMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
searchByResumeMenu.add(types.KeyboardButton("Назад"))

# меню поиска вакансий по фильтрам
filtersMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
filtersMenu.add(types.KeyboardButton("Ключевые слова"),
               types.KeyboardButton("Специальности"),
               types.KeyboardButton("График"),
               types.KeyboardButton("З/П"),
               types.KeyboardButton("Занятость"),
               types.KeyboardButton("Опыт работы"),
                types.KeyboardButton("Назад"),
                )

# меню создания резюме
createResumeMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
createResumeMenu.add(types.KeyboardButton("Имя"),
               types.KeyboardButton("Специальность"),
               types.KeyboardButton("Желаемая З/П"),
               types.KeyboardButton("Навыки"),
               types.KeyboardButton("Личные качества"),
                types.KeyboardButton("Дополнительно"),
                types.KeyboardButton("Прикрепить фото"),
                types.KeyboardButton("Назад")
                )

# клавиатура для работы с бд
dbMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
dbMenu.add(types.KeyboardButton("Добавить запись в БД"),
           types.KeyboardButton("Посмотреть записи в БД"),
           types.KeyboardButton("Назад"))
