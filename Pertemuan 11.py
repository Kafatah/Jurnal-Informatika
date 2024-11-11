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

print ('program untuk mengidentifikasi bentuk segitiga')

a = float(input("masukkan nilai a : "))
b = float(input("masukkan nilai b : "))
c = float(input("masukkan nilai c : "))

if a == 0 or b == 0 or c == 0 :
    print ('ini bukan segitiga')
elif a == b == c : 
    print ('Jenis segitiga ini adalah SEGITIGA SAMA SISI')
elif a == b or a == c or b == c :
    print ('Jenis segitiga ini adalah SEGITIGA SAMA KAKI')
else :
    print ('Segitiga ini adalah SEGITIGA SEMBARANG')

print ('PROGRAM INI ADALAH KALKULATOR UDH GITU AJA')

x = float (input('masukan angka pertama :'))
y = float (input('masukkan angka kedua : '))
op = str(input("masukkan operator : "))

if op == 'tambah' :
    print (x , op, y, 'adalah ', x+y)
elif op == 'kurang' :
    print (x , op, y, 'adalah ', x-y)
elif op == 'kali' :
    print (x , op, y, 'adalah ', x*y)
elif op == 'bagi' and y !=0 :
    print (x , op, y, 'adalah ', x/y)
else :
    print ('operasi tidak valid')
