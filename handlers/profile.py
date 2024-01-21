import sqlite3
import random
import re
from aiogram import types, Dispatcher
from config import bot
from database.DB import Database
from KEYBOARDS import inline_button
from const import (
    PROFILE_TEXT,
    NOT_REGISTERED_TEXT
)


async def my_profile_call(call: types.CallbackQuery):
    datab = Database()
    profile = datab.sql_select_profile(
        tg_id=call.from_user.id
    )
    print(profile)
    if profile:
        with open(profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=profile['name'],
                    bio=profile['bio'],
                    age=profile['age'],
                    zodiac_sign=profile['zodiac sign'],
                    job=profile['job'],
                    gender=profile['gender']
                ),
                reply_markup=await inline_button.my_profile_keyboard()
            )
    if not profile:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=NOT_REGISTERED_TEXT.format(
                name=call.from_user.first_name
            )
        )


async def random_filter_profile_call(call: types.CallbackQuery):
    datab = Database()
    profile = datab.sql_select_all_profiles(owner=call.from_user.id)
    if not profile:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='You have liked all profiles, come later'
        )
        return
    if profile:
        random_profile = random.choice(profile)
        with open(random_profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=random_profile['name'],
                    bio=random_profile['bio'],
                    age=random_profile['age'],
                    zodiac_sign=random_profile['zodiac sign'],
                    job=random_profile['job'],
                    gender=random_profile['gender']
                ),
                reply_markup=await inline_button.like_dislike_keyboard(
                    owner=random_profile['telegram_id'])
            )


async def detect_like_profiles_call(call: types.CallbackQuery):
    datab = Database()
    owner = re.sub("like_", "", call.data)
    print(call.data)
    print(owner)
    try:
        datab.sql_insert_like(
            owner=owner,
            liker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='u have liked this profile!'
        )
    finally:
        await call.message.delete()
        await random_filter_profile_call(call=call)


async def detect_dislike_profiles_call(call: types.CallbackQuery):
    datab = Database()
    owner = re.sub("dis_", "", call.data)
    print(call.data)
    print(owner)
    try:
        datab.sql_insert_dislike(
            owner=owner,
            disliker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='You have disliked this profile!'
        )
    finally:
        await call.message.delete()
        await random_filter_profile_call(call=call)


def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        random_filter_profile_call,
        lambda call: call.data == "view_profiles"
    )
    dp.register_callback_query_handler(
        detect_like_profiles_call,
        lambda call: "like_" in call.data
    )
    dp.register_callback_query_handler(
         detect_dislike_profiles_call,
         lambda call: "dis_" in call.data
    )
