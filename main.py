print("hello world")

umur = 20
ipk: float = 3.5
nama = "Ivan"
aktif = True
print(type(umur))
print(type(ipk))
print(type(nama))
print(type(aktif))

tambah_umur = 5
umur_baru = umur +2
umur_baru += 2
print(umur_baru)

umur_baru = umur_baru -2
umur_baru -= 2
print(umur_baru)

umur_baru = umur_baru *2
umur_baru *= 2
print(umur_baru)

umur_baru = umur_baru /2
umur_baru /= 2
print(umur_baru)

umur_baru = umur_baru %2
umur_baru %= 2
print(umur_baru)

umur_baru = 20 + 2 
umur_baru = 20 - 2
umur_baru = 20 * 2
umur_baru = 20 / 2
umur_baru = 20 % 2
print(umur_baru)

apakah_aktif = True == True
print(apakah_aktif)

apakah_aktif = 3 < 5
print(apakah_aktif)

apa_hasilnya = "A" < "B"
print(apa_hasilnya)

hasil_logika = True and True
print(hasil_logika)
hasil_logika = True and False
print(hasil_logika)
hasil_logika = True or False
print(hasil_logika)
hasil_logika = not True
print(hasil_logika)

nama = input("Masukkan nama anda: ")
print(nama)

umur = int(input("Masukkan umur anda: "))
print(umur)

print(type(nama))
print(type(umur))

if umur > 20:
    print(f"Halo {nama}, umur anda {umur}")
    print("Halo ", nama, ", umur anda ", umur)
    print("Halo " + nama + ", umur anda " + str(umur))
elif umur == 20:
    print(f"umur anda {umur} pas 20")

else:
    print(f"umur anda {umur} <= 20")

umur = 20
for i in range (1, 6):
    umur += 1
    print (f"Umur anda bertambah 1, jadi: {umur}")

umur = 20
while umur < 20:
    umur += 1
    print (f"Umur anda bertambah 1, jadi: {umur}")

for i in range(1, 10, 2):
    print(i)

#List
data_list = [1, 3, "Ivan", 3.9, True]
print(data_list[0])
print(data_list[1])
print(data_list[2])
print(data_list[3])
print(data_list[4])

data_list.append("7")
print(data_list[5])
data_list.remove("7")
print(data_list[5])

data_list.pop(4)
print(data_list[4])

for i in range (0, 7):
    print(data_list[i])

data_list.remove(7)

print("sudah dihapus")
for i in range (0, 6):
    print(data_list[i])

print("print baru")
for index, data in enumerate(data_list):
    print(index, data)

print("print baru 2")
for index, data in enumerate(data_list):
    print(index, data)

#Tuple

data_tuple = ("Ivan",43,43, True)
print(data_tuple.count(43))
print(data_tuple.index(43))
print(len(data_tuple))

data_sets = {1, 2, 3, 4, 5}
data_sets = {6, 9}
print(data_sets)
data_sets.add(6)
print(data_sets)
data_sets.add(1)
print(data_sets)
data_sets = data_sets.union(data_sets)
print(data_sets)

data_dict = {
    "nama": "Ivan",
    "umur": 20,
    "jurusan": "Informatika",
    "angkatan": 2026,
    "ipk": 4.0,
    "is_active": True
}

print(data_dict.get("nama"))
print(data_dict.values())
print(data_dict.keys())    
print(data_dict.update({"nama": "Ivan", "umur": 20}))

data_dict["alamat"] = "Asrama"

def Luas(p, l):
    return p * l

luas = Luas(8, 3)
print(luas)

data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_list.reverse()
print(data_list)


def balik_list(l):
    return l[::-1]

list_asli = [x for x in range(100)]
list_baru = balik_list(list_asli)
print(list_baru)

print(list_asli[-1])

list_baru = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(list_baru)
list_baru = list(set(list_baru))
print(list_baru)









