from mypackage.models import User, Item


def test_create_users_and_items(test_db):
    user1 = User(
        email="user1@example.com",
        password="password1",
    )
    user2 = User(
        email="user2@example.com",
        password="password2",
        is_active=False,
    )

    test_db.add(user1)
    test_db.add(user2)
    test_db.commit()

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

    test_db.refresh(user1)
    assert len(user1.items) == 0  # Transient state of item1 and item2
    assert len(user2.items) == 1

    test_db.add(item1)
    test_db.add(item2)
    test_db.add(item3)
    test_db.commit()

    assert len(test_db.query(User).all()) == 2
    assert len(user1.items) == 2
    assert user1.items[0].title == "Item 1"
    assert user1.items[1].description == "Description for Item 2"
    assert len(user2.items) == 1
    assert len(test_db.query(Item).all()) == 3

    assert item1.owner == user1
    assert item2.owner == user1
    assert item3.owner == user2

    assert item1.owner.is_active
    assert item2.owner.is_active
    assert not item3.owner.is_active
