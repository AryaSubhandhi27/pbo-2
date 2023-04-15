# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C 

class Mahasiswa:
    def __init__(self, jumlah_orang):
        self.jumlah_orang = jumlah_orang

class Kelompok_KKM:
    def __init__(self, jumlah_orang):
        self.jumlah_orang = jumlah_orang

class Orang:
    def __init__(self, mahasiswa, kelompok_kkm):
        self.mahasiswa = mahasiswa
        self.kelompok_kkm = kelompok_kkm
mahasiswa = Mahasiswa(329)
kelompok_kkm = Kelompok_KKM(36)
orang = Orang(mahasiswa, kelompok_kkm)
print(orang.mahasiswa.jumlah_orang) 
print(orang.kelompok_kkm.jumlah_orang) 
