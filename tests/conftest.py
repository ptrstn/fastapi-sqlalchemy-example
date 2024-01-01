import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from mypackage.database import Base, get_db
from mypackage.main import app

SQLALCHEMY_TEST_DATABASE_URL = "sqlite://"

# https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#using-a-memory-database-in-multiple-threads
engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # necessary for in-memory database
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_db():
    yield from create_session()


app.dependency_overrides[get_db] = override_get_db  # Override the get_db function


@pytest.fixture(scope="module", autouse=True)
def create_test_database():
    # Create tables for every test module
    Base.metadata.create_all(bind=engine)
    yield
    # Drop all the tables after the tests are done
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def test_db():
    yield from create_session()


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client
