from telegram import ReplyKeyboardMarkup, KeyboardButton
from services.logger import logger
from services.initial.configure import menu
from telegram.ext import ConversationHandler
import os

ADD_TEXT, ADD_PHOTO, ADD_PHOTO_TEXT = range(3)


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

    bot.send_message(update.message.chat_id, "Выберите опцию", reply_markup=reply_markup)


def input_text(update, context):
    bot = context.bot

    bot = context.bot
    # logger.info(update.message.from_user.username)

    keyboard = [
        [KeyboardButton("Отменить")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Напишите названию продукта", reply_markup=reply_markup)

    return ADD_TEXT


def input_photo(update, context):

    bot = context.bot
    # logger.info(update.message.from_user.username)

    keyboard = [
        [KeyboardButton("Отменить")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Отправте фотографию продукта", reply_markup=reply_markup)

    return ADD_PHOTO

def input_product_text(update, context):
    bot = context.bot
    # logger.info(update.message.from_user.username)






def send_product_text(update, context):
    # logger.info(update.message.from_user.username)

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


def send_product_photo(update, context):
    bot = context.bot
    # logger.info(update.message.from_user.username)

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    photo_file_id = update.message.photo[len(update.message.photo) - 1].file_id
    message = f"""Заказ продуктов\nот {first_name} {last_name} {username}\n"""

    bot.send_photo(photo=photo_file_id, chat_id=os.environ["WORKERS_CHANNEL"], caption=message)

    bot.send_message(update.message.chat_id, "Отправте название продукта")

    #menu(update, context)

    return ADD_PHOTO_TEXT


def cancel(update, context):
    menu(update, context)
    return ConversationHandler.END
