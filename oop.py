# class Mobil :
#     def __init__(self, merk, warna, tahun,) : 
#         self.merk = merk #attributs
#         self.warna = warna
#         self.tahun = tahun

#     def tampil_info(self): #method
#         print (f"mobil ini merknya adalah {self.merk}, berwarna {self.warna}, tahunnya {self.tahun}")

# Mobil1 = Mobil ("Avanza","Putih","1945")
# Mobil2 = Mobil ("Bajai", "Merah", "1019")
# Mobil3 = Mobil ("Toyota", "Pink", "1919") 

# Mobil1.tampil_info()
# Mobil2.tampil_info()
# Mobil3.tampil_info()

# #enkapsulasi
# class Manusia :
#     def __init__(self, umur):
#         self.__umur = umur

#     def ulangtahun (self, tambahUmur):
#         self.__umur += tambahUmur

#     def tampilumur (self):
#         print(f"Umur setelah ulang tahun {self.__umur} tahun")

# lale = Manusia (99)
# lale.ulangtahun(1)
# lale.tampilumur()

#enheritance
# class Film:
#     def __init__(self, judul):
#         self.judul = judul

#     def tampilJudul (self):
#         print(f"Judul film adalah {self.judul}")

# class DetailFilm(Film):
#     def __init__ (self, judul, rating, batasumur):
#         super().__init__(judul)
#         self.rating = rating
#         self.batasumur = batasumur

#     def tampilDetail(self):
#         print(f"Judul Filmnya adalah {self.judul}, dengan rating {self.rating}, dengan batas umur {self.batasumur} tahun")


# film1 = DetailFilm("godzilla", "9", "1")
# film2 = DetailFilm("monyet", "10", "5")
# film3 = DetailFilm("lale", "8", "99")

# film1.tampilDetail()
# film2.tampilDetail()
# film3.tampilDetail()

#Polymorphism
# class katakata :
#     def pesan(self):
#         return "ini lale"

# class katakatakata:
#     def pesan(self):
#         return "hahay"

# def kirimKata(bunyi):
#     print(bunyi.pesan())

# kirimKata(katakata())
# kirimKata(katakatakata())

#abstraction
# from abc import ABC, abstractmethod

# class kendaraan(ABC):
#     @abstractmethod
#     def startmobil (self):
#         pass

# class MobilListrik(kendaraan):
#     def startmobil(self):
#         print(f"Mobil Menyala")

# hahay = MobilListrik()
# hahay.startmobil()

# #instance Method
# class Mobil:
#     def __init__ (self, merk):
#         self.merk = merk

#     def tampilMerk (self):
#         print("Merk Mobil : ", self.merk)

# mobil1 = Mobil ("Porche")
# mobil1.tampilMerk()

#class Method
# class Motor :
#     jenis: "Sport"

#     @classmethod 
#     def UbahJenisMotor(cls, jenisBaru ):
#         cls.jenis = jenisBaru

# Motor.UbahJenisMotor("mio anggora")
# print(Motor.jenis)

#static method
# class Motor:
#     @staticmethod
#     def knalpot():
#         print("preketek preketek")

# Motor.knalpot()

#special method
class sepatu:
    def __init__ (self, merk, harga):
        self.merk = merk
        self.harga = harga

    def __str__ (self):
        return f"{self.merk}, Rp{self.harga}" 

    def __add__(self, tambah):
        return self.harga + tambah.harga

sepatu1 = sepatu("adibas", 200)
sepatu2 = sepatu("adidi", 123)

print (sepatu1)
print (sepatu1 + sepatu2)

        