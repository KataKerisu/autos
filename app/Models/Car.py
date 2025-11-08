from app.Models.Base import *

class Car(Base):
    id = PrimaryKeyField()
    model = CharField(max_length=255)
    licensePlate = CharField(max_length=10)
    isAvailable =