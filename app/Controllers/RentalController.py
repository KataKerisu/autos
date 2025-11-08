from app.Models.Rental import Rental
from app.Models.Car import Car
from datetime import datetime


class RentalController:
    @classmethod
    def get(cls):
        """Получить список аренду"""
        query = Rental.select()
        return query

    @classmethod
    def add(cls, carId, customerName):
        '''Начать аренду/Создать аренду'''
        Rental.create(
            carId = carId,
            customerName = customerName
        )
        Car.update(isAvailable=False).where(Car.id == carId).execute()

        return Rental

    @classmethod
    def end(cls, id):
        """Завершить аренду"""
        rental = Rental.get_or_none(Rental.id == id)
        if rental:
            Rental.update(endDate=datetime.now()).where(Rental.id == id).execute()
            Car.update(isAvailable=True).where(Car.id == rental.carId).execute()


    @classmethod
    def show(cls, id):
        """Получить аренду по ID"""
        return Rental.get_or_none(Rental.id == id)

    @classmethod
    def update(cls, id, **kwargs):
        """Обновить аренду по ID"""
        Rental.update(**kwargs).where(Rental.id == id).execute()

    @classmethod
    def delete(cls, id):
        Rental.delete().where(Rental.id == id).execute()

if __name__ == "__main__":
    RentalController.add(
        carId=1,
        customerName='Customer2'
    )
    print(RentalController.end(4))
    print(RentalController.get())
