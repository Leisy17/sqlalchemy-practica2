from typing_extensions import TypedDict


class CreateComments(TypedDict):
    comment: str
    user_id: int
    new_id: int


class UpdateComments(TypedDict):
    comment: str
    id: int


class DeleteComments(TypedDict):
    id: int


class GetComments(TypedDict):
    new_id: int
