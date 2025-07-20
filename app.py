from flask import Flask, jsonify, request
from data import products

# products = [
#     {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
#     {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
#     {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
# ]

app = Flask(__name__)

#Homepage route returns a welcome message
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "welcome"}), 200
    

#GET /products route that returns all products or filter by category
@app.route("/products", methods = ["GET"])
def get_products():
    #Return all products filtered by caategory
    category = request.args.get("category")
    if category:
        filtered = [product for product in products if product['category'] == category]
        return jsonify(filtered), 200
    return jsonify (products), 200
    

# GET /products/<id> route that returns a specific product by ID or 404
@app.route("/products/<int:id>", methods = ["GET"])
def get_product_by_id(id):
    #Search for matching product
    for product in products:
        if product.get("id")== id:
            return jsonify(product), 200
    #Not found, JSON error + 404
    return jsonify({"error": "Product not found"}), 404
     

if __name__ == "__main__":
    app.run(debug=True)