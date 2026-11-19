class Mobil: #class
    def __init__(self, merk, warna, tahun):
        self.merk = merk #atribut
        self.warna = warna
        self.tahun = tahun

    def tampilan_info(self): #method
        print (f"Mobil ini merknya adalah {self.merk}, bewarna {self.warna}, tahunnya {self.tahun}")

Mobil1 = Mobil ("Avanza", "Putih", "1945") #object
Mobil2 = Mobil ("Lambo", "Pink", "2000")

Mobil1.tampilan_info()
Mobil2.tampilan_info()

#encapsulation
class manusia:
    def __init__(self, umur,):
        self.__umur = umur #privat

    def ulangtahun(self, tambahumur):
        self.__umur += tambahumur

    def tampilumur(self):
        print (f"Umur setelah ulang tahun {self.__umur} tahun")

ika = manusia(20)
ika.ulangtahun(1)
ika.tampilumur()

#enheritance
class film:
    def __init__ (self, judul):
        self.judul = judul
    
    def tampil_judul (self):
        print (f"Judul filmnya adalah {self.judul}")

class datafilm(film):
    def __init__ (self, judul, rating, batasumur):
        super().__init__(judul)
        self.rating = rating
        self.batasumur = batasumur

    def tampil_detail(self):
        print (f"Judul filmnya adalah {self.judul} dengan rating {self.rating} batas umurnya {self.batasumur}")
    
film1 = datafilm ("Godzila", "9", "16")
film2 = datafilm ("Avengers", "10", "17")
film1.tampil_detail()
film2.tampil_detail()

#polymorphism
class katakata:
    def pesan (self):
        return "Hari ini hujan"

class katakatakata:
    def pesan (self):
        return "Selamat malam"

def kirimkatakata(bunyi):
    print (bunyi.pesan())

kirimkatakata(katakata())
kirimkatakata(katakatakata())

#abstraction
from abc import ABC, abstractmethod

class kendaraan (ABC):
    @abstractmethod
    def startmobil (self):
        pass

class mobillistrik (kendaraan):
    def startmobil (self):
        print ("mobil menyala")

icikkiwir = mobillistrik()
icikkiwir.startmobil()

# instan method
class mobil:
    def __init__(self, merk):
        self.merk = merk
    
    def tampilmerk (self):
        print ("Merk mobil: ", self.merk)

mobil1 = mobil("mercy")
mobil1.tampilmerk ()

# class method
class motor:
    jenis: "sport"

    @classmethod
    def ubahjenismotor(cls, jenisbaru):
        cls.jenis = jenisbaru

motor.ubahjenismotor("matic mberr")
print (motor.jenis)

#static method
class motor:
    @staticmethod
    def knalpot():
        print ("brot brot")
motor.knalpot()

#specialmethod
class sepatu:
    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga

    def __str__(self):
        return f"{self.merk}, Rp.{self.harga}"

    def __add__ (self, tambahan):
        return self.harga + tambahan.harga

sepatu1 = sepatu ("adidas", 2000000)
sepatu2 = sepatu ("homypad", 300000)

print (sepatu1)
print (sepatu2)
print ("jumlah keseluruhan Rp.", sepatu1+sepatu2)
