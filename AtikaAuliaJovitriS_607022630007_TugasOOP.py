from abc import ABC, abstractmethod


# 1. Abstraction
class Kegiatan(ABC):
    @abstractmethod
    def cek_prioritas(self):
        pass


# 2. Class Induk, Encapsulation, Method (Instance, Class, Static, Special)
class Tugas(Kegiatan):
    kategori_umum = "Manajemen Waktu"  # class attribute

    def __init__(self, nama_tugas, deadline, sisa_hari):
        self.nama_tugas = nama_tugas
        self.deadline = deadline
        self.__sisa_hari = sisa_hari  # private (encapsulation)

    # Instance method
    def tampil_info(self):
        print(f"Tugas: {self.nama_tugas} | Deadline: {self.deadline} | Sisa waktu: {self.__sisa_hari} hari")

    # Getter untuk mengakses private variable __sisa_hari
    def get_sisa_hari(self):
        return self.__sisa_hari

    # Polymorphism (implementasi dari abstract method)
    def cek_prioritas(self):
        if self.__sisa_hari <= 2:
            return f"{self.nama_tugas} -> Prioritas Tinggi (Kerjakan Sekarang!)"
        else:
            return f"{self.nama_tugas} -> Prioritas Normal (Bisa Dicicil)"

    # Class method
    @classmethod
    def ubah_kategori(cls, kategori_baru):
        cls.kategori_umum = kategori_baru

    # Static method
    @staticmethod
    def pengingat():
        print("Jangan menunda pekerjaan!")

    # Special method (__str__ & __add__)
    def __str__(self):
        return f"{self.nama_tugas} (Deadline: {self.deadline})"

    def __add__(self, tugas_lain):
        # Menjumlahkan total sisa hari dua tugas
        return self.__sisa_hari + tugas_lain.get_sisa_hari()


# 3. Inheritance & Polymorphism
class TugasKuliah(Tugas):
    def __init__(self, nama_tugas, deadline, sisa_hari, matkul):
        super().__init__(nama_tugas, deadline, sisa_hari)
        self.matkul = matkul

    # Polymorphism: output cek_prioritas berbeda dengan class induk
    def cek_prioritas(self):
        if self.get_sisa_hari() <= 3:
            return f"{self.nama_tugas} -> URGENT Matkul {self.matkul}! Deadline tinggal {self.get_sisa_hari()} hari"
        else:
            return f"{self.nama_tugas} -> Aman untuk Matkul {self.matkul}, masih ada {self.get_sisa_hari()} hari"


# ==========================================
# Hasil dari implementasi OOP
# ==========================================

# Membuat object
tugas1 = Tugas("OOP BOOTCAMP", "23 November", 1)
tugas2 = TugasKuliah("Laporan Praktikum", "26 November", 3, "Algoritma & Pemrograman")

# Instance method & Special method (__str__)
print("=== DAFTAR TUGAS ===")
print(tugas1)
tugas1.tampil_info()
tugas2.tampil_info()

# Polymorphism
print("\n=== CEK PRIORITAS ===")
print(tugas1.cek_prioritas())
print(tugas2.cek_prioritas())

# Class method & Static method
print("\n=== INFO TAMBAHAN ===")
Tugas.ubah_kategori("Jadwal Harian Mahasiswa")
print("Kategori:", Tugas.kategori_umum)
Tugas.pengingat()

# Special method (__add__)
print("Total gabungan waktu pengerjaan:", tugas1 + tugas2, "hari")
