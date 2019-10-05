from services.call_staff.functions import *
from telegram.ext import MessageHandler, Filters, CallbackQueryHandler
from services.language import phrases
import re


def setup(updater):
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.regex('|'.join(phrases["call_staff"].values())), select_staff))
    dispatcher.add_handler(CallbackQueryHandler(call_admin, pattern=re.compile('^call_admin$')))
    dispatcher.add_handler(CallbackQueryHandler(call_cashier, pattern=re.compile('^call_cashier$')))
