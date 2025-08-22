from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from .. import schemas, crud, database

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/", response_model=schemas.Movie)
async def create_movie(movie: schemas.MovieCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_movie(db, movie)

@router.get("/", response_model=List[schemas.Movie])
async def read_movies(db: AsyncSession = Depends(database.get_db)):
    return await crud.get_movies(db)
