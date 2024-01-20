from sqlalchemy import Boolean, Column, Integer, String
from db.orm_database import Base
from datetime import datetime
from datetime import timezone


class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True)
    driver_name = Column(String)
    driver_id=Column(Integer)
    phone_number = Column(Integer)
    overall_traveled_km = Column(String)
    # car_model = Column(String)
    disabled = Column(Boolean)
    # plate_number = Column(String)
    created_at = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    last_trip = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    assigned_car = Column(String)
