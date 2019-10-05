from services.initial.functions import *
from telegram.ext import CommandHandler, ConversationHandler
from telegram.ext import MessageHandler, Filters
from services.language import phrases


def setup(updater):
    dispatcher = updater.dispatcher
    language_selection = ConversationHandler(
         entry_points=[CommandHandler("start", start)],
         states={
             SELECT_LANG: [
                 MessageHandler(Filters.regex("^(🇬🇧 English|🇷🇺 Русский)$"), select_language)]
         },
         fallbacks=[MessageHandler(Filters.all, repeat)]

    )
    dispatcher.add_handler(MessageHandler(Filters.regex('|'.join(phrases["menu"].values())), menu))
    dispatcher.add_handler(language_selection)
