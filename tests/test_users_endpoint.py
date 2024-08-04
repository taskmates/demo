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
    user_without_email = User(name="Bob", email=None)
    db.add(user_without_email)
    db.commit()

    # Check that the user was added to the database
    assert db.query(User).count() == 1

    response = client.get(f"/users/{user_without_email.id}")
    assert response.status_code == 200
    assert response.json() == {"id": user_without_email.id, "name": user_without_email.name, "email_domain": None}
