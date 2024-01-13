import atexit

import telegram
from telegram.ext import Updater, Dispatcher, MessageHandler, Filters


class Archivarius:
    def __init__(self):
        self.bot = Updater(token='137856357:AAHZ9c5EbTtiyt_U2YZZdBQiv6nJZUMycp8', use_context=True)
        dispatcher: Dispatcher = self.bot.dispatcher

        dispatcher.add_handler(MessageHandler(Filters.text, self.process))

    def run(self):
        self.bot.start_polling()
        self.bot.idle()

    def stop(self):
        self.bot.stop()

    def process(self, update, context):
        print(update, context)


if __name__ == '__main__':
    app = Archivarius()
    app.run()
    atexit.register(app.stop)
