from ..services.database import Base
from sqlalchemy import Column, Integer, String

class Tag(Base):
    __tablename__ = "Tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String)
    role_type = Column(Integer)
    description = Column(String)