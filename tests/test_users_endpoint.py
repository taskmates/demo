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

def test_get_user_without_email(db, client):
    # Create test data for a user without an email
    user = User(name="Bob", email=None)
    db.add(user)
    db.commit()

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json() == {"id": user.id, "name": user.name}
    # Verify that email_domain is not in the response
    assert "email_domain" not in response.json()
