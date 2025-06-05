from flask import Flask, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_codex():
    name = request.args.get('name', '')
    return f"{name}Hello, Codex!"

if __name__ == '__main__':
    app.run(debug=True)
