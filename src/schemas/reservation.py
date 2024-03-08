from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReservationCreate(BaseModel):
    name: str
    description: str
    type: int
    host: str
    start_time: datetime
    end_time: datetime