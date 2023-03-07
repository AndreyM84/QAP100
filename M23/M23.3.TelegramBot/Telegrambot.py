"""Эхо бот"""
# import telebot
#
# TOKEN = "6124839638:AAHjQG45mLOyto_Bg6yrxe3JhhUVlcu_F6E"
#
# bot = telebot.TeleBot(TOKEN)
# @bot.message_handler()
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, message.text)
#
# bot.polling(none_stop=True)
"""Чтобы запустить бота, нужно воспользоваться методом polling. 
Параметр none_stop=True говорит, что бот должен стараться не прекращать работу при возникновении каких-либо ошибок."""

"""Обработчик сообщений """


# import telebot
#
# TOKEN = "6124839638:AAHjQG45mLOyto_Bg6yrxe3JhhUVlcu_F6E"
#
# bot = telebot.TeleBot(TOKEN)
# @bot.message_handler(commands=['start', 'help'])

"""Задание 23.3.1
Задание на самопроверку.

Допишите обработчик так, чтобы он из сообщения брал username и выдавал приветственное сообщение с привязкой к пользователю."""

# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")
# bot.polling(none_stop=True)

"""Ответное приветствие"""
# import telebot
#
# TOKEN = "6124839638:AAHjQG45mLOyto_Bg6yrxe3JhhUVlcu_F6E"
#
# bot = telebot.TeleBot(TOKEN)
# @bot.message_handler(commands=['start', 'help'])
# def repeat(message: telebot.types.Message):
#     print(message.text)
#     bot.reply_to(message, f'Приветствую, {message.chat.username}')
#
# bot.polling(none_stop=True)


"""Задание 23.3.2

Напишите обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD». 
Бот должен отвечать не отдельным сообщением, а с привязкой к картинке."""

import telebot

bot = telebot.TeleBot('6124839638:AAHjQG45mLOyto_Bg6yrxe3JhhUVlcu_F6E')

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

bot.polling(none_stop=True)