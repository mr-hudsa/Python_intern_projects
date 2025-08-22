from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from .. import schemas, crud, database

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_user(db, user)

@router.get("/", response_model=List[schemas.User])
async def list_users(db: AsyncSession = Depends(database.get_db)):
    return await crud.list_users(db)
