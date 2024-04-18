from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from ..models.stat import Stat
from sqlalchemy.orm import Session
from ..services.database import get_db
from ..schemas.stat import *


router = APIRouter(
    prefix="/stat", tags=["statistic"], responses={200: {"model": StatResponse}})


@router.get("/", response_model=List[StatResponse])
async def get_all_statistics(db: Session = Depends(get_db)):
    """Get all stats"""
    settings = db.query(Stat).all()
    return settings


@router.get("/{id}", response_model=StatResponse)
async def get_statistic_by_id(id: int, db: Session = Depends(get_db)):
    """Get a stats by id"""
    setting = db.query(Stat).filter(Stat.id == id).first()
    if not setting:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Statistic not found")
    return setting


@router.post("/", response_model=StatResponse)
async def create_statistic(setting: StatCreate, db: Session = Depends(get_db)):
    """Create a new statistic"""
    db_setting = Stat(**setting.model_dump())
    db_setting.lastModified = datetime.now()
    db.add(db_setting)
    db.commit()
    db.refresh(db_setting)
    return db_setting


@router.put("/{id}", response_model=StatResponse)
async def update_statistic(id: int, setting: StatUpdate, db: Session = Depends(get_db)):
    """Update a statistic"""
    db_setting = db.query(Stat).filter(Stat.id == id).first()
    if not db_setting:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Statistic not found")
    db_setting.statName = setting.statName
    db_setting.value = setting.value
    db_setting.lastModified = datetime.now()
    db.commit()
    db.refresh(db_setting)
    return db_setting


@router.delete("/{id}")
async def delete_statistic(id: int, db: Session = Depends(get_db)):
    """Delete a statistic"""
    db_setting = db.query(Stat).filter(Stat.id == id).first()
    if not db_setting:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Statistic not found")
    db.delete(db_setting)
    db.commit()
    return {"message": "Deleted statistic"}
