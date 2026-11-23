from abc import ABC, abstractmethod


class Mobil(ABC):
    jumlah_mobil = 0

    def __init__(self, merek, warna):
        self.merek = merek
        self.__warna = warna
        Mobil.jumlah_mobil += 1

    def get_warna(self):
        return self.__warna

    def set_warna(self, warna_baru):
        if Mobil.cek_warna_valid(warna_baru):
            self.__warna = warna_baru
        else:
            print("Warna tidak tersedia!")

    def cat_ulang(self, warna_baru):
        self.set_warna(warna_baru)

    def info(self):
        return f"{self.merek} berwarna {self.__warna}"

    @abstractmethod
    def jalan(self):
        pass

    @classmethod
    def total_mobil(cls):
        return f"Total mobil: {cls.jumlah_mobil}"

    @classmethod
    def dari_string(cls, data, tambahan):
        merek, warna = data.split(",")
        return cls(merek, warna, tambahan)

    @staticmethod
    def cek_warna_valid(warna):
        return warna in ("merah", "hitam", "putih", "biru", "silver")

    def __str__(self):
        return f"{self.__class__.__name__} {self.merek} warna {self.__warna}"

    def __add__(self, other):
        return f"Konvoi: {self.merek} dan {other.merek}"


class MobilListrik(Mobil):
    def __init__(self, merek, warna, pengisian):
        super().__init__(merek, warna)
        self.pengisian = pengisian

    def jalan(self):
        return f"{self.merek} jalan tanpa suara, diisi dengan {self.pengisian}."


class MobilBensin(Mobil):
    def __init__(self, merek, warna, bahan_bakar):
        super().__init__(merek, warna)
        self.bahan_bakar = bahan_bakar

    def jalan(self):
        return f"{self.merek} jalan pakai bensin {self.bahan_bakar}."


class MobilBalap(Mobil):
    def __init__(self, merek, warna, lintasan):
        super().__init__(merek, warna)
        self.lintasan = lintasan

    def jalan(self):
        return f"{self.merek} ngebut di {self.lintasan}!"


if __name__ == "__main__":
    tesla = MobilListrik("Tesla", "putih", "charger")
    toyota = MobilBensin("Toyota", "hitam", "Pertamax")
    ferrari = MobilBalap("Ferrari", "merah", "sirkuit")
    honda = MobilBensin.dari_string("Honda,biru", "Pertalite")

    print("=== Daftar Mobil ===")
    for mobil in (tesla, toyota, ferrari, honda):
        print(mobil)

    print("\n=== Mobil Jalan ===")
    for mobil in (tesla, toyota, ferrari, honda):
        print(mobil.jalan())

    print("\n=== Warna ===")
    print(toyota.info())
    toyota.cat_ulang("silver")
    print("Setelah dicat ulang:", toyota.get_warna())
    toyota.set_warna("pelangi")

    print("\n=== Cek Warna Valid ===")
    print("Warna merah valid?", Mobil.cek_warna_valid("merah"))
    print("Warna pelangi valid?", Mobil.cek_warna_valid("pelangi"))

    print("\n=== Gabung Mobil ===")
    print(tesla + toyota)

    print("\n=== Jumlah Mobil ===")
    print(Mobil.total_mobil())

    print("\n=== Class Abstrak ===")
    try:
        Mobil("Test", "merah")
    except TypeError:
        print("Mobil tidak bisa dibuat langsung")