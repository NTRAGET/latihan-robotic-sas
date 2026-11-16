#print("hello mamank")

# umur = 30
# ipk = 3.72
# nama = "sapee"
# nama = 'sapee'
# aktif = True

#print(type(umur))
#print(type(ipk))
#print(type(nama))
#print(type(aktif))

#tambah_umur = 5
#umur_baru = umur + tambah_umur
#umur_baru = umur - tambah_umur
#umur_baru = 20 + 2 #tambah
#print(umur_baru)
#umur_baru = 20 - 2 #kurang
#print(umur_baru)
#umur_baru = 20 * 2 #kali
#print(umur_baru)
#umur_baru = 20 / 2 #bagi
#print(umur_baru)
#umur_baru = 20 % 2 #sisa bagi)
#print(umur_baru)

#apakah_aktif = True == True
#print(apakah_aktif)

#apakah_aktif = True != True
#print(apakah_aktif)

#apakah_aktif = 3>5
#print(apakah_aktif)
#apakah_aktif= 3<=5
#print(apakah_aktif)


#apaan_ieu = 'A'<'B'
#print(apaan_ieu)
#apaan_ieu = 'A'>'B'
#print(apaan_ieu)


#hasil_logika = True and True
#print(hasil_logika)
#hasil_logika = True and False
#print(hasil_logika)
#hasil_logika = True or True
#print(hasil_logika)
#hasil_logika = not  True
#print(hasil_logika)

#umur_baru += 20
#print(umur_baru)

#nama = input("masukkan nama: ")
#print(nama)

#umur = int(input("Masukkan umur: "))
#print(umur)


#print(type(nama))
#print(type(umur))

#if umur > 20:
    #print(f"halo {nama}, umur {umur}")
    #print("halo", nama, "umur anda", umur)
    #print("halo " + nama + " umurnya " + str(umur))
#elif umur == 20:
    #print(f"Umur anda {umur} ngepas bet 20")
#else:
    #print(f"umur anda {umur} <= 20")
    
#umur = 10

# for i in range(1,11):
#     umur += 1
#     print("umur anda bertambah 1, jadi: ", umur)
    
# while umur < 25:
#     umur += 1
#     print("umur anda bertambah 1, jadi: ", umur)

# for i in range(1,11,3):
#     umur += 1
#     print("umur anda bertambah 1, jadi: ", umur)




#List
# data_list = [1,2,3,"abanhda", 3.9, True,2]
# print("datalist utama: ")
# print(data_list[0])
# print(data_list[1])
# print(data_list[2])
# print(data_list[3])
# print(data_list[4])
# print(data_list[5])

# # data_list.append("sapee")
# # print(data_list[6])

# # data_list.remove("sapee")
# # print(data_list[6])

# # print(data_list[4])
# # data_list.pop(4)

# print("sebelum diubah")
# for i in range(0,7):
#     print(data_list[i])
    
# data_list.remove(2)
    
# print("setelah diubah")
# for i in range(0,6):
#     print(data_list[i])
    
# print("print baru")
# for index, data in enumerate(data_list):
#     print(index, data)
 
# print("print baru 2")   
# print(*data_list)


#tuple
# data_tuple = ("bigmok",70,True,70)
# for index, data in enumerate(data_tuple):
#     print(index, data)

# print (data_tuple.count(70))
# print (data_tuple.index("bigmok"))
# print (len(data_tuple))





# data_sets = {1,2,3,4,5,6,7,8,9,10}
# data_sets2 = {5,6,7}
# print (*data_sets)
# data_sets.add(6)
# print (*data_sets)
# data_sets.discard(7)
# print (*data_sets)

# data_sets = data_sets.union(data_sets2) #gabung
# print (*data_sets)






#Dictionary
# data_dict = {
#     "nama" : "sapee",
#     "umur" : 30,
#     "jurusan" : "sastra mesin",
#     "ipk" : 3.72,
#     "aktif" : True
# }

# print (data_dict.get("nama"))
# print(data_dict.values())
# print(data_dict.keys())

# data_dict.update({"nama": "bigmok"})
# print(data_dict.get("nama"))

# data_dict["alamat"] = "Asrama"
# print(data_dict.get("alamat"))





#Function

# def luas(p,l):
#     return p*l
# print(luas(5, 3))

# def balik_list(data_ini):
#     data_baru = []
#     for i in range(len(data_ini)-1, -1, -1):
#         data_baru.append(data_ini[i])
#     return data_baru

def ngebalik_list(list):
    return list[::-1]

# data_anu = [1, 2, 3, 4, 5,6,7,8,9,10]
# print("list sebelum dibalik: ", data_anu)
# print("list setelah dibalik: ", balik_list(data_anu))


# list_asli = [x for x in range(100)]
# print(*list_asli)
# list_baru = ngebalik_list(list_asli)
# print(*list_baru)

# print (list_asli[::-1])

list_duplikat = [1,1,1,2,2,3,3,4,5,5]
list_tanpa_duplikat = list(set(list_duplikat))
print(*list_tanpa_duplikat)