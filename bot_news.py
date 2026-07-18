from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(host='0.0.0.0', port=8080)

t = Thread(target=run)
t.start()


import telebot
from gnews import GNews

# Tokeningiz
bot = telebot.TeleBot("8893137947:AAGcTghT2JEr2gb7GOxuePCyHntUsAgwMpo")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! O'yin nomini yozing (masalan: Free Fire), men sizga yangiliklarini topib beraman.")

@bot.message_handler(func=lambda message: True)
def get_game_news(message):
    query = message.text
    bot.reply_to(message, f"'{query}' bo'yicha yangiliklar izlanmoqda...")
    
    uz_news = GNews(language='uz', country='UZ', max_results=2)
    en_news = GNews(language='en', country='US', max_results=2)
    
    bot.send_message(message.chat.id, "🇺🇿 O'zbekcha yangiliklar:")
    for item in uz_news.get_news(query):
        bot.send_message(message.chat.id, f"{item['title']}\n{item['url']}")
        
    bot.send_message(message.chat.id, "🇬🇧 English news:")
    for item in en_news.get_news(query):
        bot.send_message(message.chat.id, f"{item['title']}\n{item['url']}")

bot.polling()
  
