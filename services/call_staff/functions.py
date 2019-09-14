from telegram import ReplyKeyboardMarkup, KeyboardButton
from services.logger import logger
from services.initial.configure import menu
import os


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

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["WORKERS_CHANNEL"], f"""Вызов администратора\nот {first_name} {last_name} {username}""")
    bot.send_message(update.message.chat_id, "Запрос отправлен")
    menu(update, context)


def call_cashier(update, context):
    bot = context.bot

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["WORKERS_CHANNEL"], f"""Вызов кассира\nот {first_name} {last_name} {username}""")
    bot.send_message(update.message.chat_id, "Запрос отправлен")
    menu(update, context)
