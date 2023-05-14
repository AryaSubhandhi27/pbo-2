# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

class KerucutMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luas_permukaan(cls, pi, r, s):
            return pi * r * (r + s)
        cls.luas_permukaan = classmethod(luas_permukaan)
        def volume(cls, pi, r, tinggi):
            return 1/3 * pi * r * r * tinggi 
        cls.volume = classmethod(volume)

class Kerucut(metaclass=KerucutMeta):
    pass

A = Kerucut()
B = A.luas_permukaan(3.14, 7, 12)
C = A.volume(3.14, 7, 10)
print('Luas Permukaan Kerucut:',B)
print('Volume Kerucut:',C)
