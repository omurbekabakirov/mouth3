import sqlite3

from aiogram import types, Dispatcher
from config import bot,MEDIA_DESTINATION
from database.DB import Database
from KEYBOARDS import inline_button
from const import (
START_MENU,
PROFILE_TEXT
)
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    zodiac_sign = State()
    job = State()
    gender = State()
    photo = State()


async def register(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Send me your nickname, please!"
    )
    await RegistrationStates.nickname.set()

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your biography, please!"
    )
    await RegistrationStates.next()



async def load_bio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["bio"] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your Age(use only number), please!"
    )
    await RegistrationStates.next()


async def load_age(message: types.Message, state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="I told you send me only numbers \n"
                 "registration failed\n"
                 "restart registration process"
        )
        await state.finish()
        return


    async with state.proxy() as data:
        data["age"] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your Zodiac Sign\n"
             " Aries\n"
             ", Taurus\n"
             ", Gemini\n, Cancer\n"
             ", Leo\n"
             ", Virgo\n"
             ", Libra\n"
             ", Scorpio\n"
             ", Sagittarius\n"
             ", Capricorn\n"
             ", Aquarius\n"
             ", Pisces\n"
             ", please write only zodiac sign that is in the list!!!"
    )
    await RegistrationStates.next()

zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo','Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius','Pisces']
async def load_zodiac_sign(message: types.Message, state: FSMContext):
    if message.text.capitalize() in zodiac_signs:
        async with state.proxy() as data:
            data["zodiac sign"] = message.text
            print(data)
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Send me your job, please!"
        )
        await RegistrationStates.next()
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="I told you what you needed to wrote\n"
                 "registration failed\n"
                 "restart registration process"
        )
        await state.finish()

async def load_job(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["job"] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your gender(write male or female), please!"
    )
    await RegistrationStates.next()

genders = ["male", "female"]
async def load_gender(message: types.Message, state: FSMContext):
    if message.text.lower() in genders:
        async with state.proxy() as data:
            data["gender"] = message.text
            print(data)
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Send me your photo,please !"
                 "(only in photo mode)"
        )
        await RegistrationStates.next()
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="I told you to write male or female\n"
                 "registration failed\n"
                 "restart registration process"
        )
        await state.finish()


async def load_photo(message: types.Message, state: FSMContext):
    datab = Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )
    print(message.photo)
    print(path.name)
    async with state.proxy() as data:
        datab.sql_insert_profile(
            tg_id=message.from_user.id,
            nickname=data['name'],
            bio=data['bio'],
            age=data['age'],
            zodiac_sign=data['zodiac sign'],
            job=data['job'],
            gender=data['gender'],
            photo=path.name
        )

    with open(path.name, "rb") as photo:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=PROFILE_TEXT.format(
                nickname=data['name'],
                bio=data['bio'],
                age=data['age'],
                zodiac_sign=data['zodiac sign'],
                job=data['job'],
                gender=data['gender'],
            ),
            reply_markup=await inline_button.start_keyboard()
        )
    await bot.send_message(
        chat_id=message.from_user.id,
        text="You have successfully registered ,Congratulations!!!!"
    )


def register_registration_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        register,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_name,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_bio,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_zodiac_sign,
        state=RegistrationStates.zodiac_sign,
        content_types=['text']
    )
    dp.register_message_handler(
        load_job,
        state=RegistrationStates.job,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )