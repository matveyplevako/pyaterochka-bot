from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ConversationHandler
from services.initial.configure import menu
import os
import datetime
from services.Database import DataBase
from services.Statistics.Stats import *

ADD_COMMENT = 0


def write_comment(update, context):
    bot = context.bot

    now = datetime.datetime.now()
    current_date = str('-'.join([str(now.day),  str(now.month), str(now.year)]))


    keyboard = [
        [KeyboardButton("Отменить")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Напишите отзыв о боте", reply_markup=reply_markup)

    statistics.edit_stat(current_date, "feedback")

    return ADD_COMMENT


def send_comment(update, context):
    bot = context.bot
    # logger.info(update.message.from_user.username)

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["FEEDBACK_CHANNEL"], f"""Отзыв о боте\nот {first_name} {last_name} {username}\n""" + \
                     update.message.text)
    bot.send_message(update.message.chat_id, "Спасибо за отзыв! Мы ценим ваше мнение")
    menu(update, context)
    return ConversationHandler.END
