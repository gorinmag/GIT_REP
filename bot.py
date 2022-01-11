import MM
import descrb
import mvision
import report
import tbsb
import telebot
import wenco

import config

from telebot import types

# Ключ для данного борта
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/geo.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # Основное меню, кнопки выбора темы
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Описание месторождения Наталка")
    item2 = types.KeyboardButton("Работа с MineVision")
    item3 = types.KeyboardButton("Работа с ПО Micromine")
    item4 = types.KeyboardButton("Работа с Wenco")
    item5 = types.KeyboardButton("Составление сводок и расчетов")
    item6 = types.KeyboardButton("Необходимые знания о ТБ и СБ")
    # Добавление кнопок
    markup.add(item1, item2, item3, item4, item5, item6)
    # Приветствие
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный в помощь геологам. "
                     "Тут ты найдешь короткую информацию по месторождению Наталкинское. "
                     "В данный момент я нахожусь в процессе разработки, "
                     "надеюсь что в скором будующем я буду умнее".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id,
                     "Выбери необходимый раздел в контекстном меню".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# Определение структуры информационного бота
@bot.message_handler(content_types=['text'])
def bot_body(message):
    if message.chat.type == 'private':
        if message.text == "Описание месторождения Наталка":
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1_1 = types.InlineKeyboardButton("Расположение", callback_data='1-1')
            item1_2 = types.InlineKeyboardButton("Литология", callback_data='1-2')
            item1_3 = types.InlineKeyboardButton("Тектоника", callback_data='1-3')
            item1_4 = types.InlineKeyboardButton("Магматизм", callback_data='1-4')
            item1_5 = types.InlineKeyboardButton("Околорудные изменения", callback_data='1-5')
            item1_6 = types.InlineKeyboardButton("Морфология рудных тел", callback_data='1-6')
            item1_7 = types.InlineKeyboardButton("Минеральный состав руды", callback_data='1-7')
            markup.add(item1_1, item1_2, item1_3, item1_4, item1_5, item1_6, item1_7)
            bot.send_message(message.chat.id, 'Выбери интересующий раздел', reply_markup=markup)

        elif message.text == 'Работа с MineVision':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item2_1 = types.InlineKeyboardButton("Печать бирок", callback_data='2-1')
            item2_2 = types.InlineKeyboardButton("Создание наряд-заказа", callback_data='2-2')
            item2_3 = types.InlineKeyboardButton("Добавление контрольных проб в реестр", callback_data='2-3')
            item2_4 = types.InlineKeyboardButton("Создание реестра горстьевых проб", callback_data='2-4')
            item2_5 = types.InlineKeyboardButton("Получение действующей топоповерхности", callback_data='2-5')

            markup.add(item2_1, item2_2, item2_3, item2_4, item2_5)

            bot.send_message(message.chat.id, 'MineVision это база данных завернутая в интеративную оболочку. '
                                              'Ниже можете выбрать инетересующее действие', reply_markup=markup)
        elif message.text == 'Работа с ПО Micromine':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item3_1 = types.InlineKeyboardButton("Работа со скважинами", callback_data='3-1')
            item3_2 = types.InlineKeyboardButton("Работа с 3-D поверхностями", callback_data='3-2')
            item3_3 = types.InlineKeyboardButton("Работа с блочными моделями", callback_data='3-3')
            item3_4 = types.InlineKeyboardButton("Работа с макросами", callback_data='3-4')
            item3_5 = types.InlineKeyboardButton("Дополнительные функции", callback_data='3-5')

            markup.add(item3_1, item3_2, item3_3, item3_4, item3_5)
            bot.send_message(message.chat.id, 'Micromine - это ПО предназначеное для геологов, горных-инженеров и '
                                              'маркшейдеров. Данное ПО имеет огромные возможности для режения задач '
                                              'связанных с горной промышенность, однако нельзя забывать что это '
                                              'всего лишь инструмент', reply_markup=markup)
        elif message.text == 'Работа с Wenco':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item4_1 = types.InlineKeyboardButton("Интерфейс и взаимодействие FleetControl", callback_data='4-1')
            item4_2 = types.InlineKeyboardButton("Создание и загрузка файлов в BenchView", callback_data='4-2')
            item4_3 = types.InlineKeyboardButton("Подробные параметры работы техники BenchView", callback_data='4-3')
            item4_4 = types.InlineKeyboardButton("Просмотр точек копания", callback_data='4-4')
            item4_5 = types.InlineKeyboardButton("Активация загрузочных блоков в Wenco", callback_data='4-5')

            markup.add(item4_1, item4_2, item4_3, item4_4, item4_5)

            bot.send_message(message.chat.id, 'Wenco - это система диспечеризации и база данных, '
                                              'она позволяет вести максимальный контроль за рабочей техникой в '
                                              'карьере', reply_markup=markup)
        elif message.text == 'Составление сводок и расчетов':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item5_1 = types.InlineKeyboardButton("Создание суточной совдки рудного контроля", callback_data='5-1')
            item5_2 = types.InlineKeyboardButton("Определение содержания в подаче на ЗИФ", callback_data='5-2')
            item5_3 = types.InlineKeyboardButton("Создание блочной модели по скважинам СЭР", callback_data='5-3')
            item5_4 = types.InlineKeyboardButton("Расчет ежемесячного соспоставления", callback_data='5-4')
            item5_5 = types.InlineKeyboardButton("Выгрузки из ИТС", callback_data='5-5')
            markup.add(item5_1, item5_2, item5_3, item5_4, item5_5)

            bot.send_message(message.chat.id, 'В этом разделе находятся подсказки для выполнения следующих '
                                              'работ', reply_markup=markup)
        elif message.text == 'Необходимые знания о ТБ и СБ':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item6_1 = types.InlineKeyboardButton("Что нельзя завозить на рудник", callback_data='6-1')
            item6_2 = types.InlineKeyboardButton("Необходимые СИЗ при работе в карьере", callback_data='6-2')
            item6_3 = types.InlineKeyboardButton("Требования к материальным пропускам", callback_data='6-3')
            item6_4 = types.InlineKeyboardButton("Требования при вождении ТС", callback_data='6-4')

            markup.add(item6_1, item6_2, item6_3, item6_4)
            bot.send_message(message.chat.id, 'Тут находятся самые необходимые сведения о правилах '
                                              'ТБ и СБ', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


# Ответ бота за указанные запросы




@bot.callback_query_handler(func=lambda call: True)


def callback_inline(call):
    try:
        if call.message:
            if call.data == '1-1':
                bot.send_message(call.message.chat.id, descrb.it1_1)
                with descrb.ph1_1 as ph1_1:
                    bot.send_photo(call.message.chat.id, ph1_1)
            elif call.data == '1-2':
                bot.send_message(call.message.chat.id, descrb.it1_2)
                bot.send_photo(call.message.chat.id, descrb.ph1_2)

            elif call.data == '1-3':
                bot.send_message(call.message.chat.id, descrb.it1_3)
                bot.send_photo(call.message.chat.id, descrb.ph1_3)

            elif call.data == '1-4':
                bot.send_message(call.message.chat.id, descrb.it1_4)
            elif call.data == '1-5':
                bot.send_message(call.message.chat.id, descrb.it1_5)
            elif call.data == '1-6':
                bot.send_message(call.message.chat.id, descrb.it1_6)
            elif call.data == '1-7':
                bot.send_message(call.message.chat.id, descrb.it1_7)
            elif call.data == '2-1':
                bot.send_message(call.message.chat.id, mvision.it2_1)
            elif call.data == '2-2':
                bot.send_message(call.message.chat.id, mvision.it2_2)
            elif call.data == '2-3':
                bot.send_message(call.message.chat.id, mvision.it2_3)
            elif call.data == '2-4':
                bot.send_message(call.message.chat.id, mvision.it2_4)
            elif call.data == '2-5':
                bot.send_message(call.message.chat.id, mvision.it2_5)
                bot.send_photo(call.message.chat.id, mvision.ph2_5)
            elif call.data == '3-11':
                bot.send_message(call.message.chat.id, MM.it3_11, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_11 = types.InlineKeyboardButton("Создание БД скважин", callback_data='3-11')
                item3_12 = types.InlineKeyboardButton("Визуализация скважин", callback_data='3-12')
                item3_13 = types.InlineKeyboardButton("Создание композитов по скважинам", callback_data='3-13')
                item3_14 = types.InlineKeyboardButton("Проектирование скважин", callback_data='3-14')
                item3_15 = types.InlineKeyboardButton("Опускание координат устьев к поверхности", callback_data='3-15')
                markup.add(item3_11, item3_12, item3_13, item3_14, item3_15)
                bot.send_message(call.message.chat.id, 'Вы искали из данного меню', reply_markup=markup)
            elif call.data == '3-12':
                bot.send_message(call.message.chat.id, MM.it3_12, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_11 = types.InlineKeyboardButton("Создание БД скважин", callback_data='3-11')
                item3_12 = types.InlineKeyboardButton("Визуализация скважин", callback_data='3-12')
                item3_13 = types.InlineKeyboardButton("Создание композитов по скважинам", callback_data='3-13')
                item3_14 = types.InlineKeyboardButton("Проектирование скважин", callback_data='3-14')
                item3_15 = types.InlineKeyboardButton("Опускание координат устьев к поверхности", callback_data='3-15')
                markup.add(item3_11, item3_12, item3_13, item3_14, item3_15)
                bot.send_message(call.message.chat.id, 'Вы искали из данного меню', reply_markup=markup)
            elif call.data == '3-13':
                bot.send_message(call.message.chat.id, MM.it3_13, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_11 = types.InlineKeyboardButton("Создание БД скважин", callback_data='3-11')
                item3_12 = types.InlineKeyboardButton("Визуализация скважин", callback_data='3-12')
                item3_13 = types.InlineKeyboardButton("Создание композитов по скважинам", callback_data='3-13')
                item3_14 = types.InlineKeyboardButton("Проектирование скважин", callback_data='3-14')
                item3_15 = types.InlineKeyboardButton("Опускание координат устьев к поверхности", callback_data='3-15')
                markup.add(item3_11, item3_12, item3_13, item3_14, item3_15)
                bot.send_message(call.message.chat.id, 'Вы искали из данного меню', reply_markup=markup)
            elif call.data == '3-14':
                bot.send_message(call.message.chat.id, MM.it3_14, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_11 = types.InlineKeyboardButton("Создание БД скважин", callback_data='3-11')
                item3_12 = types.InlineKeyboardButton("Визуализация скважин", callback_data='3-12')
                item3_13 = types.InlineKeyboardButton("Создание композитов по скважинам", callback_data='3-13')
                item3_14 = types.InlineKeyboardButton("Проектирование скважин", callback_data='3-14')
                item3_15 = types.InlineKeyboardButton("Опускание координат устьев к поверхности", callback_data='3-15')
                markup.add(item3_11, item3_12, item3_13, item3_14, item3_15)
                bot.send_message(call.message.chat.id, 'Вы искали из данного меню', reply_markup=markup)
            elif call.data == '3-15':
                bot.send_message(call.message.chat.id, MM.it3_15, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_11 = types.InlineKeyboardButton("Создание БД скважин", callback_data='3-11')
                item3_12 = types.InlineKeyboardButton("Визуализация скважин", callback_data='3-12')
                item3_13 = types.InlineKeyboardButton("Создание композитов по скважинам", callback_data='3-13')
                item3_14 = types.InlineKeyboardButton("Проектирование скважин", callback_data='3-14')
                item3_15 = types.InlineKeyboardButton("Опускание координат устьев к поверхности", callback_data='3-15')
                markup.add(item3_11, item3_12, item3_13, item3_14, item3_15)
                bot.send_message(call.message.chat.id, 'Вы искали из данного меню', reply_markup=markup)
            elif call.data == '3-21':
                bot.send_message(call.message.chat.id, MM.it3_21, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_21 = types.InlineKeyboardButton("Создание каркасной модели", callback_data='3-21')
                item3_22 = types.InlineKeyboardButton("Визуализация каркаса", callback_data='3-22')
                item3_23 = types.InlineKeyboardButton("Операции пересечения каркасов", callback_data='3-23')
                item3_24 = types.InlineKeyboardButton("Присвоение данных каркасной моделью", callback_data='3-24')
                item3_25 = types.InlineKeyboardButton("Очистка каркасной модели", callback_data='3-25')

                markup.add(item3_21, item3_22, item3_23, item3_24, item3_25)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-22':
                bot.send_message(call.message.chat.id, MM.it3_22, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_21 = types.InlineKeyboardButton("Создание каркасной модели", callback_data='3-21')
                item3_22 = types.InlineKeyboardButton("Визуализация каркаса", callback_data='3-22')
                item3_23 = types.InlineKeyboardButton("Операции пересечения каркасов", callback_data='3-23')
                item3_24 = types.InlineKeyboardButton("Присвоение данных каркасной моделью", callback_data='3-24')
                item3_25 = types.InlineKeyboardButton("Очистка каркасной модели", callback_data='3-25')

                markup.add(item3_21, item3_22, item3_23, item3_24, item3_25)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-23':
                bot.send_message(call.message.chat.id, MM.it3_23, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_21 = types.InlineKeyboardButton("Создание каркасной модели", callback_data='3-21')
                item3_22 = types.InlineKeyboardButton("Визуализация каркаса", callback_data='3-22')
                item3_23 = types.InlineKeyboardButton("Операции пересечения каркасов", callback_data='3-23')
                item3_24 = types.InlineKeyboardButton("Присвоение данных каркасной моделью", callback_data='3-24')
                item3_25 = types.InlineKeyboardButton("Очистка каркасной модели", callback_data='3-25')

                markup.add(item3_21, item3_22, item3_23, item3_24, item3_25)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-24':
                bot.send_message(call.message.chat.id, MM.it3_24, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_21 = types.InlineKeyboardButton("Создание каркасной модели", callback_data='3-21')
                item3_22 = types.InlineKeyboardButton("Визуализация каркаса", callback_data='3-22')
                item3_23 = types.InlineKeyboardButton("Операции пересечения каркасов", callback_data='3-23')
                item3_24 = types.InlineKeyboardButton("Присвоение данных каркасной моделью", callback_data='3-24')
                item3_25 = types.InlineKeyboardButton("Очистка каркасной модели", callback_data='3-25')

                markup.add(item3_21, item3_22, item3_23, item3_24, item3_25)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-25':
                bot.send_message(call.message.chat.id, MM.it3_25, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_21 = types.InlineKeyboardButton("Создание каркасной модели", callback_data='3-21')
                item3_22 = types.InlineKeyboardButton("Визуализация каркаса", callback_data='3-22')
                item3_23 = types.InlineKeyboardButton("Операции пересечения каркасов", callback_data='3-23')
                item3_24 = types.InlineKeyboardButton("Присвоение данных каркасной моделью", callback_data='3-24')
                item3_25 = types.InlineKeyboardButton("Очистка каркасной модели", callback_data='3-25')

                markup.add(item3_21, item3_22, item3_23, item3_24, item3_25)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-31':
                bot.send_message(call.message.chat.id, MM.it3_31, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_31 = types.InlineKeyboardButton("Создание пустой БМ", callback_data='3-31')
                item3_32 = types.InlineKeyboardButton("Нормализация БМ", callback_data='3-32')
                item3_33 = types.InlineKeyboardButton("Операции присвоения в БМ", callback_data='3-33')
                item3_34 = types.InlineKeyboardButton("Отчет по блочной модели", callback_data='3-34')
                markup.add(item3_31, item3_32, item3_33, item3_34)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)

            elif call.data == '3-32':
                bot.send_message(call.message.chat.id, MM.it3_32, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_31 = types.InlineKeyboardButton("Создание пустой БМ", callback_data='3-31')
                item3_32 = types.InlineKeyboardButton("Нормализация БМ", callback_data='3-32')
                item3_33 = types.InlineKeyboardButton("Операции присвоения в БМ", callback_data='3-33')
                item3_34 = types.InlineKeyboardButton("Отчет по блочной модели", callback_data='3-34')
                markup.add(item3_31, item3_32, item3_33, item3_34)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-33':
                bot.send_message(call.message.chat.id, MM.it3_33, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_31 = types.InlineKeyboardButton("Создание пустой БМ", callback_data='3-31')
                item3_32 = types.InlineKeyboardButton("Нормализация БМ", callback_data='3-32')
                item3_33 = types.InlineKeyboardButton("Операции присвоения в БМ", callback_data='3-33')
                item3_34 = types.InlineKeyboardButton("Отчет по блочной модели", callback_data='3-34')
                markup.add(item3_31, item3_32, item3_33, item3_34)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-34':
                bot.send_message(call.message.chat.id, MM.it3_34, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_31 = types.InlineKeyboardButton("Создание пустой БМ", callback_data='3-31')
                item3_32 = types.InlineKeyboardButton("Нормализация БМ", callback_data='3-32')
                item3_33 = types.InlineKeyboardButton("Операции присвоения в БМ", callback_data='3-33')
                item3_34 = types.InlineKeyboardButton("Отчет по блочной модели", callback_data='3-34')
                markup.add(item3_31, item3_32, item3_33, item3_34)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-41':
                bot.send_message(call.message.chat.id, MM.it3_41, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_41 = types.InlineKeyboardButton("Принцип создания макроса", callback_data='3-41')
                item3_42 = types.InlineKeyboardButton("Импорт макросов", callback_data='3-42')
                item3_43 = types.InlineKeyboardButton("Запуск макросов", callback_data='3-43')
                markup.add(item3_41, item3_42, item3_43)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-42':
                bot.send_message(call.message.chat.id, MM.it3_42, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_41 = types.InlineKeyboardButton("Принцип создания макроса", callback_data='3-41')
                item3_42 = types.InlineKeyboardButton("Импорт макросов", callback_data='3-42')
                item3_43 = types.InlineKeyboardButton("Запуск макросов", callback_data='3-43')
                markup.add(item3_41, item3_42, item3_43)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-43':
                bot.send_message(call.message.chat.id, MM.it3_43, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_41 = types.InlineKeyboardButton("Принцип создания макроса", callback_data='3-41')
                item3_42 = types.InlineKeyboardButton("Импорт макросов", callback_data='3-42')
                item3_43 = types.InlineKeyboardButton("Запуск макросов", callback_data='3-43')
                markup.add(item3_41, item3_42, item3_43)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-51':
                bot.send_message(call.message.chat.id, MM.it3_51, parse_mode='HTML')
                bot.send_message(call.message.chat.id, MM.it3_51_1)
                bot.send_message(call.message.chat.id, MM.it3_51_2, parse_mode='HTML')
                bot.send_photo(call.message.chat.id, MM.ph_351_2)
                bot.send_message(call.message.chat.id, MM.it3_51_3)
                bot.send_photo(call.message.chat.id, MM.ph_351_3)
                bot.send_message(call.message.chat.id, MM.it3_51_4, parse_mode='HTML')

                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_51 = types.InlineKeyboardButton("Установка связи с БД", callback_data='3-51')
                item3_52 = types.InlineKeyboardButton("Работа с файлами связи", callback_data='3-52')
                item3_53 = types.InlineKeyboardButton("Урезка ураганов", callback_data='3-53')
                item3_54 = types.InlineKeyboardButton("Создание чертежей", callback_data='3-54')
                item3_55 = types.InlineKeyboardButton("Настройка координатной сетки", callback_data='3-55')
                item3_56 = types.InlineKeyboardButton("Импорт и экспорт данных", callback_data='3-56')
                markup.add(item3_51, item3_52, item3_53, item3_54, item3_55, item3_56)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-52':
                bot.send_message(call.message.chat.id, MM.it3_52, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_51 = types.InlineKeyboardButton("Установка связи с БД", callback_data='3-51')
                item3_52 = types.InlineKeyboardButton("Работа с файлами связи", callback_data='3-52')
                item3_53 = types.InlineKeyboardButton("Урезка ураганов", callback_data='3-53')
                item3_54 = types.InlineKeyboardButton("Создание чертежей", callback_data='3-54')
                item3_55 = types.InlineKeyboardButton("Настройка координатной сетки", callback_data='3-55')
                item3_56 = types.InlineKeyboardButton("Импорт и экспорт данных", callback_data='3-56')
                markup.add(item3_51, item3_52, item3_53, item3_54, item3_55, item3_56)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-53':
                bot.send_message(call.message.chat.id, MM.it3_53, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_51 = types.InlineKeyboardButton("Установка связи с БД", callback_data='3-51')
                item3_52 = types.InlineKeyboardButton("Работа с файлами связи", callback_data='3-52')
                item3_53 = types.InlineKeyboardButton("Урезка ураганов", callback_data='3-53')
                item3_54 = types.InlineKeyboardButton("Создание чертежей", callback_data='3-54')
                item3_55 = types.InlineKeyboardButton("Настройка координатной сетки", callback_data='3-55')
                item3_56 = types.InlineKeyboardButton("Импорт и экспорт данных", callback_data='3-56')
                markup.add(item3_51, item3_52, item3_53, item3_54, item3_55, item3_56)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-54':
                bot.send_message(call.message.chat.id, MM.it3_54, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_51 = types.InlineKeyboardButton("Установка связи с БД", callback_data='3-51')
                item3_52 = types.InlineKeyboardButton("Работа с файлами связи", callback_data='3-52')
                item3_53 = types.InlineKeyboardButton("Урезка ураганов", callback_data='3-53')
                item3_54 = types.InlineKeyboardButton("Создание чертежей", callback_data='3-54')
                item3_55 = types.InlineKeyboardButton("Настройка координатной сетки", callback_data='3-55')
                item3_56 = types.InlineKeyboardButton("Импорт и экспорт данных", callback_data='3-56')
                markup.add(item3_51, item3_52, item3_53, item3_54, item3_55, item3_56)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-55':
                bot.send_message(call.message.chat.id, MM.it3_55, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_51 = types.InlineKeyboardButton("Установка связи с БД", callback_data='3-51')
                item3_52 = types.InlineKeyboardButton("Работа с файлами связи", callback_data='3-52')
                item3_53 = types.InlineKeyboardButton("Урезка ураганов", callback_data='3-53')
                item3_54 = types.InlineKeyboardButton("Создание чертежей", callback_data='3-54')
                item3_55 = types.InlineKeyboardButton("Настройка координатной сетки", callback_data='3-55')
                item3_56 = types.InlineKeyboardButton("Импорт и экспорт данных", callback_data='3-56')
                markup.add(item3_51, item3_52, item3_53, item3_54, item3_55, item3_56)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '3-56':
                bot.send_message(call.message.chat.id, MM.it3_56, parse_mode='HTML')
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_51 = types.InlineKeyboardButton("Установка связи с БД", callback_data='3-51')
                item3_52 = types.InlineKeyboardButton("Работа с файлами связи", callback_data='3-52')
                item3_53 = types.InlineKeyboardButton("Урезка ураганов", callback_data='3-53')
                item3_54 = types.InlineKeyboardButton("Создание чертежей", callback_data='3-54')
                item3_55 = types.InlineKeyboardButton("Настройка координатной сетки", callback_data='3-55')
                item3_56 = types.InlineKeyboardButton("Импорт и экспорт данных", callback_data='3-56')
                markup.add(item3_51, item3_52, item3_53, item3_54, item3_55, item3_56)
                bot.send_message(call.message.chat.id, 'Сообщение из данного меню', reply_markup=markup)
            elif call.data == '4-1':
                bot.send_message(call.message.chat.id, wenco.it4_1)
                bot.send_photo(call.message.chat.id, wenco.ph4_11)
                bot.send_photo(call.message.chat.id, wenco.ph4_12)
                bot.send_photo(call.message.chat.id, wenco.ph4_13)
            elif call.data == '4-2':
                bot.send_message(call.message.chat.id, wenco.it4_2, parse_mode='HTML')
                bot.send_video(call.message.chat.id, wenco.vd4_2)
            elif call.data == '4-3':
                bot.send_message(call.message.chat.id, wenco.it4_3, parse_mode='HTML')
                bot.send_video(call.message.chat.id, wenco.vd4_3)
            elif call.data == '4-4':
                bot.send_message(call.message.chat.id, wenco.it4_4, parse_mode='HTML')
                bot.send_video(call.message.chat.id, wenco.vd4_4)
            elif call.data == '4-5':
                bot.send_message(call.message.chat.id, wenco.it4_5, parse_mode='HTML')
                bot.send_video(call.message.chat.id, wenco.vd4_5)
            elif call.data == '5-1':
                bot.send_message(call.message.chat.id, report.it5_1)
            elif call.data == '5-2':
                bot.send_message(call.message.chat.id, report.it5_2)
            elif call.data == '5-3':
                bot.send_message(call.message.chat.id, report.it5_3)
            elif call.data == '5-4':
                bot.send_message(call.message.chat.id, report.it5_4)
            elif call.data == '5-5':
                bot.send_message(call.message.chat.id, report.it5_5)
            elif call.data == '6-1':
                bot.send_message(call.message.chat.id, tbsb.it6_1)
            elif call.data == '6-2':
                bot.send_message(call.message.chat.id, tbsb.it6_2)
            elif call.data == '6-3':
                bot.send_message(call.message.chat.id, tbsb.it6_3)
            elif call.data == '6-4':
                bot.send_message(call.message.chat.id, tbsb.it6_4)
            elif call.data == '3-1':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_11 = types.InlineKeyboardButton("Создание БД скважин", callback_data='3-11')
                item3_12 = types.InlineKeyboardButton("Визуализация скважин", callback_data='3-12')
                item3_13 = types.InlineKeyboardButton("Создание композитов по скважинам", callback_data='3-13')
                item3_14 = types.InlineKeyboardButton("Проектирование скважин", callback_data='3-14')
                item3_15 = types.InlineKeyboardButton("Опускание координат устьев к поверхности", callback_data='3-15')
                markup.add(item3_11, item3_12, item3_13, item3_14, item3_15)
                bot.send_message(call.message.chat.id, 'Выбери нужный пункт', reply_markup=markup)

            elif call.data == '3-2':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_21 = types.InlineKeyboardButton("Создание каркасной модели", callback_data='3-21')
                item3_22 = types.InlineKeyboardButton("Визуализация каркаса", callback_data='3-22')
                item3_23 = types.InlineKeyboardButton("Операции пересечения каркасов", callback_data='3-23')
                item3_24 = types.InlineKeyboardButton("Присвоение данных каркасной моделью", callback_data='3-24')
                item3_25 = types.InlineKeyboardButton("Очистка каркасной модели", callback_data='3-25')

                markup.add(item3_21, item3_22, item3_23, item3_24, item3_25)
                bot.send_message(call.message.chat.id, 'Выбери нужный пункт', reply_markup=markup)
            elif call.data == '3-3':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_31 = types.InlineKeyboardButton("Создание пустой БМ", callback_data='3-31')
                item3_32 = types.InlineKeyboardButton("Нормализация БМ", callback_data='3-32')
                item3_33 = types.InlineKeyboardButton("Операции присвоения в БМ", callback_data='3-33')
                item3_34 = types.InlineKeyboardButton("Отчет по блочной модели", callback_data='3-34')
                markup.add(item3_31, item3_32, item3_33, item3_34)
                bot.send_message(call.message.chat.id, 'Выбери нужный пункт', reply_markup=markup)

            elif call.data == '3-4':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_41 = types.InlineKeyboardButton("Принцип создания макроса", callback_data='3-41')
                item3_42 = types.InlineKeyboardButton("Импорт макросов", callback_data='3-42')
                item3_43 = types.InlineKeyboardButton("Запуск макросов", callback_data='3-43')
                markup.add(item3_41, item3_42, item3_43)
                bot.send_message(call.message.chat.id, 'Выбери нужный пункт', reply_markup=markup)
            elif call.data == '3-5':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3_51 = types.InlineKeyboardButton("Установка связи с БД", callback_data='3-51')
                item3_52 = types.InlineKeyboardButton("Работа с файлами связи", callback_data='3-52')
                item3_53 = types.InlineKeyboardButton("Урезка ураганов", callback_data='3-53')
                item3_54 = types.InlineKeyboardButton("Создание чертежей", callback_data='3-54')
                item3_55 = types.InlineKeyboardButton("Настройка координатной сетки", callback_data='3-55')
                item3_56 = types.InlineKeyboardButton("Импорт и экспорт данных", callback_data='3-56')
                markup.add(item3_51, item3_52, item3_53, item3_54, item3_55, item3_56)
                bot.send_message(call.message.chat.id, 'Выбери нужный пункт', reply_markup=markup)

            # remove inline buttons
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            # text="Подумаю",reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Бот находится в тестовом режиме")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=False, timeout=120)
