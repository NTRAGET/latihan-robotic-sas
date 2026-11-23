from abc import ABC, abstractmethod

NAMA_BANK = "Bank SAS"


class Rekening(ABC):
    total_rekening = 0  

    def __init__(self, nomor, nama, saldo_awal):
        self.__nomor = nomor        
        self.__saldo = saldo_awal 
        self.nama = nama
        self.mutasi = [] 
        Rekening.total_rekening += 1

    def __str__(self):
        return f"{self.nama} | {self.__nomor} | Saldo: {Rekening.format_rp(self.__saldo)}"

    def __add__(self, other):
        return self.jumlah_transaksi() + other.jumlah_transaksi()

    def get_nomor(self):
        return self.__nomor

    def cek_saldo(self):
        return self.__saldo

    def jumlah_transaksi(self):
        return len(self.mutasi)

    def kurangi_saldo(self, nominal):
        self.__saldo -= nominal

    def catat_mutasi(self, jenis, nominal):
        transaksi = {
            "jenis": jenis,
            "nominal": nominal,
            "saldo_akhir": self.__saldo
        }
        self.mutasi.append(transaksi)

    def setor(self, nominal):
            self.__saldo += nominal
            self.catat_mutasi("Setor Tunai", nominal)
            print(f"[{self.nama}] Setor {Rekening.format_rp(nominal)} berhasil.")

    def tampil_mutasi(self):
        print(f"Riwayat mutasi {self.nama}:")
        if len(self.mutasi) == 0:
            print("  Belum ada transaksi.")
        else:
            for index, trx in enumerate(self.mutasi):
                nomor = index + 1
                print(f"  {nomor}. {trx['jenis']} | {Rekening.format_rp(trx['nominal'])} | Saldo akhir: {Rekening.format_rp(trx['saldo_akhir'])}")

    @classmethod
    def get_total_rekening(cls):
        return cls.total_rekening

    @staticmethod
    def format_rp(nominal):
        return f"Rp {nominal}"

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def tarik(self, nominal):
        pass


class RekeningBiasa(Rekening):
    def __init__(self, nomor, nama, saldo_awal):
        super().__init__(nomor, nama, saldo_awal)
        self.jenis = "Gold"

    def info(self):
        print(f"Jenis   : {self.jenis}")
        print(f"Nomor   : {self.get_nomor()}")
        print(f"Pemilik : {self.nama}")
        print(f"Saldo   : {Rekening.format_rp(self.cek_saldo())}")

    def tarik(self, nominal):
            self.kurangi_saldo(nominal)
            self.catat_mutasi("Tarik Tunai", nominal)
            print(f"({self.nama}) Tarik {Rekening.format_rp(nominal)} berhasil.")


class RekeningPremium(Rekening):
    def __init__(self, nomor, nama, saldo_awal):
        super().__init__(nomor, nama, saldo_awal)
        self.jenis = "Platinum"
        self.limit_tarik = 10000000

    def info(self):
        print(f"Jenis      : {self.jenis}")
        print(f"Nomor      : {self.get_nomor()}")
        print(f"Pemilik    : {self.nama}")
        print(f"Saldo      : {Rekening.format_rp(self.cek_saldo())}")
        print(f"Limit tarik: {Rekening.format_rp(self.limit_tarik)}")

    def tarik(self, nominal):
            self.kurangi_saldo(nominal)
            self.catat_mutasi("Tarik Tunai", nominal)
            print(f"[{self.nama}] Tarik {Rekening.format_rp(nominal)} berhasil.")


def tampil_info(rekening):
    rekening.info()


print(f"{NAMA_BANK}")
print("")

rek1 = RekeningBiasa("001", "rasyid ridho", 1800000)
rek2 = RekeningPremium("002", "altap solat", 23000000)
rek3 = RekeningBiasa("003", "robi ngaji", 950000)

daftar_rekening = [rek1, rek2, rek3]

print("DATA REKENING:")
for rek in daftar_rekening:
    tampil_info(rek)
    print("")

print("DAFTAR NASABAH:")
for rek in daftar_rekening:
    print(rek)
print("")

print("TRANSAKSI:")
rek1.setor(500000)
rek1.tarik(300000)
rek1.tarik(500000)
rek3.setor(200000)
rek3.tarik(150000)          
print("")

print("MUTASI:")
for rek in daftar_rekening:
    rek.tampil_mutasi()
print("")

total = rek1 + rek2
total_semua = total + rek3.jumlah_transaksi()
print("Total transaksi Rasyhid + altap:", total)
print("Total transaksi semua nasabah:", total_semua)

print("Total rekening terdaftar:", Rekening.get_total_rekening())