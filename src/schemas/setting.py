from pydantic import BaseModel
from typing import Optional

class SettingBase(BaseModel):
    key: str
    value: str
    
    class Config:
        from_attributes = True
        
class SettingResponse(SettingBase):
    pass

class SettingUpdate(SettingBase):
    id: int
    key: Optional[str]
    value: Optional[str]
    
    class Config:
        from_attributes = True