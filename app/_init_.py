from flask import Flask
from resources.sale_receipt import routes
from resources.car import routes


app = Flask(__name__)

