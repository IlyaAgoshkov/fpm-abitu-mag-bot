from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.utils.media_group import MediaGroupBuilder

from consts.document_id import MAT_ECO, MAT_EST, TEX_MAT, FUND, INF
from consts.text import FORM_OF_TRAINING, FOCUS, PLAN_STR
from keyboards.university_kb import (
    university_kb_for_CURRICULUM, specializations_kb_mat_inf_for_plan)

router = Router()


@router.message(F.text == PLAN_STR)
async def plan(msg: Message):
    await msg.answer(FORM_OF_TRAINING, reply_markup=university_kb_for_CURRICULUM)


@router.callback_query(F.data.startswith('mat_inf'))
async def mat_infi(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(FOCUS, reply_markup=specializations_kb_mat_inf_for_plan)


@router.callback_query(F.data.startswith('plan'))
async def go_back_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(FORM_OF_TRAINING, reply_markup=university_kb_for_CURRICULUM)


@router.callback_query(F.data.startswith('fundams'))
async def first_course(call: CallbackQuery):
    media_group = MediaGroupBuilder()
    media_group.add_document(media=FUND)
    await call.answer()
    await call.message.answer_media_group(media=media_group.build())


@router.callback_query(F.data.startswith('inf_system'))
async def first_course(call: CallbackQuery):
    media_group = MediaGroupBuilder()
    media_group.add_document(media=INF)
    await call.answer()
    await call.message.answer_media_group(media=media_group.build())

# @router.callback_query(F.data.startswith('mathematical_model_sciences_and_tech'))
# async def mate_in(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text(COURCE, reply_markup=semestr)
#
#
# @router.callback_query(F.data.startswith('menu_plan'))
# async def go_back_in_menu(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text(FOCUS, reply_markup=specializations_kb_mat_inf_for_plan)
#
#
#
# @router.callback_query(F.data.startswith('sem_back'))
# async def sem_back(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text(FOCUS, reply_markup=specializations_kb_mat_inf_for_plan)
#
#
# @router.callback_query(F.data.startswith('first_sem'))
# async def first_course(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text(OBJECTS, reply_markup=objects_sem1)
#
#
# @router.callback_query(F.data.startswith('menu_objects'))
# async def sem_back(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text(OBJECTS, reply_markup=semestr)
#
#
#
#
#
#
#
#
# @router.callback_query(F.data.startswith('sem1_math_phys'))
# async def first_course(callback: CallbackQuery):
#     await callback.answer()
#     for doc_id in SEM1_MATH_PHYS:
#         await callback.message.bot.send_document(callback.message.chat.id, doc_id)


# @router.message(F.document)
# async def document_id(msg: Message):
#     await msg.answer(f"ID документа {msg.document.file_id}")

@router.callback_query(F.data.startswith('mathematical_model_sciences_and_tech'))
async def mathematical_model_sciences_and_tech(call: CallbackQuery):
    media_group = MediaGroupBuilder()
    media_group.add_document(media=MAT_ECO)
    await call.answer()
    await call.message.answer_media_group(media=media_group.build())


@router.callback_query(F.data.startswith('mathematic_modeling'))
async def mathematic_modeling(call: CallbackQuery):
    media_group = MediaGroupBuilder()
    media_group.add_document(media=MAT_EST)
    await call.answer()
    await call.message.answer_media_group(media=media_group.build())


@router.callback_query(F.data.startswith('programm_technologies'))
async def first_course(call: CallbackQuery):
    media_group = MediaGroupBuilder()
    media_group.add_document(media=TEX_MAT)
    await call.answer()
    await call.message.answer_media_group(media=media_group.build())





