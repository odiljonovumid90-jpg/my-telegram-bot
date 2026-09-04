import telebot
import requests

# Tokenlar 100% aniq joylashtirildi
BOT_TOKEN = "8653913792:AAH6vAylg3viYoUIzKSw9gfoLbHtBoxfgdw"
AI_KEY = "AQ.Ab8RN6LcyoAOzmkLBFKiOVuOKltCu1A9Axs4Kw0fT-h6T1spVA"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Salom! Men Fizika bo'yicha sun'iy intellekt botiman. 🚀\nMenga fizika haqida xohlagan savolingizni bering! 💀")

@bot.message_handler(func=lambda message: True)
def javob_ber(message):
    fizik_prompt = f"Sen kuchli va zamonaviy fiziksang. Quyidagi savolga fizika qonunlari asosida, maktab o'quvchisiga tushunarli, juda qiziqarli va ba'zan '💀' emojisini ishlatib o'zbek tilida javob ber: {message.text}"
    
    url = f"https://googleapis.com{AI_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": fizik_prompt}]}]}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        res_json = response.json()
        text_reply = res_json['candidates'][0]['content']['parts'][0]['text']
        bot.reply_to(message, text_reply)
    except Exception as e:
        bot.reply_to(message, "Xatolik yuz berdi, iltimos qaytadan urinib ko'ring.")

bot.polling(none_stop=True)
