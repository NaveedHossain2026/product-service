import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# FACTOR III: Config - Do not hardcode configurations. 
# Enable CORS for all origins to match the Rust warp::cors behavior.
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/products', methods=['GET'])
def get_products():
    # Maintain the same data structure as the original Rust service
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]
    return jsonify(products)

if __name__ == '__main__':
    # FACTOR VII: Port Binding - Export services via port binding.
    # Read the PORT from environment variables, defaulting to 5000 if not set.
    port = int(os.environ.get("PORT", 5000))
    # Listen on 0.0.0.0 to make the service accessible within the network
    app.run(host='0.0.0.0', port=port)