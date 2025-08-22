from pydantic import BaseModel
from typing import List, Optional

class RatingBase(BaseModel):
    score: int

class RatingCreate(RatingBase):
    user_id: int
    movie_id: int

class Rating(RatingBase):
    id: int
    user_id: int
    movie_id: int

    class Config:
        from_attributes = True

class MovieBase(BaseModel):
    title: str
    genre: str

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    ratings: List[Rating] = []

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    ratings: List['Rating'] = []

    class Config:
        from_attributes = True
