# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C 

import threading
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print("Thread {} is running".format(self.name))
t1 = MyThread("1")
t2 = MyThread("2")
t1.start()
t2.start()
