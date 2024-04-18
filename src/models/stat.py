from ..services.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Stat(Base):
    __tablename__ = "Stat"

    id = Column(Integer, primary_key=True, autoincrement=True)
    statName = Column(String)
    steamUuid = Column(String, nullable=True)
    userId = Column(Integer, nullable=True)
    value = Column(Integer)
    lastModified = Column(DateTime(timezone=True))
