from abc import ABC, abstractmethod
class Kendaraan(ABC):
  @abstractmethod
  def nyalakan_mesin(self):
    pass

class Mobil(Kendaraan):
  jenis_bahan_bakar = "Bensin"
  def __init__(self, merek, warna, harga):
    self.merek = merek
    self.warna = warna
    self.__harga = harga
  def nyalakan_mesin(self):
    print(f"Mobil {self.merek} menyala: Vroom Vroom...")
  def diskon_harga(self, potongan):
    self.__harga -= potongan
  def tampil_info(self):
    print(f"Mobil {self.merek}, Warna {self.warna}, Harga Rp {self.__harga:,}, Bahan Bakar {self.jenis_bahan_bakar}")

  @classmethod
  def ubah_bahan_bakar(cls, bahan_bakar_baru):
    cls.jenis_bahan_bakar = bahan_bakar_baru

  @staticmethod
  def bunyi_klakson():
    print("Tin! Tin!")

  def __str__(self):
    return f"Mobil {self.merek} ({self.warna}), Rp {self.__harga:,}"

  def __add__(self, mobil_lain):
    return self.__harga + mobil_lain.__harga

class Motor(Kendaraan):

  def __init__(self, merek, warna, harga):
    self.merek = merek
    self.warna = warna
    self.__harga = harga

  def nyalakan_mesin(self):
    print(f"Motor {self.merek} menyala: Ngenggg...")

  def __str__(self):
    return f"Motor {self.merek} ({self.warna}), Rp {self.__harga:,}"

def tes_mesin(kendaraan):
  kendaraan.nyalakan_mesin()

mobil1 = Mobil("Avanza", "Putih", 200000000)
mobil2 = Mobil("Civic", "Hitam", 500000000)
motor1 = Motor("Vario", "Merah", 25000000)

mobil1.diskon_harga(10000000)
mobil1.tampil_info()

Mobil.ubah_bahan_bakar("Listrik")
mobil2.tampil_info()

Mobil.bunyi_klakson()

tes_mesin(mobil1)
tes_mesin(motor1)

print(mobil1)
print(motor1)
print(f"Total harga {mobil1.merek} + {mobil2.merek}: Rp {mobil1 + mobil2:,}")