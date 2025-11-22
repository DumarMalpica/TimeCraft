from fastapi import APIRouter
from app.database.event_repository import (
    create_event,
    list_events,
    get_event,
    update_event,
    delete_event
)

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("/")
async def create_event_endpoint(title: str, description: str):
    data = {"title": title, "description": description}
    return await create_event(data)


@router.get("/")
async def list_events_endpoint():
    return await list_events()


@router.get("/{event_id}")
async def get_event_endpoint(event_id: str):
    return await get_event(event_id)


@router.put("/{event_id}")
async def update_event_endpoint(event_id: str, title: str, description: str):
    data = {"title": title, "description": description}
    return await update_event(event_id, data)


@router.delete("/{event_id}")
async def delete_event_endpoint(event_id: str):
    return await delete_event(event_id)
