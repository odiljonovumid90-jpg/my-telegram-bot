import telebot
from google import genai

# Sizning shaxsiy ma'lumotlaringiz joylashtirildi
BOT_TOKEN = "8653913792:AAH6vAylg3viYoUIzKSw9gfoLbHtBoxfgdw"
AI_KEY = "AQ.Ab8RN6KuL8WgkT2b44gxgzOPff0LbnrIcjRBqawN-aJfCaVtxg"

bot = telebot.TeleBot(BOT_TOKEN)
ai_client = genai.Client(api_key=AI_KEY)

# Botga /start buyrug'i berilgandagi salomlashish xabari
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Salom! Men Fizika bo'yicha sun'iy intellekt botiman. 🚀\nMenga fizika, koinot yoki tabiat qonunlari haqida xohlagan savolingizni bering, sizga ilmiy va qiziqarli javob beraman! 💀")

# Har qanday matnli xabarga AI orqali javob qaytarish
@bot.message_handler(func=lambda message: True)
def javob_ber(message):
    # Sun'iy intellektga bot o'zini qanday tutishi kerakligini uqtiramiz
    fizik_prompt = f"Sen kuchli va zamonaviy fiziksang. Quyidagi savolga fizika qonunlari asosida, maktab o'quvchisiga tushunarli, juda qiziqarli va biroz hazilomuz (ba'zan '💀' emojisini ishlatib) javob ber: {message.text}"
    
    try:
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=fizik_prompt,
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Xatolik yuz berdi, iltimos qaytadan urinib ko'ring.")

print("Bot ishga tushdi...")
bot.polling(none_stop=True)
      
