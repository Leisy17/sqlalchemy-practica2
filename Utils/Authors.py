from typing_extensions import TypedDict


class CreateAuthors(TypedDict):
    user_id: int
    profession: str
