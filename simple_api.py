from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/fixed', methods=['GET'])
def fixed_value():
    return jsonify({"message": "This is a fixed response!!"})

if __name__ == '__main__':
    app.run(debug=True)