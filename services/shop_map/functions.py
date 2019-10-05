from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ConversationHandler
from services.initial.configure import menu
import os
import datetime
from services.Statistics.Stats import *


def show_map(update, context):
    bot = context.bot
    bot.send_document(chat_id=update.message.chat_id, document=open('services/shop_map/shop_map.jpg', 'rb'))
    menu(update, context)

    now = datetime.datetime.now()
    current_date = str('-'.join([str(now.day), str(now.month), str(now.year)]))

    statistics.edit_stat(current_date, "shop_map")

    return ConversationHandler.END
