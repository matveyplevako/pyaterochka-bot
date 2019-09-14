from telegram import ReplyKeyboardMarkup, KeyboardButton
from services.logger import logger
from telegram.ext import ConversationHandler
from services.initial.configure import menu
import os

ADD_COMMENT = 0


def write_comment(update, context):
    bot = context.bot
    # logger.info(update.message.from_user.username)

    keyboard = [
        [KeyboardButton("Отменить")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Напишите отзыв о боте", reply_markup=reply_markup)

    return ADD_COMMENT


def send_comment(update, context):
    bot = context.bot
    # logger.info(update.message.from_user.username)

    bot = context.bot
    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["FEEDBACK_CHANNEL"], f"""Отзыв о боте\nот {first_name} {last_name} {username}\n""" + \
                     update.message.text)
    bot.send_message(update.message.chat_id, "Спасибо за отзыв! Мы ценим ваше мнение")
    menu(update, context)
    return ConversationHandler.END


def cancel(update, context):
    menu(update, context)
    return ConversationHandler.END
