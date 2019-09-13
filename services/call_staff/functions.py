from telegram import ReplyKeyboardMarkup, KeyboardButton
from services.logger import logger


def select_staff(update, context):
    bot = context.bot
    logger.info(update.message.from_user.username)
    keyboard = [
        [KeyboardButton("Позвать администратора")],
        [KeyboardButton("Позвать кассира")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Кого вы хотите позвать?", reply_markup=reply_markup)


def call_admin(update, context):
    bot = context.bot

    keyboard = [
        [KeyboardButton("Меню")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(-1001226207512, "Вызов администратора")
    bot.send_message(update.message.chat_id, "Запрос отправлен", reply_markup=reply_markup)



def call_cashier(update, context):
    bot = context.bot

    keyboard = [
        [KeyboardButton("Меню")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(-1001226207512, "Вызов кассира")
    bot.send_message(update.message.chat_id, "Запрос отправлен", reply_markup=reply_markup)
