from ..services.database import Base
from sqlalchemy import Column, Integer, String

class UserRole(Base):
    __tablename__ = "UserRole"
    name = Column(String, primary_key=True)
    permissions = Column(Integer)
    description = Column(String)