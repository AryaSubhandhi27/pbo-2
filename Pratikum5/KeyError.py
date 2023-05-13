# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')

try:
    print(f'{person} is {ages[person]} years old.')
except KeyError:
    print(f"{person}'s age is unknown.")
