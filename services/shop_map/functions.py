from telegram.ext import ConversationHandler
from services.initial.configure import menu
from services.Stats import *


def show_map(update, context):
    bot = context.bot
    bot.send_document(chat_id=update.message.chat_id, document=open('services/shop_map/shop_map.jpg', 'rb'))
    menu(update, context)

    edit_stat("shop_map")

    return ConversationHandler.END
