from services.initial.functions import *
from telegram.ext import CommandHandler
from telegram.ext import RegexHandler


def setup(updater):
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(RegexHandler("Меню", menu))
