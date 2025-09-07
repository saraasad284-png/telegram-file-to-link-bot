import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("❌ لطفاً متغیر محیطی BOT_TOKEN را تنظیم کنید!")
    exit()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=["document", "video", "audio", "photo"])
async def handle_file(msg: types.Message):
    file = msg.document or msg.video or msg.audio or msg.photo[-1]
    file_info = await bot.get_file(file.file_id)
    file_path = file_info.file_path

    download_link = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
    await msg.reply(f"✅ لینک مستقیم:\n{download_link}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
