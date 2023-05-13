# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("The Tuple is:", myTuple)
index = 10
print("Index is:",index)
try:
    element = myTuple[index]
    print("Element at index {} is {}".format(index, element))
except IndexError:
    print("Index should be smaller.")









# Example of IndexError
# myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print("The Tuple is:", myTuple)
# index = 10
# element = myTuple[index]
# print("Element at index {} is {}".format(index,element))
