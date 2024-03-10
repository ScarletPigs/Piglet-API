from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from ..models.poll import Poll
from sqlalchemy.orm import Session
from ..services.database import get_db
from ..schemas.poll import *


router = APIRouter(prefix="/polls", tags=["polls"], responses={200: {"model": PollResponse}})



@router.get("/", response_model=List[PollResponse])
def get_polls(db: Session = Depends(get_db)):
    """
    Get the list of all polls from the database
    """
    polls = db.query(Poll).all()
    return polls


@router.post("/")
def create_poll(poll: PollCreate, db: Session = Depends(get_db)):
    """
    Create a poll with the given poll data and add it to the database
    """
    poll_obj = Poll(**poll.model_dump())
    db.add(poll_obj)
    db.commit()
    db.refresh(poll_obj)
    return poll_obj


@router.get("/{poll_id}")
def get_poll(poll_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a poll by its ID
    """
    poll = db.query(Poll).filter_by(id=poll_id).first()
    if not poll:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poll not found")
    return poll


@router.put("/{poll_id}", response_model=int)
def update_poll(poll_id: int, poll: PollUpdate, db: Session = Depends(get_db)):
    """
    Update a poll with the given poll_id using the provided PollUpdate model.
    """
    rows_affected = db.query(Poll).filter_by(id=poll_id).update(**poll.model_dump())
    if rows_affected < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poll not found")
    db.commit()
    return rows_affected


@router.delete("/{poll_id}", response_model=int)
def delete_poll(poll_id: int, db: Session = Depends(get_db)):
    """
    Delete a poll by its ID.
    """
    rows_affected = db.query(Poll).filter_by(id=poll_id).delete()
    if rows_affected < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poll not found")
    db.commit()
    return rows_affected

