from typing import Optional
from datetime import date
from .user import Modsets
from ..services.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, text


class Reservation(Base):
    __tablename__ = "Reservations"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    type = Column(Integer)
    host = Column(String)
    created_at = Column(DateTime(timezone=True))
    last_modified = Column(DateTime(timezone=True))
    start_time = Column(DateTime(timezone=True))
    end_time = Column(DateTime(timezone=True))