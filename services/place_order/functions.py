from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from services.initial.configure import menu
from telegram.ext import ConversationHandler
from services.language import extract_language_and_update_if_not_present, translate
from services.translate import translate as translate_from_eng
from services.Stats import *

ADD_TEXT, ADD_PHOTO, ADD_PHOTO_TEXT, SELECT_TYPE = range(4)


def choose_product(update, context):
    bot = context.bot
    lang = extract_language_and_update_if_not_present(update, context)
    keyboard = [
        [KeyboardButton(f"📝{translate('send_name', lang)}")],
        [KeyboardButton(f"📸📝{translate('send_name_and_photo', lang)}")],
        [KeyboardButton(f"🚫{translate('cancel', lang)}")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, f"{translate('select_option', lang)}", reply_markup=reply_markup)

    edit_stat("place_order")
    edit_user_stat(update.message.chat_id, "place_order")
    edit_daily_active_users_stat(update.message.chat_id)

    return SELECT_TYPE


def input_text(update, context):
    bot = context.bot
    lang = extract_language_and_update_if_not_present(update, context)
    keyboard = [
        [KeyboardButton(f"🚫{translate('cancel', lang)}")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, f"{translate('enter_product_name', lang)}", reply_markup=reply_markup)

    return ADD_TEXT


def input_photo(update, context):
    bot = context.bot
    lang = extract_language_and_update_if_not_present(update, context)
    keyboard = [
        [KeyboardButton(f"🚫{translate('cancel', lang)}")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, f"{translate('enter_product_photo', lang)}", reply_markup=reply_markup)

    return ADD_PHOTO


def input_product_text(update, context):
    return ADD_TEXT


def send_product_text(update, context):
    bot = context.bot
    lang = extract_language_and_update_if_not_present(update, context)
    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(update.message.chat_id, f"{translate('request_sent', lang)}")
    menu(update, context)

    data_about_user = "order" + " " + str(update.message.chat_id) + "  " + str(update.message.message_id)

    keyboard = [
        [InlineKeyboardButton("✅Принять", callback_data=data_about_user + " 1 " + lang),
         InlineKeyboardButton("❌Отклонить",
                              callback_data=data_about_user + " 0 " + lang)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if lang == "ru":
        message = f"""🚚Заказ продуктов\nот {first_name} {last_name} {username}\nНазвание продукта:\n""" \
                  + update.message.text
    else:
        message = f"""🚚🇬🇧 Заказ продуктов\nот {first_name} {last_name} {username}\nНазвание продукта на английском:\n""" \
                  + update.message.text + "\n\nПеревод:\n" + translate_from_eng(update.message.text)

    bot.send_message(os.environ["WORKERS_CHANNEL"], message, reply_markup=reply_markup)

    return ConversationHandler.END


def send_product_photo(update, context):
    bot = context.bot
    user_data = context.user_data
    lang = extract_language_and_update_if_not_present(update, context)
    photo_file_id = update.message.photo[len(update.message.photo) - 1].file_id

    bot.send_message(update.message.chat_id, f"{translate('enter_product_name', lang)}")
    user_data["file_id"] = photo_file_id

    return ADD_PHOTO_TEXT


def send_product_text_photo(update, context):
    bot = context.bot
    user_data = context.user_data
    lang = extract_language_and_update_if_not_present(update, context)
    user = update.message.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(update.message.chat_id, f"{translate('request_sent', lang)}")
    menu(update, context)

    picture = bot.send_photo(photo=user_data["file_id"], chat_id=os.environ["WORKERS_CHANNEL"])

    data_about_user = "order" + " " + str(update.message.chat_id) + "  " + str(update.message.message_id)

    keyboard = [
        [InlineKeyboardButton("✅Принять", callback_data=data_about_user + " 1 " + lang),
         InlineKeyboardButton("❌Отклонить",
                              callback_data=data_about_user + " 0 " + lang)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if lang == "ru":
        message = f"""🚚Заказ продуктов\nот {first_name} {last_name} {username}\nНазвание продукта:\n""" \
                  + update.message.text
    else:
        message = f"""🚚🇬🇧 Заказ продуктов\nот {first_name} {last_name} {username}\nНазвание продукта на английском:\n""" \
                  + update.message.text + "\n\nПеревод:\n" + translate_from_eng(update.message.text)

    bot.send_message(os.environ["WORKERS_CHANNEL"], message, reply_to_message_id=picture.message_id,
                     reply_markup=reply_markup)

    return ConversationHandler.END


def process_selection(update, context):
    bot = context.bot
    query = update.callback_query

    user = query.from_user
    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""
    query_data = query.data.split()
    chat_id, message_id, selected = map(int, query_data[1:-1])
    lang = query_data[-1]

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=query.message.text + '\n\n\n' + f'{["Отклонён", "Принят"][selected]} {first_name} {last_name} {username}'
    )

    bot.send_message(chat_id,

                     [f"{translate('can_not_order', lang)}", f"{translate('can_order', lang)}"]
                     [selected],
                     reply_to_message_id=message_id)
