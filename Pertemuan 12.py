print ('PROGRAM KATEGORI USIA')
usia = float(input('masukan usia anda :'))

if usia < 13 :
    print ('Kategori: Anak-anak')
elif 13<=usia<=18 :
    print ('Kategori: Remaja')
elif 18<usia<=50 :
    if usia < 30 :
        print ('Kategori: Dewasa Muda')
    else :
        print ('Kategori: Dewasa')
else :
    print ('Kategori: Lansia')


print ('PROGRAM MENENTUKAN LULUS ATAU TIDAK')

nilai = int(input('Masukan nilai anda (0-100):'))
absen = int(input('Masukan persentase kehadiran (0-100) :'))

if nilai >= 75 and absen >=80 :
    print ('Selamat Anda Lulus')
elif nilai < 75 :
    if absen > 90 :
        print ('Perbaiki nilai')
    else :
        print ('Tidak Lulus')
else :
    print ('Tingkatkan Kehadiran')

print ('PROGRAM MENENTUKAN DISKON')

harga = float(input('Masukan total belanja anda :'))
status = str(input('Masukan status keanggotaan anda (member atau non-member) :'))

if status == 'member' :
    if harga > 1000000 :
        print ('Selamat anda mendapatkan diskon sebesar 20%, total belanja anda menjadi :', harga - (harga*20/100))
    elif 500000 <= harga <= 1000000 :
        print ('Selamat anda mendapatkan diskon sebesar 15%, total belanja anda menjadi :', harga - (harga*15/100))
    else :
        print ('Selamat anda mendapatkan diskon sebesar 10%, total belanja anda menjadi :', harga - (harga*10/100))
else :
    if harga > 1000000 :
        print ('Selamat anda mendapatkan diskon sebesar 10%, total belanja anda menjadi :', harga - (harga*10/100))
    elif 500000 <= harga <= 1000000 :
        print ('Selamat anda mendapatkan diskon sebesar 5%, total belanja anda menjadi :', harga - (harga*5/100))
    else :
        print ('Sayang sekali anda tidak mendapatkan diskon, jika anda ingin mendapatkan diskon silahkan join membership kami. total belanja anda menjadi :', harga)

print ('PROGRAM MENENTUKAN TARIF PARKIR')

jenis = str(input('masukan jenis kendaraan anda (Motor atau Mobil) : '))
jam = float(input('Masukan berapa lama anda parkir (dalam jam) : '))

if jenis == 'Motor' :
    if jam <= 2 :
        print ('tarif anda adalah 2000')
    else :
        print ('Tarif anda adalah', 1000 * jam )
else :
    if jam <= 2 :
        print ('Tarif parkir anda adalah 5000')
    else :
        print ('Tarif parkir anda adalah', 5000 + (2000*(jam-2)))
