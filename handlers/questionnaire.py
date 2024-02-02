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
        reply_markup=await inline_button.second_question()
    )


async def college_answers(call: types.CallbackQuery):

    await bot.send_message(
        chat_id=call.from_user.id,
        text="it is not good idea ",
        reply_markup=await inline_button.second_question()
    )


async def car_type_questionnaire(call: types.CallbackQuery):

    await bot.send_message(
        chat_id=call.from_user.id,
        text="BMW OR MERCEDES ?",
        reply_markup=await inline_button.questionnaire_second_answers()
    )


async def bmw_answer(call: types.CallbackQuery):

    await bot.send_message(
        chat_id=call.from_user.id,
        text="Good,but mercedes is better",
        reply_markup=await inline_button.third_question()
    )


async def mercedes_answer(call: types.CallbackQuery):

    await bot.send_message(
        chat_id=call.from_user.id,
        text="That's  my boy",
        reply_markup=await inline_button.third_question()
    )


async def fruit_type_questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Lemon or Banana ?",
        reply_markup=await inline_button.questionnaire_third_answers()
    )


async def lemon_answer(call: types.CallbackQuery):
    print(call.data)
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Good, vitamin C is really helpful",
        eply_markup=await inline_button.questionnaire_third_answers()
    )


async def banana_answer(call: types.CallbackQuery):
    print(call.data)

    await bot.send_message(
        chat_id=call.from_user.id,
        text="That's  my boy",
        eply_markup=await inline_button.questionnaire_third_answers()
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(questionnaire, lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(university_answers, lambda call: call.data == "university")
    dp.register_callback_query_handler(college_answers, lambda call: call.data == "college")
    dp.register_callback_query_handler(car_type_questionnaire, lambda call: call.data == "next_question")
    dp.register_callback_query_handler(bmw_answer, lambda call: call.data == "bmw")
    dp.register_callback_query_handler(mercedes_answer, lambda call: call.data == "mercedes")
    dp.register_callback_query_handler(fruit_type_questionnaire, lambda call: call.data == "last_question")
    dp.register_callback_query_handler(lemon_answer, lambda call: call.data == "lemon")
    dp.register_callback_query_handler(banana_answer, lambda call: call.data == "banana")
