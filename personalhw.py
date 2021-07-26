#Soal Nomor 1
print("="*50)
print("Soal Nomor Satu")
JumlahKakiAyam= 2
JumlahKakiKambing= 4
JumlahHewan= 13
JumlahKaki = 32
Kambing = (2*JumlahHewan-JumlahKaki)/-JumlahKakiAyam
Ayam = JumlahHewan- (2*JumlahHewan-JumlahKaki)/-JumlahKakiAyam
print(Kambing)
print(Ayam)
print(f"Adam Memiliki Ayam {Ayam} Ekor dan Kambing {Kambing} Ekor")

#Soal Nomor 2
print("="*50)
print("Soal Nomor Dua")
rasioIbu = 1/7
rasioAnak = 1/4
perbedaanTahun = 1/2
perbedaanUmur = 19

PersamaanPertama = (perbedaanUmur * rasioAnak) + perbedaanTahun
PersamaanKedua = rasioAnak - rasioIbu

umurIbu = int(PersamaanPertama/PersamaanKedua)

PersamaanKetiga = (((rasioAnak/rasioIbu)*perbedaanUmur) + ((perbedaanUmur * rasioAnak) + rasioAnak) - perbedaanUmur)
PersamaanKeempat = rasioAnak/rasioIbu - 1

umurAnak = int(PersamaanKetiga/PersamaanKeempat)

umurMelahirkan = umurIbu - umurAnak

print(f"Umur ibu saat melahirkan Anaknya adalah {umurMelahirkan} Tahun")

#Soal Nomor 3
print("="*50)
print("Soal Nomor Tiga")

jumlahUmur = 50
rasioUmurBudi = 1
rasioUmurAyah = 6
jumlahTahun = 4

#umur4TahunLalu = (jumlahUmur-8)/(rasioUmurBudi+rasioUmurAyah)
#umurBudi = umur4TahunLalu+4
#umurAyah = 6*umur4TahunLalu+4

umurAyah = (rasioUmurAyah*(jumlahUmur-jumlahTahun)+jumlahTahun)/(rasioUmurBudi+rasioUmurAyah)
umurBudi = jumlahUmur - umurAyah

print(f"usia ayah saat ini adalah {umurAyah} tahun dan usia budi saat ini adalah {umurBudi} tahun")

#Soal Nomor 4
print("="*50)
print("Soal Nomor Empat")
kalimat = input("Masukkan kalimat : ")
karakter = input("Masukkan karakter (Huruf atau Angka) : ")
kalimat_lower = kalimat.lower()
karakter_lower = karakter.lower()
jumlah = kalimat_lower.count(karakter_lower)
print(f"Jumlah karakter {karakter} di dalam kalimat '{kalimat}' adalah {jumlah} karakter")

#Soal Nomor 5
print("="*50)
print("Soal Nomor Lima")

kalimat1 = input("Masukkan kalimat : ")
vokal = input("Masukkan huruf vokal : ")
output = kalimat1.replace("a",vokal.lower())
output = output.replace("e",vokal.lower())
output = output.replace("i",vokal.lower())
output = output.replace("o",vokal.lower())
output = output.replace("u",vokal.lower())
output = output.replace("A",vokal.upper())
output = output.replace("E",vokal.upper())
output = output.replace("I",vokal.upper())
output = output.replace("O",vokal.upper())
output = output.replace("U",vokal.upper())
print(output)

#SoalNomor6
print("="*50)
print("Soal Nomor Enam")

Mulai = 9
jarak = 120
KecepatanA = 60
KecepatanB = 40
t = jarak / (KecepatanA+KecepatanB)
import math
jam = math.floor(t)
menit = round(t-jam,1)
menitper60 = round(menit * 60,)
print(f"A dan B akan bertemu pada {Mulai}:{jam,menitper60}")
