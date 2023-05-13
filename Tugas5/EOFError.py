# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

try:
    value1 = int(input("enter value 1 :"))
    value2 = int(input("enter value 2 :"))
    result = value1 + value2
    print(f"The sum of {value1} and {value2} is: {result}")
except EOFError as e:
    print("End-Of-File when reading input")
