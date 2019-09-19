from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from services.logger import logger
from services.initial.configure import menu
from telegram.ext import ConversationHandler, InlineQueryHandler
import os

ADD_TEXT, ADD_PHOTO, ADD_PHOTO_TEXT, SELECT_TYPE = range(4)


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
    return SELECT_TYPE


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
    return ADD_TEXT


def send_product_text(update, context):
    # logger.info(update.message.from_user.username)

    bot = context.bot

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(update.message.chat_id, "Ожидайте ответа от сотрудников")
    menu(update, context)

    data_about_user = "order" + " " + str(update.message.chat_id) + "  " + str(update.message.message_id)

    keyboard = [
        [InlineKeyboardButton(u"Принять заказ", callback_data=data_about_user + " 1"),
         InlineKeyboardButton(u"Отклонить",
                              callback_data=data_about_user + " 0")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = f"""Заказ продуктов\nот {first_name} {last_name} {username}\n""" + update.message.text

    bot.send_message(os.environ["WORKERS_CHANNEL"], message, reply_markup=reply_markup)

    return ConversationHandler.END


def send_product_photo(update, context):
    bot = context.bot
    # logger.info(update.message.from_user.username)
    chat_data = context.chat_data

    photo_file_id = update.message.photo[len(update.message.photo) - 1].file_id

    bot.send_message(update.message.chat_id, "Отправьте название продукта")
    chat_data["file_id"] = photo_file_id

    return ADD_PHOTO_TEXT


def send_product_text_photo(update, context):
    # logger.info(update.message.from_user.username)

    bot = context.bot
    chat_data = context.chat_data

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(update.message.chat_id, "Мы приняли ваш заказ")
    menu(update, context)

    picture = bot.send_photo(photo=chat_data["file_id"], chat_id=os.environ["WORKERS_CHANNEL"])

    data_about_user = "order" + " " + str(update.message.chat_id) + "  " + str(update.message.message_id)

    keyboard = [
        [InlineKeyboardButton(u"Принять заказ", callback_data=data_about_user + " 1"),
         InlineKeyboardButton(u"Отклонить",
                              callback_data=data_about_user + " 0")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = f"""Заказ продуктов\nот {first_name} {last_name} {username}\n""" + update.message.text

    bot.send_message(os.environ["WORKERS_CHANNEL"], message, reply_to_message_id=picture.message_id,
                     reply_markup=reply_markup)

    context.chat_data = {}

    return ConversationHandler.END


def cancel(update, context):
    menu(update, context)
    context.chat_data = {}

    return ConversationHandler.END


def process_selection(update, context):
    bot = context.bot
    query = update.callback_query

    user = query.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""
    chat_id, message_id, selected = map(int, query.data.split()[1:])

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=query.message.text + '\n\n\n' + f'{["Отклонён", "Принят"][selected]} {first_name} {last_name} {username}'
    )

    bot.send_message(chat_id,
                     ["Извините, к сожалению не можем закзать данный товар",
                      "Ваш заказ подтвердили, ожидайте поступления в ближайшее время",
                      ]
                     [selected],
                     reply_to_message_id=message_id)
