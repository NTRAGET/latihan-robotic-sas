from abc import ABC, abstractmethod

class Minuman(ABC):
    pajak_persen = 0 
    
    @classmethod
    def ubah_pajak(cls, pajak_baru):
        cls.pajak_persen = pajak_baru

    @staticmethod
    def salam():
        return "EH HII, U suka KOPI BIGMUY juga?"

    def __init__(self, nama, harga):
        self.nama = nama
        self.__harga = harga 

    def cek_harga(self):
        return self.__harga

    @abstractmethod
    def cara_bikin(self):
        pass

    def tampil_info(self):
        harga_pajak = self.__harga + (self.__harga * self.pajak_persen / 100)
        print(f"Menu: {self.nama} | Harga Asli: Rp {self.__harga} | Harga + Pajak: Rp {int(harga_pajak)}")

    def __str__(self):
        return f"Minuman {self.nama}"

    def __add__(self, minuman_lain):
        harga1_pajak = self.__harga + (self.__harga * self.pajak_persen / 100)
        harga2_pajak = minuman_lain.cek_harga() + (minuman_lain.cek_harga() * self.pajak_persen / 100)
        total = harga1_pajak + harga2_pajak
        return f"Total Harga Combo (Termasuk Pajak): Rp {int(total)}"


class Kopi(Minuman):
    def __init__(self, nama, harga, jenis_biji):
        super().__init__(nama, harga)
        self.jenis_biji = jenis_biji

    def cara_bikin(self):
        print(f"{self.nama} dibuat menggunakan mesin Espresso dengan biji {self.jenis_biji}!")


class NonKopi(Minuman):
    def __init__(self, nama, harga, rasa):
        super().__init__(nama, harga)
        self.rasa = rasa

    def cara_bikin(self):
        print(f"{self.nama} dibuat dengan cara diblender menggunakan rasa {self.rasa}!")



minuman1 = Kopi("Americano", 20000, "Arabica")
minuman2 = NonKopi("Matcha", 25000, "Matcha Premium")

daftar_menu = [minuman1, minuman2]


def tampil_menu():
    print("\n" + "="*35)
    print("     KAFE YANG MULIA BIGMUY")
    print("="*35)
    print("1. Lihat Daftar Menu")
    print("2. Lihat Cara Pembuatan")
    print("3. Cek Harga & Total Combo")
    print("4. Ubah Pajak Kafe")
    print("5. Keluar")
    print("="*35)

def lihat_menu():
    print("\n\n--- DAFTAR MENU ---")
    for i, minuman in enumerate(daftar_menu):
        print(f"{i+1}. {minuman}")
        minuman.tampil_info()
        print("-" * 20)

def lihat_cara_bikin():
    print("\n\n--- CARA PEMBUATAN ---")
    for minuman in daftar_menu:
        minuman.cara_bikin() 

def cek_harga_dan_combo():
    print("\n\n--- HARGA MASING-MASING ---")
    for minuman in daftar_menu:
        harga_pajak = minuman.cek_harga() + (minuman.cek_harga() * Minuman.pajak_persen / 100)
        print(f"{minuman.nama}: Rp {int(harga_pajak)}")
    
    print("\n\n--- JIKA DIBELI COMBO ---")
    hasil = minuman1 + minuman2 
    print(hasil)

def ubah_pajak():
    print("\n\n--- UBAH PAJAK KAFE ---")
    pajak_baru = int(input("Masukkan persentase pajak baru (contoh: 10): "))
    Minuman.ubah_pajak(pajak_baru)
    print(f"Pajak kafe sekarang: {Minuman.pajak_persen}%")


print(Minuman.salam())

while True:
    tampil_menu()
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == '1':
        lihat_menu()
    elif pilihan == '2':
        lihat_cara_bikin()
    elif pilihan == '3':
        cek_harga_dan_combo()
    elif pilihan == '4':
        ubah_pajak()
    elif pilihan == '5':
        print("\nTengkyu telah berkunjung ke Kafe Bigmuy!")
        break
    else:
        print("\nPilihan gaada bos, yang bener napa")