from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


university_kb_for_DEVELOPMENT = InlineKeyboardMarkup(inline_keyboard=
    [
        [
            InlineKeyboardButton(text='01.04.02 Прикладная математика и информатикая', callback_data='mat_info')],
            [InlineKeyboardButton(text='02.04.02 Фундаментальная информатика и информационные технологии',
                                 callback_data='fundam')],
            [InlineKeyboardButton(text='09.04.02 Информационные системы и технологии', callback_data='inf_sys'),

        ]
    ]
)

university_kb_for_CURRICULUM = InlineKeyboardMarkup(inline_keyboard=
    [
        [
            InlineKeyboardButton(text='01.04.02 Прикладная математика и информатикая', callback_data='mat_inf')],
            [InlineKeyboardButton(text='02.04.02 Фундаментальная информатика и информационные технологии',
                                 callback_data='fundams')],
            [InlineKeyboardButton(text='09.04.02 Информационные системы и технологии', callback_data='inf_system'),

        ]
    ]
)

specializations_kb_mat_inf = InlineKeyboardMarkup(inline_keyboard=
    [
        [
            InlineKeyboardButton(text='Математические и информационные технологии в цифровой экономике',
                                 callback_data='Mathematical_modeling_in_natural_sciences_and_technologies')],
            [InlineKeyboardButton(text='Математическое моделирование в естествознании и технологиях',
                                  callback_data='mathematical_modeling')],
            [InlineKeyboardButton(text='Технологии программирования и разработки информационно-коммуникационных систем',
                                 callback_data='programming_technologies'),
        ],
        [InlineKeyboardButton(text='На главную', callback_data='go_menu')]
    ]
)

specializations_kb_mat_inf_for_plan = InlineKeyboardMarkup(inline_keyboard=
    [
        [
            InlineKeyboardButton(text='Математические и информационные технологии в цифровой экономике',
                                 callback_data='mathematical_model_sciences_and_tech')],
            [InlineKeyboardButton(text='Математическое моделирование в естествознании и технологиях',
                                 callback_data='mathematic_modeling')],
            [InlineKeyboardButton(text='Технологии программирования и разработки информационно-коммуникационных систем',
                                 callback_data='programm_technologies'),
        ],
        [InlineKeyboardButton(text='На главную', callback_data='plan')]
    ]
)

go_back_kb = InlineKeyboardMarkup(inline_keyboard=
                                  [
                                    [InlineKeyboardButton(text='Вернуться назад', callback_data='go_back')]
                                  ])

go_back_kb_in = InlineKeyboardMarkup(inline_keyboard=
                                  [
                                    [InlineKeyboardButton(text='Вернуться назад', callback_data='go_back_in')]
                                  ])

sponsors_kb = InlineKeyboardMarkup(inline_keyboard=
                                   [
                                    [InlineKeyboardButton(text='Совкомбанк', callback_data='sov'),
                                        InlineKeyboardButton(text='Кубань кредит', callback_data='kub')],
                                    [InlineKeyboardButton(text='CarX', callback_data='carx'),
                                        InlineKeyboardButton(text='Портал Юг', callback_data='por')],
                                    [InlineKeyboardButton(text='Тинькофф', callback_data='tin'),
                                        InlineKeyboardButton(text='МедРокет', callback_data='med')],
                                    [InlineKeyboardButton(text='Магнит', callback_data='mag'),
                                        InlineKeyboardButton(text='Билайн', callback_data='bil')],
                                   ]
                                   )

sov_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посетить сайт', url='https://sovcombank.it/')]
])

kub_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посетить сайт', url='https://kk.bank/')]
])

carx_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посетить сайт', url='https://carx-online.com/')]
])

port_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посетить сайт', url='https://portal-yug.ru/')]
])

tin_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посетить сайт', url='https://www.tinkoff.ru/')]
])

med_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посетить сайт', url='https://medrocket.ru/')]
])

mag_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посетить сайт', url='https://magnit.ru/')]
])

bil_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Посетить сайт', url='https://beeline-r.ru/')]
])




