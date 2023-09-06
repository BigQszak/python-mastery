import csv
import collections
from collections import namedtuple

class RideData(collections.abc.Sequence):
    def __init__(self) -> None:
        # Each variable is a list with all the values (column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # Assuming all lists have the same length
        return len(self.routes)

    def __getitem__(self, index):
        # Returns data in form of a dictionary containing one value from each columns
        return {
            'route': self.routes[index],
            'date': self.dates[index],
            'daytype': self.daytypes[index],
            'rides': self.numrides[index]
        }

    def append(self, d):
        # Adding new element by appending each list with its corresponding value
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

# best memory usage
class Row:
    __slots__ = ('route', 'date', 'daytype', 'rides')
    def __init__(self, route, date, daytype, rides) -> None:
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

Row = namedtuple('Row', ('route','date','daytype','rides'))

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dicts(filename):
    #records = [] # list of dictionaries

    records = RideData()

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])

            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records

def read_rides_as_objects(filename):
    records = [] # list of objects

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = Row(
                route = row[0],
                date = row[1],
                daytype = row[2],
                rides = int(row[3])
            )
            records.append(record)

    return records

def read_rides_as_instances(filename):
    '''
    Read the bus ride data as a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    #records = RideData()

    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    """ 
    records.routes = routes
    records.dates = dates
    records.daytypes = daytypes
    records.numrides = numrides
    return records
    """
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    #rows = read_rides_as_tuples('../Data/ctabus.csv')
    #rows = read_rides_as_dicts('../Data/ctabus.csv')
    #rows = read_rides_as_objects('../Data/ctabus.csv')
    rows = read_rides_as_columns('../Data/ctabus.csv')
    #print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())


#### Log #####
# Dict (custom data container -> RideData)
# Memory Use: Current 96169710, Peak 96204193

# Dicts (list of dicts)
# Memory Use: Current 216097790, Peak 216132209

# Tuples
# Memory Use: Current 123688974, Peak 123723393

# Named tuples
# Memory Use: Current 128309975, Peak 128344394

# Columns (similar to custom container - but hard to work with)
# Memory Use: Current 96169502, Peak 96203753

# Objects (class Row)
# Memory Use: Current 119069102, Peak 119103521



