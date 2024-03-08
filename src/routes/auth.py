from fastapi import APIRouter, HTTPException, status, Depends
from ..models.event import Event
from ..models.user import Modsets
from datetime import date
from sqlalchemy.orm import Session
from ..services.database import get_db

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(db: Session = Depends(get_db)):
    user = db.query()