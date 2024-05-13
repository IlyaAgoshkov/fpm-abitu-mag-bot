# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# def generate_inline_keyboard(buttons_data: list[tuple[str, str]]) -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardMarkup()
#     for text, callback_data in buttons_data:
#         button = InlineKeyboardButton(text=text, callback_data=callback_data)
#         keyboard.add(button)
#     return keyboard
#
# # # Пример использования функции:
# # buttons_data = [
# #     ("Кнопка 1", "callback_1"),
# #     ("Кнопка 2", "callback_2"),
# #     ("Кнопка 3", "callback_3"),
# # ]
# # keyboard = generate_inline_keyboard(buttons_data)
