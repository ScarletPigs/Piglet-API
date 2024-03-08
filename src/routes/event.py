from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from ..models.event import Event
from sqlalchemy.orm import Session
from ..services.database import get_db
from ..schemas.event import *

router = APIRouter(prefix="/events", tags=["events"], responses={200: {"model": EventResponse}})


# Create a new event
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_event(event : EventCreate, db: Session = Depends(get_db)):
    """
    Creates a new event in the database.

    Parameters:
    - event (EventCreate): a EventCreate object

    Returns:
    - EventResponse: A newly created Event object
    """
    newEvent = Event(**event.model_dump())
    newEvent.created_at = datetime.now()
    newEvent.last_modified = datetime.now()
    db.add(newEvent)
    db.commit()
    db.refresh(newEvent)
    return newEvent

# Get all events
@router.get("/", response_model=List[EventResponse])
def get_events(db: Session = Depends(get_db)):
    """
    Get event from the database and return a list of EventResponse objects.
    
    Parameters:
    
    Returns:
    - List[EventResponse]: A list of EventResponse objects
    """
    return db.query(Event).all()

# Get a specific event
@router.get("/{event_id}")
def get_event(event_id, db: Session = Depends(get_db)):
    """
    Get an event by its ID.
    
    Args:
    - event_id (int): The ID of the event to retrieve.

    Returns:
    - EventResponse: The event with the specified ID.
    """
    return db.query(Event).filter(Event.id == event_id).first()

# Update a event
@router.put("/")
def update_event(event : EventUpdate, db: Session = Depends(get_db)):
    """
    Update an event in the database.

    Args:
    - event (EventUpdate): The updated event data.

    Returns:
    - EventResponse: The updated event.
    """
    db.query(Event).filter(Event.id == event.id).update(event.model_dump())
    db.commit()
    return db.query(Event).filter(Event.id == event.id).first()
    
    
# Delete an event
@router.delete("/{event_id}", response_model=int)
def delete_event(event_id : int, db: Session = Depends(get_db)):
    """
    Deletes an event from the database.

    Parameters:
    - event_id (int): The ID of the event to be deleted.
        
    Returns:
    - int: The number of rows deleted from the database.
    """
    return db.query(Event).filter(Event.id == event_id).delete() and db.commit()
    