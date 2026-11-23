from abc import ABC, abstractmethod


class PerangkatKomputer(ABC):
    jumlah = 0

    def __init__(self, nama, merek, harga):
        self.nama = nama
        self.merek = merek
        self.__harga = harga
        PerangkatKomputer.jumlah += 1

    def get_harga(self):
        return self.__harga

    def set_harga(self, harga):
        if harga >= 0:
            self.__harga = harga
        else:
            print("Harga tidak boleh negatif.")

    @abstractmethod
    def nyalakan(self):
        pass

    def tampilkan_info(self):
        return (f"Nama: {self.nama}\nMerek: {self.merek}\n"
                f"Harga: Rp{self.__harga:,}")

    @classmethod
    def tampilkan_jumlah(cls):
        return f"Jumlah perangkat: {cls.jumlah}"

    @staticmethod
    def validasi_harga(harga):
        return isinstance(harga, (int, float)) and harga >= 0

    def __str__(self):
        return f"{self.nama} - {self.merek} (Rp{self.__harga:,})"

    def __add__(self, lain):
        if isinstance(lain, PerangkatKomputer):
            return self.__harga + lain.get_harga()
        return NotImplemented


class Laptop(PerangkatKomputer):
    def __init__(self, nama, merek, harga, baterai):
        super().__init__(nama, merek, harga)
        self.baterai = baterai
    
    def nyalakan(self):
        return f"Laptop {self.nama} dinyalakan dengan tombol power."
    
    def tampilkan_info(self):
        return super().tampilkan_info() + f"\nBaterai: {self.baterai} mAh"


class Desktop(PerangkatKomputer):
    def __init__(self, nama, merek, harga, monitor):
        super().__init__(nama, merek, harga)
        self.monitor = monitor

    def nyalakan(self):
        return f"Desktop {self.nama} dinyalakan melalui tombol CPU."

    def tampilkan_info(self):
        return super().tampilkan_info() + f"\nMonitor: {self.monitor}"


def main():
    laptop = Laptop("IdeaPad Slim 1i", "Lenovo", 5500000, 4000)
    desktop = Desktop("PC Rakitan", "Custom", 8500000, "LED 24 inci")

    print("=== SISTEM MANAJEMEN PERANGKAT KOMPUTER ===")
    print("\n--- DATA PERANGKAT ---")
    print(laptop.tampilkan_info())
    print()
    print(desktop.tampilkan_info())

    print("\n--- POLYMORPHISM ---")
    for perangkat in [laptop, desktop]:
        print(perangkat.nyalakan())

    print("\n--- ENCAPSULATION ---")
    print("Harga awal:", laptop.get_harga())
    laptop.set_harga(5300000)
    print("Harga baru:", laptop.get_harga())

    print("\n--- STATIC METHOD ---")
    print("Harga valid:", PerangkatKomputer.validasi_harga(5300000))

    print("\n--- CLASS METHOD ---")
    print(PerangkatKomputer.tampilkan_jumlah())
    print("\n--- SPECIAL METHOD ---")
    print("Total harga:", laptop + desktop)
    print(laptop)
    print(desktop)
if __name__ == "__main__":
    main()