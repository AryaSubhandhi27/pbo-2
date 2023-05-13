# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21V

try:
    with open("salma.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File Not Found!")
