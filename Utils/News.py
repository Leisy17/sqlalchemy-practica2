from typing_extensions import TypedDict


class CreateNews(TypedDict):
    title: str
    abstract: str
    description: str
    author_id: int


class UpdateNews(TypedDict):
    title: str
    abstract: str
    description: str
    id: int


class DeleteNews(TypedDict):
    id: int
