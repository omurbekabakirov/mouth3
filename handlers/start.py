from aiogram import types, Dispatcher
from config import bot,MEDIA_DESTINATION
from database.DB import Database
from KEYBOARDS import inline_button
from const import (
START_MENU
)

async def start_button(message: types.Message):
    datab = Database()
    datab.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    print(message)

    with open( MEDIA_DESTINATION + "bot-animation.gif","rb") as animation:
        await bot.send_animation(
            chat_id=message.chat.id,
            animation=animation,
            caption=START_MENU.format(
                name=message.from_user.first_name
            ),
            reply_markup=await inline_button.start_keyboard()
        )


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
