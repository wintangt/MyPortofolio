#Soal Nomor 1
print("="*50)
print("Soal Nomor Satu")
try:
    jumlahHari = int(input('Masukkan jumlah hari :'))
    #Output nyatakan jumlah hari tersebut dalam
    #.... Tahun ... Bulan .... minggu ... hari

    tahun = 365 #hari
    bulan = 30  #hari 
    pekan = 7   #hari
    sisaHari = 0

    jumlahTahun =  jumlahHari//tahun
    sisaHari = jumlahHari%tahun #Menggunakan Modulus untuk melihat sisa

    jumlahBulan = sisaHari//bulan
    sisaHari = sisaHari%bulan #Menggunakan Modulus untuk melihat sisa

    jumlahPekan = sisaHari//pekan
    sisaHari = sisaHari%pekan #Menggunakan Modulus untuk melihat sisa

    if jumlahHari<=0:
        print('Jumlah Hari dibawah Batas Minimal')
    elif jumlahHari >=4000:
      print('Jumlah diatas batas maksimal')
    else:
      print(f'{"0"+str(jumlahTahun)} Tahun, {(jumlahBulan)} Bulan, {(jumlahPekan)} Minggu, {(sisaHari)} hari') 
except:
    print('jumlah hari salah')
'''
#Soal Nomor 2
print("="*50)
print("Soal Nomor Dua")
try:
    tinggiBadan =float(input('Masukan Tinggi Badan (dalam cm): '))
    beratBadan =float(input('Masukan Berat Badan(dalam kg): '))
    if beratBadan <= 0 or tinggiBadan <= 0 :
        print("berat badan atau tinggi badan tidak bisa negatif")
        exit()
    elif beratBadan > 250 or tinggiBadan >300 : 
        print("Batas maksimal berat : 250 KG dan Batas maksimal tinggi : 300 CM")
        exit()

# Tinggi badan anda ... (meter) dan berat anda ... (kg), 
# BMI anda ...(nilai BMI)... (dibulatkan 2 angka dibelakang koma)....
# dan anda termasuk .... (sesuai kondisi)....

    bmi= round(beratBadan / (tinggiBadan/100)**2, 2) #Dibagi 100 karena untuk merubahnya ke satuan METER, (,2) itu untuk round 2 angka d belakang koma

    tinggiMeter=tinggiBadan/100

    print(f'Tinggi Badan Anda {tinggiMeter} Meter dan berat anda {beratBadan} kg, BMI anda {bmi}')

    if bmi <= 18.4:
        print("dan berat badan anda termasuk Kurang")
    elif bmi <= 24.9:
        print ("dan berat badan anda termasuk Ideal")
    elif bmi <= 29.9:
        print('dan berat badan anda termasuk Berlebih')
    elif bmi <= 39.9:
        print("dan berat badan anda termasuk Sangat Berlebih")
    else:
        print(" dan berat badan anda termasuk Obesitas")
except:
    print("Angka yang anda masukan salah")

#Soal Nomor 3
print("="*50)
print("Soal Nomor Tiga")
try:
    nilai=float(input('Masukan Nilai : '))

    if nilai >= 90 :
        print(f'Nilai anda {nilai} dan Anda Grade A')
    elif nilai  >= 85 and nilai < 90 :
        print(f'Nilai anda {nilai} dan Anda Grade A-')
    elif nilai >= 80 and nilai < 85 :
        print (f'Nilai anda {nilai} dan Anda grade B')
    elif nilai  >= 75 and nilai < 80 :
        print(f'Nilai anda {nilai} dan Anda grade B-')
    elif nilai >=70 and nilai < 75 :
        print(f'Nilai anda {nilai} dan Anda grade C')
    elif nilai >=65 and nilai < 70 :
        print(f'Nilai anda {nilai} dan Anda grade D')
    elif nilai >=40 and nilai < 65 :
        print(f'Nilai anda {nilai} dan Anda Perlu REMEDIAL')
    elif nilai > 100:
        print(f'Nilai anda diluar jangkauan')
    elif nilai < 0:
        print(f'tidak menerima angka negatif')
    else:
        print(f'Nilai anda {nilai} dan Anda Tidak LULUS')
except:
    print("Angka yang anda masukan salah")
    '''