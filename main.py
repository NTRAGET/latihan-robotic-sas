# nama = input("Siapa nama lo?")
# umur = int(input("Masukin umur lo: "))

# if umur < 20:
#     print(f"Ganteng banget lu {nama}, jadi umur lo belom 20Raka")

# umur = 20
# for i in range(1, 6):
#     umur += 1
#     print("Umur anda bertambah 1, jadi: ", umur)

# print("=" * 12)
# print("Perulangan while")
# print("=" * 12)
# umur = 20
# while umur < 25:
#     umur += 1
#     print("Umur anda bertambah 1, jadi: ", umur)

# for i in range (1, 10, 2):
#     print(i)

# List
# data_list = [1, 3, "Raka", 3.9, True]
# # print(data_list[0])
# # print(data_list[1])
# # print(data_list[2])
# # print(data_list[3])
# # print(data_list[4])

# # data_list.append(7)
# # print(data_list[5])

# # data_list.remove(7)
# # data_list.pop(4)

# for i in range (0, 5):
#     print(data_list)

# for index, data in enumerate (data_list):
#     print(index, data)

# print(*data_list)

# Tuple
# data_tuple = ("Raka", 19, 19, True)
# print(data_tuple.count(19))
# print(data_tuple.index(True))
# print(len(data_tuple))

# Set
# data_set = {1, 2, 3, 4, 5}
# data_set2 = {1, 6, 7, 8, 9, 10}
# print(data_set)
# data_set.add(6)
# print(data_set)
# data_set.discard(1)
# print(data_set)
# data_set = data_set.union(data_set2)
# print(data_set)

# Dictionary
# data_dict = {
#     "nama" : "Raka",
#     "umur" : 19,
#     "jurusan" : "S1 Sistem Informasi",
#     "angkatan" : 26,
#     "is.active" : True,
# }

# print(data_dict.get("nama"))
# print(data_dict.values())
# print(data_dict.keys())
# data_dict.update(umur=20)
# print(data_dict.get("umur"))

# data_dict = {"alamat" : "asrama"}

# print(data_dict.get("alamat"))

# def luas(p, l):
#     return p * l

# hasil_luas = luas(8, 3)
# print(hasil_luas)

def balik_list(l):
    return l

list_asli = [x for x in range (100)]
#print(*list_asli)
list_baru = balik_list(list_asli)
#print(*list_baru)

#print(list_asli[-1])

list_baru = [1,1,2,2,3,3,4,4,5,5]
list_asli = list(set(list_baru))
print(*list_asli)