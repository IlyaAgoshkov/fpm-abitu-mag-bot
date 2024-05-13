from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from consts.text import (ADMIN_CREATED, ADMIN_TO_CREATE, QUESTION_TO_CREATE, ANSWER_TO_CREATE, WEIGHTS_TO_CREATE,
                         QUESTIONS_ADDED)
from keyboards.admin import finish_add_questions_kb, finish_add_answers_kb
from middlewares.admin import AdminAuthorizationMiddleware
from repositories.admin import AdminRepository
from repositories.question import QuestionRepository
from states.admin import CreateAdminState
from states.question import CreateQuestionState


router = Router()


@router.message(Command('add_admin'))
async def add_admin(message: Message, state: FSMContext):
    await message.answer(ADMIN_TO_CREATE)
    await state.set_state(CreateAdminState.waiting_for_admin_id)


@router.message(CreateAdminState.waiting_for_admin_id)
async def add_admin_id(message: Message, state: FSMContext):
    await AdminRepository.create(tg_id=int(message.text))
    await message.answer(ADMIN_CREATED.format(tg_id=message.text))
    await state.clear()


@router.message(Command('add_question'))
async def add_question(message: Message, state: FSMContext):
    await message.answer(QUESTION_TO_CREATE, reply_markup=finish_add_questions_kb)
    await state.set_state(CreateQuestionState.waiting_for_question_text)


@router.message(CreateQuestionState.waiting_for_question_text)
async def create_question(message: Message, state: FSMContext):
    await message.answer(ANSWER_TO_CREATE, reply_markup=finish_add_answers_kb)
    await state.update_data(
        question=message.text,
        answers=[]
    )
    await state.set_state(CreateQuestionState.waiting_for_answer_text)


@router.message(CreateQuestionState.waiting_for_answer_text)
async def add_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    data['answers'].append([message.text])
    await message.answer(WEIGHTS_TO_CREATE)
    await state.update_data(answers=data['answers'])
    await state.set_state(CreateQuestionState.waiting_for_weights)


@router.message(CreateQuestionState.waiting_for_weights)
async def add_weights(message: Message, state: FSMContext):
    data = await state.get_data()
    data['answers'][-1].append(message.text)
    await state.update_data(answers=data['answers'])
    await message.answer(ANSWER_TO_CREATE, reply_markup=finish_add_answers_kb)
    await state.set_state(CreateQuestionState.waiting_for_answer_text)


@router.callback_query(F.data.startswith("add_answer_"))
async def add_answer_callback(call: CallbackQuery, state: FSMContext):
    if call.data.split('_')[-1] == 'finish':
        data = await state.get_data()
        try:
            if not data['answers']:
                raise KeyError
            await QuestionRepository.create(
                question_text=data['question'],
                answers=data['answers']
            )
            await state.update_data(answers=[])
            await call.message.answer(QUESTIONS_ADDED)
        except KeyError:
            pass
        await call.answer()
        await call.message.answer(QUESTION_TO_CREATE, reply_markup=finish_add_questions_kb)
        await state.set_state(CreateQuestionState.waiting_for_question_text)


@router.callback_query(F.data.startswith("add_question_"))
async def add_question_callback(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data.split('_')[-1] == 'finish':
        try:
            if not data['answers']:
                raise KeyError
            await QuestionRepository.create(
                question_text=data['question'],
                answers=data['answers']
            )
            await call.answer()
            await call.message.answer(QUESTIONS_ADDED)
        except KeyError:
            pass
        finally:
            questions = await QuestionRepository.all()
            for question in questions:
                await QuestionRepository.destroy(question_text=question['question_text'])
            for i, question in enumerate(questions):
                await QuestionRepository.create(
                    ind=i,
                    question_text=question['question_text'],
                    answers=question['answers']
                )
        await state.clear()


router.message.middleware(AdminAuthorizationMiddleware())
