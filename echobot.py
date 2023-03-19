from telebot import TeleBot
from json import load

with open('tempData.json', 'r') as data:
    temp = load(data)
    TG_API_TOKEN = temp["telegram"]

bot = TeleBot(TG_API_TOKEN)


@bot.message_handler(commands=['start'])
def welcome_msg(message):
    bot.reply_to(message, """\
Привет, я буду повторять за тобой каждое твоё слово))
(Я тролль из 2003)
""")


@bot.message_handler()
def answer(message):
    bot.reply_to(message, text=message.text)

bot.infinity_polling()
