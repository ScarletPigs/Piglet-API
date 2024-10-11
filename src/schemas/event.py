from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventBase(BaseModel):
    name: str
    description: str
    createdByUser: str

    class Config:
        from_attributes = True


class EventCreate(EventBase):
    eventTypeId: int
    startTime: datetime
    endTime: datetime


class EventResponse(EventBase):
    id: int
    eventTypeId: int
    createdAt: datetime
    lastModified: datetime
    startTime: datetime
    endTime: datetime


class EventUpdate(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    createdByUserId: Optional[str]
    eventTypeId: Optional[int]
    startTime: Optional[datetime]
    endTime: Optional[datetime]

    class Config:
        from_attributes = True
