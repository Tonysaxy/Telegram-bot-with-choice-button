from app import bot, dp
from aiogram.types import Message
from config import admin_id
from aiogram.types import User

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот artem запущен")


@dp.message_handler()
async def echo(message: Message):
    text = f"Привет,Я Бот Артем. Я получил твоя:" + message.text + \
           " Хочешь немного сложного выбора? Тогда,пожалуйста, воспользуйтесь меню"
    await message.reply(text=text)
