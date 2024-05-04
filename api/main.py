from fastapi import FastAPI
from api.endpoints.users import router as users_router
from api.database import engine
from api.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["users"])
