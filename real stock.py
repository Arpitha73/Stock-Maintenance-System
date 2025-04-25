from flask import Flask, jsonify, request
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to fetch data from backend

# Sample stock data with 15 companies
stocks = [
    {"name": "Ola Electric", "price": 50.63, "change": -0.84},
    {"name": "Reliance", "price": 2600, "change": -0.83},
    {"name": "SBI", "price": 600, "change": 0.68},
    {"name": "Tata Motors", "price": 375.50, "change": 0.56},
    {"name": "HDFC Bank", "price": 1500, "change": -0.21},
    {"name": "ICICI Bank", "price": 720, "change": 1.12},
    {"name": "Infosys", "price": 1800, "change": 0.05},
    {"name": "Wipro", "price": 450, "change": -0.45},
    {"name": "Maruti Suzuki", "price": 7300, "change": 1.5},
    {"name": "Hindustan Unilever", "price": 2400, "change": 0.89},
    {"name": "Bajaj Auto", "price": 3900, "change": -0.02},
    {"name": "Larsen & Toubro", "price": 1650, "change": 0.12},
    {"name": "Dr Reddy's Laboratories", "price": 4500, "change": 1.25},
    {"name": "Bharti Airtel", "price": 550, "change": -0.14},
    {"name": "Axis Bank", "price": 900, "change": 0.3}
]

# Sample indices data
indices = [
    {"name": "NIFTY 50", "change": -0.33},
    {"name": "SENSEX", "change": -0.27},
    {"name": "Nifty Bank", "change": 0.007},
    {"name": "Nifty IT", "change": -0.52}
]

@app.route('/update_stock', methods=['GET'])
def update_stock():
    # Simulate stock price & index updates
    for stock in stocks:
        stock["price"] += round(random.uniform(-5, 5), 2)  # Random price fluctuation
        stock["change"] = round(random.uniform(-1, 1), 2)  # Random percentage change

    for index in indices:
        index["change"] = round(random.uniform(-1, 1), 2)  # Random index fluctuation

    return jsonify({"stocks": stocks, "indices": indices})

@app.route('/add_stock', methods=['POST'])
def add_stock():
    data = request.get_json()
    if "name" in data and "price" in data and "change" in data:
        new_stock = {
            "name": data["name"],
            "price": float(data["price"]),
            "change": float(data["change"])
        }
        stocks.append(new_stock)
        return jsonify({"message": "Stock added successfully!"}), 200
    return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)