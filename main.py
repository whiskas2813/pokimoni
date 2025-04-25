import telebot 
from config import token
from random import choice
from logic import Pokemon
from datetime import datetime, timedelta
bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")
@bot.message_handler(commands=['kormit'])
def fact_handler(message):
    feeed = choice(['ваш покемон рад и сыт '])
    bot.reply_to(message, feeed)


@bot.message_handler(commands=['infa'])
def info(message):
    username = message.from_user.username

    if username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
    else:
        bot.send_message(message.chat.id, 'у тебя нету покемона')


bot.infinity_polling(none_stop=True)