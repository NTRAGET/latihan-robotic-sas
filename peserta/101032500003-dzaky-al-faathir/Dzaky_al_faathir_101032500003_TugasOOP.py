from abc import ABC, abstractmethod


class Spesifikasi(ABC):
    def __init__(self, merk):
        self.merk = merk

    @abstractmethod
    def spek(self):
        pass


class Mobil(Spesifikasi):
    batas_kecepatan = 100

    def __init__(self, merk, tahun, jarak_tempuh):
        super().__init__(merk)
        self.tahun = tahun
        self.__jarak_tempuh = jarak_tempuh

    def jaraktempuh(self):
        return self.__jarak_tempuh

    def ijin_tampil(self):
        print(f"Merk: {self.merk}, Batas kecepatan: {self.batas_kecepatan} km/jam")

    @classmethod
    def ubah_batas_kecepatan(cls, kecepatan_baru):
        cls.batas_kecepatan = kecepatan_baru

    @staticmethod
    def satuan_jarak():
        print("Satuan jarak tempuh: km")

    def spek(self):
        print(f"Spek {self.merk}: tahun {self.tahun}, jarak tempuh {self.__jarak_tempuh} km")

    def __str__(self):
        return f"{self.merk} ({self.tahun}) - {self.__jarak_tempuh} km"

    def __add__(self, other):
        total = self.jaraktempuh() + other.jaraktempuh()
        return f"Total jarak tempuh {self.merk} + {other.merk}: {total} km"


class MobilSport(Mobil):
    def __init__(self, merk, tahun, jarak_tempuh, jumlah_slot):
        super().__init__(merk, tahun, jarak_tempuh)
        self.jumlah_slot = jumlah_slot

    def spek(self):
        print(f"Spek Sport {self.merk}: tahun {self.tahun}, "
              f"jarak tempuh {self.jaraktempuh()} km, "
              f"jumlah bangku {self.jumlah_slot}")


m1 = Mobil("ichikiwir", 1945, 120000)
m2 = MobilSport("lambo", 2000, 32000, 2)

Mobil.satuan_jarak()

m1.ijin_tampil()

Mobil.ubah_batas_kecepatan(120)
print("Batas kecepatan setelah dibore up:", Mobil.batas_kecepatan, "km/jam")
m1.ijin_tampil()
m2.ijin_tampil()

m1.spek()
m2.spek()

print(m1)
print(m2)
print(m1 + m2)