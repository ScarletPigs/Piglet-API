from pydantic import BaseModel
from typing import Optional

class UserRoleBase(BaseModel):
    name: str
    
    class Config:
        from_attributes = True
        
class UserRoleCreate(UserRoleBase):
    permissions: int
    description: Optional[str]
        
class UserRoleUpdate(UserRoleBase):
    name: str
    permissions: Optional[int]
    description: Optional[str]
    
class UserRoleResponse(UserRoleBase):
    permissions: int
    description: str