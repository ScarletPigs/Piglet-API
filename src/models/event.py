from typing import Optional
from datetime import date
from .user import User
from ..services.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, text


class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    time = Column(DateTime)
    host_id = Column(Integer, ForeignKey("users.id"))
    event_created = Column(DateTime(timezone=True))
    event_updated = Column(DateTime(timezone=True))