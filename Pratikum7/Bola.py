# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

class BolaMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luas_permukaan(cls, pi, r):
            return 4/3 * pi * r**3
        cls.luas_permukaan = classmethod(luas_permukaan)
        def volume(cls, pi, r):
            return 4 * pi * r**2 
        cls.volume = classmethod(volume)

class Bola(metaclass=BolaMeta):
    pass

A = Bola()
B = A.luas_permukaan(3.14, 7)
C = A.volume(3.14, 7)
print('Luas Permukaan Bola:',B)
print('Volume Bola:',C)
