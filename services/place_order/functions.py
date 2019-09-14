from telegram import ReplyKeyboardMarkup, KeyboardButton
from services.logger import logger
from services.initial.configure import menu
from telegram.ext import ConversationHandler
import os

CHOOSE_PRODUCT_TEXT, CHOOSE_PRODUCT_PHOTO = 0


def choose_product(update, context):
    bot = context.bot

    bot = context.bot
    # logger.info(update.message.from_user.username)

    keyboard = [
        [KeyboardButton("Отправить название")],
        [KeyboardButton("Отправить фото и название")],
        [KeyboardButton("Отменить")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Напишите название продукта, который вы хотите заказать", reply_markup=reply_markup)

    return CHOOSE_PRODUCT_TEXT

def send_product_query(update, context):
    #logger.info(update.message.from_user.username)

    bot = context.bot

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["WORKERS_CHANNEL"], f"""Заказ продуктов\nот {first_name} {last_name} {username}\n""" + \
                     update.message.text)
    bot.send_message(update.message.chat_id, "Мы приняли ваш заказ")
    menu(update, context)
    return ConversationHandler.END


def cancel(update, context):
    menu(update, context)
    return ConversationHandler.END
