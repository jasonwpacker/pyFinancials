from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/contribution/401k/<year>', methods=['GET'])
def get_401k_max(year):
    return maxima.get("401k").get(year)

@app.route('/contribution/SIMPLE/<year>', methods=['GET'])
def get_SIMPLE_max(year):
    return maxima.get("SIMPLE").get(year)

@app.route('/contribution/401kCatchUp/<year>', methods=['GET'])
def get_401kCatchUp_max(year):
    return maxima.get("401kCatchUp").get(year)

@app.route('/contribution/SIMPLECatchUp/<year>', methods=['GET'])
def get_SIMPLECatchUp_max(year):
    return maxima.get("SIMPLECatchUP").get(year)

if __name__ == '__main__':
    maxima = json.load(open('limits.json'))
    app.run(debug=True)