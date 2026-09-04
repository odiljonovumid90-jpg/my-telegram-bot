import telebot
import google.generativeai as genai

BOT_TOKEN = "8653913792:AAH6vAylg3viYoUIzKSw9gfoLbHtBoxfgdw"
AI_KEY = "AQ.Ab8RN6LcyoAOzmkLBFKiOVuOKltCu1A9Axs4Kw0fT-h6T1spVA"

# AI tizimini sozlaymiz
genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-pro')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Salom! Men Fizika bo'yicha sun'iy intellekt botiman. 🚀\nMenga fizika haqida xohlagan savolingizni bering! 💀")

@bot.message_handler(func=lambda message: True)
def javob_ber(message):
    fizik_prompt = f"Sen kuchli va zamonaviy fiziksang. Quyidagi savolga fizika qonunlari asosida, maktab o'quvchisiga tushunarli, qiziqarli va ba'zan '💀' emojisini ishlatib o'zbek tilida javob ber: {message.text}"
    try:
        response = model.generate_content(fizik_prompt)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Xatolik yuz berdi, iltimos qaytadan urinib ko'ring.")

bot.polling(none_stop=True)
