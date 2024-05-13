from config.conf import client


class BaseMongoRepository:
    client = client
    db = 'db'
    collection_name = 'base_collection'
    query = client[db][collection_name]

    @classmethod
    async def get(cls, **kwargs):
        return await cls.query.find_one(kwargs)

    @classmethod
    async def all(cls):
        return [obj async for obj in cls.query.find({})]

    @classmethod
    async def update(cls, pk, **kwargs):
        return await cls.query.update_one(
            {'_id': pk}, {'$set': kwargs}
        )

    @classmethod
    async def create(cls, **kwargs):
        return await cls.query.insert_one(kwargs)

    @classmethod
    async def destroy(cls, **kwargs):
        await cls.query.delete_many(kwargs)
