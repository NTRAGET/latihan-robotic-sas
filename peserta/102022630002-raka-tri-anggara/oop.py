from abc import ABC, abstractmethod

class Blacklist(ABC):
    jumlah = 0

    def __init__(self, peringkat, nama, mobil, kecepatan_maks):
        self.peringkat = peringkat
        self.nama = nama
        self.mobil = mobil
        self.__kecepatan_maks = kecepatan_maks  
        Blacklist.jumlah += 1

    def get_kecepatan_maks(self):
        return self.__kecepatan_maks

    @abstractmethod
    def spesifikasi_mesin(self):
        pass

    def perkenalan(self):
        print(f"Blacklist #{self.peringkat}: {self.nama} | Mobil: {self.mobil}")

    @classmethod
    def total_blacklist(cls):
        return cls.jumlah

    @staticmethod
    def sapa():
        print("Welcome to Rockport City - NFS Most Wanted!")

    def __str__(self):
        return f"#{self.peringkat} {self.nama} ({self.mobil})"

    def __add__(self, other):
        return self.__kecepatan_maks + other.__kecepatan_maks

class Razor(Blacklist):
    def spesifikasi_mesin(self):
        print(f"{self.mobil}: mesin V8 4.0 liter")

class Bull(Blacklist):
    def spesifikasi_mesin(self):
        print(f"{self.mobil}: mesin V8 5.4 liter supercharged")

Blacklist.sapa()

razor = Razor(1, "Clarence 'Razor' Callahan", "BMW M3 GTR", 389)
bull = Bull(2, "Toru 'Bull' Sato", "Mercedes-Benz SLR McLaren", 382)

razor.perkenalan()
bull.perkenalan()

razor.spesifikasi_mesin()
bull.spesifikasi_mesin()

print("Top speed Razor", razor.get_kecepatan_maks(), "km/h")
print("Top speed Bull", bull.get_kecepatan_maks(), "km/h")
print("Total top speed:", razor + bull, "km/h")
print("Jumlah blacklist:", Blacklist.total_blacklist())