from schemas import schemas
from models.models import Driver
from sqlalchemy import inspect


def object_as_dict(obj):
    return {
        c.key: getattr(obj, c.key)
        for c in inspect(obj).mapper.column_attrs
    }


def get_driver_by_id(db, driver_id):
    one_driver = db.query(Driver).filter(Driver.driver_id == driver_id).first()
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
    driver_itam = Driver(**driver.dict())
    db.add(driver_itam)
    db.commit()
    db.refresh(driver_itam)
    db.close()
    return driver_itam


# TODO UPDATE DRIVER
def update_driver(db, driver: Driver):
    delete_driver(db, driver_id=driver.driver_id)
    driver = object_as_dict(driver)
    driver_item = Driver(**driver)
    db.add(driver_item)
    db.commit()
    db.refresh(driver_item)
    db.close()
    return
