from sqlalchemy import Engine, StaticPool, create_engine
from sqlmodel import SQLModel, Session

from mypackage.settings import DatabaseSettings, database_settings


def create_engine_from_config(config: DatabaseSettings = database_settings) -> Engine:
    kwargs = {}
    if config.dialect == "sqlite":
        kwargs["connect_args"] = {"check_same_thread": False}
    if not config.database or config.database == ":memory:":
        kwargs["poolclass"] = StaticPool

    return create_engine(config.database_url, **kwargs)


engine = create_engine_from_config(config=database_settings)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def drop_db() -> None:
    SQLModel.metadata.drop_all(engine)


def get_session() -> Session:
    with Session(engine) as session:
        yield session
