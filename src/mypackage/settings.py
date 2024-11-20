from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    dialect: str = "sqlite"
    username: Optional[str] = None
    password: Optional[str] = None
    hostname: Optional[str] = None
    port: Optional[int] = None
    database: Optional[str] = "db.sqlite"

    @property
    def database_url(self) -> str:
        if self.dialect == "sqlite":
            if self.database:
                return f"{self.dialect}:///{self.database}"
            return f"{self.dialect}://"
        if not self.port:
            return (
                f"{self.dialect}://"
                f"{self.username}:{self.password}@"
                f"{self.hostname}/"
                f"{self.database}"
            )
        return (
            f"{self.dialect}://"
            f"{self.username}:{self.password}@"
            f"{self.hostname}:{self.port}/"
            f"{self.database}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="DB_",
    )


database_settings = DatabaseSettings()
