from typing import Optional

from core.security import verity_password
from db.crud_base import CRUDBase
from db.mongo import MongoDB_Wrapper
from ..models.user import User


class CRUDUser(CRUDBase[User]):
    model = User
    db_name = None
    collection_name = "users"

    def __init__(self, mongo):
        super().__init__(mongo, self.collection_name, self.db_name)

    def get_user_by_name(self, username: str):
        _user = self.collection.find_one({ "username": username })
        if _user is not None:
            return self._convert_doc_to_model(_user)
        return None

    def authenticate(self, username: str, password: str) -> Optional[User]:
        _user = self.get_user_by_name(username=username)
        print(_user)
        if not _user:
            return None
        elif not verity_password(password, _user.password):
            return None
        return _user


user = CRUDUser(MongoDB_Wrapper)
