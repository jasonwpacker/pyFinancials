from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/contribution/401k/<year>', methods=['GET'])
def get_401k_max(year):
    return maxima.get("401k").get(year, '0')

@app.route('/contribution/SIMPLE/<year>', methods=['GET'])
def get_SIMPLE_max(year):
    return maxima.get("SIMPLE").get(year, '0')

@app.route('/contribution/401kCatchUp/<year>', methods=['GET'])
def get_401kCatchUp_max(year):
    return maxima.get("401kCatchUp").get(year, '0')

@app.route('/contribution/SIMPLECatchUp/<year>', methods=['GET'])
def get_SIMPLECatchUp_max(year):
    return maxima.get("SIMPLECatchUP").get(year, '0')

if __name__ == '__main__':
    with open('limits.json') as limitsfile:
        try:
            maxima = json.load(limitsfile)
            app.run(debug=True)
        except FileNotFoundError:
            print("No Maxima File was found.")
        except PermissionError:
            print("No rights to read the limits file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
