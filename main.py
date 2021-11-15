import os
import random
import threading
from telegram.ext import *
import dialogue as dialogue
from telegram import ParseMode
import pandas_datareader as web


API_KEY = "1918094150:AAHk0F7P77RvbQhddHONLgEcPOWIxGAd_CQ"


def start(update, context):
    """
    Starting the telegram bot
    """
    update.message.reply_text("Hi! I'm a bot! Type in /help to look at the commands")


def help(update, context):
    """
    Help function`
    """
    update.message.reply_text(
        """Check out the commands: 

✅ /start - Start the bot .
✅ /stop - Stop the bot. 
✅ /help - Help function.
✅ /donate - Get the content of the website.
✅ /contact - Get the contact information.
✅ /facts - Get facts about Akshaya Patra Foundation.
✅ /verifiedlinks - Get verified links.
✅ /OngoingCampaigns - Donate / Participate in campaigns.
         """
    )


def donate(update, context):
    """
    Get the donation link of the website
    """
    update.message.reply_text(
        """
        <a href="https://www.akshayapatra.org/onlinedonations">Donate to Akshaya Patra Foundation</a>
         
         """,
        parse_mode=ParseMode.HTML,
    )


def contact(update, context):
    """
    Get the contact information
    """
    update.message.reply_text(
        """
<a href="https://www.akshayapatra.org/">🌍 Akshaya Patra Official Website</a>

<a href="https://twitter.com/AkshayaPatra?s=20">📢 Twitter</a>

<a href ="https://www.linkedin.com/company/the-akshaya-patra-foundation/">📡 LinkedIn</a>

<a href="https://www.facebook.com/TheAkshayapatraFoundation">💬 Facebook</a>

<a href="https://www.youtube.com/channel/UCQ8TSAaij9nwDLfiaLotDDA">🔗 YouTube</a>

<a href="https://www.instagram.com/theakshayapatrafoundation/">📸 Instagram</a>

<a href="https://in.pinterest.com/akshayapatra/">📫 Pinterest</a>

📫 Email: infodesk@akshayapatra.org
        """,
        parse_mode=ParseMode.HTML,
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


def events(update, context):
    """
    Get the events
    """
    update.message.reply_text(
        """

<a href="https://www.outlookindia.com/website/story/poshan-news-world-food-day-heres-what-the-akshaya-patra-foundation-aims-for/397800/">📅 : Outlook India</a>

        """,
        parse_mode=ParseMode.HTML,
    )


def verifiedlinks(update, context):
    """
    Get the verified links
    """
    update.message.reply_text(
        """
 
<a href="https://www.outlookindia.com/website/story/poshan-news-world-food-day-heres-what-the-akshaya-patra-foundation-aims-for/397800/">📰 Outlook India</a>

<a href="https://www.giveindia.org/nonprofit/the-akshaya-patra-foundation/">📰 giveindia</a>

<a href="https://telanganatoday.com/akshaya-patra-the-inexhaustible-food-vessel-in-covid-times">📰 Telangana Today</a>
 
<a href="https://frontline.thehindu.com/the-nation/independent-trustees-of-akshaya-patra-foundation-submit-resignations-amid-allegations/article33229907.ece">📰 The Hindu</a>

<a href="https://www.iskconbangalore.org/akshaya-patra/">📰 ISKCON Bangalore</a>


 
    """,
        parse_mode=ParseMode.HTML,
    )


def events(update, context):
    """
    Get the events
    """
    update.message.reply_text(
        """

<a href="https://www.outlookindia.com/website/story/poshan-news-world-food-day-heres-what-the-akshaya-patra-foundation-aims-for/397800/">📅 : Outlook India</a>

        """,
        parse_mode=ParseMode.HTML,
    )


def OngoingCampaigns(update, context):
    """
    Get the ongoing Campaigns
    """
    update.message.reply_text(
        """

        <strong>API Integration to be done with the techincal team of TAPF.</strong>

        """,
        parse_mode=ParseMode.HTML,
    )


def stop(bot, update):
    threading.Thread(target=shutdown).start()


updater = Updater(API_KEY, use_context=True)


def shutdown():
    updater = Updater(API_KEY)
    updater.stop()
    updater.is_idle = False


def main():
    # Updater Object
    disp = updater.dispatcher

    # Command Handler
    disp.add_handler(CommandHandler("start", start))  # /start
    disp.add_handler(CommandHandler("stop", stop))  # /stop
    disp.add_handler(CommandHandler("help", help))  # /help
    disp.add_handler(CommandHandler("donate", donate))  # /content
    disp.add_handler(CommandHandler("contact", contact))  # /contact
    disp.add_handler(CommandHandler("facts", facts))  # /facts
    disp.add_handler(CommandHandler("events", events))  # /events
    disp.add_handler(CommandHandler("OngoingCampaigns", OngoingCampaigns))  # /events
    disp.add_handler(CommandHandler("verifiedlinks", verifiedlinks))  # /verified-links
    disp.add_handler(MessageHandler(Filters.text, handle_message))  # /message

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
