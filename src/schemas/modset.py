from pydantic import BaseModel
from typing import Optional

class ModsetBase(BaseModel):
    filename: str
    discord_msg_id: str
    
    class Config:
        from_attributes = True
        
class ModsetResponse(ModsetBase):
    id: int
        
class ModsetUpdate(BaseModel):
    id: int
    filename: Optional[str]
    discord_msg_id: Optional[str]
    
    class Config:
        from_attributes = True