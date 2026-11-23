
from abc import ABC, abstractmethod


# CLASS INDUK
class Kendaraan(ABC):

    jumlah = 0

    # CONSTRUCTOR
    def __init__(self, nama, harga_sewa):
        self.__nama = nama
        self.__harga_sewa = harga_sewa
        Kendaraan.jumlah += 1

    # GETTER
    def get_nama(self):
        return self.__nama

    def get_harga_sewa(self):
        return self.__harga_sewa

    # INSTANCE METHOD
    def tampilkan_info(self):
        print(self)

    # ABSTRACT METHOD
    @abstractmethod
    def hitung_biaya(self, hari):
        pass

    # CLASS METHOD
    @classmethod
    def jumlah_kendaraan(cls):
        return cls.jumlah

    # STATIC METHOD
    @staticmethod
    def validasi_hari(hari):
        return hari > 0

    # DUNDER METHOD __str__
    def __str__(self):
        return f"{self.__nama} - Rp{self.__harga_sewa:,}/hari"

    # DUNDER METHOD __add__
    def __add__(self, kendaraan_lain):
        return self.get_harga_sewa() + kendaraan_lain.get_harga_sewa()


# CLASS ANAK: MOBIL
class Mobil(Kendaraan):

    def hitung_biaya(self, hari):
        return self.get_harga_sewa() * hari


# CLASS ANAK: MOTOR
class Motor(Kendaraan):

    def hitung_biaya(self, hari):
        return self.get_harga_sewa() * hari


# PROGRAM UTAMA
mobil = Mobil("Toyota Avanza", 300000)
motor = Motor("Honda Vario", 100000)

print("=== SISTEM PENYEWAAN KENDARAAN ===")

# MENAMPILKAN INFORMASI
print("\nDaftar Kendaraan:")
mobil.tampilkan_info()
motor.tampilkan_info()

# INPUT LAMA PENYEWAAN
hari = int(input("\nMasukkan lama penyewaan (hari): "))

# VALIDASI HARI
if Kendaraan.validasi_hari(hari):

    print("\n=== RINCIAN BIAYA KENDARAAN YANG DISEWA ===")

    # POLYMORPHISM
    daftar_kendaraan = [mobil, motor]

    for kendaraan in daftar_kendaraan:
        print("Kendaraan:", kendaraan.get_nama())
        print("Biaya Sewa: Rp", format(kendaraan.hitung_biaya(hari), ","))
        print()

    # DUNDER METHOD __add__
    total = (mobil + motor) * hari

    print("Jumlah kendaraan:", Kendaraan.jumlah_kendaraan())
    print("Total seluruh biaya sewa: Rp", format(total, ","))

else:
    print("Lama penyewaan harus lebih dari 0 hari!")