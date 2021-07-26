'''
### Tugas Personal
Deadline : Rabu : 17.00 => 9 Juni 2021

- Email Verification/Validation
Buatlah suatu Return Function untuk Verifikasi/validasi Email 

Input :
Masukkan Email :

Output :
Sesuai Kondisi

Contoh Penggunaan :
Email = input("Masukkan Email : ")

## Contoh Inisiasi Function
def Verification(...):
    ..... 
    ..... 
    return ......

print(Verification(Email))  ### Contoh Menggunakan-Memanggil Function

Kondisi :
Email Valid Jika :
- Memiliki Format NamaUser@namaHosting.extensi
- Nama User hanya Boleh Huruf, Angka, Underscore(_), dan dot(.)
- Nama user hanya boleh diawali dg Huruf atau Angka 
- Nama Hosting hanya boleh Huruf atau Kombinasi Huruf dan Angka 
- Nama Extensi hanya boleh huruf dan maksimal 5 karakter 
- Simbol atau karakter khsusu tidak diterima ==> $%!~&*/^ dst 
- Jumlah @ hanya boleh 1
- .co.id, .co.my, .co.sg, .go.id ==> ini dianggap sebagai 2 extensi, jadi masing-masing harus mengikuti aturan ekstensi
- Maksimal hanya untuk 2 Extensi ==> Jumlah dot(.) untuk extensi maksimal 2

Contoh Output :
"Alamat Email yg anda Masukkan Valid"

Jika Tidak Valid - Invalid, Keluar Notif Sesuai Alasannya :

"Email InValid, *Alasan*"
Alasan :
- Format Email Salah ==> Misal Tidak ada @, atau tidak ada .extensi)
- Format User name yg anda Masukkan Salah 
- Format Hosting yg anda Masukkan Salah 
- Format Extensi yg anda Masukkan Salah 

Contoh Email :
Valid :
andre@gmail.com
joni_00@yahoo.co.id 
andy.256@city.com 
steve_rogers.77@avengers01.space 

InValid :
Joni345@gmail 
@gmail.com 
_John@yahoo.com 
Johny$%^&@gmail.co.id 
John@ya$$h%%.com 
tony_stark@stark.corporation
hulk@stark.corp5
Thor@@gmail.com
'''
'''
email = str(input("Masukan Email: "))

def checkemail(email):
    if ' ' in email:
        return "format email salah"
    if email[0].isalnum()==False:
        return "Username yang anda masukan salah"
    if "@" not in email:
         return "format email salah"
    name, domain = email.split('@', 1)
    if '.' not in domain[1:]:
        return "format email salah"
    return True
print(checkemail(email))
'''

def emailVerification(email):
    Username = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._'
    simbol = ''' `,~,!,,#,$,%,^,&,*,(,),-,+,=,{,[,},},|,\,:,;,",',<,,,>,?,/'''
    hasil = ''

    try:
        cek1 = email.count('@')
        firstchar = email[0]
        xUser = email[0:email.index('@')]
        xhostingext = email[email.index('@') + 1:]
        xhosting = xhostingext[:xhostingext.index('.')]
        xExtfull = xhostingext[xhostingext.index('.') + 1:]
        xExt1 = ''
        xExt2 = ''
        flag = True
        flag2 = True

        if '.' in xExtfull:
            xExt1 = xExtfull[:xExtfull.index('.')]
            xExt2 = xExtfull[xExtfull.index('.') + 1:]

        for rec in xUser:
            if rec not in Username:
                flag = False
                break

        for rec in email:
            if rec in simbol:
                flag2 = False
                break

        if flag == True and firstchar.isalnum() and (xhosting.isalpha() or xhosting.isnumeric() == False) and ((xExt1 == '' and xExtfull.isalpha() and len(xExtfull) <= 5) or (xExt1 != '' and xExt2 != '' and xExt1.isalpha() and xExt2.isalpha() and len(xExt1) <= 5 and len(xExt1) <= 5)) and flag2 == True and cek1 == 1:
            hasil = 'Email Benar'
        else:
            hasil += 'Email Invalid! '
            if flag == False:
                hasil += 'Username Salah '

            if firstchar.isalnum() == False:
                hasil += 'Username Salah '    
            
            if xhosting.isnumeric() == True:
                hasil += 'Hosting Salah '

            if (xExt1 == '' and (xExtfull.isalpha() == False or len(xExtfull) <= 0 or len(xExtfull) >5)) or (xExt1 != '' and xExt2 != '' and (xExt1.isalpha() == False or xExt2.isalpha() == False or len(xExt1) <= 0 and len(xExt1) > 5)):
                hasil += 'Ekstensi salah '

            if flag2 == False:
                hasil += 'Format email salah, terdapat simbol/karakter khusus '

            if cek1 == 0:
                hasil += 'Format email salah, tidak terdapat @ '
            
            if cek1 > 1:
                hasil += 'Format email salah, terlalu banyak tanda @ '
    except ValueError:
        hasil += 'Format Email Salah \n'

    return hasil
                        

print('='*50)

emailUser = input('Masukkan Email : ')
print(emailVerification(emailUser))


inputHari = input('Masukkan Nama Hari : ')
convert = inputHari.lower()
hari = {'senin' : 'monday', 
'selasa' : 'tuesday', 
'rabu' : 'wednesday', 
'kamis' : 'thursday', 
'jumat' : 'friday', 
'sabtu' : 'saturday',
'minggu' : 'sunday'}

if convert.isalpha():
    if convert in hari.keys() or convert in hari.values():
        for x, y in hari.items():
            if x == convert:
                print(f'Hari yang anda pilih adalah {inputHari} dalam bahasa inggris adalah {y}')
            elif y == convert:
                print(f'The day that you choose is {inputHari} in bahasa is {x}')
    else:
        print('hari tidak ditemukan')
else:           
    print('Tidak menerima Angka dan simbol, silahkan masukkan hari yg benar!')
