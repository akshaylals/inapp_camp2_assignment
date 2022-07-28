import pyodbc
import functools
from myutils import Utils

# Commands to create db and table in railway.sql

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
            conn.commit()
            conn.close()
            return value
    return innerWrapper


@dbms
def getStops(curr: pyodbc.Cursor) -> dict:
    curr.execute('SELECT * FROM stops')
    stops = dict()
    for id, stop in curr:
        stops[id] = stop
    return stops

@dbms
def getTrains(curr: pyodbc.Cursor) -> dict:
    curr.execute('SELECT id, code, dest, berth, waitlist FROM trains')
    trains = dict()
    for id, code, dest, berth, waitlist in curr:
        trains[id] = {'code': code, 'dest': dest, 'berth': berth, 'waitlist': waitlist}
    return trains

@dbms
def getTrainSeats(curr: pyodbc.Cursor) -> dict:
    curr.execute('EXEC getTrainsSeats;')
    seats = dict()
    for code, max_berth, booked_berth, available_berth in curr:
        seats[code] = {
            'max_berth': max_berth,
            'booked_berth': booked_berth if booked_berth is not None else 0,
            'available_berth': available_berth if available_berth is not None else max_berth
        }
    return seats

@dbms
def getTrainWaitlist(curr: pyodbc.Cursor) -> dict:
    curr.execute('EXEC getTrainsWaitlist;')
    waitlist = dict()
    for code, dest, max_waitlist, booked_waitlist, available_waitlist in curr:
        waitlist[code] = {
            'dest': dest,
            'max_waitlist': max_waitlist,
            'booked_waitlist': booked_waitlist if booked_waitlist is not None else 0,
            'available_waitlist': available_waitlist if available_waitlist is not None else max_waitlist
        }
    return waitlist

@dbms
def getPassengers(curr: pyodbc.Cursor) -> dict:
    curr.execute('SELECT * FROM passengers')
    passengers = dict()
    for id, name, age, dest, train, waitlist in curr:
        passengers[id] = {'name': name, 'age': age, 'dest': dest, 'train': train, 'waitlist': waitlist}
    return passengers

 
@dbms
def addPassenger(curr: pyodbc.Cursor):
    dests = getStops()
    name = input('Name: ')
    age = Utils.getInt('Age: ')
    while(True):
        print('Destinations:')
        for key, val in dests.items():
            print(f'{key}. {val}')
        dest = Utils.getInt('> ')
        if dest in dests.keys():
            break
        print('Invalid input')
    trains = getTrains()
    seats = getTrainSeats()
    booked = False
    for id, train in trains.items():
        if train['dest'] >= dest:
            if seats[train['code']]['available_berth'] > 0:
                curr.execute(
                    'INSERT INTO passengers VALUES (?, ?, ?, ?, ?)',
                    (name, age, dest, id, 0)
                )
                print('Berth booked')
                print('Train:', train['code'])
                booked = True
                break
    wlBooked = False
    if not booked:
        waitlist = getTrainWaitlist()
        for code, wt in waitlist.items():
            if wt['dest'] >= dest:
                if wt['available_waitlist'] > 0:
                    for id, train in trains.items():
                        if train['code'] == code:
                            curr.execute(
                                'INSERT INTO passengers VALUES (?, ?, ?, ?, ?)',
                                (name, age, dest, id, 1)
                            )
                            print('Booked into waitlist')
                            print('Train:', train['code'])
                            break
                    wlBooked = True
                if wlBooked:
                    break
    if not (booked or wlBooked):
        print('No berth and waitlist full')

while (True):
    opt = Utils.getInt('''
    1. Book Passenger
    2. List Passenger
    3. List Trains
    0. Exit
    > ''')
    match opt:
        case 0: break
        case 1: addPassenger()
        case 2:
            dests = getStops()
            trains = getTrains()
            print('Passengers:')
            for id, p in getPassengers().items():
                print('Id:', id)
                print('Name:', p['name'])
                print('Age:', p['age'])
                print('Dest:', dests[p['dest']])
                print('Train:', trains[p['train']]['code'])
                print('Status:', 'Waitlist' if p['waitlist'] else 'Booked')
                print()
        case 3: 
            trains = getTrains()
            for train in trains.values():
                print('Train:', train['code'])