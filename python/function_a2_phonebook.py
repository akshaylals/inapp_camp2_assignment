# Assignment 2
#  
# Create a simple phone book app using dictionary in python.
# On starting the program give choice to the user
#  
# 1. List all contacts (stored in alphabetical order)
# 2. Add a new contact
# 3. Delete a contact
# 4. Search by name
# 5. Search by number
# 
# a. searchno() to Search for a particular number given the name
# b. searchname() Search for a particular number given the number
# c. add() Add and entry from the phone directory.
# d. delete() Delete an entry from the phone directory.
# e. sort() Print the directory in alphabetically sorted order

contacts = dict()

def searchNo():
    n = input('Enter number to search: ')
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
    name = input('Enter name: ')
    number = input('Enter number: ')
    contacts[name] = number
    print('Contact added')
    pass

def delete():
    name = input('Enter name to delete: ')
    if contacts.get(name):
        del contacts[name]
        print('Deleted')
    else:
        print(f'{name} does not exist')

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