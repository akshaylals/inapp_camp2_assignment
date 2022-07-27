import pyodbc
import functools

def dbms(func):
    @functools.wraps(func)
    def innerWrapper(*args):
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                'Server=DESKTOP-4GIE4U2\SQLEXPRESS01;'
                'Database=railway_db;'
                'Trusted_Connection=yes')
        except:
            print('Connection Error')
            return None
        else:
            curr = conn.cursor()
            value = func(curr, *args)
            conn.close()
            return value
    return innerWrapper


@dbms
def getStops(curr: pyodbc.Cursor):
    curr.execute('SELECT * FROM stops')
    stops = dict()
    for id, stop in curr:
        stops[id] = stop
    return stops

@dbms
def getTrains(curr: pyodbc.Cursor):
    curr.execute('SELECT * FROM trains')
    trains = dict()
    for id, code, dest, berth, waitlist in curr:
        trains[id] = {'code': code, 'dest': dest, 'berth': berth, 'waitlist': waitlist}
    return trains

@dbms
def getPassengers(curr: pyodbc.Cursor):
    curr.execute('SELECT * FROM passengers')
    passengers = dict()
    for id, name, age, dest, train in curr:
        passengers[id] = {'name': name, 'age': age, 'dest': dest, 'train': train}
    return passengers

@dbms
def updateTrain(curr: pyodbc.Cursor, train, **kwargs):
    if 'berth' in kwargs.keys():
        curr.execute('UPDATE trains SET berth=?;', (kwargs.get('berth')))
    if 'waitlist' in kwargs.keys():
        curr.execute('UPDATE trains SET waitlist=?;', (kwargs.get('waitlist')))
    

@dbms
def addPassenger(curr: pyodbc.Cursor):
    pass


print(getStops())
print(getTrains())
print(getPassengers())

# Stops: 
# {
#     0: 'TVM', 
#     1: 'ALP', 
#     2: 'ERN', 
#     3: 'KZK'
# }
# 
# Trains:
# {
#     1: {'code': 'TVM_ALP', 'dest': 1, 'berth': 5, 'waitlist': 0}, 
#     2: {'code': 'TVM_ERN', 'dest': 2, 'berth': 5, 'waitlist': 0}, 
#     3: {'code': 'TVM_KZK', 'dest': 3, 'berth': 5, 'waitlist': 0}
# }