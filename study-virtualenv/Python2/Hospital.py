
class Patient(object):
    patient_id = 0
    def __init__(self,p_name,allergies):
        Patient.patient_id += 1
        self.id = Patient.patient_id
        self.p_name = p_name
        self.allergies = allergies
        self.bed_num = None

        # question here about the patient


class Hospital(object):
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.patients = []
        self.beds = self.initialize_beds()
        # question about this funciton. how to relate the below def and the order

    def initialize_beds(self):
        beds = []
        for i in range (1, self.cap + 1):
            beds.append({
                'bed_id' : i,
                'available': True
            })
        return beds

    def admit(self, new_patient):
        if len(self.patients) < self.cap:
            self.patients.append(new_patient)
            for i in range(0,len(self.beds)):
                if self.beds[i]['available']:
                    new_patient.bed_num = self.beds[i]['bed_id']
                    self.beds[i]['available'] = False
                    break
            print 'Patient # {} admitted to be #{}'.format(new_patient.id, new_patient.bed_num)

        else:
            print 'Hosptial is full'
            # question about patient.xxx
        return self

    def discharge(self,patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                self.patients.remove(patient)
                for bed in self.beds:
                    if bed['bed_id'] == patient.bed_num:
                        bed['available'] = True
                        break


                print 'Patient #{} succefull discharged. Bed #{} now avialble'.format(patient.id, patient.bed_num)

        return self





patient1 = Patient('Qinqin','None')
patient2 = Patient('Huahua','Nut')
patient3 = Patient('Shanshan','Egg')

hospital = Hospital('huaxi',1)

hospital.admit(patient1).admit(patient2).admit(patient3)
