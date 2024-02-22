from ..services.database import Base
from sqlalchemy import Column, Integer, String, ARRAY, DateTime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    discord_id = Column(String)
    discord_nick = Column(String)
    user_created = Column(DateTime)
    user_updated = Column(DateTime)