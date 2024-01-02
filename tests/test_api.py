from mypackage.crud import get_user_by_email


def test_read_main(test_client):
    response = test_client.get("/api")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"Hello": "World"}


def test_get_items(test_client):
    response = test_client.get("/api/items/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == []


def test_get_users(test_client):
    response = test_client.get("/api/users")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == []


def test_post_user(test_client, test_db):
    test_user = {"email": "test@example.com", "password": "testpassword"}

    response = test_client.post("/api/users/", json=test_user)

    assert response.status_code == 201
    content = response.json()

    assert "email" in content
    assert content["email"] == "test@example.com"
    assert "id" in content
    assert type(content["id"]) is int

    user = get_user_by_email(test_db, email=test_user["email"])
    assert user.email == test_user["email"]

    # Duplicate User
    response = test_client.post("/api/users/", json=test_user)
    assert response.status_code == 422
    assert response.json()["detail"] == "Email 'test@example.com' already registered"


def test_get_users_after_post(test_client):
    response = test_client.get("/api/users")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    content = response.json()
    assert len(content) == 1


def test_create_item(test_client):
    item = {"title": "test name", "description": "test description"}
    response = test_client.post("/api/items/", json=item)
    assert response.status_code == 201
    assert response.json() == item
