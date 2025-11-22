from app.database.mongodb import db
from bson import ObjectId


async def create_event(data: dict):
    result = await db["events"].insert_one(data)
    data["_id"] = str(result.inserted_id)
    return data


async def list_events():
    events = await db["events"].find().to_list(100)
    for e in events:
        e["_id"] = str(e["_id"])
    return events


async def get_event(event_id: str):
    event = await db["events"].find_one({"_id": ObjectId(event_id)})
    if event:
        event["_id"] = str(event["_id"])
    return event


async def update_event(event_id: str, data: dict):
    await db["events"].update_one(
        {"_id": ObjectId(event_id)},
        {"$set": data}
    )
    return await get_event(event_id)


async def delete_event(event_id: str):
    await db["events"].delete_one({"_id": ObjectId(event_id)})
    return {"deleted": True}
