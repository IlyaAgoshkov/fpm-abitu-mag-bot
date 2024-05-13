from aiogram.filters.state import StatesGroup, State


class CreateAdminState(StatesGroup):
    waiting_for_admin_id = State()
