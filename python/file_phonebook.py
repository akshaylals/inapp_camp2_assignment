# File Handling: Modify Contacts Assignment
#  
# * Create a simple phone book app using files in python. 
# * On start of program, create a folder called 'contacts'
#   if not already there.
# * Create a file contacts if not there and append each contact as
#   new line (using strip() method get rid of any new line char)
# * The app should have the following functions: 
#  
# 1. List all contacts (stored in alphabetical order)
# 2. Add a new contact
# 3. Delete a contact
# 4. Search by name
# 5. Search by number

import os
import re

contacts = dict()

def init():
    if not os.path.exists('contacts'):
        os.mkdir('contacts')

    os.chdir('contacts')

    if not os.path.exists('contacts.txt'):
        f = open('contacts.txt', 'x')
        f.close()
    
def load():
    with open('contacts.txt', 'r') as f:
        for i in f.readlines():
            name, number = i.strip().split(',')
            contacts[name] = number

def save():
    with open('contacts.txt', 'w') as f:
        f.writelines([f'{name},{number}\n' for name, number in contacts.items()])

def searchNo():
    while(True):
        n = input('Enter number to search: ').strip()
        if re.match(r'\+[0-9]*', n):
            break
        else:
            print('Invalid input')
    for name, number in contacts.items():
        if number == n:
            print(f'Name: {name}')
            print(f'Number: {number}')
            return
    print(f'{n} does not exist')


def searchName():
    n = input('Enter name to search: ')
    for name, number in contacts.items():
        if name.lower() == n.lower():
            print(f'Name: {name}')
            print(f'Number: {number}')
            return
    print(f'{n} does not exist')
            
    

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
    contacts[name] = number
    print('Contact added')
    save()
    pass

def delete():
    name = input('Enter name to delete: ')
    if contacts.get(name):
        del contacts[name]
        print('Deleted')
    else:
        print(f'{name} does not exist')
    save()

def sort():
    if len(contacts) > 0:
        print('Contacts:')
        names = list(contacts.keys())
        names.sort()
        for name in names:
            print(f'Name: {name}')
            print(f'Number: {contacts[name]}\n')
    else:
        print('No contacts')

init()
load()

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