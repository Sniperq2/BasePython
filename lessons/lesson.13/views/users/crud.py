"""
Create
Read
Update
Delete
"""

# from typing import Optional
# Optional[User]

from pydantic import BaseModel

from .schemas import User, UserIn


class UsersStorage(BaseModel):
    counter: int = 0
    cache_by_id: dict[int, User] = {}

    @property
    def next_id(self) -> int:
        self.counter += 1
        return self.counter


storage = UsersStorage()


def get_users() -> list[User]:
    return list(storage.cache_by_id.values())


def create_user(user_in: UserIn) -> User:
    user = User(id=storage.next_id, **user_in.dict())
    storage.cache_by_id[user.id] = user
    return user


def get_user(user_id: int) -> User | None:
    return storage.cache_by_id.get(user_id)


def delete_user(user_id: int) -> None:
    return storage.cache_by_id.pop(user_id, None)
