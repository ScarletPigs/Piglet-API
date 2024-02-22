"""Piglet API

Used to run the Piglet API and handle requests about the schedule.
Will be split into multiple files in the future.

Todo:
    * Add DLC poll functionality
    * Keep track of modlists
"""

from fastapi import FastAPI
from fastapi.params import Body
from src.routes import events
from src.models.user import User
from src.models.event import Event
from src.services.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(events.router)

library = {}

@app.get("/api/routes", tags=["api"])
async def get_api_routes():
    return {"message": f"All routes: {app.routes}"}
