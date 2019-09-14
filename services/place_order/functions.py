from telegram import ReplyKeyboardMarkup, KeyboardButton
from services.logger import logger
from telegram.ext import ConversationHandler
import os

CHOOSE_PRODUCT = 0


def choose_product(update, context):
    bot = context.bot

    bot = context.bot
    # logger.info(update.message.from_user.username)

    keyboard = [
        [KeyboardButton("Отменить")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Напишите название продукта, который вы хотите заказать", reply_markup=reply_markup)

    return CHOOSE_PRODUCT

def send_product_query(update, context):
    bot = context.bot
    #logger.info(update.message.from_user.username)

    bot = context.bot

    keyboard = [
        [KeyboardButton("Меню")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["WORKERS_CHANNEL"], f"""Заказ продуктов\nот {first_name} {last_name} {username}\n""" + \
                     update.message.text)
    bot.send_message(update.message.chat_id, "Мы приняли ваш заказ", reply_markup=reply_markup)


    return ConversationHandler.END


def cancel(update, context):
    bot = context.bot

    keyboard = [
        [KeyboardButton("Меню")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)


    bot.send_message(update.message.chat_id, "Меню", reply_markup=reply_markup)

    return ConversationHandler.END