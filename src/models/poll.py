from ..services.database import Base
from sqlalchemy import Column, Integer, String

class Poll(Base):
    __tablename__ = "Poll"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)