from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ConversationHandler
from services.initial.configure import menu
import os

CALL_STUFF = 0


def select_staff(update, context):
    bot = context.bot
    keyboard = [
        [KeyboardButton("Позвать администратора")],
        [KeyboardButton("Позвать кассира")],
        [KeyboardButton("Отменить")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Кого вы хотите позвать?", reply_markup=reply_markup)
    return CALL_STUFF


def call_admin(update, context):
    bot = context.bot

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["WORKERS_CHANNEL"], f"""Вызов администратора\nот {first_name} {last_name} {username}""")
    bot.send_message(update.message.chat_id, "Запрос отправлен")
    menu(update, context)
    return ConversationHandler.END


def call_cashier(update, context):
    bot = context.bot

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["WORKERS_CHANNEL"], f"""Вызов кассира\nот {first_name} {last_name} {username}""")
    bot.send_message(update.message.chat_id, "Запрос отправлен")
    menu(update, context)
    return ConversationHandler.END


def cancel(update, context):
    menu(update, context)
    return ConversationHandler.END


def custom_cancel(update, context):
    print(update, context)
    return ConversationHandler.END
