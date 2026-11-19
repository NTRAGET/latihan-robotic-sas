# # # # # # class Mobil:
# # # # # #     def __init__(self, merk, warna, tahun):
# # # # # #         self.merk = merk
# # # # # #         self.warna = warna
# # # # # #         self.tahun = tahun

# # # # # #     def info(self):
# # # # # #         print(f"Merk mobil ini: {self.merk}, Warna: {self.warna}, Tahun: {self.tahun}")

# # # # # # Mobil1 = Mobil("Avanza", "Putih", "1945")
# # # # # # Mobil2 = Mobil("Lambo", "Pink", "2000")

# # # # # # Mobil1.info()
# # # # # # Mobil2.info()

# # # # # # class Manusia:
# # # # # #     def __init__(self, umur):
# # # # # #         self.umur = umur

# # # # # #     def ulangtahun(self, tambahumur):
# # # # # #         self.umur += tambahumur

# # # # # #     def tampil_umur(self):
# # # # # #         print(f"Umur saya saat ini: {self.umur}")

# # # # # # Andityo = Manusia(20)
# # # # # # Andityo.tampil_umur()
# # # # # # Andityo.ulangtahun(1)
# # # # # # Andityo.tampil_umur()

# # # # # class Film:
# # # # #     def __init__(self, judul):
# # # # #         self.judul = judul

# # # # #     def tampil_judul(self):
# # # # #         print(f"Judul film ini adalah: {self.judul}")

# # # # # class DetailFilm(Film):
# # # # #     def __init__(self, judul, rating, batasumur):
# # # # #         super().__init__(judul)
# # # # #         self.rating = rating
# # # # #         self.batasumur = batasumur

# # # # #     def tampil_detail(self):
# # # # #         print(f"Judul: {self.judul}, Rating: {self.rating}, Batas Umur Minimal: {self.batasumur}")

# # # # # film1 = DetailFilm("Godzilla", "9/10", 17)
# # # # # film2 = DetailFilm("Avengers", "10/10", 13)

# # # # # film1.tampil_detail()
# # # # # film2.tampil_detail()

# # # # class katakata:
# # # #     def pesan(self):
# # # #         return "hari ini hujan coy"

# # # # class katakatakata:
# # # #     def pesan(self):
# # # #         return "Selamat malam"

# # # # def kirim_katakata(bunyi):
# # # #     print(bunyi.pesan())

# # # # kirim_katakata(katakata())
# # # # kirim_katakata(katakatakata())

# # # from abc import ABC, abstractmethod

# # # class Kendaraan(ABC):
# # #     @abstractmethod
# # #     def startmobil(self):
# # #         pass

# # # class Mobillistrik(Kendaraan):
# # #     def startmobil(self):
# # #         print("Mobil listrik menyala")

# # # Icikiwir = Mobillistrik()
# # # Icikiwir.startmobil()

# # class Mobil:
# #     def __init__(self, merk):
# #         self.merk = merk

# #     def tampil_merk(self):
# #         print(f"Merk mobil ini adalah: {self.merk}")

# # mobil1 = Mobil("Mercy")
# # mobil1.tampil_merk()

# class Motor:
#     jenis: "Sport"

#     @classmethod
#     def ubah_jenis_motor(cls, jenis_baru):
#         cls.jenis = jenis_baru

# Motor.ubah_jenis_motor("matic mber")
# print(Motor.jenis)

# class Motor:
#     @staticmethod
#     def knalpot():
#         print("brom brom")

# Motor.knalpot()

class Sepatu:
    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga

    def __str__(self):
        return f"{self.merk}, Rp {self.harga}"

    def __add__(self, tambahan):
        return self.harga + tambahan.harga

Sepatu1 = Sepatu("Adidas", 2000000)
Sepatu2 = Sepatu("Homyped", 300000)

print(Sepatu1)
print(Sepatu2)
print(Sepatu1 + Sepatu2)