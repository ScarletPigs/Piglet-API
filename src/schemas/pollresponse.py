from pydantic import BaseModel
from typing import Optional

class PollResponseBase(BaseModel):
    pollId: int
    responseByUserId: int
    response: str
    
    class Config:
        from_attributes = True
        
class PollResponseCreate(PollResponseBase):
    pass

class PollResponseReturn(PollResponseBase):
    id: int
    
class PollResponseUpdate(BaseModel):
    response: Optional[str]
    responseByUserId: Optional[int]
    pollId: Optional[int]

    class Config:
        from_attributes = True