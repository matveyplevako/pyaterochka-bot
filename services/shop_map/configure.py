from services.initial.functions import *
from services.shop_map.functions import *
from telegram.ext import MessageHandler, Filters
from services.language import phrases


def setup(updater):
    dispatcher = updater.dispatcher

    choosing_staff = MessageHandler(Filters.regex('|'.join(phrases["shop_map"].values())), show_map)

    dispatcher.add_handler(choosing_staff)
