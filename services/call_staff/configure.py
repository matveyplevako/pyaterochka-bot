from services.initial.functions import *
from telegram.ext import RegexHandler


def setup(updater):
    dispatcher = updater.dispatcher
    dispatcher.add_handler(RegexHandler("Позвать сотрудника магазина", menu))
