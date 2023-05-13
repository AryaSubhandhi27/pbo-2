# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

class Python():
    def __init__(self):
            self.a = "Python"

obj = Python()
try:
    print(obj.a)
    print(obj.b)
except AttributeError:
    print("There is no such attribute")
