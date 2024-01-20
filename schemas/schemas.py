from pydantic import BaseModel


class Driverschema(BaseModel):
    driver_name: str
    driver_id: int
    # connection_status: bool | None = None
    phone_number: int
    overall_traveled_km: int | None = None
    # car_model: str
    disabled: bool | None = None
    # plate_number: str
    created_at: str | None = None
    last_trip: str | None = None
    assigned_car: str | None = None

    class Config:
        orm_mode = True
