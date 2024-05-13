from aiogram.types import BotCommand


START_COMMAND = 'start'
START_COMMAND_TEXT = 'Начать работу'
VK_COMMAND = 'vk'
VK_URL = 'Связаться с нами'
FACULTY_ABOUT_COMMAND = 'about_faculty'
FACULTY_ABOUT_COMMAND_TEXT = 'О факультете'
TEST_COMMAND = 'test'
TEST_COMMAND_TEXT = 'Тест для выбора направления'
UNIVERSITY_HISTORY_COMMAND = 'university_history'
UNIVERSITY_HISTORY_COMMAND_TEXT = 'История университета'


COMMANDS_LIST = [
    BotCommand(command=START_COMMAND, description=START_COMMAND_TEXT),
    BotCommand(command=VK_COMMAND, description=VK_URL),
    BotCommand(command=FACULTY_ABOUT_COMMAND, description=FACULTY_ABOUT_COMMAND_TEXT),
    BotCommand(command=UNIVERSITY_HISTORY_COMMAND, description=UNIVERSITY_HISTORY_COMMAND_TEXT),
    BotCommand(command=TEST_COMMAND, description=TEST_COMMAND_TEXT),
]