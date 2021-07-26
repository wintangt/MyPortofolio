'''
######## Team Assignment
Mini Apps v 1.0
Member 2-3 orang 


##### 
- Ketika awal program di run, akan muncul 3 pilihan 


Selamat Datang di Applikasi XXYY
1. Register
2. Login
3. Exit 

Ketika user memilih menu Register 

---- Registration ---- 

Masukkan Data :
UserId : ..... 
Ketentuan UserID :
- Harus kombinasi huruf dan angka 
- Tidak boleh ada karakter khusus/spesial char. 
- minimal 6 karakter 
- maksimal 20 karakter 
- Lakukan Pengecekan Duplikasi, Tidak boleh ada UserId yg sama 
- Jika ada duplikasi, atau tidak sesuai kriteria, akan keluar notifikasi 
- Ketika ada masalah format UserId, user diminta memasukkan lagi UserID hingga formatnya benar (Maksimal 5X percobaan)
- setelah 5X gagal, keluar dari apps 

Password : ... 
- Harus Kombinasi Huruf Kapital, Huruf Kecil, Angka dan spesial karakter / karakter khusus = &^%$#!@
- Minimal 8 karakter 

Masukkan Email : ... 
- Lakukan Verifikasi Email, Ketentuan seperti Tugas sebelumnya.
- Keluar Notif jika Email InValid 

Nama : .... (Hanya Alfabet dan Spasi)
Gender : ... (Hanya bisa Female atau Male .... Pria - wanita)
Usia : ... (Harus Integer, Minimal 17 tahun, maksimal 80 tahun)
Pekerjaan : .... (Hanya alfabet dan spasi)
Hobi : .... (hanya alfabet dan isi lebih dari satu)
Alamat : 
    Nama Kota : (hanya alfabet dan spasi)
    RT : (Numerik Integer)
    RW : (Numerik Integer)
    Zip COde : (Numerik Integer dan 5 karakter)
    Geo : 
        Lat : .... Numerik - Float/Integer
        Longitude : .... Numerik - Float/Integer
No HP : ... Harus Integer, Jumlah karakter 11 - 13

Simpan Data (Y/N) :

Y : Data tersimpan
N : data tidak tersimpan 

Setelah ini, baik memilih Y atau N akan kembali ke menu awal 

Selamat Datang di Applikasi XXYY
1. Register
2. Login
3. Exit 

#### Ketika user memilih menu Login
- user yg sudah registrasi akan bisa Login 

Login 

Masukkan UserID : ... 
Masukkan Password : ... 

Lakukan pengecekan ID dan Password 
Notif :
- ID dan Password Salah 
- Password Salah, Jika ID sudah ada, tetapi password berbeda 
- ID tidak terdaftar 
- Anda Berhasil Login

* Jika gagal melakukan Login, akan kembali ke menu utama .
* Maksimal Percobaan Login 5X 


--- Jika Berhasil Login --- 
1. User Profile 
2. Menu Transaksi 

-- Jika Pilih User Profile --- 
Akan keluar Data personal dari user yg Login 
selain username dan password 

Data Anda :
nama :
email : 
gender : 
usia : 
pekerjaan : 
hobi :
alamat : 
    Nama Kota : 
    RT :
    RW :
    ZipCOde : 
    Geo : 
        Lat : 
        Long : 
No HP : 

-- Jika pilih menu transaksi -- Menu CRUD 

1. Create Data 
2. Read data 
3. Update Data 
4. Delete Data 
5. Kembali ke Menu awal 


Data harus Dictionary :
Nama Barang - Stok ==> Apps Gudang 
Nama Barang - Harga ==> Apps Kasir 
nama Karyawan - Gaji ==> Apps Penggajian
mahasiswa - Nilai ==> Apps Kampus 
atau yg sejenis 


Ketentuan Menu CRUD :
1. Read Data (Cetak Data)
- Jika tidak ada data, keluar notif : Daftar Barang masih kosong 
- Jika ada barang, akan ditampilkan satu persatu 

2. Create Data (Tambah data)
- Pengecekan jenis data, jika salah format keluar Notif 
- Jenis format disesuaikan dg jenis data yg dipilih ==> 2365, 2gb RAM, ram 2 gb, NINJA 250RR - 20
- Pengecekan duplikasi :
Jika data sudah ada sebelumnya :
Keluar Notif 
Data sudah ada, apakah data akan disimpan? (Y/N)
Y : keluar notif => data tersimpan, dan mengupdate data barang 
N : keluar notif => Data tidak tersimpan 
- Input Values harus numerik, Minimal 0
- Integer / Float untuk Values disesuaikan dg kebutuhan

3. Update Data 
- user memasukkan nama data yg akan diubah 
- Lakukan pengecekan apakah datanya ada di dalam Dictionary atau tidak 
- Jika barang tidak ada, keluar notif : Barang tidak ditemukan
- Jika barang ditemukan 
- Ada 2 Pilihan :
    * Update Barang - Update Key 
    * Update Stok/Harga - Update Values 
- Ketika Update Key - Lakukan pengecekan Format data 
- Ketika Update Key - Lakukan Pengecekan Duplikasi - Ninja 250RR --> Yamaha R25 -5
- Ketika update Values => Jika pendekatan yg digunakan adalah Summary ==> Nilai negatif diperbolehkan, tetapi Nilai Akhir Minimal 0
                       => Jika pendekatan yg digunakan adalah Replace values ==> Tidak menerima nilai Negatif, minimal 0 



4. Delete Data
- User memasukkan nama data yg akan dihapus
- Jika data tidak ada, keluar notif : Data Tidak ditemukan
- Jika data ditemukan, 
keluar Pilihan : Apakah Data akan dihapus? (Y/N)
jika Y : Akan menghapus data/Items ==> keluar Notif : Barang Berhasil Dihapus 
jika N : Barang tidak jadi dihapus 


** Setiap selesai melakukan Proses-Fungsi CRUD 
akan keluar mini menu yg memiliki 2 opsi 
1. Kembali ke Menu (yg sedang diakses)
2. Kembali Ke Menu Utama/ Menu CRUD 

'''

cekMenu = False
angka = '1234567890'
dataUser = {'user' : [],
            'password' : [],
            'email' : [],
            'nama' : [],
            'gender' : [],
            'usia' : [],
            'pekerjaan' : [],
            'hobi' : [],
            'alamat' : {'namaKota' : [],
                        'rt' : [],
                        'rw' : [],
                        'zipCode' : [],
                        'geo' : {'lat' : [],
                                 'longitude' : []}
                        },
             'noHp' : []}
dataBarang = {'namaBarang' : [],
              'stok' : []}

def emailVerification(email):
    result = ''
    karakterKhusus = '~!#$%^&*()+<>?/|}{]['
    userContain = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._'

    try:
        cekAt = email.count('@')
        getAwalan = email[0]
        getUser = email[0:email.index('@')]
        getHostingExt = email[email.index('@') + 1:]
        getHosting = getHostingExt[:getHostingExt.index('.')]
        getExtFull = getHostingExt[getHostingExt.index('.') + 1:]
        getExt1 = ''
        getExt2 = ''
        flag = True
        flag2 = True

        if '.' in getExtFull:
            getExt1 = getExtFull[:getExtFull.index('.')]
            getExt2 = getExtFull[getExtFull.index('.') + 1:]

        for rec in getUser:
            if rec not in userContain:
                flag = False
                break

        for rec in email:
            if rec in karakterKhusus:
                flag2 = False
                break

        if flag == True and getAwalan.isalnum() and (getHosting.isalpha() or getHosting.isnumeric() == False) and ((getExt1 == '' and getExtFull.isalpha() and len(getExtFull) <= 5) or (getExt1 != '' and getExt2 != '' and getExt1.isalpha() and getExt2.isalpha() and len(getExt1) <= 5 and len(getExt1) <= 5)) and flag2 == True and cekAt == 1:
            result = 'OK'
        else:
            result += 'Email Invalid! \n'
            if flag == False:
                result += 'Format username yang anda masukkan salah \n'

            if getAwalan.isalnum() == False:
                result += 'Format username yang anda masukkan salah \n'    
            
            if getHosting.isnumeric() == True:
                result += 'Format hosting yg anda masukkan salah \n'

            if (getExt1 == '' and (getExtFull.isalpha() == False or len(getExtFull) <= 0 or len(getExtFull) >5)) or (getExt1 != '' and getExt2 != '' and (getExt1.isalpha() == False or getExt2.isalpha() == False or len(getExt1) <= 0 and len(getExt1) > 5)):
                result += 'Format extensi yg anda masukkan salah \n'

            if flag2 == False:
                result += 'Format email salah, terdapat simbol/karakter khusus \n'

            if cekAt == 0:
                result += 'Format email salah, tidak terdapat @ \n'
            
            if cekAt > 1:
                result += 'Format email salah, terlalu banyak tanda @ \n'
    except ValueError:
        result += 'Format Email Salah \n'

    return result

def menuUtama():
    print('Selamat Datang di Aplikasi Go-Ceng')
    print('=' * 50)
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    cekMenu = True

    while cekMenu == True:
        pilihMenu = input('Silahkan pilih menu : ')

        if pilihMenu.isnumeric() and pilihMenu in ['1','2','3']:
            if pilihMenu == '1':
                cekMenu = False
                registerMenu()
            elif pilihMenu == '2':
                cekMenu = False
                loginMenu()
            else:
                cekMenu = False
        else:
            cekMenu = True
            print('Masukkan angka 1 atau 2 atau 3')
    
def registerMenu():
    cekUserKarakterKhusus = False
    cekUserDuplicate = False
    cekUser = False
    cekPass = False
    cekEmail = False
    cekLoop = True
    cekNama = False
    cekGender = False
    cekUsia = False
    cekPekerjaan = False
    cekHobi = False
    cekNamaKota = False
    cekRT = False
    cekRW = False
    cekZipCode = False
    cekLat = False
    cekLongitude = False
    cekNoHp = False
    i = 1
    karakterKhusus = '~!@#$%^&*()+<>?/|}{][_-.'

    print('------- Registration --------')
    print('Masukkan Data : ')

    while i <=5:
        user = input('UserID : ')
        cekUserDuplicate = False
  
        for k,v in dataUser.items():
            if k == 'user':
                for rec in v:
                    if rec == user:
                        cekUserDuplicate = True
                        break
      
        for rec in user:
            if rec in karakterKhusus:
                cekUserKarakterKhusus = True
                break

        if user.isalnum() and user.isnumeric() == False and user.isalpha() == False and cekUserKarakterKhusus == False and (len(user) >= 6 and len(user) <= 20) and cekUserDuplicate == False:
            cekUser = True
            break
        else:
            if len(user) < 6 or len(user) > 20:
                print('Panjang karakter minimal 6 dan maksimal 20')
            elif cekUserDuplicate == True:
                print('User telah terdaftar')
            else:
                print('Harus Kombinasi Huruf & Angka')

            i += 1

    if cekUser == True:
        while cekLoop == True:
            password = input('Password : ')

            for rec2 in password:
                if rec2 in karakterKhusus:
                    cekPass = False
                    break
                else:
                    cekPass = True

            if cekPass == False:
                for rec3 in password:
                    if rec3 in angka:
                        cekPass = False
                        cekLoop = False
                        break
                    else:
                        cekPass = True
            else:
                print('Harus Kombinasi Huruf Kapital, Huruf Kecil, Angka dan Spesial Karakter')
        

        if cekPass == False and len(password) >= 8 and (password.isupper() == False or password.islower() == False):
            cekLoop = True

            while cekLoop == True:
                email = input('Masukkan Email : ')
                result = emailVerification(email)

                if result == 'OK':
                    cekEmail = False
                    cekLoop = False
                else:
                    print(result)
                    cekEmail = True

            if cekEmail == False:
                cekLoop = True

                while cekLoop == True:
                    nama = input('Nama : ')

                    replaceName = nama.replace(' ','')

                    if replaceName.isalpha():
                        cekNama = False
                        cekLoop = False
                    else:
                        cekNama = True
                        print('Nama hanya bisa diisi dengan alfabet')

                if cekNama == False:
                    cekLoop = True

                    while cekLoop == True:
                        gender = input('Gender : ')

                        if gender.isalpha():
                            if gender in ['Pria','Wanita']:
                                cekGender = False
                                cekLoop = False
                            else:
                                print('Gender hanya bisa diisi dengan Pria atau Wanita')
                                cekGender = True
                        else:
                            cekGender = True
                            print('Gender hanya bisa diisi dengan Pria atau Wanita')

                    if cekGender == False:
                        cekLoop = True

                        while cekLoop == True:
                            usia = input('Usia : ')

                            if usia.isnumeric():
                                if int(usia) >= 17 and int(usia) <= 80:
                                    cekUsia = False
                                    cekLoop = False
                                else:
                                    print('Usia minimal 17 tahun dan maksimal 80 tahun')
                                    cekUsia = True
                            else:
                                cekUsia = True
                                print('Usia Hanya bisa diisi dengan angka')
                        
                        if cekUsia == False:
                            cekLoop = True

                            while cekLoop == True:
                                pekerjaan = input('Pekerjaan : ')

                                replacePekerjaan = pekerjaan.replace(' ','')

                                if replacePekerjaan.isalpha():
                                    cekPekerjaan = False
                                    cekLoop = False
                                else:
                                    cekPekerjaan = True
                                    print('Pekerjaan hanya bisa diisi dengan alfabet')

                            if cekPekerjaan == False:
                                cekLoop = True

                                while cekLoop == True:
                                    hobi = input('Hobi : ')

                                    replaceHobi = hobi.replace(' ','')

                                    if replaceHobi.isalpha():
                                        cekHobi = False
                                        cekLoop = False
                                    else:
                                        cekHobi = True
                                        print('Cek hanya bisa diisi dengan alfabet')

                                if cekHobi == False:
                                    cekLoop = True

                                    while cekLoop == True:
                                        namaKota = input('Nama Kota : ')

                                        replaceNamaKota = namaKota.replace(' ','')

                                        if replaceNamaKota.isalpha():
                                            cekNamaKota = False
                                            cekLoop = False
                                        else:
                                            cekNamaKota = True
                                            print('Nama Kota hanya bisa diisi dengan alfabet')

                                    if cekNamaKota == False:
                                        cekLoop = True

                                        while cekLoop == True:
                                            rt = input('RT : ')

                                            if rt.isnumeric():
                                                cekRT = False
                                                cekLoop = False
                                            else:
                                                cekRT = True
                                                print('RT Hanya bisa diisi dengan angka')

                                        if cekRT == False:
                                            cekLoop = True

                                            while cekLoop == True:
                                                rw = input('RW : ')

                                                if rw.isnumeric():
                                                    cekRW = False
                                                    cekLoop = False
                                                else:
                                                    cekRW = True
                                                    print('RW Hanya bisa diisi dengan angka')

                                            if cekRW == False:
                                                cekLoop = True

                                                while cekLoop == True:
                                                    zipCode = input('Zip Code : ')

                                                    if zipCode.isnumeric():
                                                        if len(zipCode) == 5:
                                                            cekZipCode = False
                                                            cekLoop = False
                                                        else:
                                                            print('Zip Code harus terdiri dari 5 karakter')
                                                    else:
                                                        cekZipCode = True
                                                        print('Zip Code Hanya bisa diisi dengan angka')

                                                if cekZipCode == False:
                                                    cekLoop = True

                                                    while cekLoop == True:
                                                        lat = input('Latitude : ')

                                                        if lat.isnumeric() or lat.isdecimal():
                                                            cekLat = False
                                                            cekLoop = False
                                                        else:
                                                            cekLat = True
                                                            print('Lat Hanya bisa diisi dengan angka atau desimal')

                                                    if cekLat == False:
                                                        cekLoop = True

                                                        while cekLoop == True:
                                                            longitude = input('Longitude : ')

                                                            if longitude.isnumeric() or longitude.isdecimal():
                                                                cekLongitude = False
                                                                cekLoop = False
                                                            else:
                                                                cekLongitude = True
                                                                print('Longitude Hanya bisa diisi dengan angka atau desimal')

                                                        if cekLongitude == False:
                                                            cekLoop = True

                                                            while cekLoop == True:
                                                                noHp = input('No HP : ')

                                                                if noHp.isnumeric():
                                                                    if len(noHp) >= 11 and len(noHp) <= 13:
                                                                        cekNoHp = False
                                                                        cekLoop = False
                                                                    else:
                                                                        print('No HP minimal 11 karakter dan maksimal 13 karakter')
                                                                else:
                                                                    cekNoHp = True
                                                                    print('No HP Hanya bisa diisi dengan angka')

                                                            if cekNoHp == False:
                                                                cekLoop = True

                                                                while cekLoop == True:
                                                                    save = input('Simpan Data (Y/N) :')

                                                                    if save.isalpha():
                                                                        if save.upper() in ['Y','N']:
                                                                            if save.upper() == 'Y':
                                                                                try:                                                                       
                                                                                    dataUser['user'].append(user)
                                                                                    dataUser['password'].append(password)
                                                                                    dataUser['email'].append(email)
                                                                                    dataUser['nama'].append(nama)
                                                                                    dataUser['gender'].append(gender)
                                                                                    dataUser['usia'].append(usia)
                                                                                    dataUser['pekerjaan'].append(pekerjaan)
                                                                                    dataUser['hobi'].append(hobi)
                                                                                    dataUser['alamat']['namaKota'].append(namaKota)
                                                                                    dataUser['alamat']['rt'].append(rt)
                                                                                    dataUser['alamat']['rw'].append(rw)
                                                                                    dataUser['alamat']['zipCode'].append(zipCode)
                                                                                    dataUser['alamat']['geo']['lat'].append(lat)
                                                                                    dataUser['alamat']['geo']['longitude'].append(longitude)
                                                                                    dataUser['noHp'].append(noHp)
                                                                                    print('Data tersimpan')
                                                                                except:
                                                                                    print('Error! Data tidak tersimpan')
                                                                            else:
                                                                                print('Data tidak tersimpan')

                                                                            menuUtama()
                                                                            cekLoop = False
                                                                        else:
                                                                            print('Save Hanya bisa diisi dengan huruf Y atau N')
                                                                    else:
                                                                        print('Save Hanya bisa diisi dengan huruf Y atau N')
    else:
        print('Anda telah 5 kali gagal, harap coba lagi nanti')

def miniMenu():
    print('1. Kembali ke Menu CRUD')
    print('2. Kembali Ke Menu Utama')
    cekMenu = True

    while cekMenu == True:
        pilihMenu = input('Silahkan pilih menu : ')

        if pilihMenu.isnumeric() and pilihMenu in ['1','2']:
            if pilihMenu == '1':
                cekMenu = False
                transaksiMenu()
            else:
                menuUtama()
                cekMenu = False
        else:
            cekMenu = True
            print('Masukkan angka 1 atau 2 atau 3')
    
def userProfileMenu(indexUser):
    print('---------------User Profile------------------')
        
    print(f"nama : {dataUser['nama'][indexUser]}")
    print(f"email : {dataUser['email'][indexUser]}") 
    print(f"gender : {dataUser['gender'][indexUser]}") 
    print(f"usia : {dataUser['usia'][indexUser]}") 
    print(f"pekerjaan : {dataUser['pekerjaan'][indexUser]}") 
    print(f"hobi : {dataUser['hobi'][indexUser]}")
    print(f"alamat : Nama Kota : {dataUser['alamat']['namaKota'][indexUser]}") 
    print(f"\t RT : {dataUser['alamat']['rt'][indexUser]}")
    print(f"\t RW : {dataUser['alamat']['rw'][indexUser]}")
    print(f"\t ZipCode : {dataUser['alamat']['zipCode'][indexUser]}") 
    print(f"\t Geo :  Lat : {dataUser['alamat']['geo']['lat'][indexUser]}") 
    print(f"\t\tLong : {dataUser['alamat']['geo']['longitude'][indexUser]}") 
    print(f"No HP : {dataUser['noHp'][indexUser]}")

def createMenu():
    cekMenu = True
    
    while cekMenu == True:
        barang = input('Masukkan nama barang : ').title()
        stok = input('Masukkan jumlah stok barang : ')
        cekAwalanBarang = barang[0]

        if cekAwalanBarang.isalpha() and barang.isnumeric() == False and stok.isnumeric() and int(stok) >= 0:
            try:
                cekDuplicateBarang = dataBarang['namaBarang'].index(barang)
                cekDuplicateStok = dataBarang['stok'][cekDuplicateBarang]
                flagDuplicateBarang = True
            except:
                flagDuplicateBarang = False

            if flagDuplicateBarang == True:
                notifDuplicateBarang = input('Data sudah ada, apakah data akan disimpan? (Y/N)')

                if notifDuplicateBarang.upper() in ['Y','N']:
                    if notifDuplicateBarang.upper() == 'Y':
                        dataBarang['stok'] = cekDuplicateStok + int(stok)
                        print('Data Tersimpan dan Update Barang')
                        cekMenu = False
                    else:
                        cekMenu = False
                else:
                    print('Save hanya bisa diisi dengan huruf Y atau N')
            else:
                dataBarang['namaBarang'].append(barang)
                dataBarang['stok'].append(int(stok))
                print('Data Tersimpan')
                cekMenu = False
        else:
            print('Mohon input nama barang dan stok (Minimal 0) dengan benar')
            cekMenu = True

        if cekMenu == False:
            miniMenu()
        
def readMenu():
    print('-----------Data Barang-------------')

    getBarang = dataBarang['namaBarang']
    getStock = dataBarang['stok']
    i = 0

    if getBarang != []:
        while i < len(getBarang):
            print(f'{getBarang[i]}\t{getStock[i]}')
            i += 1
    else:
        print('Data barang masih kosong')

    miniMenu()

def updateMenu():
    print('------------Update Barang-----------')

    cekMenu = True

    while cekMenu == True:
        barang = input('Masukkan Nama Barang yang ingin diupdate : ').title()
        updateBarang = input('Update data barang atau stok? (barang/stok) : ')

        try:
            getBarang = dataBarang['namaBarang'].index(barang)
            getStok = dataBarang['stok'][getBarang]

            if updateBarang.lower() in ['barang','stok']:
                if updateBarang.lower() == 'barang':
                    barangPengganti = input('Masukkan Nama Barang Pengganti : ').title()
                    cekAwalanBarang = barangPengganti[0]

                    if cekAwalanBarang.isalpha() and barang.isnumeric() == False:
                        dataBarang['namaBarang'][getBarang] = barangPengganti
                        cekMenu = False
                        print('Data nama barang berhasil diupdate')
                    else:
                        print('Format nama barang belum sesuai')
                        cekMenu = True
                else:
                    stokPengganti = input('Masukkan Jumlah Stok Pengganti : ')

                    if stokPengganti.isnumeric() and int(stokPengganti) >= 0:
                        dataBarang['stok'][getBarang] = int(stokPengganti)
                        cekMenu = False
                        print('Data stok berhasil diupdate')
                    else:
                        print('Format nama barang belum sesuai')
                        cekMenu = True
            else:
                print('Masukkan input barang atau stok')
                cekMenu = True
        except:
            print('Barang tidak ditemukan')
            cekMenu = True

        if cekMenu == False:
            miniMenu()

def deleteMenu():
    print('------------Delete Barang-----------')

    cekMenu = True

    while cekMenu == True:
        barang = input('Masukkan Nama Barang yang ingin dihapus : ').title()

        try:
            getBarang = dataBarang['namaBarang'].index(barang)
            getStok = dataBarang['stok'][getBarang]
            deleteBarang = input('Apakah Data akan dihapus? (Y/N) : ')

            if deleteBarang.upper() in ['Y','N']:
                if deleteBarang.upper() == 'Y':
                    dataBarang['namaBarang'].remove(barang)
                    dataBarang['stok'].remove(getStok)
                    print('Barang berhasil dihapus')
                    cekMenu = False
                else:
                    print('Barang tidak jadi dihapus')
                    cekMenu = False
            else:
                print('Hanya bisa diisi dengan huruf Y atau N')
                cekMenu = True
        except:
            print('Data tidak ditemukan')
            cekMenu = True

        if cekMenu == False:
            miniMenu()

def transaksiMenu():
    print('--------CRUD--------')   
    print('1. Create Data')
    print('2. Read Data') 
    print('3. Update Data')
    print('4. Delete Data') 
    print('5. Kembali ke Menu awal')
    cekMenu = True

    while cekMenu == True:
        pilihMenu = input('Silahkan pilih menu : ')

        if pilihMenu.isnumeric() and pilihMenu in ['1','2','3','4','5']:
            if pilihMenu == '1':
                cekMenu = False
                createMenu()
            elif pilihMenu == '2':
                cekMenu = False
                readMenu()
            elif pilihMenu == '3':
                cekMenu = False
                updateMenu()
            elif pilihMenu == '4':
                cekMenu = False
                deleteMenu()
            else:
                menuUtama()
                cekMenu = False
        else:
            cekMenu = True
            print('Masukkan angka 1 atau 2 atau 3')

def loginMenu():
    print('---------Login------------')
    i = 1

    while i <= 5:
        cekIndexUser = False
        userLogin = input('Masukkan UserID : ')
        passLogin = input('Masukkan Password : ')
        
        try:
            indexUser = dataUser['user'].index(userLogin)
            cekIndexUser = True
        except:
            print('ID tidak terdaftar')

        if cekIndexUser == True:
            try:
                indexPass = dataUser['password'][indexUser]
                if passLogin == indexPass:
                    print('Anda berhasil login')

                    print('1. User Profie')
                    print('2. Menu Transaksi')
                    print('3. Exit')
                    cekMenu = True
                                                    
                    while cekMenu == True:
                        pilihMenu = input('Masukkan menu : ')

                        if pilihMenu in ['1','2','3'] and pilihMenu.isnumeric():
                            if pilihMenu == '1':
                                cekMenu = False
                                userProfileMenu(indexUser)
                            elif pilihMenu == '2':
                                cekMenu = False
                                transaksiMenu()
                            else:
                                cekMenu = False
                                menuUtama()
                        else:
                            cekMenu = True
                            print('Masukkan angka 1 atau 2')
                            i = 6
                else:
                    print('Password Salah')
            except:
                print('Password Salah')
                
        i += 1

menuUtama()