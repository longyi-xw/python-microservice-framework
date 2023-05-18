from typing import Generic, TypeVar, Optional

from bson import ObjectId
from pydantic import BaseModel

from db.mongo import MongoDB

ModelType = TypeVar("ModelType", bound=BaseModel)


class CRUDBase(Generic[ModelType]):
    """
    CRUD object with default methods to Create, Read, Update, Delete (CRUD).
    """
    model = None

    def __init__(self, mongo: MongoDB, collection_name: str, db_name=None):
        if db_name:
            self.db = mongo.client.get_database(db_name)
        self.db = mongo.db
        if not collection_name:
            self.collection = self.db.create_collection(collection_name)
        self.collection = self.db.get_collection(collection_name)

    def get(self, object_id: str) -> Optional[ModelType]:
        doc = self.collection.find_one({ "_id": ObjectId(object_id) })
        if doc is not None:
            return self._convert_doc_to_model(doc)
        return None

    def get_many(self, _filter=None, skip: int = 0, limit: int = 0, sort: Optional[list[tuple]] = None):
        """
        :param _filter: 查询条件
        :param skip: 页码
        :param limit: 页数
        :param sort: 排序
        :return:
        """
        if _filter is None:
            _filter = { }
        skip = limit * (skip - 1)
        cursor = self.collection.find(_filter, skip=skip, limit=limit, sort=sort)
        return [self._convert_doc_to_model(doc) for doc in cursor]

    def create(self, obj_in: ModelType) -> ModelType:
        doc = obj_in.dict()
        result = self.collection.insert_one(doc)
        obj_in.id = str(result.inserted_id)
        return obj_in

    def update(self, obj_in: ModelType) -> ModelType:
        doc = obj_in.dict()
        result = self.collection.replace_one({ "_id": ObjectId(obj_in.id) }, doc)
        if result.modified_count > 0:
            return obj_in

    def delete(self, object_id: str):
        return self.collection.delete_one({ "_id": ObjectId(object_id) })

    def _convert_doc_to_model(self, doc) -> ModelType:
        """
        doc is converted to model
        :param doc:
        :return:
        """
        obj_dict = doc.copy()
        obj_dict["id"] = str(obj_dict.pop("_id"))
        return self.model(**obj_dict)
