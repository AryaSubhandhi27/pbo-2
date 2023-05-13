# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

try:  
    l=[]  
    for i in range(1000000):  
        l.append('a')  
except MemoryError:  
    print("Memory limit is exceeded by the code")  
