from fastapi import APIRouter
from app.database.mongodb import db

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def get_users():
    users = await db["users"].find().to_list(100)
    for u in users:
        u["_id"] = str(u["_id"])
    return users
