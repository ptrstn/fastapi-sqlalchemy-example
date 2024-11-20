import pytest
from sqlalchemy.exc import SAWarning
from sqlmodel import select

from mypackage.models import User, Item


def test_create_users_and_items(session):
    user1 = User(
        email="user1@example.com",
        password="password1",
    )
    user2 = User(
        email="user2@example.com",
        password="password2",
        is_active=False,
    )

    session.add(user1)
    session.add(user2)
    session.commit()

    assert len(user1.items) == 0
    assert len(user2.items) == 0

    item1 = Item(
        title="Item 1",
        description="Description for Item 1",
        owner=user1,
    )
    item2 = Item(
        title="Item 2",
        description="Description for Item 2",
        owner=user1,
    )
    item3 = Item(
        title="Item 3",
        description="Description for Item 3",
        owner=user2,
    )

    assert len(user1.items) == 2
    assert len(user2.items) == 1

    with pytest.warns(SAWarning):
        session.refresh(user1)
        assert len(user1.items) == 0  # Transient state of item1 and item2
        assert len(user2.items) == 1

    session.add(item1)
    session.add(item2)
    session.add(item3)
    session.commit()

    all_users = session.exec(select(User)).all()
    all_items = session.exec(select(Item)).all()

    assert len(all_users) == 2
    assert len(user1.items) == 2
    assert user1.items[0].title == "Item 1"
    assert user1.items[1].description == "Description for Item 2"
    assert len(user2.items) == 1
    assert len(all_items) == 3

    assert item1.owner == user1
    assert item2.owner == user1
    assert item3.owner == user2

    assert item1.owner.is_active
    assert item2.owner.is_active
    assert not item3.owner.is_active
