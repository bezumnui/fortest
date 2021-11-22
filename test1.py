import asyncio
from aiogram import executor
from loader import db
from loader import bot
from loader import dp
from config import ADMINS
import handlers
from utils.notify_admins import on_shutdown_notify, on_startup_notify
from utils.payment import qiwi
import utils.misc




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(qiwi.listener())
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup_notify, on_shutdown=on_shutdown_notify)
