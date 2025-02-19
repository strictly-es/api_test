from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello, World!", 200

if __name__ == '__main__':
    app.run(debug=True)