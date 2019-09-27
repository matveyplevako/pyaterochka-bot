from telegram.ext import MessageHandler, Filters, CallbackQueryHandler
from services.common_items import cancel
from services.item_checker.functions import *
import re


def setup(updater):
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.regex("Узнать о наличии товара у сотрудников"), choose_product))

    choose_product_to_get_info_conversation = ConversationHandler(
        entry_points=[CallbackQueryHandler(input_text, pattern=re.compile('^send_name_info$')),
                      CallbackQueryHandler(input_photo, pattern=re.compile('^send_photo_and_name_info$'))],
        states={
            ADD_TEXT: [MessageHandler(Filters.regex("^((?!Отменить).)*$"), send_product_text)],
            ADD_PHOTO: [MessageHandler(Filters.photo, send_product_photo)],
            ADD_PHOTO_TEXT: [MessageHandler(Filters.regex("^((?!Отменить).)*$"), send_product_text_photo)],
        },
        fallbacks=[MessageHandler(Filters.text, cancel)]
    )

    dispatcher.add_handler(choose_product_to_get_info_conversation)
    dispatcher.add_handler(CallbackQueryHandler(process_selection, pattern=re.compile('^info.*')))
