# coding=utf-8           # -*- coding: utf-8 -*-
import io
import sys
from telegram.ext import Updater
import logging
from telegram.ext import MessageHandler, Filters

import core

bot_token = ""
with open("token.txt") as token_file:
    bot_token = token_file.readline().rstrip('\n')

updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Заменяю обсценную лексику на подобающие слова, случайно.")

def read_dictionary():
    file = io.open("russian-words-master/russian.txt", "r", encoding='windows-1251')
    return file.readlines()

dictionary = read_dictionary()

def handle_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=core.deprofanity(dictionary, update.message.text))

message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)



def main():
    dispatcher.add_handler(message_handler)
    updater.start_polling()
    # strings = sys.stdin.readlines()
    # for s in strings:
    #     core.deprofanity(dictionary, s)

if __name__ == "__main__":
    main()
