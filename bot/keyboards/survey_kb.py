from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

test_kb = InlineKeyboardMarkup(inline_keyboard=
    [
        [
            InlineKeyboardButton(text='Пройти тест', callback_data='test_start'),
        ]
    ]
)

confirm_kb = InlineKeyboardMarkup(inline_keyboard=
    [
        [
            InlineKeyboardButton(text='✅', callback_data='confirm_yes'),
            InlineKeyboardButton(text='❌', callback_data='confirm_no'),
        ]
    ]
)

confirm_kb_two = InlineKeyboardMarkup(inline_keyboard=
    [
        [
            InlineKeyboardButton(text='✅', callback_data='confirm_yes'),
            InlineKeyboardButton(text='❌', callback_data='confirm_no'),
        ]
    ]
)


async def get_question_kb(data, ind):
    answers = data['answers']
    # Создаем список списков для кнопок, каждый подсписок - это новая строка
    keyboard_layout = [
        [InlineKeyboardButton(text=answer[0], callback_data=f'question_{ind}_{i}')]
        for i, answer in enumerate(answers)
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard_layout)


another_time_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Пройти заново', callback_data='restart_yes'),
        ]
    ]
)