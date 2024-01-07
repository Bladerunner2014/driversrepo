from schemas import schemas
from models.models import Driver


def get_driver_by_id(db, driver_id: int):
    one_driver = db.query(Driver).filter(Driver.phone_number == driver_id).first()
    db.close()

    return one_driver


def get_drivers(db, skip: int = 0, limit: int = 100):
    drivers = db.query(Driver).offset(skip).limit(limit).all()
    db.close()

    return drivers


def delete_driver(db, driver_id: int):
    item = db.query(Driver).filter(Driver.driver_id == driver_id).first()
    db.delete(item)
    db.commit()
    db.close()
    return "item"


def create_driver(db, driver: schemas.Driverschema):
    driver_itam = Driver(driver_id=driver.driver_id, driver_name=driver.driver_name, phone_number=driver.phone_number,
                         overall_traveled_km=driver.overall_traveled_km, disabled=driver.disabled)
    db.add(driver_itam)
    db.commit()
    db.refresh(driver_itam)
    db.close()
    return driver_itam

# TODO UPDATE DRIVER
