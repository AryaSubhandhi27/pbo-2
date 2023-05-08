# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

try:
    file = open("file.txt", "r")
    num = int(file.readline())
except ValueError:
    print("Error: Input tidak valid!")
finally:
    file.close()
