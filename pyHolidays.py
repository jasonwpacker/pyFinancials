from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Reformat the data from 'holidays.txt' into JSON
@app.route('/holidays', methods=['GET'])
def get_holidays():
    return jsonify(holidays)

# If the date submitted is a holiday or weekend, increment the date until it is not
@app.route('/next-business-day/<date>', methods=['GET'])
def get_next_business_day(date):
    date = datetime.strptime(date,'%Y-%m-%d')
    while date in holidays or date.weekday() >= 5:
        date += timedelta(days=1)
    return jsonify({'next_business_day': date.strftime('%Y-%m-%d')})

if __name__ == '__main__':
    with open('holidays.txt', 'r') as f:
        holidays = [datetime.strptime(line.strip(), '%Y-%m-%d') for line in f.readlines()]
    app.run(debug=True)
