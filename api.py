import flask
import config
from flask import request, jsonify, send_from_directory, current_app
from pymongo import MongoClient

app = flask.Flask(__name__)
app.config["DEBUG"] = True
client = MongoClient('localhost', 27017)

@app.route('/add', methods=['POST'])
def addNewBarcode():
    #if 'barcode' in request.args:
    #    barcd = str(request.args['barcode'])
    request_json = request.get_json()
    db = client.barcode
    print(request_json)
    return ""

@app.route('/', methods=['GET'])
def SearchBarcodes():
    return "WIP"

app.run()