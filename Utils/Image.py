from typing_extensions import TypedDict


class UploadImage(TypedDict):
    route_image: str
    name: str
    user_id: int


class DownloadImage(TypedDict):
    id: int
    user_id: int
