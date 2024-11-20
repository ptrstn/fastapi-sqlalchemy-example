from fastapi import FastAPI

from mypackage.api.v1.router import api_router
from mypackage.database import create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(api_router)
