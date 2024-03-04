from ..services.database import Base
from sqlalchemy import Column, Integer, String

class ReservationType(Base):
    __tablename__ = "ReservationTypes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)