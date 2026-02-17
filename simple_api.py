from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/info', methods=['GET'])
def info():
    return jsonify({ 'jaime trop les filles': 'je suis un homme'    })

if __name__ == "__main__":
    app.run(debug=True)
