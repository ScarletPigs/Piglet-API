from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from ..models.pollresponse import PollResponse
from sqlalchemy.orm import Session
from ..services.database import get_db
from ..schemas.pollresponse import *


router = APIRouter(prefix="/pollresponses", tags=["pollresponses"], responses={200: {"model": PollResponseBase}})



@router.get("/", response_model=List[PollResponseReturn])
async def get_all_poll_responses(db: Session = Depends(get_db)):
    """Get all poll responses"""
    return db.query(PollResponse).all()


@router.get("/{poll_id}", response_model=List[PollResponseReturn])
async def get_poll_responses(poll_id: int, db: Session = Depends(get_db)):
    """Get all responses from specific poll"""
    poll_response = db.query(PollResponse).filter(PollResponse.pollId == poll_id).all()
    if not poll_response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poll responses not found")
    return poll_response

@router.get("/{poll_response_id}", response_model=PollResponseReturn)
async def get_poll_response(poll_response_id: int, db: Session = Depends(get_db)):
    """Get specific response"""
    poll_response = db.query(PollResponse).filter(PollResponse.id == poll_response_id).first()
    if not poll_response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poll response not found")
    return poll_response


@router.post("/")
async def create_poll_response(poll_response: PollResponseCreate, db: Session = Depends(get_db)):
    """Create a new poll response"""
    new_poll_response = PollResponse(**poll_response.model_dump())
    db.add(new_poll_response)
    db.commit()
    db.refresh(new_poll_response)
    return new_poll_response


@router.put("/{poll_response_id}")
async def update_poll_response(poll_response_id: int, poll_response: PollResponseUpdate, db: Session = Depends(get_db)):
    """Update a poll response"""
    poll_response_db = db.query(PollResponse).filter(PollResponse.id == poll_response_id).first()
    if not poll_response_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poll response not found")
    poll_response_db.update(**poll_response.model_dump())
    db.commit()
    db.refresh(poll_response_db)
    return poll_response_db


@router.delete("/{poll_response_id}")
async def delete_poll_response(poll_response_id: int, db: Session = Depends(get_db)):
    """Delete a poll response"""
    poll_response = db.query(PollResponse).filter(PollResponse.id == poll_response_id).first()
    if not poll_response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Poll response not found")
    db.delete(poll_response)
    db.commit()
    return {"message": "Deleted poll response"}



