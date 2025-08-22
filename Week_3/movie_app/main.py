from fastapi import FastAPI
from .database import engine, Base
from .routers import movies, users, ratings, recommend

app = FastAPI(title="Movie Recommendation API")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(movies.router)
app.include_router(users.router)
app.include_router(ratings.router)
app.include_router(recommend.router)
