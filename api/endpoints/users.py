from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api.database import SessionLocal
from api.models import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    print(f"Searching for user with ID: {user_id}")
    user = db.query(User).filter(User.id == user_id).first()
    print(f"Found user: {user}")
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = {"id": user.id, "name": user.name}
    if user.email:
        user_data["email_domain"] = user.email.split("@")[1]

    return user_data
