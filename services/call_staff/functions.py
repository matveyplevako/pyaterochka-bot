from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import os
import datetime
from services.Statistics.Stats import *

def select_staff(update, context):
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("❗️Позвать администратора", callback_data='call_admin')],
        [InlineKeyboardButton("❕Позвать кассира", callback_data='call_cashier')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(update.message.chat_id, "Кого вы хотите позвать?", reply_markup=reply_markup)


    now = datetime.datetime.now()
    current_date = str('-'.join([str(now.day), str(now.month), str(now.year)]))

    statistics.edit_stat(current_date, "call_staff")


def call_admin(update, context):
    bot = context.bot
    query = update.callback_query

    user = query.from_user

    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["WORKERS_CHANNEL"], f"""Вызов администратора\nот {first_name} {last_name} {username}""")
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text='Запрос отправлен'
    )


def call_cashier(update, context):
    bot = context.bot
    query = update.callback_query

    user = query.from_user

    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["WORKERS_CHANNEL"], f"""Вызов кассира\nот {first_name} {last_name} {username}""")
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text='Запрос отправлен'
    )
