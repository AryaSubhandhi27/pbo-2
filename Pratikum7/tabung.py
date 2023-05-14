# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

class TabungMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luas_permukaan(cls, pi, r, tinggi):
            return 2 * pi * r * (r + tinggi)
        cls.luas_permukaan = classmethod(luas_permukaan)
        def volume(cls, pi, r, tinggi):
            return pi * r * r * tinggi 
        cls.volume = classmethod(volume)

class Tabung(metaclass=TabungMeta):
    pass

A = Tabung()
B = A.luas_permukaan(3.14,4,5)
C = A.volume(3.14,4,5)
print('Luas Permukaan Tabung:',B)
print('Volume Tabung:',C)
