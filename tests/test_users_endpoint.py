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
