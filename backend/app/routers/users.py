from fastapi import APIRouter
from ..database import db
from ..models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def create_user(user: User):
    result = await db.users.insert_one(user.dict(exclude={"id"}))
    user.id = str(result.inserted_id)
    return user


@router.get("/")
async def get_users():
    cursor = db.users.find({})
    return [User(id=str(doc["_id"]), name=doc["name"], email=doc["email"]) async for doc in cursor]
