from abc import ABC, abstractmethod

# ==========================================
# CLASS INDUK
# ==========================================
class Kendaraan(ABC):

    jumlah_kendaraan = 0

    # CONSTRUCTOR
    def __init__(self, nama, harga_sewa):
        self.__nama = nama
        self.__harga_sewa = harga_sewa
        Kendaraan.jumlah_kendaraan += 1

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
    def jumlah_unit(cls):
        return cls.jumlah_kendaraan

    # STATIC METHOD
    @staticmethod
    def validasi_hari(hari):
        return hari > 0

    # DUNDER METHOD __str__
    def __str__(self):
        return (
            f"{self.__nama} - "
            f"Rp{self.__harga_sewa:,}/hari"
        )


# ==========================================
# CLASS ANAK: MOBIL
# ==========================================
class Mobil(Kendaraan):

    def hitung_biaya(self, hari):
        # Menghitung biaya sewa mobil
        total = self.get_harga_sewa() * hari
        return total


# ==========================================
# CLASS ANAK: MOTOR
# ==========================================
class Motor(Kendaraan):

    def hitung_biaya(self, hari):
        # Motor mendapatkan diskon 10%
        # jika disewa minimal 3 hari
        total = self.get_harga_sewa() * hari

        if hari >= 3:
            total = total - (total * 0.10)

        return total


# ==========================================
# CLASS PENYEWAAN
# ==========================================
class Penyewaan:

    def __init__(self, kendaraan, hari):
        self.kendaraan = kendaraan
        self.hari = hari
        self.total = kendaraan.hitung_biaya(hari)

    # DUNDER METHOD __str__
    def __str__(self):
        return (
            f"{self.kendaraan.get_nama()} | "
            f"{self.hari} hari | "
            f"Rp{self.total:,.0f}"
        )


# ==========================================
# CLASS KERANJANG
# ==========================================
class KeranjangSewa:

    def __init__(self):
        self.daftar_sewa = []

    # DUNDER METHOD __add__
    def __add__(self, penyewaan):
        self.daftar_sewa.append(penyewaan)
        return self

    # INSTANCE METHOD
    def tampilkan_keranjang(self):
        if len(self.daftar_sewa) == 0:
            print("\nKeranjang masih kosong!")
            return

        print("\n========== KERANJANG SEWA ==========")

        for nomor, sewa in enumerate(self.daftar_sewa, start=1):
            print(f"{nomor}. {sewa}")

        print("====================================")

    # INSTANCE METHOD
    def hitung_total(self):
        total = 0

        for sewa in self.daftar_sewa:
            total += sewa.total

        return total


# ==========================================
# PROGRAM UTAMA
# ==========================================

# Membuat objek kendaraan
mobil = Mobil("Toyota Avanza", 300000)
motor = Motor("Honda Vario", 100000)

# Membuat objek keranjang
keranjang = KeranjangSewa()

# Menyimpan pilihan menu
while True:

    print("\n=================================")
    print("    SISTEM PENYEWAAN KENDARAAN")
    print("=================================")
    print("1. Lihat daftar kendaraan")
    print("2. Sewa mobil")
    print("3. Sewa motor")
    print("4. Lihat keranjang penyewaan")
    print("5. Checkout")
    print("0. Keluar")
    print("=================================")

    pilihan = input("Masukkan pilihan menu: ")

    # MENU 1: DAFTAR KENDARAAN
    if pilihan == "1":

        print("\n========== DAFTAR KENDARAAN ==========")
        mobil.tampilkan_info()
        motor.tampilkan_info()

    # MENU 2: SEWA MOBIL
    elif pilihan == "2":

        print("\n========== PENYEWAAN MOBIL ==========")
        mobil.tampilkan_info()

        try:
            hari = int(input("Masukkan lama sewa (hari): "))

            if Kendaraan.validasi_hari(hari):

                sewa = Penyewaan(mobil, hari)

                # Menambahkan penyewaan ke keranjang
                keranjang = keranjang + sewa

                print("\nMobil berhasil ditambahkan!")
                print("Total biaya: Rp", format(sewa.total, ",.0f"))

            else:
                print("Lama penyewaan harus lebih dari 0!")

        except ValueError:
            print("Input harus berupa angka!")

    # MENU 3: SEWA MOTOR
    elif pilihan == "3":

        print("\n========== PENYEWAAN MOTOR ==========")
        motor.tampilkan_info()

        try:
            hari = int(input("Masukkan lama sewa (hari): "))

            if Kendaraan.validasi_hari(hari):

                sewa = Penyewaan(motor, hari)

                # Menambahkan penyewaan ke keranjang
                keranjang = keranjang + sewa

                print("\nMotor berhasil ditambahkan!")
                print("Total biaya: Rp", format(sewa.total, ",.0f"))

                if hari >= 3:
                    print("Selamat! Anda mendapatkan diskon 10%.")

            else:
                print("Lama penyewaan harus lebih dari 0!")

        except ValueError:
            print("Input harus berupa angka!")

    # MENU 4: KERANJANG
    elif pilihan == "4":

        keranjang.tampilkan_keranjang()

        if len(keranjang.daftar_sewa) > 0:
            print(
                "Total sementara: Rp",
                format(keranjang.hitung_total(), ",.0f")
            )

    # MENU 5: CHECKOUT
    elif pilihan == "5":

        if len(keranjang.daftar_sewa) == 0:
            print("\nBelum ada kendaraan yang disewa!")

        else:
            keranjang.tampilkan_keranjang()

            total = keranjang.hitung_total()

            print("\n========== CHECKOUT ==========")
            print("Jumlah kendaraan:",
                  len(keranjang.daftar_sewa))
            print("Total pembayaran: Rp",
                  format(total, ",.0f"))

            print("\nTerima kasih telah menyewa!")
            print("Silakan melakukan pembayaran.")

            break

    # MENU 0: KELUAR
    elif pilihan == "0":

        print("\nTerima kasih telah menggunakan program!")
        break

    else:
        print("\nPilihan tidak tersedia! Silakan coba lagi.")


# MENAMPILKAN JUMLAH OBJEK KENDARAAN
print("\nJumlah objek kendaraan:",
      Kendaraan.jumlah_unit())
