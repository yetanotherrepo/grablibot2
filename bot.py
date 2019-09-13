import requests
from bs4 import BeautifulSoup
import datetime
import telebot
from telebot import apihelper

apihelper.proxy = {'https': 'socks5://729219:z5X6ipRm@orbtl.s5.opennetwork.cc:999'}

bot = telebot.TeleBot('642865171:AAECH4AepSqIy7FPycU6EeJU7oJD00ICKdM')

dayweek = ""
if datetime.datetime.today().weekday() == 0:
    dayweek = "Понедельник"
elif datetime.datetime.today().weekday() == 1:
    dayweek = "Вторник"
elif datetime.datetime.today().weekday() == 2:
    dayweek = "Среда"
elif datetime.datetime.today().weekday() == 3:
    dayweek = "Четверг"
elif datetime.datetime.today().weekday() == 4:
    dayweek = "Пятница"
elif datetime.datetime.today().weekday() == 5:
    dayweek = "Сегодня ланча нет"
elif datetime.datetime.today().weekday() == 6:
    dayweek = "Сегодня ланча нет"
today_date = datetime.datetime.strftime(datetime.datetime.now(), '%d') + " " + dayweek
cookies = dict(p18='yes')
menu = requests.get("http://grabli.ru/magazin/#formula", cookies=cookies)
soup = BeautifulSoup(menu.text, 'html.parser')
div = soup.find("h3").find_parent()
msg = ""


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "используй /menu")


@bot.message_handler(commands=['menu'])
def handle_message(message):
    for i in range(5):
        if dayweek in div("h3")[i].get_text():
            msg = div("h3")[i].get_text(), div("ul")[i].get_text()
    if "нет" in dayweek:
        bot.send_message(message.chat.id, dayweek)
    else:
        for i in msg:
            bot.send_message(message.chat.id, i)

bot.polling()
