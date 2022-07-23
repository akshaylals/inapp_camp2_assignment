# 2. Student report card management system
# ---------------------------------------
# 
# This project requires managing student records. A student record contains a roll number,
# name and marks obtained in maths, physics, chemistry, english and prgraming. The system
# should be able to do the following
#   1. create a student record
#   2. delete a student record based on the roll number
#   3. modify the marks in a student record given in roll number
#   4. display all student records
#   5. display a students record based on the roll number


class Utils:
    @staticmethod
    def getInt(*msg):
        while(True):
            try:
                value = int(input(*msg))
                return value
            except:
                print('Invalid input')

    @staticmethod
    def getFloat(*msg):
        while(True):
            try:
                value = float(input(*msg))
                return value
            except:
                print('Invalid input')


class Student:
    def __init__(self, name, maths, physics, chemistry, english, programing) -> None:
        self.__name       = name
        self.__maths      = maths
        self.__physics    = physics
        self.__chemistry  = chemistry
        self.__english    = english
        self.__programing = programing
    
    @property
    def name(self):
        return self.__name
    
    @property
    def maths(self):
        return self.__maths
    
    @property
    def physics(self):
        return self.__physics
    
    @property
    def chemistry(self):
        return self.__chemistry
    
    @property
    def english(self):
        return self.__english
    
    @property
    def programing(self):
        return self.__programing
    
    @maths.setter
    def maths(self, newMark):
        self.__maths = newMark
    
    @maths.setter
    def physics(self, newMark):
        self.__physics = newMark
    
    @maths.setter
    def chemistry(self, newMark):
        self.__chemistry = newMark
    
    @maths.setter
    def english(self, newMark):
        self.__english = newMark
    
    @maths.setter
    def programming(self, newMark):
        self.__programming = newMark

    def display(self):
        print('Name :', self.__name)
        print('Marks:')
        print('Maths:', self.__maths)
        print('Physics:', self.__physics)
        print('Chemistry:', self.__chemistry)
        print('English:', self.__english)
        print('Programing:', self.__programing)


class SRCMS:
    students = dict()

    @staticmethod
    def create():
        rollno = Utils.getInt('Rollno: ')
        if SRCMS.students.get(rollno):
            print('Student already exist')
        else:
            name = input('Name: ')
            print('Enter marks')
            maths       = Utils.getFloat('Maths: ')
            physics     = Utils.getFloat('Physics: ')
            chemistry   = Utils.getFloat('Chemistry: ')
            english     = Utils.getFloat('English: ')
            programing  = Utils.getFloat('Programing: ')
            student  = Student(name, maths, physics, chemistry, english, programing)
            SRCMS.students[rollno] = student
            print('Student added successfully')
    
    @staticmethod
    def delete():
        rollno = Utils.getInt('Rollno: ')
        if SRCMS.students.get(rollno):
            del SRCMS.students[rollno]
            print('Student deleted successfully')
        else:
            print('Student does not exist')
    
    @staticmethod
    def modify():
        rollno = Utils.getInt('Rollno: ')
        if SRCMS.students.get(rollno):
            student = SRCMS.students.get(rollno)
            student.display()
            while(True):
                opt = Utils.getInt(f'''
Choose Mark to edit:
    1. Maths
    2. Physics
    3. Chemistry
    4. English
    5. Programing
    6. Exit

    > '''
                )
                match opt:
                    case 1: student.maths = Utils.getFloat('Maths: ')
                    case 2: student.physics = Utils.getFloat('Physics: ')
                    case 3: student.chemistry = Utils.getFloat('Chemistry: ')
                    case 4: student.english = Utils.getFloat('English: ')
                    case 5: student.programing = Utils.getFloat('Programing: ')
                    case 6: break
                    case _: print('Invalid input')
        else:
            print('Student does not exist')

    @staticmethod
    def listAllStudents():
        if len(SRCMS.students) > 0:
            print('Student details: ')
            for rollno, student in SRCMS.students.items():
                print('\nRollno: ', rollno)
                student.display()
        else:
            print('No records')

    @staticmethod
    def showStudent():
        rollno = Utils.getInt('Rollno: ')
        if SRCMS.students.get(rollno):
            print('\nRollno: ', rollno)
            SRCMS.students[rollno].display()
        else:
            print('Student does not exist')
    

while(True):
    opt = Utils.getInt('''
    1. Create Student Record
    2. Delete Student Record
    3. Modify Marks
    4. Display all Students
    5. Display a student record
    6. Exit
    
    > ''')

    match opt:
        case 1: SRCMS.create()
        case 2: SRCMS.delete()
        case 3: SRCMS.modify()
        case 4: SRCMS.listAllStudents()
        case 5: SRCMS.showStudent()
        case 6: break
        case _: print('Invalid input')