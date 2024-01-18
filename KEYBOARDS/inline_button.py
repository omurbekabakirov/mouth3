from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Start Registration",
        callback_data="registration"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    return markup


async def questionnaire_first_answers():
    markup = InlineKeyboardMarkup()
    university_button = InlineKeyboardButton(
        "University",
        callback_data=f"university ")
    college_button = InlineKeyboardButton(
        "College",
        callback_data=f"college "
    )
    markup.add(university_button)
    markup.add(college_button)
    return markup


async def second_question():
    markup = InlineKeyboardMarkup()
    second_question_button = InlineKeyboardButton(
        "Next Questionnaire",
        callback_data="next_question"
    )
    markup.add(second_question_button)
    return markup


async def questionnaire_second_answers():
    markup = InlineKeyboardMarkup()
    bmw_button = InlineKeyboardButton(
        "BMW",
        callback_data=f"bmw"
    )
    mercedes_button = InlineKeyboardButton(
        "MERCEDES",
        callback_data=f"mercedes"
    )
    markup.add(bmw_button)
    markup.add(mercedes_button)
    return markup

async def third_question():
    markup = InlineKeyboardMarkup()
    third_question_button = InlineKeyboardButton(
        "Last Questionnaire",
        callback_data=f"last_question "
    )
    markup.add(third_question_button)
    return markup
async def questionnaire_third_answers():
    markup = InlineKeyboardMarkup()
    lemon_button = InlineKeyboardButton(
        "Lemon",
        callback_data=f"lemon "
    )
    banana_button = InlineKeyboardButton(
        "Banana",
        callback_data=f"banana "
    )
    markup.add(lemon_button)
    markup.add(banana_button)
    return markup


