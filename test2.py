
"""
This Bot uses the Updater class to handle the bot.
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import csv
import time
import numpy as np
import pandas as pd

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging

import math
import numpy as np
import pandas as pd

#require user's inputs

one_pax_office = 0
four_pax_office = 0
ten_pax_office = 0
big_mtg = 0
small_mtg = 0
com_labs = 0
colleagues = 0


#back-end calculations
toilets = 0
foyer = 0
mech_elect_rms = 0
pantry = 0

TOKEN = '582470685:AAFFRlMMpq39MCM4hLRiCAbc6IknY8xtyhU'


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

FIRST_Q, SECOND_Q, THIRD_Q, THIRD_Q_2, FOURTH_Q, FOURTH_Q_2, FIFTH_Q, FIFTH_Q_2, SIXTH_Q, SIXTH_Q_2, SEVENTH_Q, SEVENTH_Q_2, EIGHTH_Q, EIGHTH_Q_2, RESULTS, PHOTO, LOCATION, BIO = range(18)


def start(bot, update):
    reply_keyboard = [['Yes', 'No']]

    update.message.reply_text(
        'Hello! Thanks for activating me!\nIs your building an office building?\n\n'
        'Send /cancel to stop talking to me.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return FIRST_Q


def first_q(bot, update):
    user = update.message.from_user
    if update.message.text == 'Yes':
        update.message.reply_text('Thank you! From here onwards, i will need you to type out your answers!\nAre you the boss of this building?')
    else:
        update.message.reply_text(
            'Sorry, this program can only help you with office building feasibility studies, Good luck!')
        return ConversationHandler.END

    return SECOND_Q


def second_q(bot, update):
    user = update.message.from_user
    if update.message.text == 'yes':
        update.message.reply_text('How many offices for one do you require?\n'
                                  'Please answer in numbers')
        return THIRD_Q
    elif update.message.text == 'no':
        update.message.reply_text(
            'How many bosses do you have?\nPlease answer in numbers')
    else:
        while True:
            update.message.reply_text(
                'There is something wrong with your answer. Please be patient and try typing your answer again :)')
            return SECOND_Q

    return THIRD_Q_2


def third_q(bot, update):
    user = update.message.from_user
    global one_pax_office
    one_pax_office = int(update.message.text)

    update.message.reply_text(
              'You entered ' + str(one_pax_office))
    update.message.reply_text(
              'How many offices for four people do you require?')
    return FOURTH_Q

def third_q_2(bot, update):
    user = update.message.from_user
    global one_pax_office
    one_pax_office = int(update.message.text)
    update.message.reply_text(
              'You entered ' + str(one_pax_office))
    update.message.reply_text(
              'How many offices for middle management do you require?')

    return FOURTH_Q_2

def fourth_q(bot, update):
    user = update.message.from_user
    global four_pax_office
    four_pax_office = int(update.message.text)
    update.message.reply_text(
              'You entered ' + str(four_pax_office))
    update.message.reply_text(
              'How many offices for ten people do you require?')

    return FIFTH_Q

def fourth_q_2(bot, update):
    user = update.message.from_user
    global four_pax_office
    four_pax_office = int(update.message.text)
    update.message.reply_text(
              'You entered ' + str(four_pax_office))
    update.message.reply_text(
              'How many colleagues do you have? (Remember to count yourself!')

    return FIFTH_Q_2

def fifth_q(bot, update):
    user = update.message.from_user
    global ten_pax_office
    ten_pax_office = int(update.message.text)
    update.message.reply_text(
              'You entered ' + str(ten_pax_office))
    update.message.reply_text(
              'How many meeting rooms do you require?')

    return SIXTH_Q

def fifth_q_2(bot, update):
    user = update.message.from_user
    colleagues = int(update.message.text)
    global ten_pax_office
    ten_pax_office = int((colleagues * 4) / 10)
    update.message.reply_text(
              'You entered ' + str(colleagues))
    update.message.reply_text(
              'How many meeting rooms do your boss require?')

    return SIXTH_Q_2

def sixth_q(bot, update):
    user = update.message.from_user
    global big_mtg
    big_mtg = int(update.message.text)
    update.message.reply_text(
              'You entered ' + str(big_mtg))
    update.message.reply_text(
              'What about discussion rooms?')

    return SEVENTH_Q

def sixth_q_2(bot, update):
    user = update.message.from_user
    global big_mtg
    big_mtg = int(update.message.text)
    update.message.reply_text(
              'You entered ' + str(big_mtg))
    update.message.reply_text(
              'How many discussion rooms do your boss require?')

    return SEVENTH_Q_2

def seventh_q(bot, update):
    user = update.message.from_user
    global small_mtg
    small_mtg = int(update.message.text)
    update.message.reply_text(
              'You entered ' + str(small_mtg))
    update.message.reply_text(
              'We are getting to the end now! How many computer labs do you require?')

    return EIGHTH_Q

def seventh_q_2(bot, update):
    user = update.message.from_user
    global small_mtg
    small_mtg = int(update.message.text)
    update.message.reply_text(
              'You entered ' + str(small_mtg))
    update.message.reply_text(
              'Hang in there! We are ending soon!\nHow many computer labs do your boss needs?')

    return EIGHTH_Q_2

def eighth_q(bot, update):
    user = update.message.from_user
    global com_labs
    com_labs = int(update.message.text)
    update.message.reply_text(
              'You entered ' + str(com_labs))
    update.message.reply_text(
              'Thank you for answering the questions.\nWe will need some time to compute the requirements now.\nPress any key for the results to run..')

    return RESULTS

def eighth_q_2(bot, update):
    user = update.message.from_user
    global com_labs
    com_labs = int(update.message.text)
    update.message.reply_text(
              'You entered ' + str(com_labs))
    update.message.reply_text(
              'Thanks for answering the questions!\nWe will need some time to compute the requirements now.\nPress any key for the results to run..')

    return RESULTS

def results(bot, update):
    # formula for SOR calculations
    g_one_pax_office = one_pax_office * 12
    g_four_pax_office = four_pax_office * 32
    g_ten_pax_office = ten_pax_office * 40
    g_big_mtg = big_mtg * 54
    g_small_mtg = small_mtg * 12
    g_com_labs = com_labs * 35

    total_req_gfa = (
            (g_one_pax_office + g_four_pax_office + g_ten_pax_office + g_big_mtg + g_small_mtg + g_com_labs) * 1.2 * 1.3)

    # calcuating back-end requirements
    toilets = int(total_req_gfa / 1000)
    g_toilets = toilets * 44
    foyer = 20
    mech_elect_rms = int(total_req_gfa / 14)
    pantry = int(total_req_gfa / 1000)
    g_pantry = pantry * 20

    total_gfa = total_req_gfa + g_toilets + foyer + mech_elect_rms + g_pantry
    rom_cost = int(1800 * total_gfa)

    index = ["One_pax Office", "Four_pax Office", "Ten_pax Office", "Meeting Rooms", "Discussion Rooms",
             "Computer Labs", "Restrooms", "Pantry", "Foyer", "M&E rooms"]
    data = {
        "Quantities": pd.Series(
            [one_pax_office, four_pax_office, ten_pax_office, big_mtg, small_mtg, com_labs, toilets, pantry, "N.A.",
             "N.A."], index),
        "Gross Floor Area": pd.Series(
            [g_one_pax_office, g_four_pax_office, g_ten_pax_office, g_big_mtg, g_small_mtg, g_com_labs, g_toilets,
             g_pantry, foyer, mech_elect_rms, ], index)
    }
    df = pd.DataFrame(data, columns=["Quantities", "Gross Floor Area"])

    user = update.message.from_user
    update.message.reply_text(
              'The office building has a gross floor area of ' + str(total_gfa) + ' metre squares')
    update.message.reply_text(
              'The rough cost estimate is approximately $' + str(rom_cost))
    update.message.reply_text(
        'Type of Rooms  |  Quantities  |  Total Gross Floor Area')
    update.message.reply_text(
        'One_pax Office' + ' | ' + str(one_pax_office) + ' | ' + str(g_one_pax_office))
    update.message.reply_text(
        'Four_pax Office' + ' | ' + str(four_pax_office) + ' | ' + str(g_four_pax_office))
    update.message.reply_text(
        'Ten_pax Office' + ' | ' + str(ten_pax_office) + ' | ' + str(g_ten_pax_office))
    update.message.reply_text(
        'Meeting Rooms' + ' | ' + str(big_mtg) + ' | ' + str(g_big_mtg))
    update.message.reply_text(
        'Discussion Rooms' + ' | ' + str(small_mtg) + ' | ' + str(g_small_mtg))
    update.message.reply_text(
        'Computer Labs' + ' | ' + str(com_labs) + ' | ' + str(g_com_labs))
    update.message.reply_text(
        'Restrooms' + ' | ' + str(toilets) + ' | ' + str(g_toilets))
    update.message.reply_text(
        'Pantry' + ' | ' + str(pantry) + ' | ' + str(g_pantry))
    update.message.reply_text(
        'Foyer' + ' | ' + 'N.A.' + ' | ' + str(foyer))
    update.message.reply_text(
        'M&E rooms' + ' | ' + 'N.A.' + ' | ' + str(mech_elect_rms))
    update.message.reply_text('Thank you for chatting with me! I hope the information is useful and we can talk again some day :)\nClick /start to try again!')

    return ConversationHandler.END

def photo(bot, update):
    user = update.message.from_user
    photo_file = bot.get_file(update.message.photo[-1].file_id)
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text('Gorgeous! Now, send me your location please, '
                              'or send /skip if you don\'t want to.')

    return LOCATION


def skip_photo(bot, update):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text('I bet you look great! Now, send me your location please, '
                              'or send /skip.')

    return LOCATION


def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
                user_location.longitude)
    update.message.reply_text('Maybe I can visit you sometime! '
                              'At last, tell me something about yourself.')

    return BIO


def skip_location(bot, update):
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text('You seem a bit paranoid! '
                              'At last, tell me something about yourself.')

    return BIO


def bio(bot, update):
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Thank you! I hope we can talk again some day.')

    return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Goodbye! I hope we can talk again some day.\nEnter /start to do the feasibility study again.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states FIRST_Q, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            FIRST_Q: [RegexHandler('^(Yes|No)$', first_q)],

            SECOND_Q: [MessageHandler(Filters.text, second_q)],

            THIRD_Q: [MessageHandler(Filters.text, third_q)],

            THIRD_Q_2: [MessageHandler(Filters.text, third_q_2)],

            FOURTH_Q: [MessageHandler(Filters.text, fourth_q)],

            FOURTH_Q_2: [MessageHandler(Filters.text, fourth_q_2)],

            FIFTH_Q: [MessageHandler(Filters.text, fifth_q)],

            FIFTH_Q_2: [MessageHandler(Filters.text, fifth_q_2)],

            SIXTH_Q: [MessageHandler(Filters.text, sixth_q)],

            SIXTH_Q_2: [MessageHandler(Filters.text, sixth_q_2)],

            SEVENTH_Q: [MessageHandler(Filters.text, seventh_q)],

            SEVENTH_Q_2: [MessageHandler(Filters.text, seventh_q_2)],

            EIGHTH_Q: [MessageHandler(Filters.text, eighth_q)],

            EIGHTH_Q_2: [MessageHandler(Filters.text, eighth_q_2)],

            RESULTS: [MessageHandler(Filters.text, results)],

            PHOTO: [MessageHandler(Filters.photo, photo),
                    CommandHandler('skip', skip_photo)],

            LOCATION: [MessageHandler(Filters.location, location),
                       CommandHandler('skip', skip_location)],

            BIO: [MessageHandler(Filters.text, bio)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)


    # Start the Bot
    updater.start_polling()


    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()