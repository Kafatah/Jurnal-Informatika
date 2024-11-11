# Pertemuan 6 (09-10-2024)
Akhirnya saya memasuki materi baru yaitu tentang komparasi dan juga bilangan boolean (true/false) setelah pertemuan sebelumnya terpotong Dies Natalis.

seperti yang di atas pada pertemuan kali ini kita membahas bilangan komparasi yaitu :
- \> : Lebih besar dari
- < : Lebih kecil dari
- \>= : Lebih besar sama dengan dari
- <= : Lebih kecil sama dengan dari
- == : Sama dengan
- != : Tidak sama dengan

dan juga saya di minta untuk mencoba latihan tentang bilangan komparasi seperti ini :

[pertemuan 6.py](https://github.com/Kafatah/Jurnal-Informatika/blob/329e8bb48be7d19927fa75a08b5dd98b618d2eba/pertemuan%206.py)

---
# Pertemuan 7 (15-10-2024)
Pada pertemuan hari ini Bu Dilla memberikan kita sebuah tugas yaitu mempelajari tentang bilangan komparasi lalu kita di minta untuk menjelaskan di depan berpasangan 2 orang. Sebenernya sih sama kayak minggu lalu yaaa

---
# Pertemuan 8 (16-10-2024)
Pada pertemuan kali ini saya tidak bisa hadir untuk pelajaran kali ini dikarenakan saya mengikuti GId (sama kayak raihan :])

Tapi pada pertemuan kali ini Bu Dilla memberikan kita materi kepada teman-teman saya di kelas tentang fungsi if (tapi saya nya tidak hadir)

---
# Pertemuan 9 (22-10-2024)

Pada pertemuan kali ini Bu Dilla memberikan materi baru ke kelas, yaitu materi tentang fungsi *if & else*

nah jadi fungsi ini tuh cara kerjanya adalah pertama mengecek kondisi dari suatu permisalan. Kalau sesuai maka akan jadi *True*, tapi kalau tidak sesuai maka akan menjadi *False* atau dalam fungsi *else*

Bu Dilla juga memberikan ke pada kita latihan soal, ini adalah codingannya :

[Pertemuan 9.py](https://github.com/Kafatah/Jurnal-Informatika/blob/main/pertemuan%209.py)

Contoh codingan :
``` python
gangen = int(input('masukan angka :'))
if gangen % 2 == 0 :
      print ('Genap')
else :
     print ('Ganjil')  

print ('===Akhir dari program===')
```

---
# Pertemuan 10 (23-10-2024)

Pada pertemuan kali kita di minta Bu Dilla untuk maju ke depan dan menjelaskan soal dari latihan kemarin, dan juga membuat flowchartnya di papan tulis

``` python
umur = int(input('masukan umur :'))
if umur >= 17 :
    print ('Selamat kamu sudah cukup umur!!!')
else :
    print('Sayang sekali kamu belum cukup umur!!!, PERGI SANA')
    
print ('===Akhir dari program===')
```

![WhatsApp Image 2024-10-23 at 08 02 56_a0332f5b](https://github.com/user-attachments/assets/3932d3d1-f0eb-47fa-926b-d11294288945)


---
# Pertemuan 11 (29-10-2024)
Pada pertemuan kali ini Bu Dilla mengajarkan kepada kita materi lanjutan dari fungsi *if&else* yaitu *elif*.

Nah *Elif* atau *Else If* nah fungsi ini gunanya itu kita bisa membuat permisalan lagi setelah else. Dan juga Bu Dilla memberikan kita tugas latihan nah ini dia :
[Pertemuan 11.py](https://github.com/Kafatah/Jurnal-Informatika/blob/main/Pertemuan%2011.py)

ini salah satu contoh soalnya :
``` python
print ('INI ADALAH PROGRAM UNTUK MENGETAHUI TAHUN KABISAT')

tahun = int(input('Masukkan Tahun : '))

if tahun % 400 == 0 :
    print ('Tahun ini adalah tahun kabisat ')
elif tahun % 100 == 0 :
    print ('Tahun ini bukan tahun kabisat')
elif tahun % 4 == 0 :
    print ('Tahun ini adalah tahun kabisat')
else :
    print ('Tahun ini bukan tahun kabisat')
```

---
# Pertemuan 12 (30-10-2024)
Pada pertemuan hari ini Bu Dilla sedang berhalangan untuk hadir tapi Bu Dilla memberikan kita tugas tentang fungsi *nested if*. *nested if* itu adalah dalam fungsi *if* kita membuat fungsi *if* lagi.

contoh soal :
[Pertemuan 12.py](https://github.com/Kafatah/Jurnal-Informatika/blob/main/Pertemuan%2012.py)
``` python
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
```
===
# Pertemuan 13 (05-11-2024)

Pada pertemuan kali ini Ibu nya baru menjelaskan kepada kita tentang apa itu *nested if* di karenakan pekan lalu Ibunya berhalangan untuk masuk

Nah Ibunya juga memberi kita latihan soal lagi nihbuat persiapan kita ujian praktik pekan depan, ini soalnya :
[Pertemuan 13.py](https://github.com/Kafatah/Jurnal-Informatika/blob/main/Pertemuan%2012.py)
``` python
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
  ```
===
# Pertemuan 14 (06-11-2024)

Pada pertemuan kali ini Bu Dilla memberikan kita semua lebih banyak latihan soal untuk persiapan ujian praktik. ini dia codingannya :
[Pertemuan 14.py](https://github.com/Kafatah/Jurnal-Informatika/blob/main/Pertemuan%2014.py)
``` python
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
```
