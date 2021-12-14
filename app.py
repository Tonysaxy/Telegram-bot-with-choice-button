import config
import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types

#loging info
logging.basicConfig(level=logging.INFO)
#bot init
bot = Bot(config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# run long polling
if __name__ == '__main__':
    from handlers import dp, send_to_admin

    executor.start_polling(dp, on_startup=send_to_admin)