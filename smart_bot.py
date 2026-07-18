import telebot

TOKEN = '8811211432:AAGsWrVfiOI-Q9EQ4xRCRQdR4sxRh5iB42U'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Smartfonlar olami botiga xush kelibsiz. Menga istalgan smartfon modelini yozing, men sizga ma'lumotlarini topishga yordam beraman.")

@bot.message_handler(func=lambda message: True)
def get_info(message):
    phone = message.text
    bot.reply_to(message, f"Siz {phone} modelini qidirdingiz. Ma'lumotlarni bazadan izlamoqdaman...")

if __name__ == '__main__':
    bot.polling()
  
