from app.Models.Base import *

class Car(Base):
    id = PrimaryKeyField()
    model = CharField(max_length=255)
    licensePlate = CharField(unique=True, max_length=10)
    isAvailable = BooleanField(default=True)

if __name__ == "__main__":
    connect_db().create_tables([Car])