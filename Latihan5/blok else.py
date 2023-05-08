# Nama    : Arya Subhandhi
# NIM     : 210511107
# Kelas   : R3/TI21C

try:
    # Buka file dan baca isinya
    with open('file.txt', 'r') as file:
        data = file.read()
    # Ubah teks menjadi bilangan bulat
    num = int(data)
except FileNotFoundError:
    print("File tidak ditemukan!")
except ValueError:
    print("Isi file harus berupa bilangan bulat!")
else:
    # Jika tidak terjadi kesalahan, tampilkan hasil konversi
    print("Isi file berhasil dikonversi menjadi bilangan bulat:", num)
