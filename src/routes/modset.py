from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from ..models.modset import Modset
from sqlalchemy.orm import Session
from ..services.database import get_db
from ..schemas.modset import *


router = APIRouter(prefix="/modsets", tags=["modsets"], responses={200: {"model": ModsetResponse}})




@router.get("/", response_model=List[ModsetResponse])
async def get_all_modsets(db: Session = Depends(get_db)):
    """Get all modsets"""
    return db.query(Modset).all()


@router.get("/{modset_id}")
async def get_modset_by_id(modset_id: int, db: Session = Depends(get_db)):
    """Get modset by id"""
    modset = db.query(Modset).filter(Modset.id == modset_id).first()
    if not modset:
        raise HTTPException(status_code=404, detail="Modset not found")
    return modset


@router.post("/")
async def create_modset(modset: ModsetBase, db: Session = Depends(get_db)):
    """Create a new modset"""
    db_modset = Modset(**modset.model_dump())
    db.add(db_modset)
    db.commit()
    db.refresh(db_modset)
    return db_modset


@router.put("/{modset_id}")
async def update_modset(modset_id: int, modset: ModsetUpdate, db: Session = Depends(get_db)):
    """Update a modset"""
    db_modset = db.query(Modset).filter(Modset.id == modset_id).first()
    if not db_modset:
        raise HTTPException(status_code=404, detail="Modset not found")
    for field in modset.__dict__.keys():
        if field != "from_attributes":
            setattr(db_modset, field, modset.__dict__[field])
    db.commit()
    db.refresh(db_modset)
    return db_modset


@router.delete("/{modset_id}")
async def delete_modset(modset_id: int, db: Session = Depends(get_db)):
    """Delete a modset"""
    modset = db.query(Modset).filter(Modset.id == modset_id).first()
    if not modset:
        raise HTTPException(status_code=404, detail="Modset not found")
    db.delete(modset)
    db.commit()
    return {"message": "Modset deleted successfully"}



