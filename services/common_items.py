from services.initial.functions import menu
from telegram.ext import ConversationHandler, MessageHandler, Filters


def cancel(update, context):
    menu(update, context)

    return ConversationHandler.END
