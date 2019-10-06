from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ConversationHandler
from services.initial.configure import menu
from services.language import extract_language_and_update_if_not_present, translate
from services.Stats import *

ADD_COMMENT = 0


def write_comment(update, context):
    bot = context.bot

    lang = extract_language_and_update_if_not_present(update, context)

    keyboard = [
        [KeyboardButton(f'🚫{translate("cancel", lang)}')],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, translate("write_feedback", lang), reply_markup=reply_markup)

    edit_stat("feedback")

    return ADD_COMMENT


def send_comment(update, context):
    bot = context.bot
    lang = extract_language_and_update_if_not_present(update, context)

    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["FEEDBACK_CHANNEL"], f"""Отзыв о боте\nот {first_name} {last_name} {username}\n""" + \
                     update.message.text)
    bot.send_message(update.message.chat_id, translate("thank_you_feedback", lang))
    menu(update, context)
    return ConversationHandler.END
