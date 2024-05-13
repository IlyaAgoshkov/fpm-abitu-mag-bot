from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Учебный план'),
                                     KeyboardButton(text='Перспективы развития')],
                                    [KeyboardButton(text='Абитуриентам КубГУ о ФКТиПМ')],
                                     [KeyboardButton(text='С нами сотрудничают')],
                                      [KeyboardButton(text='Пройти тест')],
                                    ],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')