
import logging

import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

from config import conf
from consts.commands import COMMANDS_LIST
from handlers import survey, university, admin, plan

from storage.mongo import MongoStorage


load_dotenv()


async def on_startup(dp):
    pass


async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


async def main() -> None:
    storage = MongoStorage(conf.client, db_name='aiogram_fsm')
    bot = Bot(token=conf.BOT_TOKEN, )
    dp = Dispatcher(bot=bot, storage=storage)
    dp.include_routers(survey.router, university.router, admin.router, plan.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(COMMANDS_LIST, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, on_startup=on_startup, on_shutdown=on_shutdown)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


# from motor.motor_asyncio import AsyncIOMotorClient
#
#
# client = AsyncIOMotorClient('localhost', 27017)
# async def main():
#     db = client.db
#     questions = db.questions
#     # for i in range(12):
#     #     res = await questions.delete_many({'ind': i})
#     async for quests in questions.find({}):
#         print(quests)
#
#
# if __name__ == '__main__':
#     loop = client.get_io_loop()
#     loop.run_until_complete(main())
