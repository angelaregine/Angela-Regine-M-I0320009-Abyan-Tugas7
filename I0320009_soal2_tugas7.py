#Perhitungan Juara Umum Perlombaan
sapa = "Halo panitia, silakan masukkan nilai finalis top 5 yang telah dinilai juri!"
print(sapa)

import math
nama1 = str(input("Masukkan nomor identitas finalis 1: "))
nilai1 = float(input("Masukkan nilai finalis 1: "))
ceil1 = math.ceil(nilai1)

nama2 = str(input("Masukkan nomor identitas finalis 2: "))
nilai2 = float(input("Masukkan nilai finalis 2: "))
ceil2 = math.ceil(nilai2)

nama3 = str(input("Masukkan nomor identitas finalis 3: "))
nilai3 = float(input("Masukkan nilai finalis 3: "))
ceil3 = math.ceil(nilai3)

nama4= str(input("Masukkan nomor identitas finalis 4: "))
nilai4 = float(input("Masukkan nilai finalis 4: "))
ceil4 = math.ceil(nilai4)

nama5 = str(input("Masukkan nomor identitas finalis 5: "))
nilai5 = float(input("Masukkan nilai finalis 5: "))
ceil5 = math.ceil(nilai5)

datanilai = []
datanilai1 = datanilai.append(ceil1)
datanilai2 = datanilai.append(ceil2)
datanilai3 = datanilai.append(ceil3)
datanilai4 = datanilai.append(ceil4)
datanilai5 = datanilai.append(ceil5)

nmax = max(datanilai)

print("Juara umum pada perlombaan ini adalah peserta dengan nilai: ", nmax)

#Menentukan juara hiburan untuk seluruh peserta
peserta = int(input("Jumlah seluruh peserta yang mengikuti lomba ini: "))
import random
print("Peserta yang memenangkan hadiah hiburan umum yaitu peserta dengan no identitas", random.randrange(1, peserta))