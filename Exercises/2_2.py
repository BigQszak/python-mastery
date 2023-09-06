""" 
import csv

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio 
"""

import csv
import readrides
from collections import defaultdict, Counter

rows = readrides.read_rides_as_objects('../Data/ctabus.csv')

# 1) How many bus routes exist
unique_routes = {r.route for r in rows}
print(len(unique_routes))

# 2) How many people rode the number 22 bus on February 2, 2011?  What about any route on any date of your choosing?
people = [r.rides for r in rows if r.route == '22' and r.date == '02/02/2011']
print(people)


# 3) What is the total number of rides taken on each bus route

rides_per_route = { r.route: 0 for r in rows}
for r in rows:
    rides_per_route[r.route] += r.rides
print(rides_per_route['22'])
print()
""" 
rides_per_route = Counter()
for r in rows:
    rides_per_route[r.route] += r.rides

print(rides_per_route['22'])

for route, count in rides_per_route.most_common():
    print('%5s %10d' % (route, count))
"""

# 4) What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011

rides_by_year = defaultdict(Counter)
for r in rows:
    year = r.date.split('/')[2]
    rides_by_year[year][r.route] += r.rides

diffs = rides_by_year['2011'] - rides_by_year['2001']
for route, diff in diffs.most_common(5):
    print(route, diff)