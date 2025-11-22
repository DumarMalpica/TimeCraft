from fastapi import FastAPI
from app.routes.events import router as events_router
from app.routes.users import router as users_router

def create_app():
    app = FastAPI(title="TimeCraft API")

    app.include_router(events_router)
    app.include_router(users_router)

    return app

app = create_app()
