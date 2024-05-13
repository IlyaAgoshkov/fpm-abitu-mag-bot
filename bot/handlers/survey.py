from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from consts.commands import TEST_COMMAND
from consts.text import TEST_START_TEXT, TEST_NO_CONFIRM, RESULT, RESTART, TEST
from keyboards.survey_kb import *
from repositories.human_answers import HumansAnswersRepository
from repositories.question import QuestionRepository


router = Router()


@router.message(Command(TEST_COMMAND))
async def test_command(message: Message):
    await message.answer(text=TEST_START_TEXT, reply_markup=confirm_kb)


@router.message(F.text == TEST)
async def test_command_text(message: Message):
    await message.answer(text=TEST_START_TEXT, reply_markup=confirm_kb)


@router.callback_query(F.data.startswith('test_start'))
async def test(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text=TEST_START_TEXT, reply_markup=confirm_kb)


@router.callback_query(F.data.startswith("confirm_"))
async def confirm(call: CallbackQuery):
    action = call.data.split("_")[1]
    if action == "yes":
        questions = await QuestionRepository.all()
        question = questions[0]
        await call.answer()
        await call.message.edit_text(question['question_text'], reply_markup=await get_question_kb(question, 0))
    else:
        await call.answer()
        await call.message.edit_text(TEST_NO_CONFIRM, reply_markup=confirm_kb)


@router.callback_query(F.data.startswith("question_"))
async def question(call: CallbackQuery):
    pk, ind = list(map(int, call.data.split("_")[1:]))
    questions = await QuestionRepository.all()
    kit, kpm, kmm, fun, pid = list(map(float, questions[pk]['answers'][ind][1].split(';')))
    weights = await HumansAnswersRepository.get(username=call.message.from_user.username)
    if weights:
        kit += weights['kit']
        kpm += weights['kpm']
        kmm += weights['kmm']
        fun += weights['fun']
        pid += weights['pid']
        await HumansAnswersRepository.update(
            username=call.message.from_user.username,
            kit=kit,
            kpm=kpm,
            kmm=kmm,
            fun=fun,
            pid=pid
        )
    else:
        await HumansAnswersRepository.create(
            username=call.message.from_user.username,
            kit=kit,
            kpm=kpm,
            kmm=kmm,
            fun=fun,
            pid=pid
        )
    if pk + 1 < len(questions):
        await call.answer()
        await call.message.edit_text(questions[pk + 1]['question_text'], reply_markup=await (get_question_kb(questions[pk + 1], pk + 1)))
    else:
        max_weight = 0
        speciality = ''
        weights_dict = {
            '01.04.02 Прикладная математика и информатика (Технологии программирования и разработки информационно-коммуникационных систем)': kit,
            '01.04.02 Прикладная математика и информатика (Математические и информационные технологии в цифровой экономике)': kpm,
            '01.04.02 Прикладная математика и информатика (Математическое моделирование в естествознании и технологиях)': kmm,
            '02.04.02 Фундаментальная информатика и информационные технологии (Интеллектуальные системы и технологии) ': fun,
            '09.04.02 Информационные системы и технологии (Искусственный интеллект и машинное обучение)': pid
        }
        for x in weights_dict:
            if weights_dict[x] > max_weight:
                max_weight = weights_dict[x]
                speciality = x
        await call.answer()
        await call.message.edit_text(RESULT.format(speciality=speciality), reply_markup=another_time_kb)


@router.callback_query(F.data.startswith('restart_'))
async def restart(call: CallbackQuery):
    data = F.data.split('_')[1]
    if data == 'yes':
        await HumansAnswersRepository.destroy(username=call.message.from_user.username)
        await call.answer()
        await call.message.edit_text(RESTART, reply_markup=confirm_kb)