import dataclasses

import telebot
import os
import requests
import time
import schedule

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
def create_text_simple_schedule_message():
    test_message = "Наступна пара через 10хв\nПара:{name}\nВикладач:{f}".format(name="Математични",f="апрп")
    print(test_message)
create_text_simple_schedule_message()

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot('5512808396:AAGjLNbjHGowFuVIzMGZCIUH3_at7nEsDWY')


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "hey")



@bot.message_handler(commands=['hello'])
def greet(message):
    replymarkup = InlineKeyboardMarkup([[InlineKeyboardButton(text="Посилання", url="www.google.com")]])
    bot.send_message(message.chat.id, text=test_message, reply_markup=replymarkup)


bot.polling()
@dataclasses
class rozklad:
    day:str
    starttime:float
    name: str

# def telegram_bot_sendtext(bot_message):
#     bot_token = '5512808396:AAGjLNbjHGowFuVIzMGZCIUH3_at7nEsDWY'
#     bot_chatID = '562854820'
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
#     response = requests.get(send_text)
#
#     return response.json()
#
#
# def telegram_bot_sendtext(bot_message):
#     bot_token = '5512808396:AAGjLNbjHGowFuVIzMGZCIUH3_at7nEsDWY'
#     bot_chatID = '562854820'
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
#
#     response = requests.get(send_text)
#
#     return response.json()
#
#
# def report():
#     my_balance = 10  ## Replace this number with an API call to fetch your account balance
#     my_message = "Current balance is: {}".format(my_balance)  ## Customize your message
#     telegram_bot_sendtext(my_message)
#
#
# schedule.every().day.at("22:20").do(report)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#
