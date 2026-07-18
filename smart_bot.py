import telebot
import os
from flask import Flask
import threading

TOKEN = '8811211432:AAGsWrVfiOI-Q9EQ4xRCRQdR4sxRh5iB42U'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Smartfonlar olami botiga xush kelibsiz.")

@bot.message_handler(func=lambda message: True)
def get_phone(message):
    bot.reply_to(message, f"Siz '{message.text}' ni qidirdingiz.")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    threading.Thread(target=bot.polling).start()
    app.run(host='0.0.0.0', port=port)
    
