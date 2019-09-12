from telegram.ext import Updater
import os

def main():
    TOKEN = os.environ['BOT_TOKEN']
    updater = Updater(token=TOKEN)

    # logger.info("Configured handlers")
    # logger.info("Starting")
    updater.start_polling(poll_interval=1)


if __name__ == '__main__':
    main()
