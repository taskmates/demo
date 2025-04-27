from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from api.main import app
from api.models import Base, User
from api.endpoints.users import get_db

# Use SQLite in-memory database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables before running tests
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override the get_db dependency
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_get_user_with_email(client, db):
    # Create a user with email
    user = User(name="John Doe", email="john@example.com")
    db.add(user)
    db.commit()
    db.refresh(user)

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": user.id,
        "name": "John Doe",
        "email_domain": "example.com"
    }

def test_get_user_without_email(client, db):
    # Create a user without email
    user = User(name="Jane Doe", email=None)
    db.add(user)
    db.commit()
    db.refresh(user)

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": user.id,
        "name": "Jane Doe",
        "email_domain": None
    }
