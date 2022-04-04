import telebot
from telebot import types
import api
import database


token = '5148491223:AAHgZdUyyQMpRTa7tRFauyzqX41PqtG2Tgc'
bot = telebot.TeleBot(token)


signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo",
         "Virgo", "Libra", "Scorpio", "Sagittarius",
         "Capricorn", "Aquarius", "Pisces"]

days = ['today', 'yesterday', 'tomorrow']

def main():
    @bot.message_handler(commands=['start'])
    def srart_function(message):
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup(row_width=2)
        for sign in signs:
            btn = types.InlineKeyboardButton(sign, callback_data=sign)
            markup.add(btn)
        bot.send_message(user_id, 'Введите знак', reply_markup=markup)
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        database.set_user(user_id, username, first_name, last_name)


    @bot.callback_query_handler(func=lambda call: True)
    def markups(call):
        user_id = call.from_user.id
        from_tg = call.data
        if call.data in signs:
            markup = types.InlineKeyboardMarkup(row_width=2)
            for day in days:
                btn = types.InlineKeyboardButton(day, callback_data=from_tg + "/" + day)
                markup.add(btn)
            bot.send_message(user_id, 'введите день', reply_markup=markup)
        else:
            call_data = str(call.data).split('/')
            sign = call_data[0]
            day = call_data[1]
            resp = api.aztro(sign, day)
            bot.send_message(user_id, resp)

bot.polling(non_stop=True)