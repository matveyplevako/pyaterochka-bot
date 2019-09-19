from services.initial.functions import *
from services.call_staff.functions import *
from telegram.ext import MessageHandler, Filters


def setup(updater):
    dispatcher = updater.dispatcher

    choosing_staff = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("Позвать сотрудника магазина"), select_staff)],
        states={
            CALL_STUFF: [MessageHandler(Filters.regex("Позвать администратора"), call_admin),
                         MessageHandler(Filters.regex("Позвать кассира"), call_cashier)],
        },
        fallbacks=[MessageHandler(Filters.regex("Отменить"), cancel)]
    )

    dispatcher.add_handler(choosing_staff)
