from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventTypeBase(BaseModel):
    id: int
    
    class Config:
        from_attributes = True
    
class EventTypeCreate(EventTypeBase):
    name: str
    requiredPermission: int

class EventTypeUpdate(EventTypeBase):
    name: Optional[str]
    requiredPermission: Optional[int]
    
class EventTypeResponse(EventTypeBase):
    name: str
    requiredPermission: int