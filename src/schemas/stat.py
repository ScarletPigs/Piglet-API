from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class StatBase(BaseModel):
    statName: str
    value: int

    class Config:
        from_attributes = True


class StatCreate(StatBase):
    steamUuid: Optional[str]
    userId: Optional[int]


class StatResponse(StatBase):
    id: int
    statName: str
    userId: int
    value: int
    lastModified: datetime


class StatUpdate(BaseModel):
    statName: Optional[str]
    value: Optional[int]

    class Config:
        from_attributes = True
