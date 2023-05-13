# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

def values():     #list of integer values with no limits
    x = 1             #initializing the value of integer to 1   
    while True:
        yield x
        x+=  1

def findingcubes():    
    for x in values():      
        yield x * x *x     #finding the cubes of value ‘x’

def func(y, sequence):    
    
    sequence = iter(sequence) 
    output = [ ]    #creating an output blank array 
    try:
        for x in range(y):   #using the range function of python to use for loop
            output.append(next(sequence))   #appending the output in the array
    except StopIteration:    #catching the exception
        pass
    return output   

print(func(5, findingcubes()))  #passing the value in the method ‘func’
