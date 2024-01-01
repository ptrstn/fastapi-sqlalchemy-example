from mypackage.models import User, Item


def test_create_users_and_items(test_db):
    # Create users
    user1 = User(email="user1@example.com", password="password1", is_active=True)
    user2 = User(email="user2@example.com", password="password1", is_active=True)

    test_db.add(user1)
    test_db.add(user2)
    test_db.commit()

    # Create items
    item1 = Item(
        title="Item 1", description="Description for Item 1", owner_id=user1.id
    )
    item2 = Item(
        title="Item 2", description="Description for Item 2", owner_id=user1.id
    )
    item3 = Item(
        title="Item 3", description="Description for Item 3", owner_id=user2.id
    )

    test_db.add(item1)
    test_db.add(item2)
    test_db.add(item3)
    test_db.commit()

    # Test if users and items have been added successfully
    assert len(test_db.query(User).all()) == 2
    assert len(test_db.query(Item).all()) == 3

    test_db.close()
