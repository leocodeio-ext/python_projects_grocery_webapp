from flask import Flask, request, jsonify, g
from flask_cors import CORS
from sql_connection import get_sql_connection, close_connection
import json

import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown_db(exception):
    close_connection()

@app.route('/getUOM', methods=['GET'])
def get_uom():
    connection = get_sql_connection()
    response = uom_dao.get_uoms(connection)
    return jsonify(response)

@app.route('/getProducts', methods=['GET'])
def get_products():
    connection = get_sql_connection()
    response = products_dao.get_all_products(connection)
    return jsonify(response)

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    connection = get_sql_connection()
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    return jsonify({
        'product_id': product_id
    })

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    connection = get_sql_connection()
    response = orders_dao.get_all_orders(connection)
    return jsonify(response)

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    connection = get_sql_connection()
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    return jsonify({
        'order_id': order_id
    })

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    connection = get_sql_connection()
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    return jsonify({
        'product_id': return_id
    })

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000, debug=True)

