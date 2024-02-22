from fastapi import FastAPI
from fastapi.params import Body
from src.routes import events
from src.models.user import User
from src.models.event import Event
from src.services.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(events.router)

library = {}

@app.get("/")
async def index():
    return {"message": f"All routes: {app.routes}"}
