import telebot
from telebot import types

bot = telebot.TeleBot('7940566830:AAExGibdl6WnlVNgffjN8BqJSpYFpsFbZ_A')

@bot.message_handler(commands=['start'])
def start(message):
    web_app_info = types.WebAppInfo("https://github.com/NeTook52/html-css-/blob/main/index.html")  # Замените на ваш URL
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Перейти в магазин", web_app=web_app_info)
    markup.add(button)

    bot.send_message(message.chat.id, "Добро пожаловать в магазин одежды!", reply_markup=markup)

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
