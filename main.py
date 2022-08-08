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

from bs4 import BeautifulSoup
import requests

url = "https://student.lpnu.ua/students_schedule?departmentparent_abbrname_selective=%D0%86%D0%9A%D0%9D%D0%86&studygroup_abbrname_selective=%D0%A1%D0%90-22&semestrduration=1"

response = requests.get(url)
page_content = BeautifulSoup(response.content, 'lxml')
days = page_content.find_all('div', class_='view-grouping')
for day in days:
    day_name = day.find('div', class_="view-grouping-header")
    para_names = day.find_all('div', class_='group_content')
    para_numbers = day.find_all('h3')
    # para_link = day.find_all('')
    print(day_name.text)
    array1 = []
    array2 = []
    dictionary = {}

    for para_number in para_numbers:
        # print(para_number.text)
        array1.append(para_number.text)
    print(array1)
    for para_name in para_names:
        # print(para_number.text)
        array2.append(para_name.text)
    print(array2)


    # print(array1)
    for para_number in para_numbers:
        for para_name in para_names:
            # print(para_name.text)
            array2.append(para_name.text)
            dictionary[para_number.text] = para_name.text
    # print(array2)
    print(dictionary)





# напевно не потрібний код
        # array_2 = dict(array2)

    # dictionary['array'] = array_2
    # print(dictionary)





# day_cards = page_content.find_all('div', class_='view-grouping-header')
#
# print(day_cards)
# for x in :
#     day_card_name = day_cards.find('div', class_='view-grouping-header')[day_card].text
#     print(day_card_name)


# print(day_card_name)
# tags = page_content.find_all('h2')
# for tag in tags:
#     print(tag.text)


# print(page_content.prettify())

#
# for i in page_content.find_all('div', attrs={'class':'view-grouping-content'}):
#             temp = i.parent.parent.contents[0]

# print("Schedule", temp)
