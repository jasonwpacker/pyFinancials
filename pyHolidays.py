from flask import Flask, jsonify
from json import loads
from datetime import datetime as dt, timedelta as td
from dateutil import easter

app = Flask(__name__)

def calculate_new_years_observed(year):
    nyd = dt.strptime(f'{year}-01-01','%Y-%m-%d')
    if nyd.weekday()==5:
        nyd -= td(days=1)
    if nyd.weekday()==6:
        nyd += td(days=1)
    return dt.strftime(nyd, '%Y-%m-%d')

def calculate_mlk_day(year):
    mlk = dt.strptime(f'{year}-01-01', '%Y-%m-%d')
    while mlk.weekday() != 0:
        mlk += td(days=1)
    mlk += td(days=14)
    return dt.strftime(mlk, '%Y-%m-%d')

def calculate_washington_bday(year):
    wbd = dt.strptime(f'{year}-02-01', '%Y-%m-%d')
    while wbd.weekday() != 0:
        wbd += td(days=1)
    wbd += td(days=14)
    return dt.strftime(wbd, '%Y-%m-%d')

def calculate_good_friday(year):
    gfd = easter.easter(int(year), method=3) - td(days=2)
    return dt.strftime(gfd, '%Y-%m-%d')

def calculate_memorial_day(year):
    mem = dt.strptime(f'{year}-05-31', '%Y-%m-%d')
    while mem.weekday() != 0:
        mem -= td(days=1)
    return dt.strftime(mem, '%Y-%m-%d')

def calculate_juneteenth_observed(year):
    jth = dt.strptime(f'{year}-06-19','%Y-%m-%d')
    if jth.weekday()==5:
        jth -= td(days=1)
    if jth.weekday()==6:
        jth += td(days=1)
    return dt.strftime(jth, '%Y-%m-%d')

def calculate_independence_day_observed(year):
    iday = dt.strptime(f'{year}-07-04','%Y-%m-%d')
    if iday.weekday()==5:
        iday -= td(days=1)
    if iday.weekday()==6:
        iday += td(days=1)
    return dt.strftime(iday, '%Y-%m-%d')

def calculate_labor_day(year):
    lab = dt.strptime(f'{year}-09-01', '%Y-%m-%d')
    while lab.weekday() != 0:
        lab += td(days=1)
    return dt.strftime(lab, '%Y-%m-%d')

def calculate_thanksgiving(year):
    thk = dt.strptime(f'{year}-11-01', '%Y-%m-%d')
    while thk.weekday() != 3:
        thk += td(days=1)
    thk += td(days=21)
    return dt.strftime(thk, '%Y-%m-%d')

def calculate_christmas(year):
    chr = dt.strptime(f'{year}-12-25','%Y-%m-%d')
    if chr.weekday()==5:
        chr -= td(days=1)
    if chr.weekday()==6:
        chr += td(days=1)
    return dt.strftime(chr, '%Y-%m-%d')

def calculate_veterans_day_observed(year):
    vet = dt.strptime(f'{year}-11-11','%Y-%m-%d')
    if vet.weekday()==5:
        vet -= td(days=1)
    if vet.weekday()==6:
        vet += td(days=1)
    return dt.strftime(vet, '%Y-%m-%d')

def calculate_columbus_day(year):
    col = dt.strptime(f'{year}-10-01', '%Y-%m-%d')
    while col.weekday() != 0:
        col += td(days=1)
    col += td(days=7)
    return dt.strftime(col, '%Y-%m-%d')

def holidays_by_year(year):
    holidays = [calculate_new_years_observed(year)]
    holidays.append(calculate_mlk_day(year))
    holidays.append(calculate_washington_bday(year))
    holidays.append(calculate_good_friday(year))
    holidays.append(calculate_memorial_day(year))
    holidays.append(calculate_juneteenth_observed(year))
    holidays.append(calculate_independence_day_observed(year))
    holidays.append(calculate_labor_day(year))
    holidays.append(calculate_columbus_day(year))
    holidays.append(calculate_veterans_day_observed(year))
    holidays.append(calculate_thanksgiving(year))
    holidays.append(calculate_christmas(year))
    return holidays

# Build the list from holidays.txt programmatically and return it in JSON format
@app.route('/holidays/<year>', methods=['GET'])
def get_holidays_by_year(year):
    if year.isnumeric() and (1000 <= int(year) <= 9999):
        return jsonify(holidays_by_year(year))
    return "Invalid Year Parameter (1000-9999)", 400

# If the date submitted is a holiday or weekend, increment the date until it is not
@app.route('/next-business-day/<date>', methods=['GET'])
def get_next_business_day(date):
    try:
        dt.strptime(date, '%Y-%m-%d')
    except:
        return "Invalid Date Format: YYYY-MM-DD", 400
    holidays = holidays_by_year(date[0:4])
    date = dt.strptime(date,'%Y-%m-%d')
    while date in [dt.strptime(hday, '%Y-%m-%d') for hday in holidays] or date.weekday() >= 5:
        date += td(days=1)
    return jsonify({'next_business_day': date.strftime('%Y-%m-%d')})

if __name__ == '__main__':
    app.run(debug=True)
