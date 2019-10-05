from services.initial.functions import *
from telegram.ext import MessageHandler, Filters, CallbackQueryHandler
from services.language import phrases
from common_items import cancel
from services.place_order.functions import *


def setup(updater):
    dispatcher = updater.dispatcher

    choose_product_conversation = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('|'.join(phrases["place_order"].values())),
                                     choose_product)],
        states={
            SELECT_TYPE: [MessageHandler(Filters.regex('|'.join(phrases["send_name"].values())), input_text),
                          MessageHandler(Filters.regex('|'.join(phrases["send_name_and_photo"].values())), input_photo)],
            ADD_TEXT: [MessageHandler(Filters.regex("^((?!Отменить|Cancel).)*$"), send_product_text)],
            ADD_PHOTO: [MessageHandler(Filters.photo, send_product_photo)],
            ADD_PHOTO_TEXT: [MessageHandler(Filters.regex("^((?!Отменить|Cancel).)*$"), send_product_text_photo)],
        },
        fallbacks=[MessageHandler(Filters.all, cancel)]
    )

    dispatcher.add_handler(choose_product_conversation)
    dispatcher.add_handler(CallbackQueryHandler(process_selection, pattern="^order.*"))
