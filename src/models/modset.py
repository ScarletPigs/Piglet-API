from ..services.database import Base
from sqlalchemy import Column, Integer, String, ARRAY, DateTime

class Modsets(Base):
    __tablename__ = "Modset"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String)
    discord_msg_id = Column(String)