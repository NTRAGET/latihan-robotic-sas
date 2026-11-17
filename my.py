print("hello world")

jos = "josua jacobus kore"
ipk = 3.2
umur = 19
aktif = True

# print(jos)
# print(type(jos))
# print(ipk)
# print(type(ipk))
# print(umur)
# print(type(umur))
# print(aktif)
# print(type(aktif))

# tambah_umur = 5
# umur += tambah_umur
# umur = 20 * 2
# print(umur)

# aktif = True == True
# print(aktif)

# aktif = 3 > 5
# print(aktif)

# aktif = 3 < 5
# print(aktif)
# aktif = 'A' > 'Z'
# print(aktif)


# logika = True and True
# print(logika)
# logika = True or False
# print(logika)
# logika = not True
# print(logika)

# umur += 2
# print(umur)
# umur *= 2
# print(umur)
# umur -= 2
# print(umur)
# umur /= 2
# print(umur)

# continue_program = 'y'

# while continue_program == 'y':
#     nama = input("Masukkan nama anda: ")

#     umur = int(input("Masukkan umur anda: "))
#     # print(f"Nama anda adalah: {nama} dan umur anda adalah: {umur}")
#     # print(f"Nama anda adalah: ", nama , " dan umur anda adalah:" , umur)
#     print(f"Nama anda adalah: "+ nama + " dan umur anda adalah:" + str(umur))

#     if umur >= 17:
#         print(f"anda sudah dewasa {umur}")
#     elif umur < 17 and umur >= 13:
#         print(f"anda masih dibawah umur {umur}")
#     else:
#         print(f"anda masih anak-anak {umur}")

#     continue_program = input("Apakah anda ingin melanjutkan program? (y/n): ")
    
    
# print("perulangan for")
# for i in range(1, 11):
#     umur += 1
#     print(f"umur bertambah 1 = {umur}")

# print("perulangan while")
# while umur < 30:
#     umur += 1
#     print(f"umur bertambah 1 = {umur}")
    
# for i in range(1, 10, 2):
#     print(f"nilai i = {i}")
    
    
# data_list = [1, "josua", 3.2, True]
# print(data_list[0])
# print(data_list[1])
# print(data_list[2])
# print(data_list[3])

# data_list.append("kore")
# print(data_list[4])

# data_list.remove(3.2)
# print(data_list)

# print(data_list[3])
# data_list.pop(3)
# print(data_list)

# print("setelah diubah")
# for i, index in enumerate(data_list):
#     print(f"Index: {i}, Value: {index}")
    
# data_tuple = (1, "josua", 3.2, 3.2, True)
# print(data_tuple.count(3.2))
# print(data_tuple.index("josua"))
# print(len(data_tuple))

# data_sets = {1, "kore", 3.2, True}
# data_sets1 = {2, "natal", 3.5, False}
# print(*data_sets)
# data_sets.add("josua")
# print(*data_sets)
# data_sets.discard(3.2)
# print(*data_sets)
# data_sets = data_sets.union(data_sets1)
# print(*data_sets)

# data_dict = {
#     "nama": "josua",
#     "umur": 19,
#     "jurusan": "teknik Elektro",
#     "angkatas": 25,
#     "is_active": True
# }
# print(type(data_dict["is_active"]))
# print(data_dict.get("nama"))
# print(data_dict.values())
# print(data_dict.keys())
# data_dict.update(nama = "kore", umur = 20)
# print(data_dict.values())


# def hitung_luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     return luas



# panjang = int(input("Masukkan panjang persegi panjang: "))
# lebar = int(input("Masukkan lebar persegi panjang: "))
# print(hitung_luas_persegi_panjang(panjang, lebar))

# def balik_list(list):
#     print(list[4])
#     print(list[3])
#     print(list[2])
#     print(list[1])
#     print(list[0])
    
def balik_list(list):
    for i in list:
        return list[::-1]

list_angka = [x for x in range(1,8)]
print(balik_list(list_angka))