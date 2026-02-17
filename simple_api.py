from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'app': 'Simple API',
        'version': '1.0',
        'author': 'Maxence'
    })

if __name__ == "__main__":
    app.run(debug=True)
