from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: str = Field(index=True, unique=True)
    password: str
    is_active: bool = Field(default=True)

    items: List["Item"] = Relationship(back_populates="owner")


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: str = Field(index=True)
    description: Optional[str] = Field(default=None, index=True)
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")

    owner: Optional["User"] = Relationship(back_populates="items")
