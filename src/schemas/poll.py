from pydantic import BaseModel
from typing import Optional

class PollBase(BaseModel):
    pass
    
    class Config:
        from_attributes = True
        
class PollCreate(PollBase):
    name: str
    description: str


class PollResponse(PollBase):
    id: int
    
    
class PollUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    
    class Config:
        from_attributes = True