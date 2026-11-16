# print("Helo World")
# #tipe data
# umur = 20
# print(type (umur))
# ipk = 3.85
# print(type(ipk))
# nama = "Budi"
# nama2 = 'Budi'
# print(type(nama))
# nilai = True or False
# print(type(nilai))
# #operator aritmetika
# tambah_umur =5
# umur_baru = umur + tambah_umur
# umur_baru1 = 20 + 2 #tambah
# umur_baru2 = 20 - 2 #kurang
# umur_baru3 = 20 * 2 #kali
# umur_baru4 = 20 / 2 #bagi
# umur_baru5 = 20 % 2 #sisa bagi / modular
# print(umur_baru)
# print(umur_baru1)
# print(umur_baru2)
# print(umur_baru3)
# print(umur_baru4)
# print(umur_baru5)
# #operator perbandingan
# apakah_aktif = True == True
# print(apakah_aktif)
# apakah_aktif3 = True != True
# print(apakah_aktif3)
# apakah_aktif1 = 3 < 5
# print(apakah_aktif1)
# apakah_aktif2 = 3 <= 5
# print(apakah_aktif2)
# apakah_aktif4 = "A" < "B"
# print(apakah_aktif4)
# apakah_aktif5 = "A" > "B"
# print(apakah_aktif5)
# #operator 
# hasil_logika = True and True
# print (hasil_logika)
# hasil_logika = True or False
# print (hasil_logika)
# hasil_logika = True and False
# print (hasil_logika)
# hasil_logika = not True
# print (hasil_logika)  

# umur_baru += 2 
# umur_baru -= 2
# umur_baru *= 2
# umur_baru /= 2
# #input
# nama = input("Masukan nama Anda: ")
# print(nama)
# umur = int (input ("Masukan umur Anda: "))
# print(umur)
# print (f "Halo {nama}, umur Anda {umur}")
# print ("Halo ", nama, " umur Anda", umur)
# print ("HAlO " + nama + " umur Anda" + str(umur))
# #percabangan
# if umur > 20:
#     print (f "Halo {nama}, umur Anda {umur}")
# elif umur == 20:
#     print(f "Umur anda {Umur} pas 20")
# else:
#     print(f "Umur Anda {umur} <= 20")
# #perulangan
# print("for")
# for i in range (1, 6):
#     print(i)
# umur = 20
# for i in range (1, 6):
#     umur += 1
#     print("umur anda bertambah 1, jadi: ", umur)
# print("while")
# umur = 20
# while umur < 25:
#     umur += 1
#     print("umur anda bertambah 1, jadi: ", umur)
# for i in range (1, 10, 4):
#     print(i)
#struktur data
#list
data_list = [1, 3, "ika", 3.9, True]
print(data_list[0])
print(data_list[1])
print(data_list[2])
print(data_list[3])
print(data_list[4])
#menambahkan list
data_list.append(7)
print(data_list[5])
#menghapus list
data_list.remove(7)
#print(data_list[5])
data_list.pop(4)
print(data_list)

for i in range (0, 6):
    print (i)
#tuple
data_tuple = ("ika", 43, True)
print (data_tuple)
data_tuple = ("ika", 43, True, 43)
print(data_tuple.count(43))
print(data_tuple.index(43))
print(len(data_tuple))
#set
data_set = {1, 2, 3, 4, 5}
data_set2 = {8, 9}
print(*data_set)
data_set.add (6)
print(*data_set)
data_set.discard(1)
print(*data_set)
data_set = data_set.union(data_set2)
print(*data_set)

data_dict = {
    "nama" : "ika",
    "umur" : 20,

}
print (data_dict.get("nama"))
print (data_dict.values())
print (data_dict.keys())
data_dict.update(nama="can", umur=19)
data_dict["alamat"] = "asrama"
print (data_dict)

def luas (p, l):
    return p * l
hasil = luas(8, 3)
print(hasil)

def balik_list(l):
    return l [::-1]
list_asli = [x for x in range (100)]
list_baru = balik_list(list_asli)
print(*list_baru)
list_baru = [1,1,2,2,3,3,4,4,5,5]
print (list_baru)
list_baru = (list(set(list_baru)))
print (list_baru)




 


