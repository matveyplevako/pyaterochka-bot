from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from services.language import translate, extract_language_and_update_if_not_present
from services.Stats import *


def select_staff(update, context):
    bot = context.bot
    lang = extract_language_and_update_if_not_present(update, context)
    keyboard = [
        [InlineKeyboardButton(f'❗{translate("call_admin", language=lang)}',
                              callback_data='call_admin')],
        [InlineKeyboardButton(f'❕{translate("call_cashier", language=lang)}',
                              callback_data='call_cashier')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(update.message.chat_id, translate("who_to_call", lang), reply_markup=reply_markup)

    edit_stat("call_staff")
    edit_user_stat(update.message.chat_id, "call_staff")


def call_admin(update, context):
    bot = context.bot
    query = update.callback_query
    lang = extract_language_and_update_if_not_present(query, context)
    user = query.from_user

    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["WORKERS_CHANNEL"], f"""Вызов администратора\nот {first_name} {last_name} {username}""")
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=translate("staff_request_sent", lang)
    )


def call_cashier(update, context):
    bot = context.bot
    query = update.callback_query
    lang = extract_language_and_update_if_not_present(query, context)
    user = query.from_user

    first_name = user.first_name if user.first_name is not None else ""
    last_name = user.last_name if user.last_name is not None else ""
    username = "@" + user.username if user.username is not None else ""

    bot.send_message(os.environ["WORKERS_CHANNEL"], f"""Вызов кассира\nот {first_name} {last_name} {username}""")
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=translate("staff_request_sent", lang)
    )
