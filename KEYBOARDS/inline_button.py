from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def questionnaire_first_answers():
    markup = InlineKeyboardMarkup()
    university_button = InlineKeyboardButton(
        "University",
        callback_data="1ans_university"
    )
    college_button = InlineKeyboardButton(
        "College",
        callback_data="1ans_college"
    )
    markup.add(university_button)
    markup.add(college_button)
    return markup

async def questionnaire_second_answers():
    markup = InlineKeyboardMarkup()
    bmw_button = InlineKeyboardButton(
        "BMW",
        callback_data="2ans_bmw"
    )
    mercedes_button = InlineKeyboardButton(
        "MERCEDES",
        callback_data="1ans_mercedes"
    )
    markup.add(bmw_button)
    markup.add(mercedes_button)
    return markup
async def questionnaire_third_answers():
    markup = InlineKeyboardMarkup()
    lemon_button = InlineKeyboardButton(
        "Lemon",
        callback_data="2ans_lemon"
    )
    banana_button = InlineKeyboardButton(
        "Banana",
        callback_data="1ans_banana"
    )
    markup.add(lemon_button)
    markup.add(banana_button)
    return markup


