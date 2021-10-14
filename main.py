import os
import random
from telegram.ext import *
import dialogue as dialogue
import pandas_datareader as web


API_KEY = "2052420657:AAHLqVzRPvBca74olM_7QjL6H8GQbljq3XY"


def start(update, context):
    """
    Starting the telegram bot
    """
    update.message.reply_text("Hi! I'm a bot! Type in /help to look at the commands")


def help(update, context):
    """
    Help function
    """
    update.message.reply_text(
        """Check out the commands: 
         /start - Start the bot 
         /help - Help function
         /content - Get the content of the website
         /contact - Get the contact information
         /facts - Get facts 
         """
    )


def content(update, context):
    """
    Get the content of the website
    """
    update.message.reply_text(
        """The content of the website is:
         <insert website>
         """
    )


def contact(update, context):
    """
    Get the contact information
    """
    update.message.reply_text(
        """The contact information is:
          <insert email>
         """
    )


def handle_message(update, context):
    """
    Handle the message
    """
    userText = str(update.message.text).lower()
    answer = dialogue.sample_responses(userText)
    update.message.reply_text(answer)


def facts(update, contet):
    """
    Get the facts
    """
    fact = random.choice(dialogue.facts)
    update.message.reply_text(fact)


def main():
    # Updater Object
    updater = Updater(API_KEY, use_context=True)
    disp = updater.dispatcher

    # Command Handler
    disp.add_handler(CommandHandler("start", start))  # /start
    disp.add_handler(CommandHandler("help", help))  # /help
    disp.add_handler(CommandHandler("content", content))  # /content
    disp.add_handler(CommandHandler("contact", contact))  # /contact
    disp.add_handler(CommandHandler("facts", facts))  # /contact
    disp.add_handler(MessageHandler(Filters.text, handle_message))  # /message

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
