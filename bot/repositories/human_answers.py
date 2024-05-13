from repositories.base import BaseMongoRepository


class HumansAnswersRepository(BaseMongoRepository):
    collection_name = 'human_answers'
    query = BaseMongoRepository.client[BaseMongoRepository.db][collection_name]

    @classmethod
    async def update(cls, username, **kwargs):
        return await cls.query.update_one(
            {'username': username}, {'$set': kwargs}
        )
