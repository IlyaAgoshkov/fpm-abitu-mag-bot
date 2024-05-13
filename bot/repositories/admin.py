from repositories.base import BaseMongoRepository


class AdminRepository(BaseMongoRepository):
    collection_name = 'admins'
    query = BaseMongoRepository.client[BaseMongoRepository.db][collection_name]
