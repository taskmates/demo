from api.models import User

def test_get_user(db, client):
    # Create test data
    user = User(name="Alice", email="alice@example.com")
    db.add(user)
    db.commit()

    # Check that the user was added to the database
    assert db.query(User).count() == 1

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json() == {"id": user.id, "name": user.name, "email_domain": "example.com"}

def test_get_user_no_email(db, client):
    # Create a user without an email address
    user = User(name="John Doe")
    db.add(user)
    db.commit()

    # Call the /users/{id} endpoint
    response = client.get(f"/users/{user.id}")

    # Assert the response status code is 200
    assert response.status_code == 200
    # Assert the response data contains the user's ID and name
    assert response.json() == {"id": user.id, "name": user.name}
