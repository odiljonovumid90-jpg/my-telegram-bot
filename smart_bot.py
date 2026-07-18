import telebot

TOKEN = '8811211432:AAGsWrVfiOI-Q9EQ4xRCRQdR4sxRh5iB42U'
bot = telebot.TeleBot(TOKEN)

# Oddiy bazamiz (kelajakda buni kengaytiramiz)
phones_db = {
    "samsung s26": "📱 Model: Samsung S26\n⚙️ Protsessor: Snapdragon 8 Gen 5\n💾 Xotira: 12GB RAM / 256GB\n🔋 Batareya: 5000 mAh",
    "iphone 17": "📱 Model: iPhone 17\n⚙️ Protsessor: A19 Bionic\n💾 Xotira: 8GB RAM / 256GB\n🔋 Batareya: 4500 mAh"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Smartfonlar olami botiga xush kelibsiz. Telefon nomini yozing (masalan: Samsung S26).")

@bot.message_handler(func=lambda message: True)
def get_phone(message):
    query = message.text.lower()
    if query in phones_db:
        bot.reply_to(message, phones_db[query])
    else:
        bot.reply_to(message, "Kechirasiz, bu telefon bazada yo'q. Boshqa nom yozib ko'ring.")

if __name__ == '__main__':
    bot.polling()
    
