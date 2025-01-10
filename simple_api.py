from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/fixed', methods=['GET'])
def fixed_value():
    import random
    random_number = random.randint(1, 100)
    return jsonify({"random_number": random_number})

if __name__ == '__main__':
    app.run(debug=True)