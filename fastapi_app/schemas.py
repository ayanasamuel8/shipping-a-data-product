from pydantic import BaseModel
from typing import List, Optional


class MessageStat(BaseModel):
    message_id: int
    channel: str
    message_length: int
    has_photo: bool


class ProductFrequency(BaseModel):
    product: str
    count: int


class ChannelActivity(BaseModel):
    date: str
    message_count: int


class SearchResult(BaseModel):
    message_id: int
    message: str
    channel: str