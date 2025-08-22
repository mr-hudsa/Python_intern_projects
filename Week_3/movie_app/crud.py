from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from . import models, schemas

# ---------- USERS ----------
async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    # Eager load ratings before returning
    result = await db.execute(
        select(models.User)
        .options(selectinload(models.User.ratings))
        .where(models.User.id == db_user.id)
    )
    return result.scalars().first()

async def list_users(db: AsyncSession):
    res = await db.execute(
        select(models.User).options(selectinload(models.User.ratings))
    )
    return res.scalars().all()

# ---------- MOVIES ----------
async def create_movie(db: AsyncSession, movie: schemas.MovieCreate):
    db_movie = models.Movie(title=movie.title, genre=movie.genre)
    db.add(db_movie)
    await db.commit()
    await db.refresh(db_movie)

    result = await db.execute(
        select(models.Movie)
        .options(selectinload(models.Movie.ratings))
        .where(models.Movie.id == db_movie.id)
    )
    return result.scalars().first()

async def get_movies(db: AsyncSession):
    result = await db.execute(
        select(models.Movie).options(selectinload(models.Movie.ratings))
    )
    return result.scalars().all()

# ---------- RATINGS ----------
async def create_rating(db: AsyncSession, rating: schemas.RatingCreate):
    db_rating = models.Rating(
        user_id=rating.user_id,
        movie_id=rating.movie_id,
        score=rating.score
    )
    db.add(db_rating)
    await db.commit()
    await db.refresh(db_rating)

    return db_rating

async def list_ratings(db: AsyncSession):
    res = await db.execute(
        select(models.Rating)
        .options(
            selectinload(models.Rating.user),
            selectinload(models.Rating.movie)
        )
    )
    return res.scalars().all()

# ---------- RECOMMENDATIONS ----------
async def recommend_for_user(db: AsyncSession, user_id: int):
    # genres the user liked (score >= 4)
    liked_genres_res = await db.execute(
        select(models.Movie.genre)
        .join(models.Rating, models.Rating.movie_id == models.Movie.id)
        .where(models.Rating.user_id == user_id, models.Rating.score >= 4)
    )
    liked_genres = {row[0] for row in liked_genres_res.all()}
    if not liked_genres:
        return []

    # ids of movies already rated by user
    rated_ids_res = await db.execute(
        select(models.Rating.movie_id).where(models.Rating.user_id == user_id)
    )
    rated_ids = {row[0] for row in rated_ids_res.all()}

    # recommend movies in liked genres not yet rated
    rec_res = await db.execute(
        select(models.Movie)
        .options(selectinload(models.Movie.ratings))
        .where(models.Movie.genre.in_(liked_genres))
    )
    candidates = [m for m in rec_res.scalars().all() if m.id not in rated_ids]
    return candidates
