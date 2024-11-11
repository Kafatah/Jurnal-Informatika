huruf = str(input('masukan sebuah huruf :'))

if huruf == 'a'or huruf == 'i' or huruf == 'u' or huruf == 'e' or huruf == 'o' :
    print ('Ini adalah huruf vokal')
else :
    print ('Ini adalah huruf konsonan')

hari = int(input('Masukan angka :'))

if hari == 1 :
    print ('ini adalah hari senin')
elif hari == 2 :
    print ('Ini adalah hari selasa') 
elif  hari == 3 :
    print ('Ini adalah hari rabu')   
elif  hari == 4 :
    print ('Ini adalah hari kamis')  
elif  hari == 5 :
    print ('Ini adalah hari jumat')   
elif  hari == 6 :
    print ('Ini adalah hari sabtu')   
elif  hari == 7 :
    print ('Ini adalah hari minggu')    
else :
    print ('Pilihan tidak tersedia')


nilai = int(input('Masukkan nilai anda (0-100) :'))

if 90 <= nilai <= 100 : 
    print ('Prestasi sangat baik')
elif 80 <= nilai <=89 : 
    print ('Prestasi baik')
elif 70 <= nilai <=79 : 
    print ('Prestasi cukup')
elif 60 <= nilai <=69 : 
    print ('Prestasi kurang')
else :
    print ("Tidak memenuhi prestasi minimum")

usia = int(input('Masukkan usia anda :'))
hari = str(input('Masukkan hari anda membeli tiket :'))

if usia < 12 :
    if hari == 'sabtu' or hari == 'minggu' :
        print ('Harga tiket adalah 10000')
    else :
        print ('Harga tiket adalah 5000')
else :
    if hari == 'sabtu' or hari == 'minggu' :
        print ('Harga tiket adalah 20000')
    else :
         print ('Harga tiket adalah 15000')

status = str(input('Masukkan status kerja anda :'))
jam = int(input('Masukkan jumlah jam anda terlambat :'))


if status == 'tetap' :
    if jam > 5 :
        print ('Potongan gaji adalah 10%')
    elif 1<= jam <= 5 :
        print ('Potongan gaji adalah 5%') 
    else :
        print ('Tidak ada potongan gaji')
else :
    if jam > 3 :
        print ('Potongan gaji adalah 15%')
    elif 1<= jam <= 3 :
        print ('Potongan gaji adalah 7%') 
    else :
        print ('Tidak ada potongan gaji')
