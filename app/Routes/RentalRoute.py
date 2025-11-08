import peewee
from flask import Blueprint, Flask, jsonify, request

from app.Controllers.RentalController import RentalController

rental_bp = Blueprint('rentals', __name__, url_prefix='/api/rentals')

@rental_bp.route('/', methods=['GET'])
def get():
    rentals = RentalController.get()
    list = []
    for rental in rentals:
        list.append(
            {
            'id': rental.id,
            'carId': rental.carId.id,
            'customerName': rental.customerName,
            'startDate': rental.startDate,
            'endDate': rental.endDate
        }
    )
    return jsonify(
        {
            'rentals': list
        }
    ), 200

@rental_bp.route('/', methods=['POST'])
def start_rental():
    data = request.get_json()
    carId = data['carId']
    customerName = data['customerName']
    RentalController.add(
        carId=carId,
        customerName=customerName
    )
    return jsonify({
        'message': 'Аренда открыта'
    }), 201


@rental_bp.route('/<int:id>/return', methods=['PATCH'])
def end(id):
    # Завершаем аренду
    RentalController.end(id)
    return jsonify({
        "success": True,
        "message": "Аренда завершена, автомобиль снова доступен"
    }), 200