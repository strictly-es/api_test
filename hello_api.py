from flask import Flask, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    name = request.args.get('name')
    if name:
        return f"{name} Hello, Codex!"
    else:
        return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
