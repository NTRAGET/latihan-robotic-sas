# class mobil: 
#     def __init__(self, merk, warna, tahun): #menginisialisasikan atribut merk, warna, dan tahun
#         self.merk = merk #atribut
#         self.warna = warna
#         self.tahun = tahun

#     def tampil_info(self):
#         print(f"Mobil ini merknya {self.merk}, warnya {self.warna}, dan tahun produksinya {self.tahun}.") #method untuk menampilkan informasi mobil
        
        
# mobil1 = input("Masukkan merk mobil pertama: ")
# warna1 = input("Masukkan warna mobil pertama: ")
# tahun1 = input("Masukkan tahun produksi mobil pertama: ")
# mobil2 = input("Masukkan merk mobil kedua: ")
# warna2 = input("Masukkan warna mobil kedua: ")
# tahun2 = input("Masukkan tahun produksi mobil kedua: ")
        
# Mobil1 = mobil(mobil1, warna1, tahun1)
# Mobil2 = mobil(mobil2, warna2, tahun2)

# Mobil1.tampil_info()
# Mobil2.tampil_info()

#encapsulation

# class manusia:
#     def __init__(self, nama, umur, pekerjaan): #menginisialisasikan atribut nama, umur, dan pekerjaan
#         self.__nama = nama #atribut
#         self.__umur = umur
#         self.pekerjaan = pekerjaan
        
#     def tambah_umur(self, tahun):
#         self.__umur += tahun 
        
#     def tampil_info(self):
#         print(f"Nama saya {self.__nama}, umur saya {self.__umur} tahun, dan pekerjaan saya adalah {self.pekerjaan}.") #method untuk menampilkan informasi manusia
            
            
# manusia1 = manusia("Budi", 25, "Programmer")
# manusia1.tampil_info()

# manusia1.tambah_umur(5)
# manusia1.tampil_info()

# manusia1.__umur =  45
# manusia1.tampil_info() 

#inharetance
# class film:
#     def __init__(self, judul):
#         self.judul = judul

              
#     def tampil_info(self):
#         print(f"Film ini berjudul {self.judul}") 
        
# class DetailFilm(film):
#     def __init__(self, judul, rating, batasUmur):
#         super().__init__(judul)
#         self.rating = rating
#         self.batasUmur = batasUmur
#     def tampil_detail(self):
#         print(f"Judul Film: {self.judul}, Rating: {self.rating}, Batas Umur: {self.batasUmur}")


# film1 = DetailFilm("Avengers: Endgame", "8.4", "13+")
# film1.tampil_detail()

#polymorphism

# class katakata:
#     def pesan(self):
#         return "hari ini Hujan adiiiiiks"
    
# class katakakata2:
#     def pesan(self):
#         return "hari ini cerah adiooooooos"
    
# def kirim_katakata(bunyi):
#     print(bunyi.pesan())
    
    
# kirim_katakata(katakata())
# kirim_katakata(katakakata2())
    
#ABSTRACTION

# from abc import ABC, abstractmethod

# class kendaraan(ABC):
#     @abstractmethod
#     def startMobil(self):
#         pass
    
# class MobilListrik(kendaraan):
#     def startMobil(self):
#         print("Mobil listrik dinyalakan dengan tombol start.")

# class MobilBensin(kendaraan):
#     def startMobil(self):
#         print("Mobil bensin dinyalakan dengan kunci kontak.")

# Tesla = MobilListrik()
# Tesla.startMobil()

# toyota = MobilBensin()
# toyota.startMobil()

# class motor:
#     @staticmethod
#     def startMotor():
#         print("Motor dinyalakan dengan kick starter.")
#     def jalan():
#         print("Motor berjalan di jalan raya.")
        
# motor.startMotor()
# motor.jalan()


class sepatu:
    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga
        
    def __str__(self):
        return f"{self.merk}, {self.harga}"
    
    def __add__(self, tambahan):
        return self.harga + tambahan.harga
    
sepatu1 = sepatu("abibas", 2000)
sepatu2 = sepatu("naiki", 4000)

print(sepatu1)
print(sepatu2)
print(sepatu1 + sepatu2)


