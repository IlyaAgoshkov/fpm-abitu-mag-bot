from repositories.base import BaseMongoRepository


class QuestionRepository(BaseMongoRepository):
    collection_name = 'questions'
    query = BaseMongoRepository.client[BaseMongoRepository.db][collection_name]
