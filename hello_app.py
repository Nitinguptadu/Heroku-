from flask import request
from flask import jsonify
from flask import Flask
from flask import Flask, url_for, send_from_directory, request
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS, cross_origin

import os


app = Flask(__name__ ,template_folder='static')
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/hello', methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {
        'greeting': 'Hello   , ' + name + '  this deployment server is for personal learning purpose !'
    }
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', 'https://isha0621.herokuapp.com/')
    return response


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)
