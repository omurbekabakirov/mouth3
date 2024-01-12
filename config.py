from aiogram import Dispatcher, Bot
from decouple import config

Token = config("TOKEN")
bot = Bot(token=Token)
dp = Dispatcher(bot=bot)
