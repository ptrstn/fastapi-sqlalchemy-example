# FastAPI + SQLAlchemy example package

This application is a simple REST API built with FastAPI and SQLAlchemy. It allows for basic operations for managing users and items.

## Installation

```bash
pip install -e .[test]
```

## Run

```bash
uvicorn src.mypackage.main:app
```

Afterwards you can continue with http://127.0.0.1:8000/docs

## Test

```bash
pytest
```
