from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from src.routes import reservation
from src.models.user import Modsets
from src.models.reservation import Reservation
from src.services.database import Base, engine, sessionLocal


Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(reservation.router)

@app.get("/api/routes", tags=["api"])
async def get_api_routes():
    return {"message": f"All routes: {app.routes}"}

