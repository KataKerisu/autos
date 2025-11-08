from app.Models.Car import Car

class CarController:
    @classmethod
    def get(cls):
        """Получить список авто"""
        query = Car.select()
        return query

    @classmethod
    def add(cls, model, licensePlate):
        Car.create(
            model = model,
            licensePlate = licensePlate
        )

    @classmethod
    def show(cls, id):
        """Получить авто по ID"""
        return Car.get_or_none(Car.id == id)

    @classmethod
    def get_available_cars(cls):
        """Получить список всех доступных машин (isAvailable = 1)"""
        return list(Car.select().where(Car.isAvailable == True))

    @classmethod
    def update(cls, id, **kwargs):
        """Обновить авто по ID"""
        Car.update(**kwargs).where(Car.id == id).execute()

    @classmethod
    def delete(cls, id):
        Car.delete().where(Car.id == id).execute()

if __name__ == "__main__":
    # print(CarController.add(
    #     model = 'Toyota',
    #     licensePlate= 'BB222B'
    # ))
    print(CarController.delete(1))
    # print(CarController.get_available_cars())