# Holidays and Business Days

A quick and dirty API for holidays and business days.

Routes:
* GET /holidays/<year>
Takes a four digit year as a parameter and returns a list of all 11 holidays honored by the NYSE and the Federal Reserve

* GET /next-business-day/<date>
Takes a date in the YYYY-DD-MM format and returns either the same date or, if it is a holiday or weekend, the next business day.
