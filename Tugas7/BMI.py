# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

class BMIMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

    def bmi(cls, weight, height):
        hitung_bmi = weight / (height ** 2)
        if hitung_bmi < 18.5:
            category = "Kurus"
        elif hitung_bmi < 24.9:
            category = "Normal"
        else:
            category = "Kelebihan berat badan (Obesitas)"
        return hitung_bmi, category
        cls.bmi = staticmethod(bmi)

class BMI(metaclass=BMIMeta):
    pass

hitung_bmi, category = BMI.bmi(55, 1.70)
print("BMI:", hitung_bmi)
print("Kategori:", category)
