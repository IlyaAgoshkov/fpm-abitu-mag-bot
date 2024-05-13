from aiogram.filters.state import StatesGroup, State


class CreateQuestionState(StatesGroup):
    waiting_for_question_text = State()
    waiting_for_answer_text = State()
    waiting_for_weights = State()
