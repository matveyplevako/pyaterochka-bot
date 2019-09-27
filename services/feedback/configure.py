from services.initial.functions import *
from telegram.ext import MessageHandler, Filters, CommandHandler
from services.feedback.functions import *
from services.common_items import cancel


def setup(updater):
    dispatcher = updater.dispatcher

    adding_comment = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("Оставить отзыв о боте"), write_comment)],
        states={
            ADD_COMMENT: [MessageHandler(Filters.regex("^((?!Отменить).)*$"), send_comment)],
        },
        fallbacks=[MessageHandler(Filters.regex("Отменить"), cancel)]
    )

    dispatcher.add_handler(adding_comment)
