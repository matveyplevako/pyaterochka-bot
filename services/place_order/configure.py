from services.initial.functions import *
from telegram.ext import MessageHandler, Filters


def setup(updater):
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.regex("Заказать отсутсвующую продукцию"), menu))
