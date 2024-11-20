from mypackage.settings import DatabaseSettings


def test_in_memory_sqlite():
    settings = DatabaseSettings(dialect="sqlite", database=":memory:")
    assert settings.database_url == "sqlite:///:memory:"


def test_in_memory_sqlite_no_filename():
    settings = DatabaseSettings(dialect="sqlite", database=None)
    assert settings.database_url == "sqlite://"

    settings = DatabaseSettings(dialect="sqlite", database="")
    assert settings.database_url == "sqlite://"


def test_sqlite_file():
    settings = DatabaseSettings(dialect="sqlite", database="db.sqlite3")
    assert settings.database_url == "sqlite:///db.sqlite3"


def test_mongodb():
    settings = DatabaseSettings(
        dialect="mongodb",
        username="user",
        password="password",
        hostname="localhost",
        port=27017,
        database="mydb",
    )
    assert settings.database_url == "mongodb://user:password@localhost:27017/mydb"


def test_postgres():
    settings = DatabaseSettings(
        dialect="postgresql",
        username="user",
        password="password",
        hostname="localhost",
        port=5432,
        database="mydb",
    )
    assert settings.database_url == "postgresql://user:password@localhost:5432/mydb"


def test_postgres_no_port():
    settings = DatabaseSettings(
        dialect="postgresql",
        username="user",
        password="password",
        hostname="localhost",
        database="mydb",
    )
    assert settings.database_url == "postgresql://user:password@localhost/mydb"
