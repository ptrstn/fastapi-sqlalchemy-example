[![Python package](https://github.com/ptrstn/fastapi-sqlalchemy-pytest-example/actions/workflows/python-package.yml/badge.svg)](https://github.com/ptrstn/fastapi-sqlalchemy-pytest-example/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/ptrstn/fastapi-sqlalchemy-pytest-example/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/fastapi-sqlalchemy-pytest-example)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-darkblue.svg)](http://unlicense.org/)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

# FastAPI + SQLAlchemy + Pytest Example Package

This application is a simple REST API built with FastAPI and SQLAlchemy and tested with pytest. 
It allows for basic operations for managing users and items.

This code is in the public domain, so feel free to do with it whatever you want.

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/ptrstn/fastapi-sqlalchemy-pytest-example/
cd fastapi-sqlalchemy-pytest-example
python -m venv venv
. venv/bin/activate
```

Then install the package (and the optional testing dependencies) with:

```bash
pip install -e .[test]
```

## Usage

```bash
uvicorn src.mypackage.main:app
```

## Endpoints

### User Endpoints

- **POST /users/**  
  This endpoint creates a new user. 
  It accepts a JSON body with email and password fields and creates a new user record in the database. 
  If successful, it returns the details of the created user. 
  If a user with the specified email already exists, it returns a 422 Unprocessable Entity error with a message indicating that the email is already registered.
- **GET /users/**  
  This endpoint retrieves a list of all users. 
  When a GET request is sent to this endpoint, it will return a list of all users in the database.

### Item Endpoints:
- **POST /items/**  
  This endpoint creates a new item. 
  It accepts a JSON body with required item details. 
  Upon successful creation, it returns a response with the details of the created item.
- **GET /items/**  
  This endpoint retrieves a list of all items. 
  When a GET request is sent to this endpoint, it will return a list of items existing in the database.


For more details proceed to the built-in docs at http://127.0.0.1:8000/docs


## Testing

The tests for this application use an in-memory SQLite database. 
Before each test module, a new database is created. 
This approach keeps the tests isolated, ensuring that changes made in one test do not affect any others.
The application's main database connection is overwritten in the testing environment to use the in-memory SQLite database instead. 
This is done by overriding the get_db dependency in the tests [conftest.py](/tests/conftest.py), which supplies the FastAPI application with the database session. 
We replace the standard application database with the session of our in-memory SQLite database instead.
By doing this, we can test the application's interaction with the database, without modifying the actual database. 
Also, using an in-memory SQLite database makes these tests much faster to run compared to if they were to use a standard SQL database.

To run the tests, execute the pytest command from the project's root directory:

```bash
pytest
```
