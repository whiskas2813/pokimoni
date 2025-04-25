import telebot 
from config import token
from random import choice
from logic import Pokemon
from datetime import datetime
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
    feed = choice(['ваш покемон рад и сыт '])
    bot.reply_to(message, feed)
@bot.message_handler(commands=['feed'])
def feed(self, feed_interval = 20, hp_increase = 10 ):
    current_time = datetime.now()  
    delta_time = timedelta(seconds=feed_interval)  
    if (current_time - self.last_feed_time) > delta_time:
        self.hp += hp_increase
        self.last_feed_time = current_time
        return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
    else:
        return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"


@bot.message_handler(commands=['infa'])
def info(message):
    username = message.from_user.username

    if username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
    else:
        bot.send_message(message.chat.id, 'у тебя нету покемона')


bot.infinity_polling(none_stop=True)