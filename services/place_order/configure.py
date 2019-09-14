from services.initial.functions import *
from telegram.ext import MessageHandler, Filters
from services.place_order.functions import *


def setup(updater):
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.regex("Заказать отсутсвующую продукцию"), choose_product))

    choose_product_text_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("Отправить название"), input_text)],
        states={
            ADD_TEXT: [MessageHandler(Filters.regex("^((?!Отменить).)*$"), send_product_text)],
        },
        fallbacks=[MessageHandler(Filters.regex("Отменить"), cancel)]
    )

    choose_product_photo_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("Отправить фото и название"), input_photo)],
        states={
            ADD_PHOTO: [MessageHandler(Filters.photo, send_product_photo)],
            ADD_PHOTO_TEXT: [MessageHandler(Filters.regex("^((?!Отменить).)*$"), send_product_text)],
        },
        fallbacks=[MessageHandler(Filters.regex("Отменить"), cancel)]
    )

    dispatcher.add_handler(choose_product_text_handler)
    dispatcher.add_handler(choose_product_photo_handler)
