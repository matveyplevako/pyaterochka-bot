from telegram import ReplyKeyboardMarkup, KeyboardButton
from services.initial.configure import menu
from telegram.ext import ConversationHandler
from services.language import extract_language_and_update_if_not_present, translate
from services.Stats import *

ADD_COMMENT_RECEIPT = 0


def wrong_receipt(update, context):
    bot = context.bot
    lang = extract_language_and_update_if_not_present(update, context)

    keyboard = [
        [KeyboardButton(f"🚫{translate('cancel', lang)}")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, f"{translate('send_wrong_tag', lang)}",
                     reply_markup=reply_markup)

    edit_stat("wrong_receipt")
    edit_user_stat(update.message.chat_id, "wrong_receipt")

    return ADD_COMMENT_RECEIPT


def send_photo(update, context):
    bot = context.bot
    lang = extract_language_and_update_if_not_present(update, context)
    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    photo_file_id = update.message.photo[len(update.message.photo) - 1].file_id
    message = f"Отзыв о неправильном ценнике\nот {first_name} {last_name} {username}\n"

    bot.send_photo(photo=photo_file_id, chat_id=os.environ["WORKERS_CHANNEL"], caption=message)

    bot.send_message(update.message.chat_id, f"{translate('thank_fix_tag', lang)}")

    menu(update, context)

    return ConversationHandler.END
