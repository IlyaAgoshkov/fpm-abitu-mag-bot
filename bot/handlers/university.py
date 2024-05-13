from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from consts.photo_id import MAT_ECO, MAT_MOD, TEXNOLOGY, FUNDAM, INFO, START_PHOTO, SOV_ID, KUB_ID, CARX_ID, PORT_ID, \
    TIN_ID, MED_ID, MAG_ID, BIL_ID
from consts.text import (START_TEXT, UNIVERSITY_HISTORY, FACULTY_ABOUT, FORM_OF_TRAINING, FOCUS, APPLIVANT_INFO, VK_URL,\
    ABITUR_INFO, CAPTION_MAT_ECO, PROSPECTS, CAPTION_MAT_MOD, CAPTION_TEXNOL, CAPTION_FUNDAM, CAPTION_INFO_SYS, \
    UNIVERSIYU_HYSTORY2, SPONSORS, SOV_TEXT, KUB_TEXT, CARX_TEXT, PORT_TEXT, TIN_TEXT, MED_TEXT, MAG_TEXT, BIL_TEXT, \
    START_TEXT_TWO)
from consts.commands import (START_COMMAND, VK_COMMAND, FACULTY_ABOUT_COMMAND, UNIVERSITY_HISTORY_COMMAND)
from keyboards.reply_kb import main
from keyboards.survey_kb import test_kb
from keyboards.university_kb import (university_kb_for_DEVELOPMENT,
                                     specializations_kb_mat_inf, go_back_kb, go_back_kb_in, sponsors_kb, sov_kb, kub_kb,
                                     carx_kb, port_kb, tin_kb, mag_kb, med_kb, bil_kb)

router = Router()


@router.message(Command(START_COMMAND))
async def start(msg: Message):
    await msg.answer_photo(photo=START_PHOTO,
                           caption=START_TEXT.format(username=msg.from_user.first_name), reply_markup=test_kb)
    # await msg.answer(START_TEXT.format(username=msg.from_user.first_name), reply_markup=
    await msg.answer(
            START_TEXT_TWO, reply_markup=main)



@router.message(Command(UNIVERSITY_HISTORY_COMMAND))
async def university(msg: Message):
    await msg.answer(UNIVERSITY_HISTORY)
    await msg.answer(UNIVERSIYU_HYSTORY2)


@router.message(Command(FACULTY_ABOUT_COMMAND))
async def faculty_about(msg: Message):
    await msg.answer(FACULTY_ABOUT)


@router.message(Command(VK_COMMAND))
async def vk(msg: Message):
    await msg.answer(VK_URL)


@router.message(F.text == PROSPECTS)
async def curriculum(msg: Message):
    await msg.answer(FORM_OF_TRAINING, reply_markup=university_kb_for_DEVELOPMENT)


# @router.message(F.text == APPLIVANT_INFO)
# @router.message(Command(DEVELOPMENT_COMMAND))
# async def development(msg: Message):
#     await msg.answer(FORM_OF_TRAINING, reply_markup=university_kb_for_DEVELOPMENT)
#
#
# @router.message(Command(THE_CURRICULUM_COMMAND))
# async def development(msg: Message):
#     await msg.answer(FORM_OF_TRAINING, reply_markup=university_kb_for_CURRICULUM)


@router.callback_query(F.data == 'fundam')
async def programming_technologies(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo=FUNDAM, caption=CAPTION_FUNDAM, reply_markup=go_back_kb_in)


@router.callback_query(F.data == 'inf_sys')
async def info_sys(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo=INFO, caption=CAPTION_INFO_SYS, reply_markup=go_back_kb_in)


@router.callback_query(F.data.startswith('go_back_in'))
async def go_back_in(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text=FORM_OF_TRAINING, reply_markup=university_kb_for_DEVELOPMENT)


@router.callback_query(F.data == 'mat_info')
async def focus(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(FOCUS, reply_markup=specializations_kb_mat_inf)


@router.callback_query(F.data.startswith('go_menu'))
async def go_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text=FORM_OF_TRAINING, reply_markup=university_kb_for_DEVELOPMENT)


@router.message(F.text == ABITUR_INFO)
async def applicant_info(msg: Message):
    await msg.answer(APPLIVANT_INFO)


@router.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.callback_query(F.data.startswith('Mathematical_modeling_in_natural_sciences_and_technologies'))
async def mathmatic_mod(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo=MAT_ECO, caption=CAPTION_MAT_ECO, reply_markup=go_back_kb)


@router.callback_query(F.data.startswith('go_back'))
async def go_back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text=FOCUS, reply_markup=specializations_kb_mat_inf)


@router.callback_query(F.data.startswith('mathematical_modeling'))
async def mathmatic_mod_in_es(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo=MAT_MOD, caption=CAPTION_MAT_MOD, reply_markup=go_back_kb)


@router.callback_query(F.data.startswith('programming_technologies'))
async def programming_technologies(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo=TEXNOLOGY, caption=CAPTION_TEXNOL, reply_markup=go_back_kb)


@router.message(F.text == SPONSORS)
async def sponsors(msg: Message):
    await msg.answer(text='Выберите спорнсора:', reply_markup=sponsors_kb)


@router.callback_query(F.data == 'sov')
async def sov(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo=SOV_ID, caption=SOV_TEXT, reply_markup=sov_kb)


@router.callback_query(F.data == 'kub')
async def sov(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo=KUB_ID, caption=KUB_TEXT, reply_markup=kub_kb)


@router.callback_query(F.data == 'carx')
async def sov(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo=CARX_ID, caption=CARX_TEXT, reply_markup=carx_kb)


@router.callback_query(F.data == 'por')
async def sov(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo=PORT_ID, caption=PORT_TEXT, reply_markup=port_kb)


@router.callback_query(F.data == 'tin')
async def sov(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo=TIN_ID, caption=TIN_TEXT, reply_markup=tin_kb)


@router.callback_query(F.data == 'med')
async def sov(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo=MED_ID, caption=MED_TEXT, reply_markup=med_kb)


@router.callback_query(F.data == 'mag')
async def sov(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo=MAG_ID, caption=MAG_TEXT, reply_markup=mag_kb)


@router.callback_query(F.data == 'bil')
async def sov(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo=BIL_ID, caption=BIL_TEXT, reply_markup=bil_kb)

