from typing_extensions import TypedDict


class CreateUsers(TypedDict):
    name: str
    lastname: str
    email: str
    birthday: str
    password: str


class DeleteUsers(TypedDict):
    email: str
    password: str
