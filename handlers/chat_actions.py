import datetime
from aiogram import types, Dispatcher
from config import bot, GROUP_ID
from database.DB import Database
from const import (
    BAN_USER_TEXT,
    CHECK_BAN_USER_TEXT,
    CHECK_BAN_USER_TEXT_NEGATIVE
)
from profanity_check import predict_prob


async def check_ban_list(message: types. Message):
    datab = Database()
    potential = datab.sql_select_ban_users(
        tg_id=message.from_user.id
    )
    if potential:
        await bot. send_message(
            chat_id=message.chat.id,
            text=CHECK_BAN_USER_TEXT_NEGATIVE
        )

    else:
        await bot. send_message(
            chat_id=message.chat.id,
            text=CHECK_BAN_USER_TEXT
        )


async def chat_messages(message: types.Message):
    datab = Database()
    if message.chat.id == int(GROUP_ID):
        ban_words_predict_prob = predict_prob([message.text])
        print(message.chat)
        if ban_words_predict_prob > 0.8:
            potential = datab.sql_select_ban_users(
                tg_id=message.from_user.id
            )
            print(potential)
            if potential:

                datab.sql_update_ban_count(
                    tg_id=message.from_user.id,
                )

            elif not potential:
                datab.sql_insert_ban_user(
                    tg_id=message.from_user.id
                )

            await message.delete()
            await bot.send_message(
                chat_id=message.chat.id,
                text=BAN_USER_TEXT.format(
                    name=message.from_user.first_name,
                    count=potential['count'] + 1
                )
            )

            if potential["count"] >= 3:
                bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    until_date=datetime.datetime.now() + datetime.timedelta(minutes=5)
                )
            print(ban_words_predict_prob)


def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(check_ban_list, commands=['ban_list'])
    dp.register_message_handler(chat_messages)
