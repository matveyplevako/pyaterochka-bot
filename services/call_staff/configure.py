from services.call_staff.functions import *
from telegram.ext import MessageHandler, Filters, CallbackQueryHandler
import re


def setup(updater):
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.regex("Позвать сотрудника магазина"), select_staff))
    dispatcher.add_handler(CallbackQueryHandler(call_admin, pattern=re.compile('^call_admin$')))
    dispatcher.add_handler(CallbackQueryHandler(call_cashier, pattern=re.compile('^call_cashier$')))
