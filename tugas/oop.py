from abc import ABC, abstractmethod


# ===== ABSTRACTION: class induk abstrak (ABC + @abstractmethod) =====
class Penyanyi(ABC):
    label = "Indie Records"   # atribut class (dipakai class method)

    # ===== CONSTRUCTOR =====
    def __init__(self, nama, genre, pendengar):
        self.nama = nama
        self.genre = genre
        self.__pendengar = pendengar   # ===== ENCAPSULATION: private variable =====

    # ===== INSTANCE METHOD =====
    def tambahPendengar(self, jumlah):
        self.__pendengar += jumlah

    def tampilInfo(self):
        print(f"{self.nama} | genre {self.genre} | {self.__pendengar} pendengar | label {self.label}")

    # ===== CLASS METHOD =====
    @classmethod
    def ubahLabel(cls, labelBaru):
        cls.label = labelBaru

    # ===== STATIC METHOD =====
    @staticmethod
    def sapaPenonton():
        print("Halo semuanya, selamat malam!")

    @abstractmethod
    def tampil(self):
        pass

    # ===== SPECIAL / DUNDER METHOD =====
    def __str__(self):
        return f"{self.nama} ({self.genre})"

    def __add__(self, tambah):
        return self.__pendengar + tambah.__pendengar


# ===== INHERITANCE: class anak mewarisi Penyanyi =====
class PenyanyiSolo(Penyanyi):
    # ===== POLYMORPHISM =====
    def tampil(self):
        print(f"{self.nama} bernyanyi sendirian, genre {self.genre}")


class Band(Penyanyi):
    def __init__(self, nama, genre, pendengar, jumlahAnggota):
        super().__init__(nama, genre, pendengar)
        self.jumlahAnggota = jumlahAnggota

    # ===== POLYMORPHISM =====
    def tampil(self):
        print(f"{self.nama} tampil bareng {self.jumlahAnggota} anggota, genre {self.genre}")


# ===== PROGRAM UTAMA =====
Penyanyi.sapaPenonton()         # static method

solo1 = PenyanyiSolo("Drake", "Hip-Hop", 5000)
band1 = Band("Wave to Earth", "Indie Rock", 8000, 3)

solo1.tampil()                  # polymorphism
band1.tampil()

solo1.tambahPendengar(500)      # instance method + encapsulation
solo1.tampilInfo()
band1.tampilInfo()

Penyanyi.ubahLabel("Republic Records")   # class method
band1.tampilInfo()

print(solo1)                    # __str__
print("Total pendengar:", solo1 + band1)   # __add__