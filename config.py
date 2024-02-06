from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PROXY_URL = "http://proxy.server:3128"
storage = MemoryStorage()
Token = config("TOKEN")
bot = Bot(token=Token,proxy=PROXY_URL)
dp = Dispatcher(bot=bot, storage=storage)
MEDIA_DESTINATION = config("MEDIA_DESTINATION")
GROUP_ID = config("GROUP_ID")
