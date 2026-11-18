
# ==================================================
# 1. TIPE DATA
# ==================================================
# Tipe data menentukan jenis nilai yang disimpan
# dalam sebuah variabel.

# umur = 20
# ipk = 3.14
# nama = "lale"
# aktif = True

# print(type(umur))
# print(type(ipk))
# print(type(nama))
# print(type(aktif))


# ==================================================
# 2. OPERATOR
# ==================================================
# Operator digunakan untuk melakukan operasi
# matematika, perbandingan, logika, dan assignment.

# Aritmatika
# tambahUmur = 5
# umurBaru = umur + tambahUmur
# umurBaru = umur - tambahUmur
# umurBaru = umur * tambahUmur
# umurBaru = umur / tambahUmur
# umurBaru = umur % tambahUmur
# print(umurBaru)

# Perbandingan
# apakahAktif = True == True
# print(apakahAktif)

# apakahAktif = True != True
# print(apakahAktif)

# apakahAktif = 3 > 5
# print(apakahAktif)

# apakahAktif = 2 > 1
# print(apakahAktif)

# apakahAktif = "A" > "B"
# print(apakahAktif)

# apakahAktif = "B" < "C"
# print(apakahAktif)

# Logika
# hasilLogika = True and True
# print(hasilLogika)

# hasilLogika = True and False
# print(hasilLogika)

# hasilLogika = True or False
# print(hasilLogika)

# hasilLogika = not True
# print(hasilLogika)

# Assignment
# umurBaru = tambahUmur + 2
# umurBaru += 2
# print(umurBaru)

umur = 20
tambahUmur = 5

umurBaru = umur - tambahUmur
umurBaru -= 2
print(umurBaru)

umurBaru = umur * tambahUmur
umurBaru *= 2
print(umurBaru)

umurBaru = umur / tambahUmur
umurBaru /= 2
# print(umurBaru)

# umurBaru = umur % tambahUmur
# umurBaru =+ 2
# print(umurBaru)


# ==================================================
# 3. INPUT DAN OUTPUT
# ==================================================
# Input menerima data dari pengguna, sedangkan
# output menampilkan data ke layar.

# nama = input("Masukkan Nama Anda: ")
# print(nama)

# umur = int(input("Masukkan umur anda: "))
# print(umur)

# print(f"Halo {nama}, umur anda {umur}")
# print("Halo", nama, "umur anda", umur)
# print("Halo " + nama + " umur anda " + str(umur))


# ==================================================
# 4. PERCABANGAN
# ==================================================
# Percabangan menjalankan perintah berdasarkan
# kondisi menggunakan if, elif, dan else.

# if umur > 20:
#     print(f"Halo {nama}, umur anda {umur}")
#     print("Halo", nama, "umur anda", umur)
#     print("Halo " + nama + " umur anda " + str(umur))
# elif umur == 20:
#     print("hahay")
# else:
#     print(f"umur anda {umur} <= 20")


# ==================================================
# 5. PERULANGAN
# ==================================================
# Perulangan digunakan untuk menjalankan kode
# secara berulang menggunakan for dan while.

# umur = 20
# for i in range(1, 6):
#     umur += 1
#     print("umur anda bertambah 1 yey, jadi :", umur)

# umur = 20
# while umur < 25:
#     umur += 1
#     print("Umur lu nambah 1, jadinye :", umur)

# for i in range(1, 10, 2):
#     print(i)


# ==================================================
# 6. LIST
# ==================================================
# List menyimpan beberapa data dalam satu variabel
# dan elemennya dapat diubah.

data_list = [1, 7, 20, "Lale", 3.5, True, 7]

print(data_list[0])
print(data_list[1])
print(data_list[2])
print(data_list[3])
print(data_list[4])

# Menambah list
# append() menambahkan elemen ke akhir list.

# data_list.append(7)
# print(data_list[5])

# Menghapus element list
# remove() menghapus elemen berdasarkan nilai.

# data_list.remove(7)
# print(data_list[5])

# Menghapus index
# pop() menghapus elemen berdasarkan index.

# data_list.pop(4)
# print(data_list[4])

# Perulangan list
print("Sebelum dihapus")
for i in range(0, len(data_list)):
    print(i)

print("Sesudah dihapus")
for i in range(0, len(data_list)):
    print(i)

data_list.remove(7)

# Menampilkan elemen list menggunakan for
print("print baru")
for data in data_list:
    print(data)

# Menampilkan seluruh elemen menggunakan unpacking
print("print baru 2")
print(*data_list)

# enumerate() menampilkan index dan nilai elemen
print("print baru")
for index, data in enumerate(data_list):
    print(index, data)


# ==================================================
# 7. TUPLE
# ==================================================
# Tuple menyimpan beberapa data yang elemennya
# tidak dapat diubah.

data_tuple = ("lale", 43, 43, 43, True)

print(data_tuple.count(43))
print(data_tuple.index(43))
print(len(data_tuple))


# ==================================================
# 8. SET
# ==================================================
# Set menyimpan data unik tanpa elemen duplikat
# dan tidak memiliki index.

data_sets = {1, 2, 3, 4, 5}
data_sets2 = {8, 9}

print(*data_sets)

data_sets.add(6)
print(*data_sets)

data_sets.discard(1)
print(*data_sets)

data_sets = data_sets.union(data_sets2)
print(*data_sets)


# ==================================================
# 9. DICTIONARY
# ==================================================
# Dictionary menyimpan data dalam bentuk pasangan
# key dan value.

data_dict = {
    "nama": "Lale",
    "umur": 19,
    "jurusan": "D3TK",
    "angkatan": 50,
    "is_active": True,
}

print(data_dict.get("nama"))
print(data_dict.values())
print(data_dict.keys())

data_dict.update(nama="laleAja", umur=30)

# Bikin key baru
data_dict["alamat"] = "sukapura"
print(data_dict)


# ==================================================
# 10. FUNCTION
# ==================================================
# Function merupakan blok kode yang dibuat untuk
# menjalankan tugas tertentu dan dapat digunakan kembali.

# Function menghitung luas persegi panjang
def luas(p, l):
    return p * l


hasil_luas = luas(8, 3)
print(hasil_luas)


# Function membalik sebuah list
def balik_list(data):
    return data[::-1]


data = [1, 2, 3]
print(*data)

list_asli = [x for x in range(100)]
print(*list_asli)

list_baru = balik_list(list_asli)
print(*list_baru)


# Menghilangkan data duplikat pada list
list_baru = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

print(*list_baru)

list_baru = list(set(list_baru))
print(*list_baru)
