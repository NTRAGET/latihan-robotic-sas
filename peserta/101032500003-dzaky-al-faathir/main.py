print("Hello, World!")

# deklarasi variable
umur = 20
ipk = 3.9
nama = "Dzaky"
aktif = True
print("\n")

# print tipe variable
print(type(umur))
print(type(ipk))
print(type(nama))
print(type(aktif))
print("\n")

# operasi aritmatika
tambah_umur = 5
umur_barut = umur + tambah_umur #tambah
umur_baruk = umur - tambah_umur #kurang
umur_barikl = umur * tambah_umur #kali
umur_barub = umur / tambah_umur #bagi
print("\n")

# print hasil operasi aritmatika
print("Umur baru adalah:", umur_barut)
print("Umur baru adalah:", umur_baruk)
print("Umur baru adalah:", umur_barikl)
print("Umur baru adalah:", umur_barub)
print("\n")

# operasi logika
apakah_aktif = True == True
print("Apakah aktif:", apakah_aktif)
apakah_aktif = True != False
print("Apakah aktif:", apakah_aktif)
apakah_aktif = True or False
print("Apakah aktif:", apakah_aktif)
apakah_aktif = 3 < 5
print("Apakah aktif:", apakah_aktif)
apa_hasilnya = 'A' < 'B'
print("Apakah aktif:", apa_hasilnya)
hasil_logika = True and True
print("Hasil logika:", hasil_logika)
hasil_logika = True and False
print("Hasil logika:", hasil_logika)
hasil_logika = True or False
print("Hasil logika:", hasil_logika)
hasil_logika = False or False
print("Hasil logika:", hasil_logika)
hasil_logika = not True
print("Hasil logika:", hasil_logika)
print("\n")

# operasi penugasan
umur_barut += tambah_umur #tambah
umur_baruk -= tambah_umur #kurang
umur_barikl *= tambah_umur #kali
umur_barub /= tambah_umur #bagi
print("\n")

# print hasil operasi penugasan
print("Umur baru adalah:", umur_barut)
print("Umur baru adalah:", umur_baruk)
print("Umur baru adalah:", umur_barikl)
print("Umur baru adalah:", umur_barub)
print("\n")

# input user dan print
namain = input("Masukkan nama Anda: ")
umurin = int(input("Masukkan umur Anda: "))
print(f"Nama Anda adalah {namain} dan umur Anda adalah {umurin}")
print("Nama Anda adalah " + namain + " dan umur Anda adalah " + str(umurin))
print("\n")

# percabangan if else
if umurin >= 20:
    print("Anda sudah dewasa, berumur minimal 20 tahun")
elif umurin == 20:
    print("Anda berumur tepat 20 tahun")
elif umurin < 20:
    print("Anda masih remaja, berumur kurang dari 20 tahun")
else:
    print("Umur Anda tidak valid")
print("\n")

#perulangan for
print("Perulangan for")
umur = 20
for i in range(1, 6):
    print("Perulangan ke-"+str(i))
    umur += 1
    print("Umur Anda sekarang adalah " + str(umurin))
print("\n")

#perulangan while
print("Perulangan while")
umur = 20
while umur <25:
    print("Umur Anda sekarang adalah " + str(umur))
    umur += 1
print("\n")

#perulangan for lewat 2
print("Perulangan for lewat 2")
umur = 20
for i in range(1, 10, 2):
    print("Perulangan ke-"+str(i))
    umur += 1
    print("Umur Anda sekarang adalah " + str(umur))
print("\n")

#List
data_list = [1, 3, "Dzaky", 3.9, True]
print("Data list:", data_list)
print(data_list[0])
print(data_list[1])
print(data_list[2])
print(data_list[3])
print(data_list[4])

#menambahkan data ke list
data_list.append("7") 
print("Data list setelah ditambahkan:", data_list)

#menghapus data 3 dari list
data_list.remove(3) 
print("Data list setelah dihapus:", data_list) 

#menghapus elemen ke 3 dari list
data_list.pop(2)
print("Data list setelah dihapus:", data_list)

for index, data in enumerate(data_list):
    print(index, data)
print(*data_list)
print("\n")

#tuple
print("Tuple")
data_tuple = (1, 3, "Dzaky", 3.9, True)
print("Data tuple:", data_tuple)
print(data_tuple.count(3))
print(data_tuple.index("Dzaky"))
print(len(data_tuple))

#set
print("Set")
data_set = {1, 1, 3, 4, 5}
data_set2 = {6, 7, 8, 9}
print(data_set)
data_set.add(10)
print(data_set)
data_set.discard(1)
print(data_set)
data_set = data_set.union(data_set2)
print(*data_set)
print("\n")

#dictionary
print("Dictionary")
data_dict = {
    "nama": "Dzaky",
    "umur": 19,
    "jurusan": "S1 Teknik Komputer",
    "angkatan": 2025,
    "is_active": True
}
print(data_dict)
print(data_dict["nama"])
print(data_dict.values())
print(data_dict.keys())
data_dict.update(nama="aky")
print(data_dict)
data_dict["alamat"] = "Cikoneng"
print(data_dict)
print("\n")

#function
print("Function")
def luasp (p, l):
    return p * l

print("Luas : ", luasp(5, 3))

#membalikkan list
listb = [x for x in range(100)]
def balik_list(data):
    return data[::-1]

list_baru = balik_list(listb)
print("List baru : ", list_baru)
