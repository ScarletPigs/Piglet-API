from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from ..models.userrole import UserRole
from sqlalchemy.orm import Session
from ..services.database import get_db
from ..schemas.userrole import *


router = APIRouter(prefix="/userroles", tags=["userroles"], responses={200: {"model": UserRoleResponse}})


@router.get("/", response_model=List[UserRoleResponse])
def get_all_user_roles(db: Session = Depends(get_db)):
    """
    Retrieve all user roles in the database.

    Returns:
    - List[UserRoleResponse]: A list of user roles.
    """
    user_roles = db.query(UserRole).all()
    return user_roles

@router.get("/{name}")
def get_user_role(name: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific user role by name.

    Parameters:
    - name (str): The name of the user role.

    Returns:
    - UserRoleResponse: The user role.
    """
    user_role = db.query(UserRole).filter(UserRole.name == name).first()
    if user_role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User role not found")
    return user_role

@router.post("/")
def create_user_role(user_role: UserRoleCreate, db: Session = Depends(get_db)):
    """
    Create a new user role.

    Parameters:
    - user_role (UserRoleCreate): The user role to be created.

    Returns:
    - UserRoleResponse: The created user role.
    """
    new_user_role = UserRole(**user_role.model_dump())
    db.add(new_user_role)
    db.commit()
    db.refresh(new_user_role)
    return new_user_role

@router.delete("/{name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_role(name: str, db: Session = Depends(get_db)):
    """
    Delete a user role by name.

    Parameters:
    - name (str): The name of the user role to be deleted.
    """
    user_role = db.query(UserRole).filter(UserRole.name == name).first()
    if user_role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User role not found")
    db.delete(user_role)
    db.commit()


@router.put("/{name}")
def update_user_role(name: str, user_role: UserRoleUpdate, db: Session = Depends(get_db)):
    """
    Update a user role by name.

    Parameters:
    - name (str): The name of the user role to be updated.
    - user_role (UserRoleUpdate): The updated user role.

    Returns:
    - UserRoleResponse: The updated user role.
    """
    db_user_role = db.query(UserRole).filter(UserRole.name == name).first()
    if db_user_role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User role not found")
    for field in user_role.dict():
        setattr(db_user_role, field, getattr(user_role, field))
    db.commit()
    db.refresh(db_user_role)
    return db_user_role

