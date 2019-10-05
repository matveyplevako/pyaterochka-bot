from services.initial.functions import *
from telegram.ext import MessageHandler, Filters
from services.wrong_receipt.functions import *
from services.common_items import cancel
from services.language import phrases


def setup(updater):
    dispatcher = updater.dispatcher

    adding_comment = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('|'.join(phrases["wrong_tag"].values())), wrong_receipt)],
        states={
            ADD_COMMENT_RECEIPT: [MessageHandler(Filters.photo, send_photo)],
        },
        fallbacks=[MessageHandler(Filters.all, cancel)]
    )

    dispatcher.add_handler(adding_comment)
