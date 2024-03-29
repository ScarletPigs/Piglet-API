from ..services.database import Base
from sqlalchemy import Column, Integer, String

class Setting(Base):
    __tablename__ = "Setting"
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String)
    value = Column(String)