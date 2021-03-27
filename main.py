from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'pies': 'chuj'})


if __name__ == '__main__':
    app.run(debug=True)
