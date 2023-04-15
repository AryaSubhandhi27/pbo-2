# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

class Capital_City:
    def __init__(self, name):
        self.name = name
class Language:
    def __init__(self, language):
        self.language = language
class Country:
    def __init__(self, capital_city, language):
        self.capital_city = capital_city
        self.language = language
capital_city1 = Capital_City("London")
capital_city2 = Capital_City("Toronto")
capital_city3 = Capital_City("Canberra")
capital_city4 = Capital_City("Washington, D.C.")
language = Language("English")
country = Country([capital_city1, capital_city2, capital_city3, capital_city4], language)
print(country.capital_city[0].name) 
