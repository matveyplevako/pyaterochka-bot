from services.initial.functions import *
from telegram.ext import MessageHandler, Filters
from services.place_order.functions import *


def setup(updater):
    dispatcher = updater.dispatcher

    choose_product_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("Заказать отсутсвующую продукцию"), choose_product)],
        states={
            CHOOSE_PRODUCT: [MessageHandler(Filters.regex("^((?!Отменить).)*$"), send_product_query)],
        },
        fallbacks=[MessageHandler(Filters.regex("Отменить"), cancel)]
    )

    dispatcher.add_handler(choose_product_handler)