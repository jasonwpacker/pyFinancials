# Holidays and Business Days

A quick and dirty API for holidays and business days.

Routes:
* GET /holidays/<year>
Takes a four digit year as a parameter and returns a list of all 11 holidays honored by the NYSE and the Federal Reserve

* GET /next-business-day/<date>
Takes a date in the YYYY-DD-MM format and returns either the same date or, if it is a holiday or weekend, the next business day.


# Retirement Account Contribution Maxima

A quick and dirty API for the maximum contributions for 401k and SIMPLE 401k's, including options for catch up amounts

Routes:
* GET /contribution/401k/<year>
Takes in a year >= 2019 and returns the maximum normal contribution for the year for 401k

* GET /contribution/SIMPLE/<year>
Takes in a year >= 2019 and returns the maximum normal contribution for the year for SIMPLE 401k

* GET /contribution/401kCatchUp/<year>
Takes in a year >= 2019 and returns the catch-up contribution maximum for the year for 401k

* GET /contribution/SIMPLECatchUp/<year>
Takes in a year >= 2019 and returns the catch-up contribution maximum for the year for SIMPLE 401k

# Requirements

Install the 'dateutil' package 
**pip install python-dateutil**
