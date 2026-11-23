from abc import ABC, abstractmethod
class Koleksi(ABC):
    total_koleksi = 0
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True
        Koleksi.total_koleksi += 1
    def cek_status(self):
        return self.__tersedia
    def pinjam(self):
        if self.__tersedia:
            self.__tersedia = False
            print("Buku berhasil dipinjam.")
        else:
            print("Buku sedang dipinjam orang lain.")
    def kembalikan(self):
        if not self.__tersedia:
            self.__tersedia = True
            print("Buku berhasil dikembalikan.")
        else:
            print("Buku ini belum dipinjam.")
    @staticmethod
    def cek_input(teks):
        return teks.strip() != ""
    @classmethod
    def hitung_koleksi(cls):
        return cls.total_koleksi
    @abstractmethod
    def jenis_koleksi(self):
        pass
    def __str__(self):
        if self.__tersedia:
            status = "Tersedia"
        else:
            status = "Dipinjam"

        return (
            "Judul: " + self.judul
            + "\nPenulis: " + self.penulis
            + "\nJenis: " + self.jenis_koleksi()
            + "\nStatus: " + status
        )
class Buku(Koleksi):
    def __init__(self, judul, penulis, halaman):
        super().__init__(judul, penulis)
        self.halaman = halaman

    def jenis_koleksi(self):
        return "Buku cetak"

    def __add__(self, buku_lain):
        if isinstance(buku_lain, Buku):
            return self.halaman + buku_lain.halaman
        return NotImplemented
class Majalah(Koleksi):
    def __init__(self, judul, penulis, edisi):
        super().__init__(judul, penulis)
        self.edisi = edisi

    def jenis_koleksi(self):
        return "Majalah"
class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.__pinjaman = []

    def pinjam_koleksi(self, koleksi):
        if koleksi.cek_status():
            koleksi.pinjam()
            self.__pinjaman.append(koleksi)
        else:
            print("Peminjaman tidak berhasil.")

    def kembalikan_koleksi(self, nomor):
        if nomor >= 1 and nomor <= len(self.__pinjaman):
            koleksi = self.__pinjaman.pop(nomor - 1)
            koleksi.kembalikan()
        else:
            print("Nomor pinjaman tidak valid.")

    def lihat_pinjaman(self):
        if len(self.__pinjaman) == 0:
            print("Belum ada buku yang dipinjam.")
        else:
            print("\nDaftar buku yang dipinjam:")
            for i in range(len(self.__pinjaman)):
                print(str(i + 1) + ". " + self.__pinjaman[i].judul)

daftar_koleksi = [
    Buku("Laskar Pelangi", "Andrea Hirata", 529),
    Buku("Bumi", "Tere Liye", 440),
    Majalah("Majalah Teknologi", "Tim Redaksi", 12)
]
anggota = None
def tampilkan_koleksi():
    print("\n===== DAFTAR KOLEKSI =====")
    for i in range(len(daftar_koleksi)):
        print("\nNomor:", i + 1)
        print(daftar_koleksi[i])
def menu():
    global anggota
    while True:
        print("\n==============================")
        print("   SISTEM PERPUSTAKAAN")
        print("==============================")
        print("1. Tampilkan koleksi")
        print("2. Daftar anggota")
        print("3. Pinjam koleksi")
        print("4. Kembalikan koleksi")
        print("5. Lihat daftar pinjaman")
        print("6. Hitung jumlah koleksi")
        print("7. Jumlah halaman dua buku")
        print("8. Keluar")
        print("==============================")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_koleksi()
        elif pilihan == "2":
            nama = input("Masukkan nama anggota: ")
            if Koleksi.cek_input(nama):
                anggota = Anggota(nama)
                print("Pendaftaran berhasil. Selamat datang,", nama)
            else:
                print("Nama tidak boleh kosong.")
        elif pilihan == "3":
            if anggota is None:
                print("Daftar sebagai anggota terlebih dahulu.")
                continue
            tampilkan_koleksi()
            try:
                nomor = int(input("Masukkan nomor koleksi: "))
                if nomor >= 1 and nomor <= len(daftar_koleksi):
                    anggota.pinjam_koleksi(daftar_koleksi[nomor - 1])
                else:
                    print("Nomor koleksi tidak tersedia.")
            except ValueError:
                print("Masukkan angka yang benar.")
        elif pilihan == "4":
            if anggota is None:
                print("Belum ada anggota yang terdaftar.")
            else:
                anggota.lihat_pinjaman()
                try:
                    nomor = int(input("Nomor buku yang dikembalikan: "))
                    anggota.kembalikan_koleksi(nomor)
                except ValueError:
                    print("Masukkan angka yang benar.")

        elif pilihan == "5":
            if anggota is None:
                print("Daftar sebagai anggota terlebih dahulu.")
            else:
                print("Nama anggota:", anggota.nama)
                anggota.lihat_pinjaman()

        elif pilihan == "6":
            print("Jumlah seluruh koleksi:", Koleksi.hitung_koleksi())

        elif pilihan == "7":
            buku1 = daftar_koleksi[0]
            buku2 = daftar_koleksi[1]
            jumlah_halaman = buku1 + buku2
            print("Jumlah halaman", buku1.judul, "dan", buku2.judul,
                  "adalah", jumlah_halaman, "halaman.")
        elif pilihan == "8":
            print("Terima kasih telah menggunakan perpustakaan.")
            break
        else:
            print("Pilihan tidak tersedia. Silakan coba lagi.")
if __name__ == "__main__":
    menu()
