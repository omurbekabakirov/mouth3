from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import (_create_link)
from config import bot, MEDIA_DESTINATION
from database.DB import Database
from KEYBOARDS import inline_button
from const import (
    START_MENU
)
from scraping.news_scraper import NewsScraper
import sqlite3


async def start_button(message: types.Message):
    datab = Database()
    datab.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    print(message.get_full_command())
    command = message.get_full_command()

    if command[1] != "":
        link = await _create_link('start', payload=command[1])
        owner = datab.sql_select_user_by_link(
            link=link
        )
        if owner['telegram_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="U can not use own link!!!"
            )
            return

        try:
            datab.sql_insert_referral(
                username=message.from_user.first_name,
                owner=owner['telegram_id'],
                referral=message.from_user.id
            )
            datab.sql_update_balance(
                owner=owner['telegram_id']
            )
        except sqlite3.IntegrityError:
            pass

    with open(MEDIA_DESTINATION + "bot-animation.gif", "rb") as animation:
        await bot.send_animation(
            chat_id=message.chat.id,
            animation=animation,
            caption=START_MENU.format(
                name=message.from_user.first_name
            ),
            reply_markup=await inline_button.start_keyboard()
        )


async def latest_kg_news(call: types.CallbackQuery):
    scraper = NewsScraper()
    data = scraper.parse_data()
    datab = Database()
    for link in data[:5]:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=scraper.START_URL + link
        )
        datab.sql_insert_kg_news(
            link=scraper.START_URL + link
        )


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
    dp.register_callback_query_handler(latest_kg_news, lambda call: call.data == 'latest_news')
