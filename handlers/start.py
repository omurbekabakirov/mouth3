from aiogram import types, Dispatcher
from config import bot
from database.DB import Database
from KEYBOARDS import inline_button


async def start_button(message: types.Message):
    datab = Database()
    datab.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    print(message)
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Hi {message.from_user.first_name}',
        reply_markup=await inline_button.start_keyboard()
    )


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
