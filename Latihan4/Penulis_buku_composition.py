# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

class Penulis:
    def __init__(self, nama):
        self.nama = nama
class Buku:
    def __init__(self, judul):
        self.judul = judul
class Perpustakaan:
    def __init__(self, penulis, buku):
        self.penulis = penulis
        self.buku = buku
penulis1 = Penulis("Arya Subhandhi")
penulis2 = Penulis("Morgan Housel")
penulis3 = Penulis("Robert Cialdini")
buku = Buku("The Psychology of Money")
perpustakaan = Perpustakaan([penulis1, penulis2, penulis3], buku)
print(perpustakaan.penulis[1].nama) 
