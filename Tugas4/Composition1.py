# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C 

class House:
    def __init__(self, area):
        self.area = area

class Apartment:
    def __init__(self, area):
        self.area = area

class Building:
    def __init__(self, house, apartment):
        self.house = house
        self.apartment = apartment
house = House("72 square meters")
apartment = Apartment("30 square meters")
building = Building(house, apartment)
print(building.house.area) # output: 8
print(building.apartment.area) # output: 500
