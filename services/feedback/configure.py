from services.initial.functions import *
from telegram.ext import MessageHandler, Filters, CommandHandler
from services.feedback.functions import *


def setup(updater):
    dispatcher = updater.dispatcher

    adding_comment = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("Оставить отзыв о боте"), write_comment)],
        states={
            ADD_COMMENT: [MessageHandler(Filters.regex("^((?!Отменить).)*$"), send_comment, pass_chat_data=True,
                                         pass_job_queue=True)],
        },
        fallbacks=[MessageHandler(Filters.regex("Отменить"), cancel)]
    )

    dispatcher.add_handler(adding_comment)
