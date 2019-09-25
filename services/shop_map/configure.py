from services.initial.functions import *
from services.shop_map.functions import *
from telegram.ext import MessageHandler, Filters


def setup(updater):
    dispatcher = updater.dispatcher

    choosing_staff = MessageHandler(Filters.regex("Показать карту магазина"), show_map)

    dispatcher.add_handler(choosing_staff)
