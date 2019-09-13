from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton


def menu(bot, update):
    keyboard = [
        [KeyboardButton("Позвать сотрудника магазина")],
        [KeyboardButton("Заказать отсутсвующую продукцию")],
        [KeyboardButton("Сообщить о неправильном ценнике")],
        [KeyboardButton("Оставить отзыв о боте")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Что вас интересует?", reply_markup=reply_markup)


def start(bot, update):
    keyboard = [
        [KeyboardButton("Позвать работника")],
        [KeyboardButton("Заказать отсутсвующую продукцию")],
        [KeyboardButton("Сообщить о неправильном ценнике")],
        [KeyboardButton("Оставить отзыв о боте")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)
    bot.send_message(update.message.chat_id, "Привет! Я чат бот пятёрочки города Иннополис. Что вас интересует?",
                     reply_markup=reply_markup)
