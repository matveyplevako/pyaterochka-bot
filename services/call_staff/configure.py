from services.initial.functions import *
from services.call_staff.functions import *
from telegram.ext import MessageHandler, Filters


def setup(updater):
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.regex("Позвать сотрудника магазина"), select_staff))
    dispatcher.add_handler(MessageHandler(Filters.regex("Позвать администратора"), call_admin))
    dispatcher.add_handler(MessageHandler(Filters.regex("Позвать кассира"), call_cashier))

