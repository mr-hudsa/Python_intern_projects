from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from .. import schemas, crud, database

router = APIRouter(prefix="/ratings", tags=["Ratings"])

@router.post("/", response_model=schemas.Rating)
async def create_rating(rating: schemas.RatingCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_rating(db, rating)

@router.get("/", response_model=List[schemas.Rating])
async def list_ratings(db: AsyncSession = Depends(database.get_db)):
    return await crud.list_ratings(db)
