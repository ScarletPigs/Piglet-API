from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from ..models.setting import Setting
from sqlalchemy.orm import Session
from ..services.database import get_db
from ..schemas.setting import *


router = APIRouter(prefix="/settings", tags=["settings"], responses={200: {"model": SettingResponse}})




@router.get("/", response_model=List[SettingResponse])
async def get_all_settings(db: Session = Depends(get_db)):
    """Get all settings"""
    settings = db.query(Setting).all()
    return settings


@router.get("/{id}", response_model=SettingResponse)
async def get_setting_by_id(id: int, db: Session = Depends(get_db)):
    """Get a setting by id"""
    setting = db.query(Setting).filter(Setting.id == id).first()
    if not setting:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Setting not found")
    return setting


@router.post("/", response_model=SettingResponse)
async def create_setting(setting: SettingBase, db: Session = Depends(get_db)):
    """Create a new setting"""
    db_setting = Setting(setting.model_dump())
    db.add(db_setting)
    db.commit()
    db.refresh(db_setting)
    return db_setting


@router.put("/{id}", response_model=SettingResponse)
async def update_setting(id: int, setting: SettingUpdate, db: Session = Depends(get_db)):
    """Update a setting"""
    db_setting = db.query(Setting).filter(Setting.id == id).first()
    if not db_setting:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Setting not found")
    db_setting.name = setting.name
    db_setting.value = setting.value
    db.commit()
    db.refresh(db_setting)
    return db_setting


@router.delete("/{id}")
async def delete_setting(id: int, db: Session = Depends(get_db)):
    """Delete a setting"""
    db_setting = db.query(Setting).filter(Setting.id == id).first()
    if not db_setting:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Setting not found")
    db.delete(db_setting)
    db.commit()
    return {"message": "Deleted setting"}

