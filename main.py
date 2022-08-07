import dataclasses
import pytz
import telebot
import os
import requests
import time
import schedule
from datetime import datetime
from pytz import timezone
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot_token = '5512808396:AAGjLNbjHGowFuVIzMGZCIUH3_at7nEsDWY'
bot_chatID = '562854820'
bot = telebot.TeleBot(bot_token)

def create_text_simple_schedule_message(subject, teacher):
    text_message = "Наступна пара через 10хв\nПара:{subject_name}\nВикладач:{teacher_name}".format(subject_name=subject,teacher_name=teacher)
    return text_message

#time, not used, but in the future, maybe maybe...
format = " %H:%M"
now_utc = datetime.now(timezone('UTC'))
# print(now_utc.strftime(format))
now_asia = now_utc.astimezone(timezone('Europe/Kiev'))
# print(now_asia.strftime(format))

@bot.message_handler(commands=['next'])
def greet(message):
    list_message_id = []
    # потрібна ще одна функція, яка буде готувати пакети даних(ім'я викладча, назва пари, посилання і інше),скоріш за все тут будемо юзати словник
    for i in range(0, 2):
        replymarkup = InlineKeyboardMarkup([[InlineKeyboardButton(text="Посилання", url="www.google.com")]])
        message = bot.send_message(message.chat.id, text=create_text_simple_schedule_message('Hello', "dsfs"),reply_markup=replymarkup)
        list_message_id.append(message.message_id)
        bot.pin_chat_message(bot_chatID, message.message_id, disable_notification=True)
    time.sleep(5)
    for id in list_message_id:
        bot.unpin_chat_message(bot_chatID, id)
        bot.delete_message(bot_chatID, id)
bot.polling()

# не потрібний код, але най буде...
# def telegram_bot_sendtext(bot_message):
#     bot_token = '5512808396:AAGjLNbjHGowFuVIzMGZCIUH3_at7nEsDWY'
#     bot_chatID = '562854820'
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
#
#     response = requests.get(send_text)
#
#     return response.json()
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
