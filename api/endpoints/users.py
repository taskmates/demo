from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import SessionLocal
from ..models import User

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

    if user.email:
        email_domain = user.email.split("@")[1]
        return {"id": user.id, "name": user.name, "email_domain": email_domain}
    else:
        return {"id": user.id, "name": user.name}
