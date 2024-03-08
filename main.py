from fastapi import FastAPI
from src.routes import event, eventtype
from src.services.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(event.router)
app.include_router(eventtype.router)

@app.get("/api/routes", tags=["api"])
async def get_api_routes():
    """
    Get the API routes and return them as a list of BaseRoute objects.
    """
    return app.routes

