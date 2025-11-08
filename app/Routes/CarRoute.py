import peewee
from flask import Blueprint, Flask, jsonify, request

from app.Controllers.CarController import CarController
from app.Controllers.RentalController import RentalController

car_bp = Blueprint('cars', __name__, url_prefix='/api/cars')

@car_bp.route('/', methods=['GET'])
def get():
    cars = CarController.get()
    list = []
    for car in cars:
        list.append(
            {
            'id': car.id,
            'model': car.model,
            'licensePlate': car.licensePlate,
            'isAvailable': car.isAvailable
        }
    )
    return jsonify(
        {
            'cars': list
        }
    ), 200

@car_bp.route('/available', methods=['GET'])
def get_available():
    cars = CarController.get_available_cars()
    list = []
    for car in cars:
        list.append(
            {
            'id': car.id,
            'model': car.model,
            'licensePlate': car.licensePlate,
            'isAvailable': car.isAvailable
        }
    )
    return jsonify(
        {
            'cars': list
        }
    ), 200

@car_bp.route('/', methods=['POST'])
def add_car():
    data = request.get_json()
    model = data['model']
    license_plate = data['licensePlate']
    CarController.add(
        model=model,
        licensePlate=license_plate
    )
    return jsonify({
        'message': 'Авто создано'
    }), 201

@car_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    CarController.delete(id)
    return jsonify(
        {
            "success": True,
            "message": f"Машина удалена"
        }
    ), 200


@car_bp.route('/<int:id>/rentals', methods=['GET'])
def get_car_rentals(id):
    # Получаем все аренды через RentalController
    car_rentals = RentalController.get()
    rentals_list = []
    for rental in car_rentals:
        rentals_list.append({
            'id': rental.id,
            'customerName': rental.customerName,
            'startDate': rental.startDate.isoformat(),
            'endDate': rental.endDate.isoformat() if rental.endDate else None,
        })

    return jsonify({
        "success": True,
        "carId": id,
        "rentals": rentals_list,
        "total": len(rentals_list)
    }), 200