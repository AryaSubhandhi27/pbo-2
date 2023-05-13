# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C


# importing os module
import os
	
# create a pipe using os.pipe() method
# it will return a pair of
# file descriptors (r, w) usable for
# reading and writing, respectively.
r, w = os.pipe()

# (using exception handling technique)
# try to get the terminal device associated
# with the file descriptor r or w
try :
	print(os.ttyname(r))
	
except OSError as error :
	print(error)
	print("File descriptor is not associated with any terminal device")
