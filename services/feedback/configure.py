from services.initial.functions import *
from telegram.ext import MessageHandler, Filters, CommandHandler
from services.language import phrases
from services.feedback.functions import *
from services.common_items import cancel


def setup(updater):
    dispatcher = updater.dispatcher

    adding_comment = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('|'.join(phrases["leave_feedback"].values())), write_comment)],
        states={
            ADD_COMMENT: [MessageHandler(Filters.regex("^🚫(Отменить|Cancel)$"), cancel),
                          MessageHandler(Filters.text, send_comment)],
        },
        fallbacks=[MessageHandler(Filters.all, cancel)]
    )

    dispatcher.add_handler(adding_comment)
