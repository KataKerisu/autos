from app.Models.Base import *
from app.Models.Car import Car
from datetime import datetime

class Rental(Base):
    id = PrimaryKeyField()
    carId = ForeignKeyField(Car, backref='rentals')
    customerName = CharField(max_length=255)
    startDate = DateTimeField(default=datetime.now)
    endDate = DateTimeField()


if __name__ == "__main__":
    connect_db().create_tables([Rental])