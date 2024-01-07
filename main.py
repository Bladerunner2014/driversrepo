from fastapi import HTTPException, status
from fastapi.responses import ORJSONResponse

from models import models
from schemas import schemas
from db.orm_database import SessionLocal, engine
from dotenv import dotenv_values
from fastapi import FastAPI
import logging
from log import log
from fastapi.middleware.cors import CORSMiddleware
from dao import driver_dao

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
config = dotenv_values(".env")
logger = logging.getLogger(__name__)


@app.post("/driver/", response_model=schemas.Driverschema)
def create_car(driver: schemas.Driverschema):
    db = SessionLocal()
    db_user = driver_dao.get_driver_by_id(db, driver.driver_id)
    if db_user:
        raise HTTPException(status_code=400, detail="driver already registered")
    res = driver_dao.create_driver(db=db, driver=driver)
    return res


@app.get("/driver/")
def read_cars(skip: int = 0, limit: int = 100):
    db = SessionLocal()
    drivers = driver_dao.get_drivers(db, skip=skip, limit=limit)
    if drivers is None:
        raise HTTPException(status_code=404, detail="no driver found")
    return drivers


@app.get("/driver/{driver_id}", response_model=schemas.Driverschema)
def read_car(driver_id):
    db = SessionLocal()
    plate = driver_dao.get_driver_by_id(db, driver_id=driver_id)
    if plate is None:
        raise HTTPException(status_code=404, detail="driver not found")
    return plate


@app.delete("/drivers/{driver_id}", response_model=schemas.Driverschema)
def delete_car(driver_id: int):
    db = SessionLocal()
    db_user = driver_dao.get_driver_by_id(db, driver_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="driver not found")
    plate = driver_dao.delete_driver(db, driver_id=driver_id)
    return ORJSONResponse(status_code=status.HTTP_200_OK, content={"message": "driver deleted successfully"})


log.setup_logger()
