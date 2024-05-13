from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


finish_add_answers_kb = InlineKeyboardMarkup(inline_keyboard=
    [
        [
            InlineKeyboardButton(text='Перейти к внесению следующего вопроса', callback_data='add_answer_finish'),
        ]
    ]
)

finish_add_questions_kb = InlineKeyboardMarkup(inline_keyboard=
    [
        [
            InlineKeyboardButton(text='Все вопросы внесены', callback_data='add_question_finish'),
        ]
    ]
)
