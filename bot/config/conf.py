from os import getenv

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()


BOT_TOKEN = getenv('BOT_TOKEN')
ADMINISTRATORS = list(map(int, getenv('ADMINS').split(',')))
MONGO_HOST = getenv("MONGO_HOST")
MONGO_PORT = int(getenv("MONGO_PORT"))

client = AsyncIOMotorClient(MONGO_HOST, MONGO_PORT)
