from contextlib import asynccontextmanager

from fastapi import FastAPI

from mypackage.api.v1.router import api_router
from mypackage.database import create_db_and_tables


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
