from fastapi import APIRouter, HTTPException, status, Depends
from ..models.event import Event
from ..models.user import User
from datetime import date
from sqlalchemy.orm import Session
from ..services.database import get_db

router = APIRouter(prefix="/events")

events = []

# Create a new event
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_event(body, db: Session = Depends(get_db)):
    newEvent = Event(**body)
    db.add(newEvent)
    db.commit()
    db.refresh(newEvent)
    return {"status": "success", "data": newEvent}

# Get all/multiple events
@router.get("/")
def get_events(db: Session = Depends(get_db)):
    return {"status": "success", "data": db.query(Event).all()}

# Get a specific event
# @router.get("/{event_id}")
# def get_event(event_id: int):
#     for event in events:
#         if event.id == event_id:
#             return event
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found!")