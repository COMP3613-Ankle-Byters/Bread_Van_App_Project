from App.models import Resident, Stop, Drive, Area, Street, DriverStock, Driver
from App.database import db

def resident_create(username, password, area_id, street_id, house_number):
    resident = Resident(username=username, password=password, areaId=area_id, streetId=street_id, houseNumber=house_number)
    db.session.add(resident)
    db.session.commit()
    return resident

def resident_request_stop(resident, drive_id):
    drives = Drive.query.filter_by(areaId=resident.areaId, streetId=resident.streetId, status="Upcoming").all()
    if not any(d.id == drive_id for d in drives):
        raise ValueError("Invalid drive choice.")
    existing_stop = Stop.query.filter_by(driveId=drive_id, residentId=resident.id).first()
    if existing_stop:
        raise ValueError(f"You have already requested a stop for drive {drive_id}.")
    
    try:
        new_stop = Stop(driveId=drive_id, residentId=resident.id)
        db.session.add(new_stop)
        db.session.commit()
        return new_stop
    except Exception:
        db.session.rollback()
        return None

def resident_cancel_stop(resident, drive_id):
    stop = Stop.query.filter_by(driveId=drive_id, residentId=resident.id).first()
    if not stop:
        raise ValueError("No stop requested for this drive.")
    db.session.delete(stop)
    db.session.commit()
    return stop

def resident_view_inbox(user_or_resident):
    if isinstance(user_or_resident, Resident):
        return [notif.get_json() for notif in user_or_resident.inbox]

    resident = Resident.query.filter_by(id=user_or_resident.id).first()
    if resident:
        return [notif.get_json() for notif in resident.inbox]
    
    raise ValueError("Could not find resident profile")

def resident_view_driver_stats(resident, driver_id):
    driver = Driver.query.get(driver_id)
    if not driver:
        raise ValueError("Driver not found.")

    stocks = DriverStock.query.filter_by(driverId=driver_id).all()
    stock_json = [s.get_json() for s in stocks]

    driver_info = driver.get_json() if hasattr(driver, 'get_json') else {
        "id": driver.id,
        "username": driver.username,
        "areaId": getattr(driver, "areaId", None),
        "streetId": getattr(driver, "streetId", None)
    }

    driver_info["stock"] = stock_json
    return driver_info

def resident_view_stock(resident, driver_id):
    driver = Driver.query.get(driver_id)
    if not driver:
        raise ValueError("Driver not found.")
    stocks = DriverStock.query.filter_by(driverId=driver_id).all()
    return stocks
