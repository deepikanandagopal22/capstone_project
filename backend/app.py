from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "db",
    "user": "root",
    "password": "password",
    "database": "ecommerce",
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Backend API!"})

@app.route('/products', methods=['GET'])
def get_products():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify({"products": products})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

@app.route('/add-product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    if not name or not price:
        return jsonify({"error": "Invalid input"}), 400

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Product added successfully!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

