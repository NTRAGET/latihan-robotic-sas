# print("Hello World")

# umur = 20
# ipk = 3.85
# nama = "Rahfi"
# aktif = True

# print(type(umur))
# print(type(ipk))
# print(type(nama))
# print(type(aktif))


# tambah_umur = 5
# # umur_baru = umur + tambah_umur
# umur_baru = umur - tambah_umur
# umur_baru = 20 + 2 # tambah
# umur_baru = 20 - 2 # kurang
# umur_baru = 20 * 2 # kali
# umur_baru = 20 / 2 # bagi
# umur_baru = 20 % 2 # sisa bagi
# print(umur_baru)



# apakah_aktif = True == True
# print(apakah_aktif)


# apakah_aktif = True != True
# print(apakah_aktif)

# apakah_aktif = 3 > 5
# apakah_aktif = 3 < 5
# print(apakah_aktif)

# apa_hasilnya = "A" < "B"
# print(apa_hasilnya) 

# hasil_logika = True and True
# print(hasil_logika)
# hasil_logika = True and False
# print(hasil_logika)
# hasil_logika = True or False
# print(hasil_logika)
# hasil_logika = not True
# print(hasil_logika)


# umur_baru = umur_baru + 2
# umur_baru += 2
# print(umur_baru)
# umur_baru = umur_baru - 2
# umur_baru -= 2
# print(umur_baru)
# umur_baru = umur_baru * 2
# umur_baru *= 2
# print(umur_baru)
# umur_baru = umur_baru / 2
# umur_baru /= 2
# print(umur_baru)

# nama = input("Masukkan nama: ")
# print(nama) 

# umur = input("Masukkan umur: ")
# print(umur)

# if umur > 20:
#     print(f"Hallo {nama}, umur kamu {umur} ")
#     print("Hallo", nama, "umur anda", umur)
#     print("Hallo" + nama + "umur anda" + str(umur))
# elif umur == 20:
#     print(f"umur anda {umur} == 20")

# else:
#     print(f"umur anda {umur} <= 20")
# umur = 20
# for i in range(1, 6):
#     umur += 1
#     print("umur anda bertambah 1, jadi: ", umur)

# while umur < 25:
#     umur += 1
#     print("umur anda bertambah 1, jadi: ", umur)

# for i in range(1, 10, 2):
#     print(i)

data_list = [1, 3, "Rahfi", 3.9, True]
# print(data_list[0])
# print(data_list[1])
# print(data_list[2])
# print(data_list[3])
# print(data_list[4])

# data_list.append(7)
# print(data_list[5])
# data_list.remove(7)
# print(data_list[5])

for i in range (0,5):
    print(data_list)

print("print baru")
for index, data in enumerate(data_list):
    print(index, data)


data_tuple = ("Rahfi", 43, 43, True)
print(data_tuple.count(43))
print(data_tuple.index(43))
print(len(data_tuple))

data_sets = {1, 2, 3, 4, 5}
print(*data_sets)
data_sets.add(6)
print(*data_sets)
data_sets.discard(1)
print(*data_sets)
data_sets = data_sets.union(data_sets)
print(*data_sets)

data_dict = {
    "nama" : "Rahfi",
    "umur" : 19,
    "jurusan" : "D3 Teknologi Komputer",
    "angkatan" : 26,
    "is_active" : True
}

print(data_dict.get("nama"))
print(data_dict.values())
print(data_dict.keys())
data_dict.update(nama = "Al'araaf", umur = 21)

def luas(p, l):
    return p * l

hasil_luas = luas(p=7, l=4) 
print(hasil_luas)

def balik_list(l):
    l.reverse()
    return l

list_asli = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_baru = balik_list(l=list_asli)
print(*list_baru)

list_baru = [1,1,2,2,3,3,4,4,5,5]
list_baru = list(set(list_baru))
print(*list_baru)














