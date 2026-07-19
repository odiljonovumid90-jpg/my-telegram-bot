import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import yt_dlp
import os

# TOKENINGIZNI SHU YERGA QO'YING
TOKEN = "8608936741:AAGERok01uO43C4VQIzNbQAyg1g51VLSEGo"
CHANNEL_ID = "@myoyinnews"  # Kanal username yoki ID

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Majburiy obunani tekshirish
async def check_subscription(user_id):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
        return False
    except:
        return False

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Salom! Video yuklash uchun menga link yuboring. \n\n⚠️ Eslatma: Ishlatishdan avval kanalimizga obuna bo'ling: https://t.me/myoyinnews")

@dp.message(F.text.startswith("http"))
async def download_handler(message: types.Message):
    user_id = message.from_user.id
    
    if not await check_subscription(user_id):
        kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL_ID.replace('@', '')}")]])
        await message.answer("Botdan foydalanish uchun kanalimizga obuna bo'ling!", reply_markup=kb)
        return

    await message.answer("Video yuklanmoqda, kuting...")
    
    url = message.text
    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        await message.answer_video(types.FSInputFile("video.mp4"))
        os.remove("video.mp4")
    except Exception as e:
        await message.answer(f"Xatolik yuz berdi: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
  
