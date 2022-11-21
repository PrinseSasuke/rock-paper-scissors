from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.db_gino import db
BOT_TOKEN = "5627423061:AAFUk2pQ334NPNMgxaJ0vg_OdS8wZ-nBM5Y"
from data import config
bot = Bot(token = BOT_TOKEN, parse_mode= types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage =storage)
__all__ = ['bot', 'storage', 'dp', 'db']
