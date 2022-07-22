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

class CMS:
    patients = dict()
    slno = 0

    def __printPatientDetails(self):
        print(f'Name: {self.name}')
        print(f'Gender: {self.gender}')
        print(f'Age: {self.age}')
        print(f'DOB: {self.dob}')
        print(f'Blood: {self.blood}')
    
    def __init__(self, name, gender, age, dob, blood):
        self.name   = name
        self.gender = gender
        self.age    = age
        self.dob    = dob
        self.blood  = blood

    def admit(name, gender, age, dob, blood):
        patient = CMS(name, gender, age, dob, blood)
        CMS.slno += 1
        CMS.patients[CMS.slno] = patient
        return CMS.slno
    
    def listPatients():
        print('\nPatient details: ')
        for id, patient in CMS.patients.items():
            print(f'\nID: {id}')
            patient.__printPatientDetails()
    
    def search(id):
        if CMS.patients.get(id):
            print('Patient details: ')
            print(f'ID: {id}')
            CMS.patients[id].__printPatientDetails()
        else:
            print(f'{id} does not exist')

    def delete(id):
        if CMS.patients.get(id):
            del CMS.patients[id]
        else:
            print(f'{id} does not exist')

    def update(id, name, gender, age, dob, blood):
        if CMS.patients.get(id):
            CMS.patients[id].name   = name
            CMS.patients[id].gender = gender
            CMS.patients[id].age    = age
            CMS.patients[id].dob    = dob
            CMS.patients[id].blood  = blood
        else:
            print(f'{id} does not exist')


class OP(CMS):
    pass


class NonOP(CMS):
    opTicketNo = 0




id = CMS.admit('superman', 'M', 12, '01/02/2010', 'O+')
print(id)

id = CMS.admit('spiderman', 'M', 12, '01/02/2010', 'A+')
print(id)

CMS.listPatients()

CMS.update(2, 'spiderman', 'M', 12, '10/02/2010', 'B+')

CMS.listPatients()
