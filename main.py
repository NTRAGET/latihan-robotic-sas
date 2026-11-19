#  print("Hello World")
#  umur = 20
#  ipk = 3.85
#  nama = "budi"
#  aktif = True
#  print(type(umur))
#  print(type(ipk))
#  print(type(nama))
#  print(type(aktif))

#  tambah_umur = 5
#  umur_baru = umur + tambah_umur
#  umur_baru = umur - tambah_umur
# umur_baru = 20 + 2
# print(umur_baru)
# umur_baru = 20 - 2
# print(umur_baru)
# umur_baru = 20 * 2
# print(umur_baru)
# umur_baru = 20 / 2
# print(umur_baru)
# umur_baru = 20 % 2
# print(umur_baru)

# apakah_aktif=True == True
# print(apakah_aktif)
# apakah_aktif=True != True
# print(apakah_aktif)
# apakah_aktif= 3>5
# print(apakah_aktif)
# apakah_aktif=3<5
# print(apakah_aktif)
# apakah_aktif= 3>=5
# print(apakah_aktif)
# apakah_aktif=3<=5
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

# umur_baru = umur_baru / 2
# umur_baru /= 2
# print(umur_baru)

# umur_baru = umur_baru * 2
# umur_baru *= 2
# print(umur_baru)

# nama = input("Masukkan nama anda: ")
# print(nama)

# umur = int(input("Masukkan umur anda: "))
# print(umur)


# print(type(nama))
# print(type(umur))

# if umur > 20:
#     print(f"halo {nama}, umur anda {umur}")
#     print(f"halo",nama, "umur anda",umur)
#     print("halo " + nama + ", umur anda " + str(umur))
# elif umur == 20:
#     print(f"Umur anda {umur}, pas 20")
# else:
    # print(f"Umur anda {umur}, <= 20")
# print("perulangan for")
# umur = 20
# for i in range(1,6):
#     umur += 1
#     print("umur anda bertambah 1, menjadi", umur)

# print("perulangan while")
# umur = 20
# while umur < 25:
#     umur += 1
#     print("umur anda bertambah 1, menjadi", umur)

# for i in range(1, 10, 2):
#     print(i)

# data_list = [1,3, "altap solat", 3.9, True]
# print(data_list[0])
# print(data_list[1])
# print(data_list[2])
# print(data_list[3])
# print(data_list[4])

# data_list.append(7)
# print(data_list[5])
# #Menghapus elemen
# data_list.remove(7)
# #print(data_list[5])

# #print(data_list[4])
# data_list.pop(4)


# data_list = [1,3,7, "altap solat", 3.9, True,7]

# print("sebelum dihapus")
# for i in range(0,7):
#     print(data_list[i])

# data_list.remove(7)

# print("sesudah dihapus")
# for i in range(0,6):
#     print(data_list[i])

# for index, data in enumerate(data_list):
#     print(index,data)


# data_tuple = ("AltapSolat", 43, 43, True)
# print(data_tuple.count(43))
# print(data_tuple.index(43))
# print(len(data_tuple))

# data_sets = {1, 2, 3, 4, 5,}
# data_sets2 = {8,9}
# print(*data_sets)
# data_sets.add(6)
# print(*data_sets)
# data_sets.discard(1)
# print(*data_sets)
# data_sets = data_sets.union(data_sets2)
# print(*data_sets)

# data_dict = {
#     "nama": "Altap Solat",
#     "umur": 20,
#     "Jurusan": "S1 Teknik Komputer",
#     "angkatan": 25,
#     "is_active": True,
# }

# print(data_dict.get("nama"))
# print(data_dict.values())
# print(data_dict.keys())
# data_dict.update(nama="Ridho", umur=21)
# data_dict["alamat"] = "Sukabirus"
# print(data_dict.values())

# def luas(p, l):
#     return p * l

# hasil_luas = luas(10, 5)
# print(hasil_luas)

def balik_list(l):
    return l[::-1]


list_asli = [x for x in range(20)]
print(*list_asli)
list_baru = balik_list(list_asli)
print(*list_baru)

print(list_asli[-5])

list_baru = [1,1,2,2,3,3,4,4,5,5]
print(*list_baru)
list_baru = list(set(list_baru))
print(*list_baru)