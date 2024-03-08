from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from ..models.eventtype import EventType
from sqlalchemy.orm import Session
from ..services.database import get_db
from ..schemas.eventtype import *


router = APIRouter(prefix="/eventtypes", tags=["eventtypes"], responses={200: {"model": EventTypeResponse}})



@router.get("/", response_model=List[EventTypeResponse])
def get_eventtypes(db: Session = Depends(get_db)):
    """
    Get event types from the database and return a list of EventTypeResponse objects.

    Parameters:

    Returns:
    - List[EventTypeResponse]: A list of EventTypeResponse objects.
    """
    return db.query(EventType).all()



@router.get("/{eventtype_id}", response_model=EventTypeResponse)
def get_eventtype_by_id(eventtype_id: int, db: Session = Depends(get_db)):
    """
    Get an event type by its ID from the database and return an EventTypeResponse object.

    Parameters:
    - eventtype_id (int): The ID of the event type to retrieve.

    Returns:
    - EventTypeResponse: The event type with the specified ID.

    Raises:
    - HTTPException 404: If no event type with the specified ID exists in the database.
    """
    eventtype = db.query(EventType).filter(EventType.id == eventtype_id).first()
    if eventtype is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event Type not found")
    return eventtype




@router.post("/", status_code=status.HTTP_201_CREATED)
def create_eventtype(eventtype : EventTypeCreate, db: Session = Depends(get_db)):
    """
    Creates a new event type in the database.

    Parameters:
    - eventtype (EventTypeCreate): A EventTypeCreate object.

    Returns:
    - EventTypeResponse: A newly created EventType object.
    """
    newEventType = EventType(**eventtype.model_dump())
    db.add(newEventType)
    db.commit()
    db.refresh(newEventType)
    return newEventType


@router.delete("/{eventtype_id}", response_model=int)
def delete_eventtype(eventtype_id : int, db: Session = Depends(get_db)):
    """
    Deletes an event type from the database.

    Parameters:
    - eventtype_id (int): The ID of the event type to be deleted.

    Returns:
    - int: The number of rows deleted from the database.
    """
    return db.query(EventType).filter(EventType.id == eventtype_id).delete() and db.commit()


@router.put("/{eventtype_id}", response_model=EventTypeResponse)
def update_eventtype(eventtype_id: int, eventtype: EventTypeUpdate, db: Session = Depends(get_db)):
    """
    Updates an event type in the database.

    Parameters:
    - eventtype_id (int): The ID of the event type to be updated.
    - eventtype (EventTypeUpdate): An EventTypeUpdate object.

    Returns:
    - EventTypeResponse: The updated EventType object.
    """
    db_eventtype = db.query(EventType).filter(EventType.id == eventtype_id).first()
    if db_eventtype is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event type not found")
    for field in eventtype.model_dump():
        setattr(db_eventtype, field, eventtype.model_dump()[field])
    db.commit()
    db.refresh(db_eventtype)
    return db_eventtype
