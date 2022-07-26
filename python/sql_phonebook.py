# SQL: Modify Contacts Assignment
#  
# * Create a simple phone book app using SQL in python. 
# * The app should have the following functions: 
#  
# 1. List all contacts (stored in alphabetical order)
# 2. Add a new contact
# 3. Delete a contact
# 4. Search by name
# 5. Search by number

import re
import pyodbc


conn = pyodbc.connect('Driver={SQL Server};'
            'Server=DESKTOP-4GIE4U2\SQLEXPRESS01;'
            'Database=contacts_db;'
            'Trusted_Connection=yes')

myCursor = conn.cursor()

try:
    myCursor.execute('''CREATE TABLE Contacts(
        Id INT IDENTITY NOT NULL PRIMARY KEY,
        Name VARCHAR(20) NOT NULL UNIQUE,
        Phone VARCHAR(20) NOT NULL
    );
    ''')
    conn.commit()
except:
    try:
        myCursor.execute('SELECT * FROM Contacts;')
    except:
        print('Failed to create table')
        exit()


def searchNo():
    n = input('Enter number to search: ')
    try:
        myCursor.execute(
            'SELECT name, phone FROM Contacts WHERE Phone=?',
            (n)
        )
    except:
        print('Failed to fetch contacts')
    else:
        contacts = myCursor.fetchall()
        if len(contacts) > 0:
            print('Contacts:')
            for name, phone in contacts:
                print(f'Name: {name}')
                print(f'Phone: {phone}\n')
        else:
            print('Number not found')


def searchName():
    n = input('Enter name to search: ')
    try:
        myCursor.execute(
            'SELECT name, phone FROM Contacts WHERE Name LIKE ?',
            (f'%{n}%')
        )
    except:
        print('Failed to fetch contacts')
    else:
        contacts = myCursor.fetchall()
        if len(contacts) > 0:
            print('Contacts:')
            for name, phone in contacts:
                print(f'Name: {name}')
                print(f'Phone: {phone}\n')
        print(f'{len(contacts)} contacts matches {n}')

def add():
    while(True):
        name = input('Enter name: ').strip()
        if ',' in name:
            print(', not allowed in name')
        else:
            break
    while(True):
        number = input('Enter number: ').strip()
        if re.match(r'\+[0-9]*', number):
            break
        else:
            print('Invalid input')
    try:
        myCursor.execute(
            'INSERT INTO Contacts VALUES (?, ?);',
            (name, number)
        )
        conn.commit()
    except:
        print('Failed to add contact')
    else:
        print('Contact added')

def delete():
    name = input('Enter name to delete: ')
    try:
        myCursor.execute(
            'DELETE FROM Contacts WHERE Name=?',
            (name)
        )
        conn.commit()
    except:
        print('Failed to delete')
    else:
        if myCursor.rowcount > 0:
            print('Deleted')
        else:
            print(f'{name} does not exist')

def sort():
    try:
        myCursor.execute('SELECT Name, Phone FROM Contacts ORDER BY Name;')
    except:
        print('Failed to fetch contacts')
    else:
        contacts = myCursor.fetchall()
        if len(contacts) > 0:
            print('Contacts:')
            for name, phone in contacts:
                print(f'Name: {name}')
                print(f'Phone: {phone}\n')
        print(f'{len(contacts)} contacts')


while(True):
    print('''
    1. List all contacts
    2. Add new contact
    3. Delete a contact
    4. Search by name
    5. Search by number
    6. Exit
    ''')
    opt = int(input('> '))
    match opt:
        case 1: sort()
        case 2: add()
        case 3: delete()
        case 4: searchName()
        case 5: searchNo()
        case 6: break
        case _: print('Invalid input')

conn.close()