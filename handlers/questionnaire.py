from aiogram import types, Dispatcher
from config import bot
from KEYBOARDS import inline_button


async def questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="University or College ?",
        reply_markup=await inline_button.questionnaire_first_answers()
    )


async def university_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool.",
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text='BMW OR MERCEDES ?',
        reply_markup=await inline_button.questionnaire_second_answers()
    )



async def college_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="it is not good idea ",
    )

    await bot.send_message(
        chat_id=call.from_user.id,
        text='lemon or Banana ?',
        reply_markup=await inline_button.questionnaire_third_answers()
    )



def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(questionnaire,
    lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(university_answers,
    lambda call: call.data.startswith("1ans_"))
    dp.register_callback_query_handler(college_answers,
    lambda call: call.data.startswith("2ans_"))




