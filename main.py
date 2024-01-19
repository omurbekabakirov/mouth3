from aiogram import executor
from config import dp
from handlers import (
    start,
    questionnaire,
    chat_actions,
    registration
)
from database.DB import Database


def on_startup():
    datab = Database()
    datab.sql_create_table()


start.register_start_handler(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
registration.register_registration_handler(dp=dp)
chat_actions.register_chat_actions_handlers(dp=dp)


if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup()
    )
