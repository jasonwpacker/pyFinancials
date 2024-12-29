from flask import Flask, jsonify
import json

app = Flask(__name__)

def contribution_max(type, year):
    with open('limits.json') as limitsfile:
        try:
            maxima = json.load(limitsfile)
            return maxima.get(type).get(year, 0)
        except FileNotFoundError:
            print("No Maxima File was found.")
        except PermissionError:
            print("No rights to read the limits file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


@app.route('/contribution/401k/<year>', methods=['GET'])
def get_401k_max(year):
    return contribution_max("401k", year)

@app.route('/contribution/SIMPLE/<year>', methods=['GET'])
def get_SIMPLE_max(year):
    return contribution_max("SIMPLE", year)

@app.route('/contribution/401kCatchUp/<year>', methods=['GET'])
def get_401kCatchUp_max(year):
    return contribution_max("401kCatchUp", year)

@app.route('/contribution/SIMPLECatchUp/<year>', methods=['GET'])
def get_SIMPLECatchUp_max(year):
    return contribution_max("SIMPLECatchUp", year)

if __name__ == '__main__':
    app.run(debug=True)

