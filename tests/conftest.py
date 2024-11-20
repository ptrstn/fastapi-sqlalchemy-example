import pytest
from fastapi.testclient import TestClient

from mypackage import database
from mypackage.main import app


@pytest.fixture(scope="module", autouse=True)
def create_test_database():
    database.create_db_and_tables()
    yield
    database.drop_db()


@pytest.fixture(scope="function")
def session():
    yield from database.get_session()


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client
