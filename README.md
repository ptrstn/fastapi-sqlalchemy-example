![example workflow](https://github.com/ptrstn/fastapi-sqlalchemy-example/actions/workflows/python-package.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# FastAPI + SQLAlchemy Example Package

This application is a simple REST API built with FastAPI and SQLAlchemy. It allows for basic operations for managing users and items.

## Installation

```bash
pip install -e .[test]
```

## Run

```bash
uvicorn src.mypackage.main:app
```

Afterwards you can proceed to http://127.0.0.1:8000/docs

## Test

```bash
pytest
```
