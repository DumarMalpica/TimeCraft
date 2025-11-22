from fastapi import FastAPI
from .routers import users

app = FastAPI(title="AI Projects Backend")

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Backend funcionando correctamente"}
