from ..services.database import Base
from sqlalchemy import Column, Integer, String

class PollResponse(Base):
    __tablename__ = "PollResponse"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    pollId = Column(Integer)
    responseByUserId = Column(Integer)
    response = Column(String)