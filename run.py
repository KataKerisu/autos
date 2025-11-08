from flask import Flask,jsonify,request
import locale

from app.Routes.CarRoute import car_bp
from app.Routes.RentalRoute import rental_bp

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
application = Flask(__name__)

application.register_blueprint(car_bp)
application.register_blueprint(rental_bp)


if __name__ == "__main__":
    application.run(debug=True,port=5111)