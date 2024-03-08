from typing import Optional
from datetime import date
from ..services.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, text, BigInteger


class Event(Base):
    __tablename__ = "Event"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    eventTypeId = Column(Integer)
    createdByUserId = Column(Integer)
    modsetId = Column(Integer)
    createdAt = Column(DateTime(timezone=True))
    lastModified = Column(DateTime(timezone=True))
    startTime = Column(DateTime(timezone=True))
    endTime = Column(DateTime(timezone=True))