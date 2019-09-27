from telegram import ReplyKeyboardMarkup, KeyboardButton
from services.initial.configure import menu
from telegram.ext import ConversationHandler
import os

ADD_COMMENT_RECEIPT = 0


def write_receipt(update, context):
    bot = context.bot
    # logger.info(update.message.from_user.username)

    keyboard = [
        [KeyboardButton("Отменить")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Пожалуйста, пришлите фотографию неправильного ценника",
                     reply_markup=reply_markup)

    return ADD_COMMENT_RECEIPT


def send_photo(update, context):
    bot = context.bot
    # logger.info(update.message.from_user.username)

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    photo_file_id = update.message.photo[len(update.message.photo) - 1].file_id
    message = f"""Отзыв о неправильном ценнике\nот {first_name} {last_name} {username}\n"""

    bot.send_photo(photo=photo_file_id, chat_id=os.environ["WORKERS_CHANNEL"], caption=message)

    bot.send_message(update.message.chat_id, "Спасибо за отзыв! Мы решим проблему с ценником в ближайшее время")

    menu(update, context)

    return ConversationHandler.END


def cancel(update, context):
    menu(update, context)
    return ConversationHandler.END
