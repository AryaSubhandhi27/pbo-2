# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

class Jurnal:
    def __init__(self, judul, tanggal):
        self.judul = judul
        self.tanggal = tanggal
class Peneliti:
    def __init__(self, nama, jurnal):
        self.nama = nama
        self.jurnal = jurnal
    def daftar_jurnal(self):
        for jurnal in self.jurnal:
            print(jurnal.judul, jurnal.tanggal)
jurnal1 = Jurnal("Robotics and Computer-Integrated Manufacturing,", "October 2023")
jurnal2 = Jurnal("Progress in Energy and Combustion Science,", "May 2023")
peneliti = Peneliti("ABC", [jurnal1, jurnal2])
peneliti.daftar_jurnal()
