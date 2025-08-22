from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from .. import schemas, crud, database

router = APIRouter(prefix="/recommend", tags=["Recommendation"])

@router.get("/{user_id}", response_model=List[schemas.Movie])
async def recommend_movies(user_id: int, db: AsyncSession = Depends(database.get_db)):
    return await crud.recommend_for_user(db, user_id)
