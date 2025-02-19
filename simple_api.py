from flask import Flask, jsonify, request
import hashlib

app = Flask(__name__)

@app.route('/api/fixed', methods=['GET'])
def fixed_value():
    import random
    random_number = random.randint(1, 100)
    return jsonify({"random_number": random_number})

@app.route('/api/hash', methods=['POST'])
def hash_string():
    data = request.get_json()
    if 'input_string' not in data:
        return jsonify({"error": "No input_string provided"}), 400
    
    input_string = data['input_string']
    hashed_value = hashlib.sha256(input_string.encode()).hexdigest()
    return jsonify({"hashed_value": hashed_value})

if __name__ == '__main__':
    app.run(debug=True)
