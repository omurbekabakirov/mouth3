from aiogram import types, Dispatcher
from config import bot
from database.DB import Database
from KEYBOARDS import inline_button
from aiogram.utils.deep_linking import _create_link
import os
import binascii
from const import REFERENCE_MENU_TEXT


async def reference_menu_call(call: types.CallbackQuery):
    datab = Database()
    data = datab.sql_select_referral_menu_info(
        owner=call.from_user.id
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text=REFERENCE_MENU_TEXT.format(
            user=call.from_user.first_name,
            balance=data['balance'],
            total=data['total_referrals']
        ),
        reply_markup=await inline_button.referral_keyboard()
    )


async def generate_link(call: types.CallbackQuery):
    datab = Database()
    user = datab.sql_select_user(tg_id=call.from_user.id)
    if not user['link']:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link("start", payload=token)
        print(link)
        datab.sql_update_link(
            link=link,
            tg_id=call.from_user.id
        )
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Here is your new link: {link}",
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Here is your old link: {user['link']}",
        )
async def my_refs(call: types.CallbackQuery):
    datab = Database()
    my_users = datab.sql_select_my_refs(call.from_user.id)
    list_ref = ''
    for user in my_users:
        list_ref += (f"@{user['username']}\n")
    await bot.send_message(
        chat_id=call.from_user.id,
        text=list_ref
    )

def register_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        reference_menu_call,
        lambda call: call.data == "reference_menu"
    )
    dp.register_callback_query_handler(
        generate_link,
        lambda call: call.data == "generate_link"
    )
    dp.register_callback_query_handler(
        my_refs,
        lambda call: call.data == "my_r"
    )