from telegram.ext import Updater
from services.initial.configure import setup as setup_initial
from services.shop_map.configure import setup as setup_map
from services.call_staff.configure import setup as setup_call_staff
from services.feedback.configure import setup as setup_feedback
from services.place_order.configure import setup as setup_place_order
from services.wrong_receipt.configure import setup as setup_wrong_receipt
from services.item_checker.configure import setup as setup_item_checker
import os

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    TOKEN = os.environ['BOT_TOKEN']
    updater = Updater(TOKEN, use_context=True)
    setup_map(updater)
    setup_call_staff(updater)
    setup_feedback(updater)
    setup_place_order(updater)
    setup_wrong_receipt(updater)
    setup_item_checker(updater)
    setup_initial(updater)

    updater.start_polling(poll_interval=5)


if __name__ == '__main__':
    main()
