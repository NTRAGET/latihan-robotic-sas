# # # print("hello world")

# # # umur = 20
# # # ipk = 3.85
# # # nama = "nopal"
# # # nama2 = "alex"
# # # aktif = True

# # # print(type(umur))
# # # print(type(ipk))
# # # print(type(nama))
# # # print(type(aktif))

# # # tambah_umur= 5
# # # umurBaru= umur + tambah_umur
# # # # print(umurBaru)

# # # # apakahAktif = True == True
# # # # print(apakahAktif)

# # # # apakahAktif = 3 > 5
# # # # print(apakahAktif)

# # # # apakahAktif = 3 <= 3
# # # # print(apakahAktif)

# # # # apakahAktif = True == True
# # # # print(apakahAktif)

# # # # hasil_logika = True and True
# # # # print(hasil_logika)

# # # # hasil_logika = True and False
# # # # print(hasil_logika)

# # # # hasil_logika = True or False
# # # # print(hasil_logika)

# # # # hasil_logika = not True
# # # # print(hasil_logika)

# # # nama = input("Masukkan nama anda: ")
# # # print(f"halo {nama}")

# # # umur = int(input("Masukkan umur anda: "))
# # # print(umur)

# # # # print(f"halo {nama}, umur anda {umur}")

# # # if umur > 20:
# # #     print(f"halo {nama}, umur anda {umur}")
# # # elif umur == 20:
# # #     print("umur anda 20")
# # # else:
# # #     print("umur dibawah 20")

# # # for i in range(1,6):
# # #     umur += 1
# # #     print("umur anda bertambah 1, Jadi: ", umur)

# # umur = 20
# # while umur <25:
# #     umur += 1
# #     print("umur anda bertambah 1, Jadi: ", umur)

# # print()
# # for i in range(1,10,2):
# #     print(i)

# # List
# # data_list = [1,3, "Yudha", 3.9, True]
# # print(data_list[0])
# # print(data_list[1])
# # print(data_list[2])
# # print(data_list[3])
# # print(data_list[4])

# # data_list.append(7)
# # print(data_list[5])

# # data_list.pop(3.9)
# # print(data_list[4])

# # print("print baru")
# # for index, data in enumerate(data_list):
# #     print(index, data)

# # print(data_list)

# data_tuple= ("alex", 12,12, True)

# print("tuple")
# # for index, data in enumerate(data_tuple):
# #     print(index, data)

# # print(data_tuple)

# print(data_tuple.count(12))
# print(data_tuple.index(12))
# print(len(data_tuple))

# data_set={1,2,3,4,5}
# data_set2={8,9}
# print(*data_set)
# data_set.add(0)
# print(*data_set)
# data_set.discard(0)
# print(*data_set)
# data_set = data_set.union(data_set2)
# print(*data_set)

# data_dict = {
#     "nama" : "alex",
#     "umur" : 20,
#     "jurusan" : "S1 Elektro",
#     "angkatan" : 25,
#     "is_active" : True,
# }

# print (data_dict.get("nama"))
# print (data_dict.values())
# print (data_dict.keys())
# data_dict.update(nama = "nopal")

# data_dict["alamat"] = "asrama"

# def luas(p,l):
#     return(p * l)

# # print (luas(8, 3))

# hasil_luas = luas(8,3)
# print(hasil_luas)

from ast import While


l = [4,3,2,1]
def balik_list(l):
    return l[::-1]

list_baru = balik_list(l)
print(*list_baru)