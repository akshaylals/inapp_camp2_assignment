# Write a program to build a simple Clinic Management System using Python which
# can perform following operations inside the class CMS
# * Admit - This method takes patient details from the user like name,
#   gender, age, dob, blood group. A patient_id should be automatically generated
# * listPatients - This method displays the details of every patient.
# * search - searches for a particular patient using patient_id
# * Delete - deletes the record of a particular patient using patient_id
# * Update - will ask for the patient_id and other details. It will replace
#   the other details with new details.
# Create inherited classes 'OP' and 'NonOP'. 'OP' should have the additional
# Admit function and Non OP a function to generate an OP Ticket with 
# incrementing no for every patient


class Patient:
    def __init__(self, name, gender, age, dob, blood):
        self.name   = name
        self.gender = gender
        self.age    = age
        self.dob    = dob
        self.blood  = blood

    def printPatientDetails(self):
        print(f'Name: {self.name}')
        print(f'Gender: {self.gender}')
        print(f'Age: {self.age}')
        print(f'DOB: {self.dob}')
        print(f'Blood: {self.blood}')

    def update(self, name, gender, age, dob, blood):
        self.name   = name
        self.gender = gender
        self.age    = age
        self.dob    = dob
        self.blood  = blood
    

class CMS:
    patients = dict()
    slno = 0

    @staticmethod
    def register(name, gender, age, dob, blood):
        patient = Patient(name, gender, age, dob, blood)
        CMS.slno += 1
        CMS.patients[CMS.slno] = patient
        return CMS.slno
    
    @staticmethod
    def listPatients():
        print('\nPatient details: ')
        for id, patient in CMS.patients.items():
            print(f'\nID: {id}')
            patient.printPatientDetails()
    
    @staticmethod
    def search(id):
        if CMS.patients.get(id):
            print('Patient details: ')
            print(f'ID: {id}')
            CMS.patients[id].printPatientDetails()
        else:
            print(f'{id} does not exist')

    @staticmethod
    def delete(id):
        if CMS.patients.get(id):
            del CMS.patients[id]
        else:
            print(f'{id} does not exist')

    @staticmethod
    def update(id, name, gender, age, dob, blood):
        if CMS.patients.get(id):
            CMS.patients[id].update(name, gender, age, dob, blood)
        else:
            print(f'{id} does not exist')


class OP(Patient):
    def admit():
        # disease, no fo days
        pass


class NonOP(Patient):
    opTicketNo = 0




id = CMS.register('superman', 'M', 12, '01/02/2010', 'O+')
print(id)

id = CMS.register('spiderman', 'M', 12, '01/02/2010', 'A+')
print(id)

CMS.listPatients()

CMS.update(2, 'spiderman', 'M', 12, '10/02/2010', 'B+')

CMS.listPatients()
