from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import configparser
import logging
from telegram import ChatAction,ParseMode
from telegram.ext.dispatcher import run_async
from random import choice
import os


BOTNAME = 'codeshows_bot'

@run_async
def send_async(bot, *args, **kwargs):
    bot.sendMessage(*args, **kwargs)

#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('bot.ini')


updater = Updater('TOKEN')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(
        chat_id=update.message.chat_id, text= '''
Hey!! I'm CodeshowsBot currently working with Codeshows.
To hire me contact my admin.
Use /help to get help.
        '''
    )

def invitelink(bot, update):
    bot.sendChatAction(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['invite_link'])


def website(bot, update):
    bot.sendChatAction(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['website'])

def facebok(bot, update):
    bot.sendChatAction(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['facebook'])

def github(bot,update):
    bot.sendChatAction(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['github'])

def help(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(
         chat_id=update.message.chat_id,
         text='''
Use one of the following commands:
/invitelink - to get codeshows Telegram group link
/facebook - to get a link to codeshows  Facebook page
/website - to get codeshows website link
/github - link to codeshows github repos
            '''
    )

def welcome(bot, update):
    message = update.message
    chat_id = message.chat.id
    phrases = [
        'Hello {}! Welcome to {} .Please introduce yourself.'
        .format(message.new_chat_member.first_name,message.chat.title),
    ]
    text = choice(phrases)
    send_async(bot, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)

def intro(bot, update):
    message = update.message
    chat_id = message.chat.id
    text = 'Hi everyone,I am a python bot working to serve Codeshows.'
    send_async(bot, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML) 

def empty_message(bot, update):

    if update.message.new_chat_member is not None:
        if update.message.new_chat_member.username == BOTNAME:
            return intro(bot, update)
        else:
            return welcome(bot, update)

if __name__ == '__main__':
    dispatcher.add_handler(CommandHandler('website', website))
    dispatcher.add_handler(CommandHandler('facebook', facebok))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler([Filters.status_update], empty_message))
    dispatcher.add_handler(CommandHandler('invitelink',invitelink))
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('github',github))
    updater.start_polling()
    updater.idle()