from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton


def menu(update, context):
    bot = context.bot
    keyboard = [
        [KeyboardButton("Позвать сотрудника магазина")],
        [KeyboardButton("Заказать отсутсвующую продукцию")],
        [KeyboardButton("Сообщить о неправильном ценнике")],
        [KeyboardButton("Оставить отзыв о боте")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False, resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Что вас интересует?", reply_markup=reply_markup)


def start(update, context):
    bot = context.bot

    keyboard = [
        [KeyboardButton("Меню")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False, resize_keyboard=True)
    bot.send_message(update.message.chat_id, "Привет! Я чат бот пятёрочки города Иннополис",
                     reply_markup=reply_markup)

def wrong_input(update, context):
    bot = context.bot

    bot.send_message(update.message.chat_id, "Я не искуственный интеллект: не понимаю ваш запрос")