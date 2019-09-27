from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ConversationHandler
from services.initial.configure import menu
import os


def show_map(update, context):
    bot = context.bot
    bot.send_photo(chat_id=update.message.chat_id, photo=open('services/shop_map/shop_map.jpg', 'rb'))
    menu(update, context)
    return ConversationHandler.END
