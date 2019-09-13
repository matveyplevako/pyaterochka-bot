from telegram.ext import Updater
from services.initial.configure import setup as setup_initial
from services.call_staff.configure import setup as setup_call_staff
from services.feedback.configure import setup as setup_feedback
from services.place_order.configure import setup as setup_place_order
from services.wrong_receipt.configure import setup as setup_wrong_receipt
import os

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s:%(lineno)d'
                           ' - %(message)s', handlers=[logging.StreamHandler()], level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    TOKEN = os.environ['BOT_TOKEN']
    updater = Updater(token=TOKEN)
    setup_initial(updater)
    setup_call_staff(updater)
    setup_feedback(updater)
    setup_place_order(updater)
    setup_wrong_receipt(updater)
    updater.start_polling(poll_interval=1)


if __name__ == '__main__':
    main()
