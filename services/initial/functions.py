from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton
from services.language import extract_language_and_update_if_not_present, translate
from services.DataBase import DB

SELECT_LANG = range(1)


def menu(update, context):
    bot = context.bot
    lang = extract_language_and_update_if_not_present(update, context)
    keyboard = [
        [KeyboardButton(f"🗺{translate('shop_map', lang)}")],
        [KeyboardButton(f"🏃{translate('call_staff', lang)}")],
        [KeyboardButton(f"🔎{translate('request_information_about_product', lang)}")],
        [KeyboardButton(f"🚚{translate('place_order', lang)}")],
        [KeyboardButton(f"📵{translate('wrong_tag', lang)}")],
        [KeyboardButton(f"⭐{translate('leave_feedback', lang)}")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False, resize_keyboard=True)

    bot.send_message(update.message.chat_id, translate("select_menu", lang), reply_markup=reply_markup)


def start(update, context):
    bot = context.bot

    keyboard = [
        [KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇬🇧 English")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=False,
                                       resize_keyboard=True)

    bot.send_message(update.message.chat_id, "Выберите язык\nSelect your language",
                     reply_markup=reply_markup)
    return SELECT_LANG


def repeat(update, context):
    return start(update, context)


def select_language(update, context):
    bot = context.bot

    text = update.message.text
    if "English" in text:
        lang = "eng"
    else:
        lang = "ru"

    language_preference = DB('language_selection', chat_id="TEXT", language="TEXT")
    res = language_preference.get_items(chat_id=update.message.chat_id)
    print(res)
    if len(res) != 0 and res[0][1] != lang:
        language_preference.delete_item(chat_id=update.message.chat_id)
        res = []
    if len(res) == 0:
        language_preference.add_item(chat_id=update.message.chat_id, language=lang)
    bot.send_message(update.message.chat_id, translate("greeting", lang))
    context.user_data["language"] = lang
    menu(update, context)
    return ConversationHandler.END
