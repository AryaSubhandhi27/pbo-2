# name    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

class Doctor:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        
class Hospital:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def daftar_doctor(self):
        for position in self.position:
            print(position.name, position.department)
doctor1 = Doctor("Arya Subhandhi", "Cardiologist")
doctor2 = Doctor("Caroline Smith", "Pediatric")
hospital = Hospital("ABC", [doctor1, doctor2])
hospital.daftar_doctor()
