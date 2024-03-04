from fastapi import APIRouter, HTTPException, status, Depends
from ..models.reservation import Reservation
from ..models.user import Modsets
from datetime import date
from sqlalchemy.orm import Session
from ..services.database import get_db

router = APIRouter(prefix="/reservations", tags=["reservations"])


# Create a new reservation
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_reservation(body, db: Session = Depends(get_db)):
    newEvent = Reservation(**body)
    db.add(newEvent)
    db.commit()
    db.refresh(newEvent)
    return {"status": "success", "data": newEvent}

# Get all reservations
@router.get("/")
def get_reservations(db: Session = Depends(get_db)):
    return {"status": "success", "data": db.query(Reservation).all()}

# Get a specific reservation
@router.get("/{event_id}")
def get_reservation(event_id, db: Session = Depends(get_db)):
    return {"status": "success", "data": db.query(Reservation).filter(Reservation.id == event_id).first()}

# Update a reservation
@router.put("/{event_id}")
def update_reservation(event_id, body, db: Session = Depends(get_db)):
    return {"status": "success", "data": db.query(Reservation).filter(Reservation.id == event_id).update(body) and db.commit()}

# Delete a reservation
@router.delete("/{event_id}")
def delete_reservation(event_id, db: Session = Depends(get_db)):
    return {"status": "success", "data": db.query(Reservation).filter(Reservation.id == event_id).delete()
            and db.commit()
            and db.query(Reservation).filter(Reservation.id == event_id).first()}