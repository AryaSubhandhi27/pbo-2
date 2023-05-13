# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

print("Program that uses SystemExit as Exception instead of BaseException.")
try:
    raise SystemExit
    
except SystemExit:
    print("Specifying SystemError exception in this block works.")
