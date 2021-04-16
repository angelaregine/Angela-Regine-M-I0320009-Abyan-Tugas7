#Program Pengecekkan Buku Mata Pelajaran

opening = "Selamat Datang di Website Perpustakaan SMA Global Mandiri"
o = opening.center(90,'-')
print(o)
print()

sapa = "Silahkan mengecek ketersediaan buku yang Anda cari dengan memasukkan nama Anda"
print(sapa)
siswa = str(input("Masukkan nama Anda: "))
siswa2 = siswa.upper()
print("Halo,", siswa2, "silahkan cek ketersediaan buku mata pelajaran yang dapat dipinjam!")

mata_pelajaran = ("Matematika, Kewarganegaraan, Seni Budaya, Bahasa Indonesia, Bahasa Inggris, Sejarah, Agama")
print("Berikut daftar buku yang masih tersedia pada hari ini: ", mata_pelajaran)
cari = str(input("Masukkan buku yang Anda cari: "))
cari2 = cari.capitalize()
hasil = mata_pelajaran.count(cari2)
if hasil == 1:
    print("Buku", cari2, "TERSEDIA!", "Silahkan menuju ke perpustakaan untuk mengambilnya.")
else:
    print("Buku", cari2, "TIDAK TERSEDIA")