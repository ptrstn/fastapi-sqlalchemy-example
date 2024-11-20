from mypackage.crud import get_user_by_email


def test_read_main(client):
    response = client.get("/api")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"Hello": "World"}


def test_get_items(client):
    response = client.get("/api/items/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == []


def test_get_users(client):
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == []


def test_post_user(client, session):
    test_user = {"email": "test@example.com", "password": "testpassword"}

    response = client.post("/api/users/", json=test_user)

    assert response.status_code == 201
    user = response.json()

    assert user["email"] == "test@example.com"
    assert "password" not in user
    assert user["id"] == 1
    assert user["is_active"]

    user = get_user_by_email(session, email=test_user["email"])
    assert user.email == test_user["email"]

    # Duplicate User
    response = client.post("/api/users/", json=test_user)
    assert response.status_code == 422
    assert response.json()["detail"] == "Email 'test@example.com' already registered"


def test_get_users_after_post(client):
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    content = response.json()
    assert len(content) == 1
    for user in content:
        assert "email" in user
        assert "password" not in user
        assert "id" in user
        assert "is_active" in user


def test_create_item(client):
    item = {"title": "test name", "description": "test description"}
    response = client.post("/api/items/", json=item)
    assert response.status_code == 201
    assert response.json() == item


def test_create_item_for_user(client):
    response = client.get("/api/users")
    users = response.json()
    assert len(users) == 1
    user = users[0]
    assert user["email"] == "test@example.com"
    user_id = user["id"]

    item = {"title": "Item2"}
    response = client.post(f"/api/users/{user_id}/items/", json=item)
    assert response.status_code == 201

    item_response_content = response.json()
    assert item_response_content["owner_id"] == user_id

    response = client.post(f"/api/users/{user_id + 1}/items/", json=item)
    assert response.status_code == 404
    assert response.json()["detail"] == "User with id '2' not found"
