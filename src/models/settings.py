from ..services.database import Base
from sqlalchemy import Column, Integer, String

class Settings(Base):
    __tablename__ = "Settings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String)
    value = Column(String)