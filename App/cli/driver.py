import sys
from flask import Flask
from App.database import db
from App.models.driver import Driver

def register_driver_commands(app: Flask):
    @app.cli.command("list-drivers")
    def list_drivers():
        drivers = Driver.query.all()
        if not drivers:
            print("No drivers found")
            return
        for driver in drivers:
            print(f"ID: {driver.id}, Username: {driver.username}, Status: {driver.status}, Area: {driver.areaId}, Street: {driver.streetId}")

    @app.cli.command("create-driver")
    def create_driver():
        username = input("Username: ")
        password = input("Password: ")
        status = input("Status: ")
        area_id = int(input("Area ID: "))
        street_id = input("Street ID (optional): ")

        driver = Driver(
            username=username,
            password=password,
            status=status,
            areaId=area_id,
            streetId=street_id
        )

        db.session.add(driver)
        db.session.commit()
        print(f"Driver created with ID: {driver.id}")


    @app.cli.command("update-driver")
    def update_driver():
        driver_id = int(input("Driver ID: "))
        
        driver = Driver.query.get(driver_id)
        if not driver:
            print("Driver not found.")
            return

        print(f"Current username: {driver.username}")
        username = input("New username (press enter to keep current): ")
        
        print(f"Current status: {driver.status}")
        status = input("New status (press enter to keep current): ")
        
        print(f"Current area ID: {driver.areaId}")
        area_id_input = input("New area ID (press enter to keep current): ")
        
        print(f"Current street ID: {driver.streetId}")
        street_id_input = input("New street ID (press enter to keep current): ")

        if username:
            driver.username = username
        if status:
            driver.status = status
        if area_id_input:
            driver.areaId = int(area_id_input)
        if street_id_input:
            driver.streetId = int(street_id_input)

        db.session.commit()
        print(f"Driver {driver_id} updated successfully.")

    @app.cli.command("delete-driver")
    def delete_driver():
        driver_id = int(input("Driver ID to delete: "))
        
        driver = Driver.query.get(driver_id)
        if not driver:
            print("Driver not found.")
            return

        confirmation = input(f"Are you sure you want to delete driver '{driver.username}' (Y/N)) ")
        if confirmation.lower() in ['y', 'yes']:
            db.session.delete(driver)
            db.session.commit()
            print(f"Driver {driver_id} deleted successfully")
        else:
            print("Deletion failed")