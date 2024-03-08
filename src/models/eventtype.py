from ..services.database import Base
from sqlalchemy import Column, Integer, String

class EventType(Base):
    __tablename__ = "EventType"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    requiredPermission = Column(Integer)